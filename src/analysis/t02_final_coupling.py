r"""t02: is 'Final' a stop signal? Reads eval outputs only (results.jsonl), so it is not a forward pass.
Round 2 plans to weaken the brake on 'Final'. That only helps if saying 'Final' leads to stopping. For every run:
where the capitalised word 'Final' first appears in the reasoning (fraction of the text), how many characters
follow the first and the last one before the reasoning ends, what follows it ('Final Answer', 'Final check'...),
and whether runs that say 'Final' finish. Also 'Therefore' for comparison.
Usage: python src/analysis/t02_final_coupling.py 2B/math500/A64x3_8k_q8 ...
Output: logs/t02_final_coupling.json
"""
import json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORDS = {"Final": re.compile(r"(?<![A-Za-z])Final"), "Therefore": re.compile(r"(?<![A-Za-z])Therefore")}


def med(xs):
    xs = sorted(xs)
    return xs[len(xs) // 2] if xs else None


def main(runs):
    out = {}
    for name in runs:
        rows = [json.loads(l) for l in open(ROOT / "runs" / name / "results.jsonl", encoding="utf-8")]
        res = {}
        for w, rx in WORDS.items():
            st = Counter()
            first_at, tail_first, tail_last, nxt = [], [], [], Counter()
            for r in rows:
                txt = r["reasoning"]
                ms = [m.start() for m in rx.finditer(txt)]
                fin = r["finish"] != "length"
                st["fin" if fin else "trunc"] += 1
                if not ms:
                    continue
                st[("fin" if fin else "trunc") + "_with"] += 1
                st[("fin" if fin else "trunc") + "_count"] += len(ms)
                if fin:
                    st["fin_with_right"] += r["correct"]
                    first_at.append(ms[0] / max(1, len(txt)))
                    tail_first.append(len(txt) - ms[0])
                    tail_last.append(len(txt) - ms[-1])
                for p in ms:
                    nxt[" ".join(txt[p:p + 40].split()[:2])[:24]] += 1
            st["fin_without_right"] = sum(r["correct"] for r in rows if r["finish"] != "length"
                                          and not rx.search(r["reasoning"]))
            res[w] = dict(stats=dict(st), first_at_median=med(first_at), chars_after_first_median=med(tail_first),
                          chars_after_last_median=med(tail_last), next_words=nxt.most_common(8))
            print(f"{name} {w!r}: finished {st['fin']} ({st['fin_with']} say it, {st['fin_count']} times; first at "
                  f"{res[w]['first_at_median'] and round(res[w]['first_at_median'], 2)} of the text, then "
                  f"{res[w]['chars_after_first_median']} chars to the end, {res[w]['chars_after_last_median']} after the "
                  f"last); truncated {st['trunc']} ({st['trunc_with']} say it, {st['trunc_count']} times). "
                  f"Right when finished: with {st['fin_with_right']}, without {st['fin_without_right']}. "
                  f"Next: {nxt.most_common(5)}")
        out[name] = res
    json.dump(out, open(ROOT / "logs" / "t02_final_coupling.json", "w", encoding="utf-8"), indent=1,
              ensure_ascii=False)


if __name__ == "__main__":
    main(sys.argv[1:])
