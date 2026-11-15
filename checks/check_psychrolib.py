"""psychrolib checks. SI internally (degC, Pa, kg/kg, J/kg).

Unverified. Not for stamped or issued work. Check against the adopted code edition.
"""
import psychrolib as pl
from common import Report, sweep

P = 101325.0                       # Pa, standard atmosphere
MW_RATIO = 18.015268 / 28.966      # molar mass water / dry air = 0.621945
TDB = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]          # degC
RH = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]


def run(examples=None):
    r = Report("psychrolib")
    pl.SetUnitSystem(pl.SI)

    # 1. Round trip RH -> W -> RH over the grid (same library, must be exact)
    sweep(r, "1 Round trip RH->W->RH", (
        (f"{t} degC {rh:.0%}", pl.GetRelHumFromHumRatio(t, pl.GetHumRatioFromRelHum(t, rh, P), P), rh)
        for t in TDB for rh in RH), 1e-9, "-")

    # 2. First principles: W = 0.621945 pw / (p - pw), pw = RH * pws
    def w_fp(t, rh):
        pw = rh * pl.GetSatVapPres(t)
        return MW_RATIO * pw / (P - pw)
    sweep(r, "2 W vs ideal-gas mixing relation", (
        (f"{t} degC {rh:.0%}", pl.GetHumRatioFromRelHum(t, rh, P), w_fp(t, rh))
        for t in TDB for rh in RH), 1e-5, "-")

    # 3. First principles: h = 1006 t + W (2 501 000 + 1860 t), J/kg dry air
    def h_fp(t, w):
        return 1006.0 * t + w * (2501000.0 + 1860.0 * t)
    sweep(r, "3 h vs linear enthalpy relation", (
        (f"{t} degC {rh:.0%}", pl.GetMoistAirEnthalpy(t, pl.GetHumRatioFromRelHum(t, rh, P)),
         h_fp(t, pl.GetHumRatioFromRelHum(t, rh, P)))
        for t in TDB for rh in RH), 1.0, "J/kg", kind="abs")

    # 4. Saturation: at RH = 100 %, Twb = Tdp = Tdb
    sweep(r, "4 Twb at saturation equals Tdb", (
        (f"{t} degC", pl.GetTWetBulbFromRelHum(t, 1.0, P), t) for t in TDB if t > 0), 0.01, "K", kind="abs")
    sweep(r, "4 Tdp at saturation equals Tdb", (
        (f"{t} degC", pl.GetTDewPointFromRelHum(t, 1.0), t) for t in TDB if t > 0), 0.01, "K", kind="abs")

    # 5. Independent cross-check: CoolProp HAPropsSI (different formulation, ASHRAE RP-1485)
    try:
        from CoolProp.HumidAirProp import HAPropsSI
        pts = [(t, rh) for t in TDB if t >= 5 for rh in RH if rh < 1.0]
        sweep(r, "5 W vs CoolProp HAPropsSI", (
            (f"{t} degC {rh:.0%}", pl.GetHumRatioFromRelHum(t, rh, P),
             HAPropsSI("W", "T", t + 273.15, "P", P, "R", rh)) for t, rh in pts), 0.005, "-")
        sweep(r, "5 Twb vs CoolProp HAPropsSI", (
            (f"{t} degC {rh:.0%}", pl.GetTWetBulbFromRelHum(t, rh, P),
             HAPropsSI("Twb", "T", t + 273.15, "P", P, "R", rh) - 273.15) for t, rh in pts), 0.1, "K", kind="abs")
        sweep(r, "5 Tdp vs CoolProp HAPropsSI", (
            (f"{t} degC {rh:.0%}", pl.GetTDewPointFromRelHum(t, rh),
             HAPropsSI("Tdp", "T", t + 273.15, "P", P, "R", rh) - 273.15) for t, rh in pts), 0.1, "K", kind="abs")
        sweep(r, "5 v vs CoolProp HAPropsSI", (
            (f"{t} degC {rh:.0%}", pl.GetMoistAirVolume(t, pl.GetHumRatioFromRelHum(t, rh, P), P),
             HAPropsSI("Vda", "T", t + 273.15, "P", P, "R", rh)) for t, rh in pts), 0.002, "-")
    except ImportError as e:
        r.skip("5 CoolProp cross-check", f"CoolProp not installed: {e}")

    # 6. Unit round trip: same state in IP mode, compare W and Tdp after exact conversion
    t, rh = 35.0, 0.40
    w_si = pl.GetHumRatioFromRelHum(t, rh, P)
    td_si = pl.GetTDewPointFromRelHum(t, rh)
    pl.SetUnitSystem(pl.IP)
    t_f = t * 9 / 5 + 32
    p_psi = P / 6894.757293168     # 1 psi = 6894.757293168 Pa (exact)
    w_ip = pl.GetHumRatioFromRelHum(t_f, rh, p_psi)
    td_ip_c = (pl.GetTDewPointFromRelHum(t_f, rh) - 32) * 5 / 9
    pl.SetUnitSystem(pl.SI)
    r.rel("6 W, SI mode vs IP mode (35 degC 40 %)", w_ip, w_si, 1e-4, "-",
          "IP mode uses its own saturation fit; small difference expected")
    r.abs_("6 Tdp, SI mode vs IP mode (35 degC 40 %)", td_ip_c, td_si, 0.02, "K")

    # 7. Published worked example (Validated candidate). Values entered by the tester.
    ex = (examples or {}).get("psychrolib")
    if ex and ex.get("expected") and all(v is not None for v in ex["expected"].values()):
        i = ex["inputs"]
        w = pl.GetHumRatioFromTWetBulb(i["tdb_C"], i["twb_C"], i["p_Pa"])
        got = {"W_kg_per_kg": w,
               "h_kJ_per_kg": pl.GetMoistAirEnthalpy(i["tdb_C"], w) / 1000,
               "tdp_C": pl.GetTDewPointFromHumRatio(i["tdb_C"], w, i["p_Pa"]),
               "rh_pct": 100 * pl.GetRelHumFromHumRatio(i["tdb_C"], w, i["p_Pa"]),
               "v_m3_per_kg": pl.GetMoistAirVolume(i["tdb_C"], w, i["p_Pa"])}
        for k, exp in ex["expected"].items():
            lim = ex["limits"][k]
            r.abs_(f"7 Worked example {k}", got[k], exp, lim, k.split("_", 1)[1],
                   ex.get("source", ""))
    else:
        r.skip("7 Worked example", "expected values not entered in worked_examples.json")
    return r
