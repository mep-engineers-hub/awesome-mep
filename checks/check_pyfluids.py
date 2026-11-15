"""pyfluids checks (CoolProp wrapper). pyfluids inputs: Pa, degC. SI internally.

Unverified. Not for stamped or issued work. Check against the adopted code edition.
"""
from pyfluids import Fluid, FluidsList, Input
from common import Report, sweep

P = 101325.0
T_LIST = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90]   # degC


def water(t_c, p=P):
    return Fluid(FluidsList.Water).with_state(Input.pressure(p), Input.temperature(t_c))


def run(examples=None):
    r = Report("pyfluids")

    # 1. Independent implementation: iapws (pure Python), IAPWS-95 and IAPWS-IF97
    try:
        import iapws
        sweep(r, "1 Water density vs iapws IAPWS95", (
            (f"{t} degC", water(t).density, iapws.IAPWS95(T=t + 273.15, P=P / 1e6).rho)
            for t in T_LIST), 1e-6, "-")
        sweep(r, "1 Water cp vs iapws IAPWS95", (
            (f"{t} degC", water(t).specific_heat, iapws.IAPWS95(T=t + 273.15, P=P / 1e6).cp * 1000)
            for t in T_LIST), 1e-5, "-")
        sweep(r, "1 Water viscosity vs iapws IAPWS95", (
            (f"{t} degC", water(t).dynamic_viscosity, iapws.IAPWS95(T=t + 273.15, P=P / 1e6).mu)
            for t in T_LIST), 1e-4, "-")
        sweep(r, "1 Water density vs iapws IAPWS97 (other formulation)", (
            (f"{t} degC", water(t).density, iapws.IAPWS97(T=t + 273.15, P=P / 1e6).rho)
            for t in T_LIST), 2e-4, "-")
    except ImportError as e:
        r.skip("1 iapws cross-check", f"iapws not installed: {e}")

    # 2. First principles: h(T2) - h(T1) = integral cp dT (trapezoid, 0.1 K steps)
    for t1, t2 in [(7, 12), (40, 45), (60, 80)]:
        n = int((t2 - t1) / 0.1)
        ts = [t1 + k * (t2 - t1) / n for k in range(n + 1)]
        cps = [water(t).specific_heat for t in ts]
        integ = sum((cps[k] + cps[k + 1]) / 2 * (ts[k + 1] - ts[k]) for k in range(n))
        r.rel(f"2 dh vs integral cp dT, {t1}-{t2} degC", water(t2).enthalpy - water(t1).enthalpy,
              integ, 1e-5, "-")

    # 3. First principles: chilled-water load Q = rho V cp dT, compared with m dh
    v = 0.010                      # m3/s (10 l/s)
    w1, w2 = water(7), water(12)
    m = w1.density * v
    q_dh = m * (w2.enthalpy - w1.enthalpy)
    q_cp = m * (w1.specific_heat + w2.specific_heat) / 2 * 5.0
    r.rel("3 10 l/s, 7-12 degC: m cp dT vs m dh", q_cp, q_dh, 1e-4, "-")
    r.info("3 10 l/s, 7-12 degC: load", q_dh / 1000, "kW")

    # 4. Unit round trip: degC in, K back from the state; Pa in, Pa back
    st = water(20)
    r.abs_("4 Temperature round trip", st.temperature, 20.0, 1e-9, "degC")
    r.rel("4 Pressure round trip", st.pressure, P, 1e-12, "-")

    # 5. Glycol mixture (info only: compare with your glycol supplier's data sheet)
    try:
        g = Fluid(FluidsList.MPG, 30).with_state(Input.pressure(P), Input.temperature(5))
        r.info("5 MPG 30 % at 5 degC: density", g.density, "kg/m3", "check against supplier data")
        r.info("5 MPG 30 % at 5 degC: cp", g.specific_heat, "J/(kg.K)", "check against supplier data")
        r.info("5 MPG 30 % at 5 degC: viscosity", g.dynamic_viscosity * 1000, "mPa.s",
               "check against supplier data")
    except Exception as e:
        r.error("5 MPG 30 %", e)

    # 6. Published verification values (Validated candidate): IAPWS-95, single-phase (T, rho)
    ex = (examples or {}).get("pyfluids")
    pts = [p for p in (ex or {}).get("points", []) if all(v is not None for v in p.values())]
    if pts:
        from CoolProp.CoolProp import PropsSI
        for p in pts:
            st = Fluid(FluidsList.Water).with_state(
                Input.temperature(p["T_K"] - 273.15), Input.density(p["rho_kg_m3"]))
            lbl = f"T={p['T_K']} K rho={p['rho_kg_m3']}"
            got = {"p_MPa": st.pressure / 1e6,
                   "cp_kJ_kgK": st.specific_heat / 1000,
                   "w_m_s": st.sound_speed,
                   "s_kJ_kgK": st.entropy / 1000,
                   # pyfluids has no cv property: read from the same CoolProp backend
                   "cv_kJ_kgK": PropsSI("Cvmass", "T", p["T_K"], "D", p["rho_kg_m3"], "Water") / 1000}
            for k, exp in p.items():
                if k in got:
                    r.rel(f"6 IAPWS-95 {k}, {lbl}", got[k], exp, 1e-7, "-",
                          ex.get("source", "") + (" (cv via CoolProp PropsSI)" if k == "cv_kJ_kgK" else ""))
    else:
        r.skip("6 IAPWS-95 verification values", "values not entered in worked_examples.json")
    return r
