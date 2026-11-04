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


# GitHub renders at most about 1950 math expressions per page; every one after that shows
# "Unable to render expression" (tested 2026-11-03 in headless Chrome). Long transcripts are split
# into parts under this many. The local count runs at or above GitHub's, so 1800 leaves margin.
MATH_CAP = 1800


def chunks(lines):
    """Split Markdown lines into parts of at most MATH_CAP math expressions, cutting only outside
    code fences and display math, so each part renders on its own. Qwen can write a whole
    transcript as one nested list, so a cut may land mid-list; the part is then dedented, since
    a page that opens on an indented line reads as code."""
    cost, safe, fence, math = [], [], None, False
    for i, ln in enumerate(lines):
        safe.append(not fence and not math and bool(ln))
        c = 0
        if fence:
            if ln.strip().startswith(fence):
                fence = None
        elif math:  # an unpaired $$ may not open display math on GitHub: count inline spans too
            math = ln.count("$$") % 2 == 0
            c = (not math) + sum(s.startswith("$") for s in SPAN.findall(ln))
        elif OPEN.match(ln):
            fence = OPEN.match(ln).group(1)
        else:
            c = sum(s.startswith("$") for s in SPAN.findall(ln))
            math = "".join(SPAN.split(ln)[::2]).count("$$") % 2 == 1
        cost.append(c)
    parts, start, n, last = [], 0, 0, None
    for i, c in enumerate(cost):
        if safe[i] and i > start:
            last = (i, n)  # cut here: lines[start:i] hold n expressions
        n += c
        if n > MATH_CAP and last:
            cut, before = last
            parts.append(lines[start:cut])
            start, n, last = cut, n - before, None
            if safe[i] and i > start:
                last = (i, n - c)
    return [parts[0]] + [dedent(p) for p in parts[1:] + [lines[start:]]] if parts else [lines]


def dedent(part):
    """Take the first line's indentation off every line of a part (not inside code fences)."""
    d = len(part[0]) - len(part[0].lstrip(" "))
    out, fence = [], None
    for ln in part:
        if fence:
            if ln.strip().startswith(fence):
                fence = None
        else:
            ln = ln[min(d, len(ln) - len(ln.lstrip(" "))):]
            m = OPEN.match(ln)
            fence = m.group(1) if m else None
        out.append(ln)
    return out


def pages(r):
    """One page, or several when the transcript has too much math for GitHub to render on one."""
    s = slug(r["id"])
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
    ]
    body = [md(r["reasoning"]) if r["reasoning"].strip() else "*(empty)*", "", "## Answer", "",
            md(r["content"]) if r["content"].strip() else "*(none: the token cap hit during thinking)*", ""]
    parts = chunks("\n".join(head + body).split("\n"))
    k = len(parts)
    name = lambda i: f"{s}.md" if i == 0 else f"{s}_p{i + 1}.md"
    out = {}
    for i, p in enumerate(parts):
        if i:  # later parts: a title and a way back
            back = f"[Previous part]({name(i - 1)})" + (f" · [Start]({name(0)})" if i > 1 else "")
            p = [f"# {r['id']}, part {i + 1} of {k}", "", back, ""] + p
        if i < k - 1:
            p = p + ["", f"*Continued in [part {i + 2} of {k}]({name(i + 1)}): GitHub stops rendering "
                         f"math on pages this long, so the transcript is split.*", ""]
        out[name(i)] = "\n".join(p)
    return out


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
        for old in out.glob(f"{s}_p*.md"):  # parts from an earlier, longer split
            old.unlink()
        for fn, text in pages(r).items():
            (out / fn).write_text(text, encoding="utf-8")
    (out / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"exported {rd.relative_to(RUNS).as_posix()}: {len(rows)} transcripts")


if __name__ == "__main__":
    runs = [find(n) for n in sys.argv[1:]] or all_runs() + sorted(
        d for d in RUNS.glob("*/*/_aborted/*") if (d / "results.jsonl").exists())
    for rd in runs:
        export(rd)
