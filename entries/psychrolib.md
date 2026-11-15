# psychrolib

> **Unverified. Not for stamped or issued work. Check against the adopted code edition.**

> 1 FAIL, explained under Known limits (limit kept at 0.5 %, decision 15.11.2026).

| Field | Value |
| --- | --- |
| Link | <https://github.com/psychrometrics/psychrolib> |
| What it does | Psychrometric property functions for moist air (W, h, Twb, Tdp, RH, v) in SI or IP. |
| Area | HVAC loads and psychrometrics |
| License | MIT |
| Platform | Python library (also C, C#, Fortran, JavaScript, VBA ports) |
| Setup difficulty | Easy (pip install psychrolib; pure Python) |
| Units | SI or IP, one global switch (SetUnitSystem) |
| Standard and edition | ASHRAE Handbook - Fundamentals (2017), Ch. 1 equations, as cited in the library's own docstrings. Citation only. |
| Tier | Tried |
| Tested by | HusseinRagab |
| Test date | 15.11.2026 |
| Version tested | 2.5.0 (Python 3.12.10) |
| Worked example | n/a |

## Result

Ran the hub check script `checks/check_psychrolib.py` on Windows-11-10.0.26300-SP0, Python 3.12.10. Summary: 10 PASS, 1 FAIL, 1 SKIP.

| Status | Check | Worst difference | Limit | Note |
| --- | --- | --- | --- | --- |
| PASS | 1 Round trip RH->W->RH | 3.700743415e-16 | 1e-09 - | 110 points, 0 outside limit, worst at 50 degC 30% |
| PASS | 2 W vs ideal-gas mixing relation | 5.067923498e-07 | 1e-05 - | 110 points, 0 outside limit, worst at 40 degC 100% |
| PASS | 3 h vs linear enthalpy relation | 2.910383046e-11 | 1 J/kg | 110 points, 0 outside limit, worst at 40 degC 100% |
| PASS | 4 Twb at saturation equals Tdb | 0 | 0.01 K | 10 points, 0 outside limit, worst at 5 degC |
| PASS | 4 Tdp at saturation equals Tdb | 0 | 0.01 K | 10 points, 0 outside limit, worst at 5 degC |
| FAIL | 5 W vs CoolProp HAPropsSI | 0.006088148372 | 0.005 - | 90 points, 26 outside limit, worst at 50 degC 90% |
| PASS | 5 Twb vs CoolProp HAPropsSI | 0.02385475944 | 0.1 K | 90 points, 0 outside limit, worst at 5 degC 10% |
| PASS | 5 Tdp vs CoolProp HAPropsSI | 0.01826598398 | 0.1 K | 90 points, 0 outside limit, worst at 50 degC 10% |
| PASS | 5 v vs CoolProp HAPropsSI | 0.000536116192 | 0.002 - | 90 points, 0 outside limit, worst at 5 degC 10% |
| PASS | 6 W, SI mode vs IP mode (35 degC 40 %) | 4.452277287e-07 | 0.0001 - | IP mode uses its own saturation fit; small difference expected |
| PASS | 6 Tdp, SI mode vs IP mode (35 degC 40 %) | 3.756392424e-07 | 0.02 K |  |
| SKIP | 7 Worked example |  |   | expected values not entered in worked_examples.json |

## Known limits

- Unit system is a global setting: mixing SI and IP calls in one program gives wrong numbers without an error.
- IP enthalpy datum is 0 degF dry air; SI datum is 0 degC. Do not convert h between modes with 2.326 alone.
- Humidity ratio runs 0.42-0.61 % below CoolProp HAPropsSI (5-50 degC, 10-90 % RH, 101.325 kPa): the ideal-gas relations leave out the enhancement factor (ratio matches CoolProp's saturation-pressure ratio). Gap is largest hot and humid, so latent loads come out slightly low.
- Ideal-gas mixing relations; check the stated validity range in the source before using it outside normal HVAC conditions.

## Notes

The library's source file carries an ASHRAE copyright notice for the equations and coefficients. Read it before any commercial reuse (hub rule 1).
