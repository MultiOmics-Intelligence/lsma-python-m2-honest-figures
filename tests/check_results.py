"""Automatic checks for LSMA Introduction to Python, Module 2 project.

Run from the top folder of your copy:   python tests/check_results.py
It reads only the files you commit in results/ and scripts/, uses the Python
standard library only, and prints PASS or FAIL for each task.
"""
import csv
import hashlib
import re
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
SCRIPTS = ROOT / "scripts"
DATA = ROOT / "data"
_failed = []


class Fail(Exception):
    pass


def check(label):
    """Run one labelled check and print PASS or FAIL."""
    def wrap(fn):
        try:
            fn()
        except Fail as err:
            print(f"FAIL  {label}: {err}")
            _failed.append(label)
        except Exception as err:  # an unreadable file should guide, not crash
            print(f"FAIL  {label}: could not read your results ({type(err).__name__}: {err})")
            _failed.append(label)
        else:
            print(f"PASS  {label}")
        return fn
    return wrap


def finish():
    print()
    if _failed:
        print(f"{len(_failed)} check(s) failed. Read the messages above, fix that task and push again.")
        sys.exit(1)
    print("Every checkpoint passed. Well done.")


def need(path):
    path = Path(path)
    if not path.exists():
        raise Fail(f"{path.relative_to(ROOT)} not found; create it and commit it")
    return path


def read_rows(path):
    """Read a CSV (or tab-separated) file into a list of dicts with lower-case keys."""
    text = need(path).read_text(encoding="utf-8-sig")
    dialect = "excel-tab" if "\t" in text.splitlines()[0] else "excel"
    rows = list(csv.DictReader(text.splitlines(), dialect=dialect))
    return [{(k or "").strip().lower(): (v or "").strip() for k, v in r.items()} for r in rows]


def column(rows, *names, path=""):
    if not rows:
        raise Fail(f"{path} has no data rows")
    for n in names:
        if n in rows[0]:
            return n
    raise Fail(f"{path} needs a column called {names[0]}; found {', '.join(rows[0])}")


def num(value, what):
    try:
        return float(str(value).replace("%", "").strip())
    except ValueError:
        raise Fail(f"{what}: '{value}' is not a number")


def near(a, b, tol):
    return abs(a - b) <= tol


def _norm(text):
    return re.sub(r"\s+", " ", text.replace("\r", "")).strip()


def sha(path):
    return hashlib.sha256(_norm(Path(path).read_text(encoding="utf-8")).encode()).hexdigest()


def edited(path, starter_sha):
    path = need(path)
    if sha(path) == starter_sha:
        raise Fail(f"{path.relative_to(ROOT)} is still the untouched starter; write your code in it")
    return path


def png_info(path):
    """Width, height and dpi (None if not stored) of a PNG file."""
    data = Path(path).read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    w, h = struct.unpack(">II", data[16:24])
    dpi = None
    i = 8
    while i + 8 <= len(data):
        length, kind = struct.unpack(">I4s", data[i:i + 8])
        if kind == b"pHYs":
            x, _, unit = struct.unpack(">IIB", data[i + 8:i + 17])
            if unit == 1:
                dpi = x * 0.0254
            break
        if kind == b"IDAT":
            break
        i += 12 + length
    return w, h, dpi


def image(path, min_px=300, min_bytes=5000):
    """Check that a PNG or SVG is a real image of sensible size; return PNG info."""
    path = need(path)
    rel = path.relative_to(ROOT)
    size = path.stat().st_size
    if size < min_bytes:
        raise Fail(f"{rel} is only {size} bytes; it looks empty")
    if path.suffix.lower() == ".svg":
        head = path.read_text(encoding="utf-8", errors="replace")[:5000]
        if "<svg" not in head:
            raise Fail(f"{rel} is not a valid SVG file")
        return None
    info = png_info(path)
    if info is None:
        raise Fail(f"{rel} is not a real PNG file (was it renamed from another format?)")
    w, h, _ = info
    if w < min_px or h < min_px // 3:
        raise Fail(f"{rel} is only {w} x {h} pixels; save it with a higher dpi")
    return info


def text_of(path, min_words=0):
    path = need(path)
    text = path.read_text(encoding="utf-8", errors="replace")
    words = len(re.findall(r"\w+", text))
    if words < min_words:
        raise Fail(f"{path.relative_to(ROOT)} has {words} words; write at least {min_words}")
    return text


@check("Setup · Your script")
def _():
    edited(SCRIPTS / "remake_figure.py", "8e1a29347c0b1e3059748e5cade239b7a52a4b2e2687370f5c5bf09b69cc54b1")


PROBLEMS = {
    "3D": r"\b3\s*-?\s*d\b|three.dimension",
    "rainbow colours": r"rainbow|jet",
    "the truncated y-axis": r"truncat|start\w* at 5|zero|baseline of the axis|y.axis",
    "SE bars without points": r"\bse\b|standard error|error bar",
    "red-green colours": r"red.{0,6}green",
    "over-labelling": r"label",
    "the unscaled heatmap": r"unscaled|not scaled|raw|z.?score",
    "the file format": r"jpe?g|72\s*dpi|screenshot|file format",
}


@check("Task 1 · List the problems")
def _():
    text = text_of(RESULTS / "problems.md")
    items = [l for l in text.splitlines() if re.match(r"\s*(\d+[.)]|[-*])\s+\S", l)]
    if len(items) < 8:
        raise Fail(f"results/problems.md lists {len(items)} problem(s); the draft has at least eight. "
                   "Put each on its own numbered line")
    low = text.lower()
    missing = [name for name, pat in PROBLEMS.items() if not re.search(pat, low)]
    if missing:
        raise Fail(f"your list does not yet mention {missing[0]}; read the draft phrase by phrase again")
    if not re.search(r"lesson", low):
        raise Fail("name the lesson that fixes each problem")


def t975(df):
    table = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365,
             8: 2.306, 9: 2.262, 10: 2.228, 19: 2.093, 29: 2.045}
    return table[df]


@check("Task 2 · Panel A: the experiment")
def _():
    groups = {}
    for r in read_rows(DATA / "toothgrowth.csv"):
        groups.setdefault((r["supp"], float(r["dose"])), []).append(float(r["len"]))
    path = "results/panel_a_summary.csv"
    rows = read_rows(RESULTS / "panel_a_summary.csv")
    for c in ("supp", "dose", "n", "mean", "ci_low", "ci_high"):
        column(rows, c, path=path)
    if len(rows) != 6:
        raise Fail(f"expected 6 rows (one per group) in {path}, found {len(rows)}")
    names = {"oj": "OJ", "orange juice": "OJ", "vc": "VC", "ascorbic acid": "VC"}
    seen = set()
    for r in rows:
        supp = names.get(r["supp"].lower())
        key = (supp, num(r["dose"], "dose"))
        if key not in groups:
            raise Fail(f"{path}: unknown group {r['supp']} {r['dose']}; use the supp and dose values")
        seen.add(key)
        v = groups[key]
        n = len(v)
        mean = sum(v) / n
        sd = (sum((x - mean) ** 2 for x in v) / (n - 1)) ** 0.5
        half = t975(n - 1) * sd / n ** 0.5
        if int(num(r["n"], "n")) != n:
            raise Fail(f"{path}: group {r['supp']} {r['dose']} should have n = {n} (every animal shown)")
        if not near(num(r["mean"], "mean"), mean, 0.02):
            raise Fail(f"{path}: the mean of group {r['supp']} {r['dose']} is not right")
        lo, hi = num(r["ci_low"], "ci_low"), num(r["ci_high"], "ci_high")
        if near(hi - mean, sd / n ** 0.5, 0.05) or near(hi - mean, sd, 0.05):
            raise Fail(f"{path}: the interval for {r['supp']} {r['dose']} looks like an SE or SD bar, "
                       "not a 95% confidence interval")
        if not (near(lo, mean - half, 0.05) and near(hi, mean + half, 0.05)):
            raise Fail(f"{path}: the 95% confidence interval of group {r['supp']} {r['dose']} is not right "
                       "(lesson 3: mean ± t × SD / √n)")
    if len(seen) != 6:
        raise Fail(f"{path} should have one row for each of the six groups")


@check("Task 3 · Panel B: the volcano")
def _():
    de = read_rows(DATA / "de_results_example.csv")
    want = {"up": 0, "down": 0, "not significant": 0}
    for r in de:
        p, l = float(r["padj"]), float(r["log2foldchange"])
        want["up" if p < 0.05 and l > 1 else "down" if p < 0.05 and l < -1 else "not significant"] += 1
    path = "results/volcano_counts.csv"
    rows = read_rows(RESULTS / "volcano_counts.csv")
    s = column(rows, "status", path=path)
    c = column(rows, "count", path=path)
    got = {r[s].lower(): int(num(r[c], "count")) for r in rows}
    for k, v in want.items():
        if got.get(k) != v:
            raise Fail(f"{path}: the count for '{k.capitalize()}' is not right "
                       "(both thresholds: padj < 0.05 and |log2 fold change| > 1)")
    top5 = {r["gene"] for r in sorted(de, key=lambda r: float(r["padj"]))[:5]}
    labels = [l.strip() for l in text_of(RESULTS / "labelled_genes.txt").splitlines() if l.strip()]
    if len(labels) != 5:
        raise Fail(f"results/labelled_genes.txt should name exactly 5 genes, found {len(labels)}")
    if set(labels) != top5:
        raise Fail("results/labelled_genes.txt: these are not the five genes with the smallest "
                   "adjusted p-values; sort by padj")


@check("Task 4 · Panel C: the heatmap")
def _():
    order = [l.strip() for l in text_of(RESULTS / "heatmap_sample_order.txt").splitlines() if l.strip()]
    samples = [f"ctrl_{i}" for i in range(1, 5)] + [f"treat_{i}" for i in range(1, 5)]
    if sorted(order) != sorted(samples):
        raise Fail("results/heatmap_sample_order.txt should list the 8 sample names, one per line, "
                   "in the clustered order")
    if order == samples:
        raise Fail("results/heatmap_sample_order.txt is in file order; write the order from clustermap "
                   "(dendrogram_col.reordered_ind)")
    first = {s.split("_")[0] for s in order[:4]}
    if len(first) != 1:
        raise Fail("the clustered samples do not split into control and treated; did you z-score by gene?")


@check("Task 5 · Assemble and export")
def _():
    pdf = need(RESULTS / "figure.pdf")
    if pdf.read_bytes()[:5] != b"%PDF-" or pdf.stat().st_size < 10000:
        raise Fail("results/figure.pdf is not a real PDF figure; save it with fig.savefig(...pdf)")
    w, h, dpi = image(RESULTS / "figure.png", min_px=1000, min_bytes=50000)
    if dpi is None or not near(dpi, 600, 5):
        raise Fail("results/figure.png was not saved at 600 dpi")
    if not 3400 <= w <= 4450:
        raise Fail(f"results/figure.png is {w} pixels wide; at 180 mm and 600 dpi it should be "
                   "about 4,250 (a little less with bbox_inches='tight')")


@check("Task 6 · Legend and alt text")
def _():
    text = text_of(RESULTS / "legend.md", min_words=120)
    parts = re.split(r"^#+\s*", text, flags=re.M)
    heads = {p.splitlines()[0].strip().lower(): p for p in parts if p.strip()}
    for h in ("figure legend", "alt text", "greyscale check"):
        if h not in heads:
            raise Fail(f"results/legend.md needs a heading '{h.capitalize()}'")
    legend = heads["figure legend"].lower()
    for word, what in (("n =", "the number in each group (n = ...)"),
                       ("confidence", "what the error bars are"), ("z-score", "what the heatmap colours mean")):
        if word not in legend.replace("z score", "z-score").replace("n=", "n ="):
            raise Fail(f"the figure legend should say {what}")
    alt = re.findall(r"[.!?](\s|$)", heads["alt text"].split("\n", 1)[-1])
    if len(alt) < 2:
        raise Fail("write two sentences of alt text")


finish()
