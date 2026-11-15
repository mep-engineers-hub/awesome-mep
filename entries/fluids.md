# fluids

> **Unverified. Not for stamped or issued work. Check against the adopted code edition.**

| Field | Value |
| --- | --- |
| Link | <https://github.com/CalebBell/fluids> |
| What it does | Pipe friction factors, Darcy-Weisbach pressure drop, fittings K values, pipe schedules, pumps. |
| Area | Duct and pipe sizing |
| License | MIT |
| Platform | Python library |
| Setup difficulty | Easy (pip install fluids; pure Python) |
| Units | SI only (m, Pa, kg/s, Pa.s) |
| Standard and edition | Pipe dimensions follow ASME B36.10M per the library's docs. Citation only. |
| Tier | Tried |
| Tested by | HusseinRagab |
| Test date | 15.11.2026 |
| Version tested | 1.3.1 (Python 3.12.10) |
| Worked example | n/a |

## Result

Ran the hub check script `checks/check_fluids.py` on Windows-11-10.0.26300-SP0, Python 3.12.10. Summary: 23 PASS, 10 CHECK.

| Status | Check | Worst difference | Limit | Note |
| --- | --- | --- | --- | --- |
| PASS | 1 Darcy f (default Clamond) vs own Colebrook | 1.163369564e-15 | 1e-09 - | 56 points, 0 outside limit, worst at Re=1e+06 e/D=0.05 |
| PASS | 1 Darcy f (Method=Colebrook) vs own Colebrook | 1.093894746e-14 | 1e-09 - | 56 points, 0 outside limit, worst at Re=3e+04 e/D=0.05 |
| PASS | 2 Laminar f vs 64/Re | 0 | 1e-12 - | 4 points, 0 outside limit, worst at Re=100 |
| CHECK | 2 Laminar/turbulent switch | Re < 2040 laminar (fluids default)  | | no transition zone model: check this suits your case; not compared yet |
| PASS | 3 dP NPS 4 Sch 40, 2 l/s, 100 m | 1.533779656e-16 | 1e-08 - |  |
| PASS | 3 dP NPS 4 Sch 40, 5 l/s, 100 m | 3.495714955e-16 | 1e-08 - |  |
| PASS | 3 dP NPS 4 Sch 40, 10 l/s, 100 m | 6.439739916e-16 | 1e-08 - |  |
| PASS | 3 dP NPS 4 Sch 40, 15 l/s, 100 m | 2.397481417e-16 | 1e-08 - |  |
| PASS | 3 dP NPS 4 Sch 40, 20 l/s, 100 m | 1.385668859e-16 | 1e-08 - |  |
| PASS | 4 dP rises with flow (2-20 l/s) |  |   |  |
| PASS | 4 Flow exponent n = 1.880 within 1.75-2.0 |  |   |  |
| PASS | 5 Sch 40 NPS 0.5: Di = Do - 2t | 0 | 1e-12 m |  |
| CHECK | 5 Sch 40 NPS 0.5: OD / wall / ID | 21.3 / 2.77 / 15.76 mm | | check against ASME B36.10M, edition you hold; not compared yet |
| PASS | 5 Sch 40 NPS 1: Di = Do - 2t | 0 | 1e-12 m |  |
| CHECK | 5 Sch 40 NPS 1: OD / wall / ID | 33.4 / 3.38 / 26.64 mm | | check against ASME B36.10M, edition you hold; not compared yet |
| PASS | 5 Sch 40 NPS 2: Di = Do - 2t | 0 | 1e-12 m |  |
| CHECK | 5 Sch 40 NPS 2: OD / wall / ID | 60.3 / 3.91 / 52.48 mm | | check against ASME B36.10M, edition you hold; not compared yet |
| PASS | 5 Sch 40 NPS 3: Di = Do - 2t | 0 | 1e-12 m |  |
| CHECK | 5 Sch 40 NPS 3: OD / wall / ID | 88.9 / 5.49 / 77.92 mm | | check against ASME B36.10M, edition you hold; not compared yet |
| PASS | 5 Sch 40 NPS 4: Di = Do - 2t | 0 | 1e-12 m |  |
| CHECK | 5 Sch 40 NPS 4: OD / wall / ID | 114.3 / 6.02 / 102.26 mm | | check against ASME B36.10M, edition you hold; not compared yet |
| PASS | 5 Sch 40 NPS 6: Di = Do - 2t | 2.775557562e-17 | 1e-12 m |  |
| CHECK | 5 Sch 40 NPS 6: OD / wall / ID | 168.3 / 7.11 / 154.08 mm | | check against ASME B36.10M, edition you hold; not compared yet |
| PASS | 5 Sch 40 NPS 8: Di = Do - 2t | 2.775557562e-17 | 1e-12 m |  |
| CHECK | 5 Sch 40 NPS 8: OD / wall / ID | 219.1 / 8.18 / 202.74 mm | | check against ASME B36.10M, edition you hold; not compared yet |
| PASS | 5 Sch 40 NPS 10: Di = Do - 2t | 0 | 1e-12 m |  |
| CHECK | 5 Sch 40 NPS 10: OD / wall / ID | 273.0 / 9.27 / 254.46 mm | | check against ASME B36.10M, edition you hold; not compared yet |
| PASS | 5 Sch 40 NPS 12: Di = Do - 2t | 0 | 1e-12 m |  |
| CHECK | 5 Sch 40 NPS 12: OD / wall / ID | 323.8 / 10.31 / 303.18 mm | | check against ASME B36.10M, edition you hold; not compared yet |
| PASS | 6 1 US gpm round trip | 0 | 1e-14 - |  |
| PASS | 6 50 US gpm round trip | 0 | 1e-14 - |  |
| PASS | 6 250 US gpm round trip | 0 | 1e-14 - |  |
| PASS | 6 1000 US gpm round trip | 0 | 1e-14 - |  |

## Known limits

- SI only: convert gpm, ft and psi yourself at the boundary.
- Laminar/turbulent switch at Re 2040 by default, with no transition-zone model.
- Default friction method is Clamond (exact Colebrook solution); many other correlations are selectable, so state the one you used.

## Notes

None.
