"""fluids (CalebBell) checks: friction factor, Darcy-Weisbach, pipe schedule. SI internally.

Unverified. Not for stamped or issued work. Check against the adopted code edition.
"""
import math
import fluids
from common import Report, sweep

RE_LIST = [4e3, 1e4, 3e4, 1e5, 3e5, 1e6, 1e7, 1e8]
ED_LIST = [0.0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 5e-2]
US_GAL_M3 = 3.785411784e-3          # exact by definition


def colebrook(re, ed):
    """Own Colebrook-White solution, fixed-point on 1/sqrt(f), to machine precision."""
    x = 1 / math.sqrt(0.02)
    for _ in range(200):
        x_new = -2 * math.log10(ed / 3.7 + 2.51 * x / re)
        if abs(x_new - x) < 1e-15:
            break
        x = x_new
    return 1 / x_new ** 2


def run(examples=None):
    r = Report("fluids")

    # 1. Turbulent friction factor vs own Colebrook solution
    sweep(r, "1 Darcy f (default Clamond) vs own Colebrook", (
        (f"Re={re:.0e} e/D={ed:g}", fluids.friction_factor(re, ed), colebrook(re, ed))
        for re in RE_LIST for ed in ED_LIST), 1e-9, "-")
    sweep(r, "1 Darcy f (Method=Colebrook) vs own Colebrook", (
        (f"Re={re:.0e} e/D={ed:g}", fluids.friction_factor(re, ed, Method="Colebrook"), colebrook(re, ed))
        for re in RE_LIST for ed in ED_LIST), 1e-9, "-")

    # 2. Laminar: f = 64 / Re
    sweep(r, "2 Laminar f vs 64/Re", (
        (f"Re={re}", fluids.friction_factor(re, 0.0), 64 / re) for re in [100, 500, 1000, 2000]), 1e-12, "-")
    r.info("2 Laminar/turbulent switch", "Re < 2040 laminar (fluids default)", "",
           "no transition zone model: check this suits your case")

    # 3. Darcy-Weisbach pressure drop vs first principles
    D, L, rough = 0.10226, 100.0, 0.045e-3          # NPS 4 Sch 40 ID, 100 m, commercial steel
    rho, mu = 998.2071504679437, 1.001596143120583e-3  # water 20 degC (IAPWS-95 via CoolProp)
    for q_ls in [2, 5, 10, 15, 20]:
        q = q_ls / 1000
        m = rho * q
        v = q / (math.pi * D ** 2 / 4)
        re = rho * v * D / mu
        dp_fp = colebrook(re, rough / D) * L / D * rho * v ** 2 / 2
        r.rel(f"3 dP NPS 4 Sch 40, {q_ls} l/s, 100 m", fluids.one_phase_dP(m, rho, mu, D, rough, L), dp_fp, 1e-8, "-")

    # 4. Parameter sweep: turbulent dP proportional to Q^n with 1.75 <= n <= 2.0
    qs = [0.002 * k for k in range(1, 11)]
    dps = [fluids.one_phase_dP(rho * q, rho, mu, D, rough, L) for q in qs]
    mono = all(b > a for a, b in zip(dps, dps[1:]))
    n = math.log(dps[-1] / dps[2]) / math.log(qs[-1] / qs[2])
    r.true("4 dP rises with flow (2-20 l/s)", mono)
    r.true(f"4 Flow exponent n = {n:.3f} within 1.75-2.0", 1.75 <= n <= 2.0)

    # 5. Pipe schedule: internal consistency, and values for a check against ASME B36.10M
    for nps in [0.5, 1, 2, 3, 4, 6, 8, 10, 12]:
        nps_, di, do, t = fluids.nearest_pipe(NPS=nps, schedule="40")
        r.abs_(f"5 Sch 40 NPS {nps}: Di = Do - 2t", di, do - 2 * t, 1e-12, "m")
        r.info(f"5 Sch 40 NPS {nps}: OD / wall / ID", f"{do*1000:.1f} / {t*1000:.2f} / {di*1000:.2f}", "mm",
               "check against ASME B36.10M, edition you hold")

    # 6. Unit round trip: US gpm -> m3/s -> US gpm, exact factor
    for gpm in [1, 50, 250, 1000]:
        q = gpm * US_GAL_M3 / 60
        r.rel(f"6 {gpm} US gpm round trip", q * 60 / US_GAL_M3, gpm, 1e-14, "-")
    return r
