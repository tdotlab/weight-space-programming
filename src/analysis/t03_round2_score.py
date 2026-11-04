r"""t03: score round 2 against its pre-registered predictions (logs/edit_session.md, "Predictions, written before any
round-2 eval", pushed in commit 71fda4f before any round-2 model existed). Reads eval outputs only (results.jsonl),
so it is not a forward pass. Every clause is checked exactly as written. Anything that needs judgment (which branch
of prediction 7, what a failure means) is printed as a note, not scored.

Counts use the same regexes as t02 on the reasoning text: 'Final' and 'Therefore' are case-sensitive and not preceded
by a letter. Rates are per 1000 reasoning characters over all problems the run and its reference share. A run (one
problem) "runs away" when its own 'Final' (or 'Therefore') density reaches 5 per kchar.
Usage: python src/analysis/t03_round2_score.py      (scores every prediction whose run has finished)
Output: logs/t03_round2_score.json and logs/t03_round2_score.txt
"""
import io, json, random, re, statistics as st, sys
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "runs"
RX = {"Final": re.compile(r"(?<![A-Za-z])Final"), "Therefore": re.compile(r"(?<![A-Za-z])Therefore"),
      "Final check": re.compile(r"(?<![A-Za-z])Final [Cc]heck"), "Final Answer": re.compile(r"(?<![A-Za-z])Final [Aa]nswer"),
      "Wait": re.compile(r"(?<![A-Za-z])[Ww]ait"), "No,": re.compile(r"(?<![A-Za-z])No[,.]")}
RUNAWAY = 5.0
EARLY = 2000  # a 'Final Answer' followed by more than this many reasoning chars counts as premature

_rows = [json.loads(l) for l in open(ROOT / "docs" / "math500.jsonl", encoding="utf-8")]
ORDER = [r["unique_id"] for r in random.Random(0).sample(_rows, 100)]  # eval_math.load_problems(100, 0)
HELDOUT = set(ORDER[40:])
T01 = json.load(open(ROOT / "logs" / "t01_answer_in_hand.json", encoding="utf-8"))

PRED = [
    dict(id=6, run="2B/math500/A64x3Fh_8k_q8", ref="2B/math500/A64x3_8k_q8", word="Final", n=100),
    dict(id=7, run="2B/math500/A64x3F0_8k_q8", ref="2B/math500/A64x3Fh_8k_q8", word="Final", n=100),
    dict(id=8, run="2B/math500/Fh_8k_q8", ref="2B/math500/base_8k_q8", word="Final", n=100),
    dict(id=9, run="0.8B/math500/A64x3Fh_q8", ref="0.8B/math500/A64x3_q8", word="Final", n=40),
    dict(id=10, run="0.8B/math500/A64x3F0_q8", ref="0.8B/math500/A64x3Fh_q8", word="Final", n=40),
    dict(id=11, run="2B/math500/A64x3T0_8k_q8", ref="2B/math500/A64x3_8k_q8", word="Therefore", n=100),
]


def load(name):
    p = RUNS / name / "results.jsonl"
    return {d["id"]: d for d in map(json.loads, open(p, encoding="utf-8"))} if p.exists() else {}


def sign_p(a, b):
    t, k = a + b, min(a, b)
    return min(1.0, 2 * sum(comb(t, i) for i in range(k + 1)) / 2 ** t) if t else 1.0


def aih(ref):
    """t01's answer-in-hand list for a reference run: truncated problems that stated a right answer before the cap."""
    return {k for k, v in T01[ref]["truncated"].items() if v and v["any_right"]} if ref in T01 else set()


def metrics(rows):
    fin = [x for x in rows if x["finish"] != "length"]
    kchar = sum(len(x["reasoning"]) for x in rows) / 1000
    m = dict(n=len(rows), acc=sum(x["correct"] for x in rows), trunc=len(rows) - len(fin), fin=len(fin),
             fin_wrong=sum(not x["correct"] for x in fin), tokens_median=int(st.median(x["tokens"] for x in rows)),
             fin_chars_median=int(st.median(len(x["reasoning"]) for x in fin)) if fin else None,
             per_kchar={k: round(sum(len(r.findall(x["reasoning"])) for x in rows) / kchar, 3) for k, r in RX.items()})
    for w in ("Final", "Therefore"):
        dens = sorted(((1000 * len(RX[w].findall(x["reasoning"])) / max(len(x["reasoning"]), 1),
                        len(RX[w].findall(x["reasoning"])), len(x["reasoning"]), x["id"]) for x in rows), reverse=True)
        m[f"{w}_max_run"] = [round(dens[0][0], 2), dens[0][1], dens[0][2], dens[0][3]]
        m[f"{w}_runaways"] = [[round(d, 2), c, n, i] for d, c, n, i in dens if d >= RUNAWAY]
    first, after = [], []
    for x in fin:
        ms = [q.start() for q in RX["Final"].finditer(x["reasoning"])]
        if ms:
            first.append(ms[0] / len(x["reasoning"]))
            after.append(len(x["reasoning"]) - ms[0])
    m["fin_saying_Final"] = len(first)
    m["fin_first_Final_at_median"] = round(st.median(first), 2) if first else None
    m["fin_chars_after_first_Final_median"] = int(st.median(after)) if after else None
    m["premature_Final_Answer"] = sum(1 for x in rows for q in RX["Final Answer"].finditer(x["reasoning"])
                                      if len(x["reasoning"]) - q.start() > EARLY)
    m["runs_with_premature_Final_Answer"] = sum(any(len(x["reasoning"]) - q.start() > EARLY
                                                    for q in RX["Final Answer"].finditer(x["reasoning"])) for x in rows)
    return m


def compare(run, ref, ids):
    g = sorted(i for i in ids if run[i]["correct"] and not ref[i]["correct"])
    l = sorted(i for i in ids if ref[i]["correct"] and not run[i]["correct"])
    newly_fin = sorted(i for i in ids if ref[i]["finish"] == "length" and run[i]["finish"] != "length")
    newly_trunc = sorted(i for i in ids if ref[i]["finish"] != "length" and run[i]["finish"] == "length")
    return dict(gained=g, lost=l, p=sign_p(len(g), len(l)), newly_finished=newly_fin, newly_truncated=newly_trunc)


def score(p, out, done):
    run, ref = load(p["run"]), load(p["ref"])
    if len(run) < p["n"] or not ref:
        print(f"\nPrediction {p['id']}: {p['run']} has {len(run)}/{p['n']} results"
              + ("" if ref else f"; reference {p['ref']} not finished") + ", not scored yet.")
        return None
    ids = sorted(set(run) & set(ref))
    a, b = metrics([run[i] for i in ids]), metrics([ref[i] for i in ids])
    c = compare(run, ref, ids)
    w = p["word"]
    ratio = a["per_kchar"][w] / b["per_kchar"][w] if b["per_kchar"][w] else float("inf")
    hand = aih(p["ref"]) & set(ids)
    ref_trunc = [i for i in ids if ref[i]["finish"] == "length"]
    share = len(set(c["gained"]) & hand) / len(c["gained"]) if c["gained"] else None
    res = dict(run=p["run"], ref=p["ref"], shared=len(ids), run_m=a, ref_m=b, cmp=c, ratio=round(ratio, 2),
               answer_in_hand=dict(list=len(hand), of_ref_truncated=len(ref_trunc),
                                   gained_from_list=sorted(set(c["gained"]) & hand), share=share),
               clauses=[], notes=[])
    if len(ids) == 100:
        h = [i for i in ids if i in HELDOUT]
        hc = compare(run, ref, h)
        res["heldout"] = dict(run=sum(run[i]["correct"] for i in h), ref=sum(ref[i]["correct"] for i in h), n=len(h),
                              gained=len(hc["gained"]), lost=len(hc["lost"]), p=hc["p"])

    def clause(text, ok):
        res["clauses"].append([text, bool(ok)])

    runaway_key = f"{w}_runaways"
    if p["id"] in (6, 8, 9, 11):
        lo, hi = (2, 16) if p["id"] == 9 else (1.5, 10)
        clause(f"'{w}' per kchar up {lo}x-{hi}x: {b['per_kchar'][w]} -> {a['per_kchar'][w]} (x{ratio:.2f})", lo <= ratio <= hi)
        clause(f"no run runs away ('{w}' >= {RUNAWAY}/kchar): densest {a[w + '_max_run'][:3]}", not a[runaway_key])
    if p["id"] == 6:
        clause(f"accuracy 46-54: {a['acc']}", 46 <= a["acc"] <= 54)
        clause(f"gained >= lost: +{len(c['gained'])}/-{len(c['lost'])}", len(c["gained"]) >= len(c["lost"]))
        clause(f"truncated <= 55: {a['trunc']}", a["trunc"] <= 55)
        clause(f"finished wrong <= 2: {a['fin_wrong']}", a["fin_wrong"] <= 2)
        clause(f"at least half the gains from the {len(hand)} answer-in-hand problems: "
               f"{len(res['answer_in_hand']['gained_from_list'])}/{len(c['gained'])}", share is not None and share >= 0.5)
        if ratio > 1 and a["trunc"] >= b["trunc"]:
            res["notes"].append("'Final' rose and truncation did not fall: by the pre-registered reading, the Final brake "
                                "is not a stop lever.")
    if p["id"] == 7:
        clause(f"'Final' higher than under Fh: {b['per_kchar'][w]} -> {a['per_kchar'][w]}", a["per_kchar"][w] > b["per_kchar"][w])
        A = a["acc"] > b["acc"]
        B = a["fin_wrong"] >= 3 and a["acc"] < b["acc"]
        res["branch"] = "A (more gain than Fh)" if A else "B (edge of runaway)" if B else "neither"
        res["notes"].append(f"branch: {res['branch']}; accuracy {b['acc']} -> {a['acc']}, finished wrong "
                            f"{b['fin_wrong']} -> {a['fin_wrong']}, 'Final check' per kchar {b['per_kchar']['Final check']} -> "
                            f"{a['per_kchar']['Final check']}, premature 'Final Answer's {b['premature_Final_Answer']} -> "
                            f"{a['premature_Final_Answer']}. I leaned to A.")
    if p["id"] == 8:
        clause(f"accuracy >= 26: {a['acc']}", a["acc"] >= 26)
        clause(f"gained >= lost: +{len(c['gained'])}/-{len(c['lost'])}", len(c["gained"]) >= len(c["lost"]))
        clause(f"finished wrong <= 2: {a['fin_wrong']}", a["fin_wrong"] <= 2)
        clause(f"at least half the gains from the {len(hand)} answer-in-hand problems: "
               f"{len(res['answer_in_hand']['gained_from_list'])}/{len(c['gained'])}", share is not None and share >= 0.5)
    if p["id"] == 9:
        clause(f"accuracy >= 13: {a['acc']}", a["acc"] >= 13)
        clause(f"truncated <= 27: {a['trunc']}", a["trunc"] <= 27)
        clause(f"finished wrong <= 1: {a['fin_wrong']}", a["fin_wrong"] <= 1)
    if p["id"] == 10:
        clause(f"'Final' above A64x3Fh's: {b['per_kchar'][w]} -> {a['per_kchar'][w]}", a["per_kchar"][w] > b["per_kchar"][w])
        clause(f"at least one run at {RUNAWAY}/kchar or more: {len(a[runaway_key])} (densest {a[w + '_max_run'][:3]})",
               a[runaway_key])
        clause(f"accuracy at or below A64x3Fh's: {b['acc']} -> {a['acc']}", a["acc"] <= b["acc"])
        if not a[runaway_key]:
            res["notes"].append("No run ran away: by the pre-registered reading, the runaway threshold depends on the "
                                "token, and the readout's dose limit is too cautious for rare tokens.")
    if p["id"] == 11:
        d_acc, d_tr = a["acc"] - b["acc"], a["trunc"] - b["trunc"]
        clause(f"accuracy unchanged within +-5: {b['acc']} -> {a['acc']} ({d_acc:+d})", abs(d_acc) <= 5)
        clause(f"truncation unchanged within +-5: {b['trunc']} -> {a['trunc']} ({d_tr:+d})", abs(d_tr) <= 5)
        fh = done.get(6)
        if fh:
            d_fh = fh["run_m"]["acc"] - fh["ref_m"]["acc"]
            res["notes"].append(f"Fh moved accuracy {d_fh:+d}, T0 {d_acc:+d}. "
                                + ("T0 moved it as much as Fh: by the pre-registered reading, the Fh effect is generic "
                                   "brake removal." if d_fh and abs(d_acc) >= abs(d_fh) else
                                   "T0 moved it less than Fh."))
    out[p["id"]] = res
    return res


def show(p, r):
    a, b, c = r["run_m"], r["ref_m"], r["cmp"]
    ok = sum(x[1] for x in r["clauses"])
    print(f"\nPrediction {p['id']}: {p['run']} vs {p['ref']} ({r['shared']} shared problems). "
          f"{ok}/{len(r['clauses'])} clauses hold.")
    for t, v in r["clauses"]:
        print(f"  {'PASS' if v else 'FAIL'}  {t}")
    for n in r["notes"]:
        print(f"  note: {n}")
    print(f"  accuracy {b['acc']} -> {a['acc']} (+{len(c['gained'])}/-{len(c['lost'])}, sign test p {c['p']:.3g}); "
          f"truncated {b['trunc']} -> {a['trunc']} (newly finished {len(c['newly_finished'])}, newly truncated "
          f"{len(c['newly_truncated'])}); finished wrong {b['fin_wrong']} -> {a['fin_wrong']}")
    if "heldout" in r:
        h = r["heldout"]
        print(f"  held-out 60: {h['ref']} -> {h['run']} (+{h['gained']}/-{h['lost']}, p {h['p']:.3g})")
    ah = r["answer_in_hand"]
    print(f"  answer-in-hand ({ah['list']} of the reference's {ah['of_ref_truncated']} truncated): gains from it "
          f"{len(ah['gained_from_list'])}/{len(c['gained'])} {ah['gained_from_list']}")
    print(f"  per kchar: {b['per_kchar']} -> {a['per_kchar']}")
    print(f"  finished runs saying 'Final' {b['fin_saying_Final']}/{b['fin']} -> {a['fin_saying_Final']}/{a['fin']}; first "
          f"'Final' at {b['fin_first_Final_at_median']} -> {a['fin_first_Final_at_median']} of the text, then "
          f"{b['fin_chars_after_first_Final_median']} -> {a['fin_chars_after_first_Final_median']} chars to the end; "
          f"finished median length {b['fin_chars_median']} -> {a['fin_chars_median']} chars; median tokens "
          f"{b['tokens_median']} -> {a['tokens_median']}")
    print(f"  premature 'Final Answer' (>{EARLY} chars before the end): {b['premature_Final_Answer']} in "
          f"{b['runs_with_premature_Final_Answer']} runs -> {a['premature_Final_Answer']} in "
          f"{a['runs_with_premature_Final_Answer']} runs; densest 'Final' run {b['Final_max_run'][:3]} -> {a['Final_max_run'][:3]}")
    print(f"  gained {c['gained']}\n  lost {c['lost']}")


def main():
    buf, real = io.StringIO(), sys.stdout

    class Tee:
        def write(self, s):
            real.write(s)
            buf.write(s)

        def flush(self):
            real.flush()

    sys.stdout = Tee()
    out = {}
    for p in PRED:
        r = score(p, out, out)
        if r:
            show(p, r)
    sys.stdout = real
    json.dump(out, open(ROOT / "logs" / "t03_round2_score.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    (ROOT / "logs" / "t03_round2_score.txt").write_text(buf.getvalue(), encoding="utf-8")


if __name__ == "__main__":
    main()
