"""ezdxf checks: write a small MEP-style DXF, read it back, audit, compare. Lengths in mm.

Unverified. Not for stamped or issued work. Check against the adopted code edition.
"""
import math
import os
import ezdxf
from common import Report

LAYERS = {"M-DUCT-SUPP": 1, "M-PIPE-CHWS": 5, "M-PIPE-CHWR": 4, "M-ANNO-TEXT": 7}
SEGMENTS = [((0, 0), (12500, 0)), ((12500, 0), (12500, 8400)), ((12500, 8400), (30000, 8400))]  # mm


def run(examples=None, out_dir="."):
    r = Report("ezdxf")
    path = os.path.join(out_dir, "ezdxf_check.dxf")

    # 1. Write
    doc = ezdxf.new("R2018", setup=True)
    doc.header["$INSUNITS"] = 4          # 4 = millimetres
    doc.header["$MEASUREMENT"] = 1       # metric
    for name, color in LAYERS.items():
        doc.layers.add(name, color=color)
    msp = doc.modelspace()
    for a, b in SEGMENTS:
        msp.add_line(a, b, dxfattribs={"layer": "M-PIPE-CHWS"})
    msp.add_lwpolyline([(0, 600), (12500, 600), (12500, 9000)], dxfattribs={"layer": "M-PIPE-CHWR"})
    msp.add_circle((30000, 8400), radius=150, dxfattribs={"layer": "M-DUCT-SUPP"})
    msp.add_text("CHWS DN100", height=250, dxfattribs={"layer": "M-ANNO-TEXT"}).set_placement((1000, 300))
    # ezdxf's preset "EZDXF" dimstyle assumes 1 unit = 1 m and shows cm (dimlfac 100).
    # This drawing is in mm, so override to show mm at a readable size.
    dim = msp.add_linear_dim(base=(0, -1000), p1=(0, 0), p2=(12500, 0), dimstyle="EZDXF",
                             override={"dimlfac": 1, "dimtxt": 250, "dimasz": 250,
                                       "dimexo": 125, "dimexe": 125, "dimgap": 60},
                             dxfattribs={"layer": "M-ANNO-TEXT"})
    dim.render()
    doc.saveas(path)
    n_written = len(msp)

    # 2. Read back and audit
    doc2 = ezdxf.readfile(path)
    auditor = doc2.audit()
    r.abs_("2 Audit errors after read-back", len(auditor.errors), 0, 0, "count")
    r.abs_("2 Audit fixes after read-back", len(auditor.fixes), 0, 0, "count")
    msp2 = doc2.modelspace()
    r.abs_("2 Entity count round trip", len(msp2), n_written, 0, "count")
    r.true("2 Layers round trip", all(n in doc2.layers for n in LAYERS))
    r.abs_("2 $INSUNITS round trip (4 = mm)", doc2.header.get("$INSUNITS", 0), 4, 0, "-")
    r.info("2 DXF version written", doc2.dxfversion, "", "AC1032 = R2018")

    # 3. Geometry round trip: line endpoints exact, total length vs first principles
    lines = list(msp2.query('LINE[layer=="M-PIPE-CHWS"]'))
    got = sorted((tuple(l.dxf.start)[:2], tuple(l.dxf.end)[:2]) for l in lines)
    ref = sorted((tuple(map(float, a)), tuple(map(float, b))) for a, b in SEGMENTS)
    r.true("3 LINE endpoints round trip exactly", got == ref)
    total_mm = sum(math.dist(l.dxf.start, l.dxf.end) for l in lines)
    total_ref = sum(math.dist(a, b) for a, b in SEGMENTS)
    r.rel("3 CHWS run length (mm)", total_mm, total_ref, 1e-12, "-")
    r.rel("3 CHWS run length mm -> m -> mm", (total_mm / 1000) * 1000, total_ref, 1e-12, "-")
    pl_ = msp2.query("LWPOLYLINE").first
    pl_len = sum(math.dist(a, b) for a, b in zip(list(pl_.vertices()), list(pl_.vertices())[1:]))
    r.rel("3 LWPOLYLINE length (mm)", pl_len, 12500 + 8400, 1e-12, "-")
    c = msp2.query("CIRCLE").first
    r.rel("3 CIRCLE area from radius (m2)", math.pi * (c.dxf.radius / 1000) ** 2, math.pi * 0.15 ** 2, 1e-12, "-")
    dims = list(msp2.query("DIMENSION"))
    r.true("3 DIMENSION present", len(dims) == 1)
    if dims:
        r.abs_("3 DIMENSION measurement (mm)", dims[0].get_measurement(), 12500.0, 1e-9, "mm")
        # Displayed text, as CAD shows it (added 15.11.2026 after the first Windows run showed 1250000)
        blk = doc2.blocks.get(dims[0].dxf.geometry)
        texts = [e.text for e in blk if e.dxftype() == "MTEXT"] if blk else []
        r.true(f"3 DIMENSION displayed text is 12500 (got {texts})", texts == ["12500"])

    r.info("4 Manual step", "results/ezdxf_check.dxf", "",
           "open this DXF in your CAD (AutoCAD, BricsCAD or DWG TrueView): 4 layers, dimension reads 12500, text CHWS DN100")
    return r
