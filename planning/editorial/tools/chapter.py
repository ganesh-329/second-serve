#!/usr/bin/env python3
"""Chapter tools for arc1.md (chapters 1 to 18).

  chapter.py stats [FIRST LAST]       prose words per chapter (default 1 to 13) and the total
  chapter.py extract N OUTDIR         writes OUTDIR/chNN_prose.md and OUTDIR/chNN_cont.md (LF)
  chapter.py replace N PROSE CONT     rewrites chapter N of arc1.md in place, CRLF kept
  chapter.py check                    verifies extract then replace is a no-op for chapters 1 to 13
  chapter.py facts N PROSE            lists quoted lines, *italic* thoughts and scores named in chapter N's
                                      current Continuity block that are missing from PROSE (a prompt for
                                      human or checker judgement, since Continuity bullets paraphrase)

"Prose" is the chapter from its "## Chapter N:" heading up to its "**Continuity (ch N)**" block.
Word counts exclude the heading line and the "---" scene breaks.
Run with: python3 -I planning/editorial/tools/chapter.py ...
"""
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ARC = ROOT / "arc1.md"


def read_arc():
    return ARC.read_text(encoding="utf-8", newline="")


def bounds(text, n):
    start = text.index(f"## Chapter {n}:")
    nxt = text.find(f"## Chapter {n + 1}:")
    end = len(text) if nxt == -1 else nxt
    return start, end


def split_chapter(text, n):
    start, end = bounds(text, n)
    chunk = text[start:end].replace("\r\n", "\n")
    m = re.search(r"\*\*Continuity \(ch %d\b" % n, chunk)
    if not m:
        raise SystemExit(f"chapter {n}: no Continuity block found")
    return chunk[: m.start()].rstrip("\n"), chunk[m.start():].strip("\n")


def words(prose):
    body = prose.split("\n", 1)[1] if "\n" in prose else prose
    body = re.sub(r"^---\s*$", "", body, flags=re.M)
    return len(re.findall(r"\b[\w'-]+\b", body))


def cmd_stats(args):
    first, last = (int(args[0]), int(args[1])) if len(args) == 2 else (1, 13)
    text = read_arc()
    total = 0
    for n in range(first, last + 1):
        prose, _ = split_chapter(text, n)
        title = prose.split("\n", 1)[0].replace("## ", "")
        w = words(prose)
        total += w
        print(f"{title:<42} {w:>6}")
    print(f"{'TOTAL':<42} {total:>6}")


def cmd_extract(args):
    n, out = int(args[0]), Path(args[1])
    out.mkdir(parents=True, exist_ok=True)
    prose, cont = split_chapter(read_arc(), n)
    (out / f"ch{n:02d}_prose.md").write_text(prose + "\n", encoding="utf-8", newline="")
    (out / f"ch{n:02d}_cont.md").write_text(cont + "\n", encoding="utf-8", newline="")
    print(f"wrote {out}/ch{n:02d}_prose.md ({words(prose)} words) and ch{n:02d}_cont.md")


def build(prose_text, cont_text):
    return (prose_text.rstrip("\n") + "\n\n" + cont_text.strip("\n") + "\n\n").replace("\r\n", "\n").replace("\n", "\r\n")


def cmd_replace(args):
    n = int(args[0])
    prose = Path(args[1]).read_text(encoding="utf-8")
    cont = Path(args[2]).read_text(encoding="utf-8")
    if not prose.lstrip().startswith(f"## Chapter {n}:"):
        raise SystemExit(f"prose file must start with '## Chapter {n}:'")
    if not re.match(r"\*\*Continuity \(ch %d\b" % n, cont.lstrip()):
        raise SystemExit(f"continuity file must start with '**Continuity (ch {n}...'")
    text = read_arc()
    start, end = bounds(text, n)
    new = text[:start] + build(prose, cont) + text[end:]
    ARC.write_text(new, encoding="utf-8", newline="")
    print(f"replaced chapter {n}: {end - start} -> {len(build(prose, cont))} chars")


SKIP_BULLET = re.compile(r"^\s*-\s*\**(for ch|next|review fixes)", re.I)


def tokens(t):
    t = t.replace("\u201c", '"').replace("\u201d", '"').replace("\u2019", "'").replace("\u2018", "'")
    return re.findall(r"[a-z0-9']+", t.lower())


def present(fact_tokens, prose_tokens, prose_bigrams):
    """Exact run for short facts; for longer ones, 75% of word pairs must appear in the prose.
    The looser test survives a dialogue tag cutting a quoted line in two."""
    k = len(fact_tokens)
    if k == 0:
        return True
    if k <= 3:
        return any(prose_tokens[i:i + k] == fact_tokens for i in range(len(prose_tokens) - k + 1))
    pairs = list(zip(fact_tokens, fact_tokens[1:]))
    return sum(1 for pr in pairs if pr in prose_bigrams) / len(pairs) >= 0.75


def cmd_facts(args):
    n = int(args[0])
    prose_tokens = tokens(Path(args[1]).read_text(encoding="utf-8"))
    prose_bigrams = set(zip(prose_tokens, prose_tokens[1:]))
    cont = split_chapter(read_arc(), n)[1].replace("\u201c", '"').replace("\u201d", '"')
    wanted = []
    for line in cont.split("\n"):
        if SKIP_BULLET.match(line):
            continue
        line = line.replace("**", "")
        for q in re.findall(r'"([^"\n]*)"', line):          # pair quotes first, filter by length after
            wanted += [f for f in re.split(r"\.\.\.|\u2026", q)]
        wanted += re.findall(r"\*([^*\n]+?)\*", line)
    facts = []
    for w in wanted:
        tk = tokens(w)
        if len(tk) >= 3 and tk not in [f[1] for f in facts]:
            facts.append((w.strip(), tk))
    scores = sorted(set(re.findall(r"\b\d{1,2}-\d{1,2}\b", "\n".join(l for l in cont.split("\n") if not SKIP_BULLET.match(l)))))
    prose_text = " ".join(prose_tokens)
    miss = [w for w, tk in facts if not present(tk, prose_tokens, prose_bigrams)]
    miss_scores = [x for x in scores if x.replace("-", " ") not in prose_text and x not in Path(args[1]).read_text(encoding="utf-8")]
    print(f"chapter {n}: {len(facts) - len(miss)} of {len(facts)} quoted or italic facts present; "
          f"{len(scores) - len(miss_scores)} of {len(scores)} scores present")
    for w in miss:
        print("  missing line:  ", w)
    for x in miss_scores:
        print("  missing score: ", x)


def cmd_check(_):
    text = read_arc()
    bad = 0
    for n in range(1, 14):
        prose, cont = split_chapter(text, n)
        start, end = bounds(text, n)
        if build(prose, cont) != text[start:end]:
            print(f"chapter {n}: round trip differs")
            bad += 1
    print("round trip OK for chapters 1 to 13" if not bad else f"{bad} chapter(s) differ")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    cmds = {"stats": cmd_stats, "extract": cmd_extract, "replace": cmd_replace, "check": cmd_check, "facts": cmd_facts}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        raise SystemExit(__doc__)
    cmds[sys.argv[1]](sys.argv[2:])
