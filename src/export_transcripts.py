"""Export a run's results.jsonl to Markdown: <run>/transcripts/index.md plus one file per problem.

The model's text is rendered as Markdown (not fenced), so GitHub wraps it and draws the LaTeX.
results.jsonl stays the exact record; these files are a view of it and can be regenerated any time.

Usage: uv run python src/export_transcripts.py            (all runs, _aborted included)
       uv run python src/export_transcripts.py A64x3_q8   (one run; bare name or path under runs/)
"""
import json, re, sys

from runs import ROOT, RUNS, all_runs, find

PROBLEMS = {}
for l in open(ROOT / "docs" / "math500.jsonl", encoding="utf-8"):
    d = json.loads(l)
    PROBLEMS[d["unique_id"]] = d["problem"]

SPAN = re.compile(r"(\$\$.*?\$\$|\$[^$\n]+?\$|`[^`\n]+`)")  # inline math and code: left alone
TAG = re.compile(r"<(?=[A-Za-z/!?])")                       # would be eaten as an HTML tag
RULE = re.compile(r"\s*(-{3,}|={3,})\s*")                    # would turn the line above into a heading
OPEN = re.compile(r"\s{0,3}(`{3,}|~{3,})")


LIST = re.compile(r"(\s*)([-+*]|\d+[.)])(?=\s|$)")


def art(ln):
    """Hand-drawn layout (long division, aligned sums): digits and symbols, no words outside math."""
    bare = ln.strip()
    if not bare or "$" in bare or "\\" in bare or "`" in bare:  # math or code: let it render
        return False
    return not re.search(r"[A-Za-z]{2,}", bare) and bool(re.search(r"[\d|_/=+-]", bare))


def md(text):
    """Model text -> Markdown that renders as written: one line stays one line, fences and
    display math the model left open get closed so they can't swallow the rest of the file,
    and runs of hand-drawn layout go in a monospace block so they keep their alignment.
    Qwen indents prose as if continuing a list; left alone, Markdown turns everything after
    the list's end into one code block. So indentation survives only on list items in a list."""
    out, fence, math, in_list, blank, offset = [], None, False, False, True, 0
    lines = [l.rstrip() for l in text.split("\n")]
    i = 0
    while i < len(lines):
        ln = lines[i]
        i += 1
        if fence:
            if re.fullmatch(r"\s*" + re.escape(fence[0]) + r"{%d,}\s*" % len(fence), ln):
                ln, fence = ln.strip(), None  # Qwen indents closing fences; Markdown allows 3 spaces
            out.append(ln)
            continue
        if math:
            out.append(ln)
            math = ln.count("$$") % 2 == 0
            continue
        if not ln:
            out.append("")
            blank = True
            continue
        if art(ln):
            j = i
            while j < len(lines) and art(lines[j]):
                j += 1
            if j > i:  # two or more layout lines in a row
                out += ["", "```text", *lines[i - 1:j], "```", ""]
                i, in_list, blank = j, False, True
                continue
            ln = LIST.sub(lambda m: m.group(1) + "\\" + m.group(2) if m.group(2)[0] in "-+*"
                          else m.group(1) + m.group(2)[:-1] + "\\" + m.group(2)[-1], ln, count=1)
        lm = LIST.match(ln)
        is_list = bool(lm) and not ln.lstrip().startswith("\\")
        if is_list and in_list:
            # a nested item more than 3 spaces past its parent's text is code: clamp it
            ind = min(len(lm.group(1)), offset)
            ln = " " * ind + ln.lstrip()
        else:
            ln = ln.lstrip()
        if is_list:
            m = re.match(r"\s*(?:[-+*]|\d+[.)])( *)", ln)
            gap = len(m.group(1))
            offset = len(m.group(0)) if 1 <= gap <= 4 else len(m.group(0)) - gap + 1
        in_list = is_list or (in_list and not blank)
        blank = False
        m = OPEN.match(ln)
        if m:  # a fence at column 0 ends any list, so what follows starts flush again
            fence, in_list = m.group(1), False
            out.append(ln)
            continue
        if RULE.fullmatch(ln):
            out += ["", ln]
            in_list = False
            continue
        parts = SPAN.split(ln)
        ln = "".join(p if k % 2 else TAG.sub("&lt;", p) for k, p in enumerate(parts))
        # an unpaired $$ opens a display block running over the next lines
        math = "".join(parts[::2]).count("$$") % 2 == 1
        out.append(ln + ("  " if not math else ""))  # two spaces = hard line break
    if fence:
        out.append(fence)
    if math:
        out.append("$$")
    return "\n".join(out)


def slug(uid):
    return re.sub(r"[^a-zA-Z0-9]+", "_", uid.replace("test/", "").replace(".json", ""))


def page(r):
    prob = PROBLEMS.get(r["id"])
    head = [f"# {r['id']} ({r['subject']}, level {r['level']})", ""]
    if prob:
        head += ["> " + l if l else ">" for l in md(prob).split("\n")] + [""]
    head += [
        f"**{'Correct' if r['correct'] else 'Wrong'}.** Gold `{r['answer']}`, predicted `{r['pred']}`. "
        f"Finish: {r['finish']}, {r['tokens']} tokens, {r.get('waits')} waits, {r['secs']} s.",
        "",
        "*Model text rendered as Markdown; the exact strings are in `../results.jsonl`.*",
        "",
        "## Thinking",
        "",
        md(r["reasoning"]) if r["reasoning"].strip() else "*(empty)*",
        "",
        "## Answer",
        "",
        md(r["content"]) if r["content"].strip() else "*(none: the token cap hit during thinking)*",
        "",
    ]
    return "\n".join(head)


def export(rd):
    rows = [json.loads(l) for l in open(rd / "results.jsonl", encoding="utf-8")]
    if not rows:
        return
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
        (out / f"{s}.md").write_text(page(r), encoding="utf-8")
    (out / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"exported {rd.relative_to(RUNS).as_posix()}: {len(rows)} transcripts")


if __name__ == "__main__":
    runs = [find(n) for n in sys.argv[1:]] or all_runs() + sorted(
        d for d in RUNS.glob("*/*/_aborted/*") if (d / "results.jsonl").exists())
    for rd in runs:
        export(rd)
