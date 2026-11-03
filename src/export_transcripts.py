"""Export a run's results.jsonl to readable Markdown: <run>/transcripts/index.md plus one file per problem.

Usage: uv run python src/export_transcripts.py            (all runs)
       uv run python src/export_transcripts.py A64x3_q8   (one run; bare name or path under runs/)
"""
import json, re, sys

from runs import RUNS, all_runs, find


def slug(uid):
    return re.sub(r"[^a-zA-Z0-9]+", "_", uid.replace("test/", "").replace(".json", ""))


def export(rd):
    rows = [json.loads(l) for l in open(rd / "results.jsonl", encoding="utf-8")]
    rows.sort(key=lambda r: r["id"])
    out = rd / "transcripts"
    out.mkdir(exist_ok=True)
    summ = rd / "summary.json"
    lines = [f"# Run: {rd.relative_to(RUNS).as_posix()}\n"]
    if summ.exists():
        lines.append("```json\n" + summ.read_text(encoding="utf-8") + "\n```\n")
    lines.append("| problem | level | correct | finish | tokens | waits/kchar | gold | pred |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in rows:
        s = slug(r["id"])
        lines.append(f"| [{s}]({s}.md) | {r['level']} | {'Y' if r['correct'] else 'n'} | {r['finish']} | "
                     f"{r['tokens']} | {r.get('waits_per_kchar', '')} | `{r['answer']}` | `{r['pred']}` |")
        body = [
            f"# {r['id']}  ({r['subject']}, level {r['level']})\n",
            f"- gold: `{r['answer']}`\n- pred: `{r['pred']}`\n- correct: {r['correct']}\n"
            f"- finish: {r['finish']}, tokens: {r['tokens']}, waits: {r.get('waits')}, secs: {r['secs']}\n",
            "## Thinking (reasoning_content)\n", "````text", r["reasoning"], "````\n",
            "## Answer (content)\n", "````text", r["content"], "````\n",
        ]
        (out / f"{s}.md").write_text("\n".join(body), encoding="utf-8")
    (out / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"exported {rd.relative_to(RUNS).as_posix()}: {len(rows)} transcripts")


if __name__ == "__main__":
    for rd in [find(n) for n in sys.argv[1:]] or all_runs():
        export(rd)
