# python-hvac

> **Unverified. Not for stamped or issued work. Check against the adopted code edition.**

> 1 FAIL, explained under Known limits (limit kept at 0.5 %, decision 15.11.2026).

| Field | Value |
| --- | --- |
| Link | <https://github.com/TomLXXVI/python-hvac> |
| What it does | HVAC toolkit: humid air, hydronic and duct networks, pipe/duct sizing, cooling and heating loads, refrigeration helpers. |
| Area | HVAC loads and psychrometrics |
| License | MIT |
| Platform | Python library (Python 3.11 or 3.12 only) |
| Setup difficulty | Medium (install from GitHub; needs Python below 3.13 and pint 0.24.x, see Known limits) |
| Units | Any, through pint quantities; SI inside |
| Standard and edition | Load methods cite ASHRAE methods in the repo docs; not checked in this entry. Citation only. |
| Tier | Tried |
| Tested by | HusseinRagab |
| Test date | 15.11.2026 |
| Version tested | 0.1.3 (Python 3.12.10) |
| Worked example | n/a |

## Result

Ran the hub check script `checks/check_python_hvac.py` on Windows-11-10.0.26300-SP0, Python 3.12.10. Summary: 15 PASS, 1 FAIL, 2 CHECK.

| Status | Check | Worst difference | Limit | Note |
| --- | --- | --- | --- | --- |
| CHECK | 0 pint version | 0.24.4  | | python-hvac 0.1.3 fails to import with pint 0.26 (unit string 'J/(kg.K)'); 0.24.4 works; not compared yet |
| PASS | 0 import hvac |  |   |  |
| FAIL | 1 W vs psychrolib | 0.006125440965 | 0.005 - | 50 points, 16 outside limit, worst at 50 degC 90% |
| PASS | 1 Twb vs psychrolib | 0.02385475944 | 0.1 K | 50 points, 0 outside limit, worst at 5 degC 10% |
| PASS | 1 Tdp vs psychrolib | 0.01826598398 | 0.1 K | 50 points, 0 outside limit, worst at 50 degC 10% |
| CHECK | 1 h datum | CoolProp humid-air enthalpy  | | python-hvac h comes from CoolProp; compare h differences, not absolute h, with other tools; not compared yet |
| PASS | 2 dP DN100 (ID 102.26 mm), 2 l/s, 100 m vs fluids | 9.413916235e-06 | 0.0001 - |  |
| PASS | 2 dP DN100 (ID 102.26 mm), 5 l/s, 100 m vs fluids | 4.406765295e-06 | 0.0001 - |  |
| PASS | 2 dP DN100 (ID 102.26 mm), 10 l/s, 100 m vs fluids | 1.343103623e-06 | 0.0001 - |  |
| PASS | 2 dP DN100 (ID 102.26 mm), 15 l/s, 100 m vs fluids | 5.098944983e-07 | 0.0001 - |  |
| PASS | 2 dP DN100 (ID 102.26 mm), 20 l/s, 100 m vs fluids | 2.266551814e-07 | 0.0001 - |  |
| PASS | 3 pint 50 US gpm -> m3/s vs exact factor | 1.374796383e-16 | 1e-12 - |  |
| PASS | 3 pint 50 US gpm round trip | 1.421085472e-16 | 1e-12 - |  |
| PASS | 3 pint 250 US gpm -> m3/s vs exact factor | 2.199674212e-16 | 1e-12 - |  |
| PASS | 3 pint 250 US gpm round trip | 2.273736754e-16 | 1e-12 - |  |
| PASS | 3 pint 1000 US gpm -> m3/s vs exact factor | 2.199674212e-16 | 1e-12 - |  |
| PASS | 3 pint 1000 US gpm round trip | 2.273736754e-16 | 1e-12 - |  |
| PASS | 3 pint 1 psi -> Pa vs exact definition | 3.957331621e-16 | 1e-12 - |  |

## Known limits

- Fails to import with pint 0.26 (unit string parse error in hvac/fluids/constants.py); pin pint 0.24.4.
- Requires Python >=3.11,<3.13.
- Only humid air and straight-pipe pressure drop were checked here; load-calculation modules were not tried.

## Notes

Humid-air properties come from CoolProp HAPropsSI.
