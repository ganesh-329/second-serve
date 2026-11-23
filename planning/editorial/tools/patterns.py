#!/usr/bin/env python3
"""Pattern counter for the editorial pass: how often each artificial-writing habit occurs per chapter.

  patterns.py [FIRST LAST]            table of counts per 1,000 words for chapters (default 1 to 13)
  patterns.py show N PATTERN [LIMIT]  prints the matching lines of chapter N (PATTERN is a column name)

These are signals for judgement, not rules. A count says where to look; the editor decides whether a
given line is a problem. Run with: python3 -I planning/editorial/tools/patterns.py
"""
import re
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import chapter as ch  # noqa: E402

PATTERNS = {
    "looked":  r"\blook(?:ed|s|ing)?\s+(?:at|up|down|across|over|back|round|away|along|past)\b",
    "eyes":    r"\beyes?\b",
    "hands":   r"\bhands?\b",
    "as_if":   r"\bas (?:if|though)\b",
    "the_way": r"\bthe way\b",
    "like":    r"\blike (?:a|an|the|somebody|someone|he|she|they|it)\b",
    "negpar":  r"(?:\b(?:It|He|She|That|This)\s+(?:wasn't|isn't|didn't|hadn't|couldn't)\b[^.\n]{0,70}\.\s+(?:It|He|She|That|They|Just)\b|\bNot [a-z]+(?:,| \w+,)?[^.\n]{0,30}\.\s+[A-Z]|\bnot\b[^.\n]{0,30},\s+but\b)",
    "micro":   r"\b(?:nodd(?:ed|ing)|nods?|shrugg?(?:ed|ing)|glanc(?:ed|ing)|blink(?:ed|ing)|shift(?:ed|ing)|paus(?:ed|ing)|looked away|turned (?:his|her) head|a beat|half a beat)\b",
    "mm":      r"\"Mm[,.]?",
    "tags":    r"\b(?:he|she|they|[A-Z][a-z]+) (?:said|asked|told|answered|replied)\b",
}


def prose_of(text, n):
    prose, _ = ch.split_chapter(text, n)
    body = prose.split("\n", 1)[1]
    return re.sub(r"^---\s*$", "", body, flags=re.M)


def paragraphs(body):
    return [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]


def short_runs(paras, maxw=7, minrun=3):
    runs, cur = 0, 0
    for p in paras:
        if not p.startswith('"') and len(p.split()) <= maxw:
            cur += 1
        else:
            runs += cur >= minrun
            cur = 0
    return runs + (cur >= minrun)


def sentence_stats(body):
    sents = [s for s in re.split(r"(?<=[.!?])[\"')]*\s+", re.sub(r"\s+", " ", body)) if s]
    lens = [len(s.split()) for s in sents]
    return (statistics.mean(lens), statistics.pstdev(lens)) if lens else (0, 0)


def row(text, n):
    body = prose_of(text, n)
    w = ch.words("x\n" + body)
    c = {k: len(re.findall(p, body)) for k, p in PATTERNS.items()}
    paras = paragraphs(body)
    dialog = sum(1 for p in paras if p.startswith('"'))
    mean, sd = sentence_stats(body)
    return w, c, len(paras), dialog, short_runs(paras), sum(1 for p in paras if len(p.split()) <= 7), mean, sd


def cmd_table(args):
    first, last = (int(args[0]), int(args[1])) if len(args) == 2 else (1, 13)
    text = ch.read_arc()
    cols = list(PATTERNS)
    print("per 1,000 words".ljust(8) + "  words " + " ".join(f"{c:>7}" for c in cols) + "  dlg% short% runs  sentLen sd")
    tot = {c: 0 for c in cols}
    tw = 0
    for n in range(first, last + 1):
        w, c, np_, dg, runs, shorts, mean, sd = row(text, n)
        tw += w
        for k in cols:
            tot[k] += c[k]
        print(f"ch {n:<5}".ljust(8) + f"{w:>7} " + " ".join(f"{c[k] * 1000 / w:>7.1f}" for k in cols)
              + f"  {100 * dg / np_:>4.0f} {100 * shorts / np_:>6.0f} {runs:>4}  {mean:>7.1f} {sd:>4.1f}")
    print("ALL".ljust(8) + f"{tw:>7} " + " ".join(f"{tot[k] * 1000 / tw:>7.1f}" for k in cols))


def cmd_show(args):
    n, name = int(args[0]), args[1]
    limit = int(args[2]) if len(args) > 2 else 12
    body = prose_of(ch.read_arc(), n)
    shown = 0
    for line in body.split("\n"):
        if re.search(PATTERNS[name], line):
            print("-", line.strip()[:230])
            shown += 1
            if shown >= limit:
                break


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "show":
        cmd_show(sys.argv[2:])
    else:
        cmd_table(sys.argv[1:])
