"""Compare eval runs on the problems they share (default: those in the first run listed after the reference).

Usage: .venv/Scripts/python.exe src/compare_runs.py base_q8 P64_q8 R64_q8 [...]
Prints acc / truncated / finished and self-doubt marker rates per 1000 reasoning chars, all restricted to the
problem ids every listed run has completed, so partial runs compare fairly.
"""
import json, re, statistics as st, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKERS = {
    "Wait": r"(?<![A-Za-z])[Ww]ait",
    "No,": r"(?<![A-Za-z])No[,.]",
    "Actually": r"Actually,",
    "Let me re": r"Let me re-?(?:check|verify|examine|read|consider)",
    "Hmm": r"Hmm",
    "But": r"\nBut ",
}


def load(name):
    p = ROOT / "runs" / f"{name}.jsonl"
    return {d["id"]: d for d in map(json.loads, open(p, encoding="utf-8"))} if p.exists() else {}


def main(names):
    runs = {n: load(n) for n in names}
    common = set.intersection(*(set(r) for r in runs.values() if r)) if any(runs.values()) else set()
    print(f"{len(common)} problems shared by: {', '.join(n for n, r in runs.items() if r)}")
    for n, r in runs.items():
        g = [r[i] for i in common if i in r]
        if not g:
            print(f"{n:10s} (no results yet)")
            continue
        fin = [x for x in g if x["finish"] != "length"]
        kchar = sum(len(x["reasoning"]) for x in g) / 1000
        rates = {k: round(sum(len(re.findall(v, x["reasoning"])) for x in g) / kchar, 2) for k, v in MARKERS.items()}
        print(f"{n:10s} acc {sum(x['correct'] for x in g):3d}/{len(g)}  trunc {len(g) - len(fin):3d}  "
              f"fin {len(fin):3d} (correct {sum(x['correct'] for x in fin)})  "
              f"tokens med {int(st.median(x['tokens'] for x in g))}  per kchar {rates}")


if __name__ == "__main__":
    main(sys.argv[1:])
