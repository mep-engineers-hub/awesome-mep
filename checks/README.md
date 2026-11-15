# Tool checks

> **Unverified. Not for stamped or issued work. Check against the adopted code edition.**

Scripts that take an index entry from **Found** to **Tried** (and, with a published worked example, to **Validated**). Each script runs one tool against its own round trips, first-principles relations, an independent second library and parameter sweeps, all in SI, then writes a results file and a draft entry for [`entries/`](../entries/).

Code in this folder is under the [MIT licence](LICENSE). The rest of this repo (index and docs) stays under CC BY 4.0.

| Script | Tool | Checked against |
| --- | --- | --- |
| `check_psychrolib.py` | psychrolib | RH round trip, ideal-gas W and h relations, saturation, CoolProp HAPropsSI, SI vs IP mode; worked example optional |
| `check_pyfluids.py` | pyfluids | iapws (IAPWS-95 and IAPWS-IF97), dh vs integral cp dT, chilled-water load, unit round trips; IAPWS-95 verification values optional |
| `check_fluids.py` | fluids | own Colebrook solution, 64/Re, Darcy-Weisbach, flow exponent, Sch 40 consistency, exact US gpm factor |
| `check_python_hvac.py` | python-hvac | psychrolib, fluids, exact gpm and psi factors |
| `check_ezdxf.py` | ezdxf | write, read back, audit, geometry and displayed dimension text; manual open in CAD |

## Run (Windows)

Python 3.12 is needed (python-hvac does not install on 3.13). In PowerShell, in this folder:

```
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe run_all.py --tester YourGitHubHandle
```

Git must be on PATH (python-hvac installs from GitHub). Results go to `results/`, which is not committed.

## Statuses

- PASS: inside the limit set before the run.
- FAIL: outside that limit. Never widen a limit after seeing the result; explain the gap under Known limits in the entry.
- CHECK: a value to compare by eye with a source you hold. Marked "not compared yet" until someone does.
- SKIP: optional input not provided.

## Worked examples (Validated)

Enter values from your own copy of the source in `worked_examples.json`, locally. Do not commit them: entries cite document, edition and table or example number only (hub rule 2).
