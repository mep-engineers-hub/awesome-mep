"""Shared check helpers. SI internally. MIT licence (hub rule 1).

Unverified. Not for stamped or issued work. Check against the adopted code edition.
"""
import math

class Report:
    def __init__(self, tool):
        self.tool = tool
        self.rows = []      # dicts: name, kind, got, ref, diff, limit, unit, status, note

    def _add(self, **kw):
        self.rows.append(kw)
        return kw["status"] == "PASS"

    def rel(self, name, got, ref, limit, unit="", note=""):
        """Relative difference |got-ref|/|ref| must be <= limit."""
        d = abs(got - ref) / abs(ref) if ref != 0 else abs(got - ref)
        ok = math.isfinite(got) and d <= limit
        return self._add(name=name, kind="rel", got=got, ref=ref, diff=d, limit=limit,
                         unit=unit, status="PASS" if ok else "FAIL", note=note)

    def abs_(self, name, got, ref, limit, unit="", note=""):
        """Absolute difference |got-ref| must be <= limit (in unit)."""
        d = abs(got - ref)
        ok = math.isfinite(got) and d <= limit
        return self._add(name=name, kind="abs", got=got, ref=ref, diff=d, limit=limit,
                         unit=unit, status="PASS" if ok else "FAIL", note=note)

    def true(self, name, cond, note=""):
        return self._add(name=name, kind="bool", got=bool(cond), ref=True, diff=None,
                         limit=None, unit="", status="PASS" if cond else "FAIL", note=note)

    def info(self, name, value, unit="", note=""):
        """Value for the engineer to check by eye against a source he holds."""
        return self._add(name=name, kind="info", got=value, ref=None, diff=None,
                         limit=None, unit=unit, status="CHECK", note=note)

    def skip(self, name, note):
        return self._add(name=name, kind="skip", got=None, ref=None, diff=None,
                         limit=None, unit="", status="SKIP", note=note)

    def error(self, name, exc):
        return self._add(name=name, kind="error", got=None, ref=None, diff=None, limit=None,
                         unit="", status="FAIL", note=f"{type(exc).__name__}: {exc}")

    def counts(self):
        c = {}
        for r in self.rows:
            c[r["status"]] = c.get(r["status"], 0) + 1
        return c


def worst(report, prefix):
    """Worst row (largest diff/limit ratio) among rows whose name starts with prefix."""
    rows = [r for r in report.rows if r["name"].startswith(prefix) and r["limit"]]
    return max(rows, key=lambda r: r["diff"] / r["limit"]) if rows else None


def sweep(report, label, items, limit, unit, kind="rel"):
    """Collapse a parameter sweep into one row: the worst point, plus point count.

    items: iterable of (point_label, got, ref).
    """
    worst_pt, worst_d, n, fails = None, -1.0, 0, 0
    for pt, got, ref in items:
        n += 1
        if kind == "rel":
            d = abs(got - ref) / abs(ref) if ref != 0 else abs(got - ref)
        else:
            d = abs(got - ref)
        if not math.isfinite(got) or d > limit:
            fails += 1
        if not math.isfinite(d) or d > worst_d:
            worst_pt, worst_d, wg, wr = pt, d, got, ref
    status = "PASS" if fails == 0 and n > 0 else "FAIL"
    report.rows.append(dict(name=label, kind=kind, got=wg, ref=wr, diff=worst_d, limit=limit,
                            unit=unit, status=status,
                            note=f"{n} points, {fails} outside limit, worst at {worst_pt}"))
    return status == "PASS"
