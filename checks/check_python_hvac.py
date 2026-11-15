"""python-hvac (TomLXXVI) checks: humid air and pipe pressure drop. SI internally.

Unverified. Not for stamped or issued work. Check against the adopted code edition.
"""
import math
import warnings
from common import Report, sweep

P = 101325.0
TDB = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
RH = [0.10, 0.30, 0.50, 0.70, 0.90]
US_GAL_M3 = 3.785411784e-3


def run(examples=None):
    r = Report("python-hvac")
    warnings.filterwarnings("ignore")
    import pint
    r.info("0 pint version", pint.__version__, "",
           "python-hvac 0.1.3 fails to import with pint 0.26 (unit string 'J/(kg.K)'); 0.24.4 works")
    try:
        from hvac import Quantity as Q_
        from hvac.fluids import HumidAir, Fluid
        from hvac.fluid_flow import Pipe, Circular
    except Exception as e:
        r.error("0 import hvac", e)
        return r
    r.true("0 import hvac", True)

    # 1. Humid air vs psychrolib (python-hvac wraps CoolProp HAPropsSI)
    try:
        import psychrolib as pl
        pl.SetUnitSystem(pl.SI)
        pts = [(t, rh) for t in TDB for rh in RH]
        def ha(t, rh):
            return HumidAir(Tdb=Q_(t, "degC"), RH=Q_(rh, "frac"))
        sweep(r, "1 W vs psychrolib", ((f"{t} degC {rh:.0%}", ha(t, rh).W.to("kg/kg").m,
              pl.GetHumRatioFromRelHum(t, rh, P)) for t, rh in pts), 0.005, "-")
        sweep(r, "1 Twb vs psychrolib", ((f"{t} degC {rh:.0%}", ha(t, rh).Twb.to("degC").m,
              pl.GetTWetBulbFromRelHum(t, rh, P)) for t, rh in pts), 0.1, "K", kind="abs")
        sweep(r, "1 Tdp vs psychrolib", ((f"{t} degC {rh:.0%}", ha(t, rh).Tdp.to("degC").m,
              pl.GetTDewPointFromRelHum(t, rh)) for t, rh in pts), 0.1, "K", kind="abs")
        r.info("1 h datum", "CoolProp humid-air enthalpy", "",
               "python-hvac h comes from CoolProp; compare h differences, not absolute h, with other tools")
    except ImportError as e:
        r.skip("1 psychrolib cross-check", f"psychrolib not installed: {e}")

    # 2. Pipe pressure drop vs fluids (independent friction solver)
    try:
        import fluids
        st = Fluid("Water")(T=Q_(20, "degC"), P=Q_(P, "Pa"))
        rho, mu = st.rho.to("kg/m^3").m, st.mu.to("Pa*s").m
        D, L, e = 0.10226, 100.0, 0.045e-3
        for q_ls in [2, 5, 10, 15, 20]:
            p = Pipe.create(length=Q_(L, "m"), wall_roughness=Q_(e * 1000, "mm"), fluid=st,
                            cross_section=Circular.create(Q_(D * 1000, "mm")),
                            volume_flow_rate=Q_(q_ls, "L/s"))
            ref = fluids.one_phase_dP(rho * q_ls / 1000, rho, mu, D, e, L)
            r.rel(f"2 dP DN100 (ID 102.26 mm), {q_ls} l/s, 100 m vs fluids",
                  p.pressure_drop.to("Pa").m, ref, 1e-4, "-")
    except ImportError as e:
        r.skip("2 fluids cross-check", f"fluids not installed: {e}")

    # 3. Unit round trip through pint (python-hvac's unit layer)
    for gpm in [50, 250, 1000]:
        q = Q_(gpm, "gallon/minute").to("m^3/s").m
        r.rel(f"3 pint {gpm} US gpm -> m3/s vs exact factor", q, gpm * US_GAL_M3 / 60, 1e-12, "-")
        r.rel(f"3 pint {gpm} US gpm round trip", Q_(q, "m^3/s").to("gallon/minute").m, gpm, 1e-12, "-")
    psi_pa = 0.45359237 * 9.80665 / 0.0254 ** 2     # exact from lb, g_n and inch definitions
    r.rel("3 pint 1 psi -> Pa vs exact definition", Q_(1, "psi").to("Pa").m, psi_pa, 1e-12, "-")
    return r
    r.true("0 import hvac", True)

    # 1. Humid air vs psychrolib (python-hvac wraps CoolProp HAPropsSI)
    try:
        import psychrolib as pl
        pl.SetUnitSystem(pl.SI)
        pts = [(t, rh) for t in TDB for rh in RH]
        def ha(t, rh):
            return HumidAir(Tdb=Q_(t, "degC"), RH=Q_(rh, "frac"))
        sweep(r, "1 W vs psychrolib", ((f"{t} degC {rh:.0%}", ha(t, rh).W.to("kg/kg").m,
              pl.GetHumRatioFromRelHum(t, rh, P)) for t, rh in pts), 0.005, "-")
        sweep(r, "1 Twb vs psychrolib", ((f"{t} degC {rh:.0%}", ha(t, rh).Twb.to("degC").m,
              pl.GetTWetBulbFromRelHum(t, rh, P)) for t, rh in pts), 0.1, "K", kind="abs")
        sweep(r, "1 Tdp vs psychrolib", ((f"{t} degC {rh:.0%}", ha(t, rh).Tdp.to("degC").m,
              pl.GetTDewPointFromRelHum(t, rh)) for t, rh in pts), 0.1, "K", kind="abs")
        r.info("1 h datum", "CoolProp humid-air enthalpy", "",
               "python-hvac h comes from CoolProp; compare h differences, not absolute h, with other tools")
    except ImportError as e:
        r.skip("1 psychrolib cross-check", f"psychrolib not installed: {e}")

    # 2. Pipe pressure drop vs fluids (independent friction solver)
    try:
        import fluids
        st = Fluid("Water")(T=Q_(20, "degC"), P=Q_(P, "Pa"))
        rho, mu = st.rho.to("kg/m^3").m, st.mu.to("Pa*s").m
        D, L, e = 0.10226, 100.0, 0.045e-3
        for q_ls in [2, 5, 10, 15, 20]:
            p = Pipe.create(length=Q_(L, "m"), wall_roughness=Q_(e * 1000, "mm"), fluid=st,
                            cross_section=Circular.create(Q_(D * 1000, "mm")),
                            volume_flow_rate=Q_(q_ls, "L/s"))
            ref = fluids.one_phase_dP(rho * q_ls / 1000, rho, mu, D, e, L)
            r.rel(f"2 dP DN100 (ID 102.26 mm), {q_ls} l/s, 100 m vs fluids",
                  p.pressure_drop.to("Pa").m, ref, 1e-4, "-")
    except ImportError as e:
        r.skip("2 fluids cross-check", f"fluids not installed: {e}")

    # 3. Unit round trip through pint (python-hvac's unit layer)
    for gpm in [50, 250, 1000]:
        q = Q_(gpm, "gallon/minute").to("m^3/s").m
        r.rel(f"3 pint {gpm} US gpm -> m3/s vs exact factor", q, gpm * US_GAL_M3 / 60, 1e-12, "-")
        r.rel(f"3 pint {gpm} US gpm round trip", Q_(q, "m^3/s").to("gallon/minute").m, gpm, 1e-12, "-")
    r.rel("3 pint 1 inch_H2O_39F -> Pa", Q_(1, "inch_H2O_39F").to("Pa").m, 249.08891, 1e-6, "-",
          "1 inH2O (39.2 degF) = 249.08891 Pa")
    return r
