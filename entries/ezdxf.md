# ezdxf

> **Unverified. Not for stamped or issued work. Check against the adopted code edition.**

| Field | Value |
| --- | --- |
| Link | <https://github.com/mozman/ezdxf> |
| What it does | Read, write and audit DXF files from Python (layers, lines, polylines, text, dimensions, blocks). |
| Area | CAD/BIM data exchange |
| License | MIT |
| Platform | Python library |
| Setup difficulty | Easy (pip install ezdxf; pure Python) |
| Units | Drawing units set by the $INSUNITS header (this check: 4 = mm) |
| Standard and edition | none |
| Tier | Tried |
| Tested by | HusseinRagab |
| Test date | 15.11.2026 |
| Version tested | 1.4.5 (Python 3.12.10) |
| Worked example | n/a |

## Result

Ran the hub check script `checks/check_ezdxf.py` on Windows-11-10.0.26300-SP0, Python 3.12.10. Summary: 13 PASS, 2 CHECK. Both CHECK rows were then confirmed by opening the file in AutoCAD.

| Status | Check | Worst difference | Limit | Note |
| --- | --- | --- | --- | --- |
| PASS | 2 Audit errors after read-back | 0 | 0 count |  |
| PASS | 2 Audit fixes after read-back | 0 | 0 count |  |
| PASS | 2 Entity count round trip | 0 | 0 count |  |
| PASS | 2 Layers round trip |  |   |  |
| PASS | 2 $INSUNITS round trip (4 = mm) | 0 | 0 - |  |
| CHECK | 2 DXF version written | AC1032  | | AC1032 = R2018; opened in AutoCAD |
| PASS | 3 LINE endpoints round trip exactly |  |   |  |
| PASS | 3 CHWS run length (mm) | 0 | 1e-12 - |  |
| PASS | 3 CHWS run length mm -> m -> mm | 0 | 1e-12 - |  |
| PASS | 3 LWPOLYLINE length (mm) | 0 | 1e-12 - |  |
| PASS | 3 CIRCLE area from radius (m2) | 0 | 1e-12 - |  |
| PASS | 3 DIMENSION present |  |   |  |
| PASS | 3 DIMENSION measurement (mm) | 0 | 1e-09 mm |  |
| PASS | 3 DIMENSION displayed text is 12500 (got ['12500']) |  |   |  |
| CHECK | 4 Manual step: open results/ezdxf_check.dxf in CAD | | | Done: opened in AutoCAD: 4 layers, dimension 12500, text OK |

## Known limits

- DXF only; DWG needs a separate converter (for example ODA File Converter).
- $INSUNITS is a label: ezdxf does not scale geometry when you change it.
- Preset dimstyles (EZDXF, EZ_M_*) assume 1 drawing unit = 1 m and display cm (dimlfac 100): in a mm drawing a 12500 mm dimension shows 1250000. Use Standard or override dimlfac = 1.

## Notes

Manual step: the check writes results/ezdxf_check.dxf for opening in your CAD.
