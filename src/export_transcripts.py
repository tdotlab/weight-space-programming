"""Export runs/<name>.jsonl to readable Markdown: runs/<name>/index.md plus one file per problem.

Usage: uv run python src/export_transcripts.py            (all runs)
       uv run python src/export_transcripts.py base_qwen  (one run)
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"


def slug(uid):
    return re.sub(r"[^a-zA-Z0-9]+", "_", uid.replace("test/", "").replace(".json", ""))


def export(name):
    rows = [json.loads(l) for l in open(RUNS / f"{name}.jsonl", encoding="utf-8")]
    rows.sort(key=lambda r: r["id"])
    out = RUNS / name
    out.mkdir(exist_ok=True)
    summ = RUNS / f"{name}.summary.json"
    lines = [f"# Run: {name}\n"]
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
    print(f"exported {name}: {len(rows)} transcripts -> {out}")


if __name__ == "__main__":
    names = sys.argv[1:] or [p.stem for p in RUNS.glob("*.jsonl")]
    for n in names:
        export(n)
