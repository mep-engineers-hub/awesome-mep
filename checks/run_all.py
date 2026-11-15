"""Run all hub tool checks and write results + draft entry files.

Usage (from the checks folder):  python run_all.py --tester YourGitHubHandle
Outputs: checks/results/RESULTS_<DD.MM.YYYY>.md and .json,
         checks/results/entries/<tool>.md (draft entries), checks/results/ezdxf_check.dxf

Unverified. Not for stamped or issued work. Check against the adopted code edition.
MIT licence.
"""
import argparse, datetime, importlib, importlib.metadata as md, json, os, platform, sys, traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from entry_meta import META      # noqa: E402

TOOLS = [("psychrolib", "check_psychrolib", "psychrolib"),
         ("pyfluids", "check_pyfluids", "pyfluids"),
         ("fluids", "check_fluids", "fluids"),
         ("python-hvac", "check_python_hvac", "python-hvac"),
         ("ezdxf", "check_ezdxf", "ezdxf")]
DEPS = ["psychrolib", "CoolProp", "pyfluids", "fluids", "ezdxf", "iapws", "pint", "python-hvac", "numpy"]


def ver(p):
    try:
        return md.version(p)
    except md.PackageNotFoundError:
        return "not installed"


def summary(c):
    return ", ".join(f"{c[k]} {k}" for k in ("PASS", "FAIL", "CHECK", "SKIP") if k in c)


def fmt(x):
    if isinstance(x, float):
        return f"{x:.10g}"
    return "" if x is None else str(x)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tester", default="<github-handle>")
    ap.add_argument("--only", nargs="*", help="run only these tools")
    a = ap.parse_args()

    out = os.path.join(HERE, "results")
    os.makedirs(os.path.join(out, "entries"), exist_ok=True)
    today = datetime.date.today().strftime("%d.%m.%Y")
    env = {"date": today, "os": platform.platform(), "python": sys.version.split()[0],
           "packages": {p: ver(p) for p in DEPS}}
    with open(os.path.join(HERE, "worked_examples.json"), encoding="utf-8") as f:
        examples = json.load(f)

    reports = {}
    for tool, mod, _ in TOOLS:
        if a.only and tool not in a.only:
            continue
        try:
            m = importlib.import_module(mod)
            rep = m.run(examples, out_dir=out) if tool == "ezdxf" else m.run(examples)
        except Exception as e:
            from common import Report
            rep = Report(tool)
            rep.error("module import/run", e)
            rep.rows[-1]["note"] += " | " + traceback.format_exc().splitlines()[-3].strip()
        reports[tool] = rep
        print(f"{tool:12s} {rep.counts()}")

    # Results file
    L = [f"# Tool check results, {today}", "",
         "> **Unverified. Not for stamped or issued work. Check against the adopted code edition.**", "",
         f"Tester: {a.tester}  ", f"OS: {env['os']}  ", f"Python: {env['python']}  ", "",
         "| Package | Version |", "| --- | --- |"] + [f"| {k} | {v} |" for k, v in env["packages"].items()]
    for tool, rep in reports.items():
        L += ["", f"## {tool}", "", f"Summary: {summary(rep.counts())}", "",
              "| Status | Check | Tool value | Reference | Difference | Limit | Unit | Note |",
              "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for r in rep.rows:
            L.append("| " + " | ".join([r["status"], r["name"], fmt(r["got"]), fmt(r["ref"]),
                     fmt(r["diff"]), fmt(r["limit"]), r["unit"], r["note"].replace("|", "/")]) + " |")
    with open(os.path.join(out, f"RESULTS_{today}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(out, f"RESULTS_{today}.json"), "w", encoding="utf-8") as f:
        json.dump({"env": env, "tester": a.tester,
                   "reports": {t: rep.rows for t, rep in reports.items()}}, f, indent=1, default=str)

    # Draft entries
    for tool, _, pkg in TOOLS:
        if tool not in reports:
            continue
        rep, m = reports[tool], META[tool]
        c = rep.counts()
        validated = any(r["name"].startswith(m["validated_prefix"]) and r["status"] == "PASS"
                        for r in rep.rows) if m.get("validated_prefix") else False
        any_fail = c.get("FAIL", 0) > 0
        tier = "Validated against a worked example (pending reviewer)" if validated and not any_fail else "Tried"
        res = [f"Ran the hub check script `checks/{dict((t, mo) for t, mo, _ in TOOLS)[tool]}.py` "
               f"on {env['os']}, Python {env['python']}. Summary: {summary(c)}.", "",
               "| Status | Check | Worst difference | Limit | Note |", "| --- | --- | --- | --- | --- |"]
        for r in rep.rows:
            if r["kind"] in ("info",):
                note = (r["note"] + "; " if r["note"] else "") + "not compared yet"
                res.append(f"| CHECK | {r['name']} | {fmt(r['got'])} {r['unit']} | | {note} |")
            else:
                res.append(f"| {r['status']} | {r['name']} | {fmt(r['diff'])} | {fmt(r['limit'])} {r['unit']} | {r['note']} |")
        body = [f"# {m['name']}", "",
                "> **Unverified. Not for stamped or issued work. Check against the adopted code edition.**", "",
                "| Field | Value |", "| --- | --- |",
                f"| Link | <{m['link']}> |", f"| What it does | {m['what']} |", f"| Area | {m['area']} |",
                f"| License | {m['license']} |", f"| Platform | {m['platform']} |",
                f"| Setup difficulty | {m['setup']} |", f"| Units | {m['units']} |",
                f"| Standard and edition | {m['standard']} |", f"| Tier | {tier} |",
                f"| Tested by | {a.tester} |", f"| Test date | {today} |",
                f"| Version tested | {ver(pkg)} (Python {env['python']}) |",
                f"| Worked example | {m['worked'] if validated else 'n/a'} |", "",
                "## Result", ""] + res + ["", "## Known limits", ""] + [f"- {k}" for k in m["limits"]] + \
               ["", "## Notes", "", m.get("notes", "None.")]
        if any_fail:
            body.insert(4, f"> ⚠ {c['FAIL']} check(s) outside the limit set before the run. Explain each under Known limits "
                           "before raising the tier; never widen a limit after seeing the result.\n")
        with open(os.path.join(out, "entries", f"{tool}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(body) + "\n")
    print(f"Wrote results/RESULTS_{today}.md and results/entries/*.md")
    return 1 if any(rep.counts().get("FAIL") for rep in reports.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
