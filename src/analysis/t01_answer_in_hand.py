r"""t01: for runs that hit the token cap, was the answer already in hand? Reads eval outputs only (results.jsonl),
so it is not a forward pass. The model never writes \boxed{} inside its reasoning on its own, so a stated answer is
either a \boxed{...} it drafts there or the math/number right after an answer phrase ("Final Answer: 76",
"the answer is $\frac{1}{2}$"). For each truncated problem, grade the first and the last stated answer against gold.
'First right' is roughly what an edit that makes the model stop at its first commitment could cash; 'any right' is
the ceiling for stopping at the best moment. For finished problems: how the reasoning ends.
Usage: python src/analysis/t01_answer_in_hand.py 0.8B/math500/base_q8 2B/math500/A64x3_8k_q8 ...
Output: logs/t01_answer_in_hand.json (all runs given)
"""
import json, re, sys
from collections import Counter
from pathlib import Path

from math_verify import parse, verify

ROOT = Path(__file__).resolve().parents[2]
BOX = "\\boxed{"
PHRASE = re.compile(r"(?i)(?:final answer|the answer is|answer is|answer:|the result is|result is)"
                    r"(?:\s*(?:seems to be|would be|should be|is|:))?\s*")
MATH = re.compile(r"\$([^$\n]{1,60})\$")
PLAIN = re.compile(r"(-?\d[\d.,/^]*(?:\s*\\?(?:sqrt|pi|frac)[\w{}]*)?)(?=\s*(?:degrees|units|cm|\.\s|\.$|,|;|\n|$|"
                   r" or | and | if | because|\)))")


def boxed(text):
    out, i = [], 0
    while True:
        i = text.find(BOX, i)
        if i < 0:
            return out
        j, depth = i + len(BOX), 1
        while j < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            j += 1
        if depth == 0:
            out.append((i, text[i + len(BOX):j - 1]))
        i = j


def candidates(text):
    """(position, answer) for every answer the reasoning states, sorted by position."""
    out = boxed(text)
    for m in PHRASE.finditer(text):
        rest = text[m.end():m.end() + 80]
        mm = MATH.match(rest) or PLAIN.match(rest)
        if mm:
            out.append((m.start(), mm.group(1).strip().rstrip(".")))
    return sorted(out)


def right(gold, ans):
    try:
        p = parse("$" + ans + "$", parsing_timeout=None)
        return bool(p) and verify(gold, p, timeout_seconds=None)
    except Exception:
        return False


def main(runs):
    res = {}
    for name in runs:
        rows = [json.loads(l) for l in open(ROOT / "runs" / name / "results.jsonl", encoding="utf-8")]
        trunc = [r for r in rows if r["finish"] == "length"]
        fin = [r for r in rows if r["finish"] != "length"]
        st, first_pos, per = Counter(), [], {}
        for r in trunc:
            gold = parse("$" + r["answer"] + "$", parsing_timeout=None)
            c = candidates(r["reasoning"])
            st["trunc"] += 1
            if not c:
                per[r["id"]] = None
                continue
            st["has_answer"] += 1
            first_pos.append(c[0][0] / max(1, len(r["reasoning"])))
            f, l = right(gold, c[0][1]), right(gold, c[-1][1])
            a = f or l or any(right(gold, b) for _, b in c[1:-1])
            st["first_right"] += f
            st["last_right"] += l
            st["any_right"] += a
            st["n_answers"] += len(c)
            per[r["id"]] = dict(first=c[0][1], last=c[-1][1], n=len(c), first_right=f, last_right=l, any_right=a,
                                first_at=round(c[0][0] / max(1, len(r["reasoning"])), 2))
        ends = Counter()
        for r in fin:
            st["fin"] += 1
            st["fin_right"] += r["correct"]
            last = [x for x in r["reasoning"].strip().split("\n") if x.strip()]
            ends[re.sub(r"[\d$\\{}^_=+\-*/().,:` ]+", " ", last[-1]).strip()[:24] if last else ""] += 1
        fp = sorted(first_pos)
        st["first_at_median"] = round(fp[len(fp) // 2], 2) if fp else None
        res[name] = dict(stats=dict(st), finished_last_line=ends.most_common(8), truncated=per)
        print(f"{name}: {st['trunc']} truncated; {st['has_answer']} state an answer in the reasoning (first one at "
              f"{st['first_at_median']} of the text, median; {st['n_answers']} statements). Right: first "
              f"{st['first_right']}, last {st['last_right']}, any {st['any_right']}. Finished {st['fin']} "
              f"({st['fin_right']} right).")
    json.dump(res, open(ROOT / "logs" / "t01_answer_in_hand.json", "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1:])
