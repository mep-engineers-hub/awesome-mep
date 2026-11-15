# pyfluids

> **Unverified. Not for stamped or issued work. Check against the adopted code edition.**

| Field | Value |
| --- | --- |
| Link | <https://github.com/portyanikhin/pyfluids> |
| What it does | Object-style Python wrapper over CoolProp for fluids (water, refrigerants, glycol mixtures) and humid air. |
| Area | Python libraries |
| License | MIT |
| Platform | Python library (wheels for Windows, macOS, Linux) |
| Setup difficulty | Easy (pip install pyfluids; pulls CoolProp) |
| Units | SI with degC and percent by default (units_system SIWithCelsiusAndPercents) |
| Standard and edition | Water: IAPWS-95 formulation through CoolProp's default backend. Citation only. |
| Tier | Tried |
| Tested by | HusseinRagab |
| Test date | 15.11.2026 |
| Version tested | 4.0.0 (Python 3.12.10) |
| Worked example | n/a |

## Result

Ran the hub check script `checks/check_pyfluids.py` on Windows-11-10.0.26300-SP0, Python 3.12.10. Summary: 10 PASS, 4 CHECK, 1 SKIP.

| Status | Check | Worst difference | Limit | Note |
| --- | --- | --- | --- | --- |
| PASS | 1 Water density vs iapws IAPWS95 | 2.853634842e-14 | 1e-06 - | 14 points, 0 outside limit, worst at 5 degC |
| PASS | 1 Water cp vs iapws IAPWS95 | 3.463882083e-11 | 1e-05 - | 14 points, 0 outside limit, worst at 70 degC |
| PASS | 1 Water viscosity vs iapws IAPWS95 | 6.027420618e-14 | 0.0001 - | 14 points, 0 outside limit, worst at 5 degC |
| PASS | 1 Water density vs iapws IAPWS97 (other formulation) | 1.503872866e-05 | 0.0002 - | 14 points, 0 outside limit, worst at 60 degC |
| PASS | 2 dh vs integral cp dT, 7-12 degC | 2.599247951e-08 | 1e-05 - |  |
| PASS | 2 dh vs integral cp dT, 40-45 degC | 4.104030273e-09 | 1e-05 - |  |
| PASS | 2 dh vs integral cp dT, 60-80 degC | 3.147081766e-09 | 1e-05 - |  |
| PASS | 3 10 l/s, 7-12 degC: m cp dT vs m dh | 6.482083211e-05 | 0.0001 - |  |
| CHECK | 3 10 l/s, 7-12 degC: load | 209.7859899 kW | | not compared yet |
| PASS | 4 Temperature round trip | 0 | 1e-09 degC |  |
| PASS | 4 Pressure round trip | 0 | 1e-12 - |  |
| CHECK | 5 MPG 30 % at 5 degC: density | 1029.893369 kg/m3 | | check against supplier data; not compared yet |
| CHECK | 5 MPG 30 % at 5 degC: cp | 3816.290612 J/(kg.K) | | check against supplier data; not compared yet |
| CHECK | 5 MPG 30 % at 5 degC: viscosity | 5.569380791 mPa.s | | check against supplier data; not compared yet |
| SKIP | 6 IAPWS-95 verification values |  |   | values not entered in worked_examples.json |

## Known limits

- Temperatures in degC and fractions in percent by default: easy to pass K or 0-1 fractions by mistake.
- No cv property on the state object (read it from CoolProp directly).
- Glycol mixture data come from CoolProp's incompressible fits: check concentration and temperature limits and compare with the supplier's data sheet.

## Notes

Results depend on the CoolProp version underneath; record both versions.
