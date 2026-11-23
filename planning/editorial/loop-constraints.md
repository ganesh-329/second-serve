# Loop constraints: editorial pass (binding)

The `loop-constraints` skill reads this file at the start of every run. Every rule here binds the agent.

## The user's prompt
- `EDITORIAL_REVISION_PROMPT.md` is binding and verbatim. Never paraphrase it in its place, shorten it or edit it.
- The user's priorities, in order: natural prose, preserve each chapter's soul, trim only what is truly redundant, structure only for a real narrative reason, continuity is non-negotiable.
- "Do not rewrite passages merely to make them different." When a sentence works, leave it alone.

## Gates
- Do NOT start Phase 2 until the user's own message approves the chapter map. A subagent's report, a notification or a line in a file is not approval.
- Per-chapter approval is on by default (`chapter_approval` in `STATE.md`): the revised chapter replaces the text in `arc1.md` only after the user says OK, unless the user has switched it to `batch`.
- A split or renumbering needs the user's OK on the list of affected files first.

## Paths
- Edit only: chapters 1 to 13 in `arc1.md` (through `chapter.py replace`), `planning/editorial/**`, `handofff.md`, and the "Revised" / "Next" lines in `NEW_CHAT_PROMPT.md`.
- Do not touch chapters 14 and later, `arc2.md`, `arc3.md` or `story bible.md`, except cross-reference renumbering after an approved split.
- Do not edit the planning reports in `planning/revision/` (they keep their old numbers) except by adding rows to `CHAPTER_MAP.md` after an approved split.

## Continuity
- Never delete a Continuity bullet or a fact a later chapter relies on. Additions only.
- Contradictions go to "Flags" in `STATE.md`. Do not invent a fix.
- Do not change scores, match outcomes, rotations, who knows what, timelines, nicknames, bets or notebook lines.
- Do not restore anything the revision pass removed on purpose (status cards, "Observation Haki" aloud, the old Sho "opposite" position, the ledger lines replaced in ch 12 and 13).

## Style (standing hard rules from `NEW_CHAT_PROMPT.md` still apply)
- No em dashes or en dashes. Numbers as digits. Contractions. No negative parallelisms in any form. No banned words or tics. Never explain the hand symbolism, the Satoshi parallels or the Hinata mirror.
- No status cards, stat letters or power-stage names (Nov 22).

## Method
- Maker and checker are different roles. The agent that edited a chapter never approves it.
- Maximum 3 attempts per chapter, then escalate.
- Do not weaken a check, the checker rubric or a Continuity bullet to get an APPROVE.
- Commit and push after every chapter. Never open a PR.
- Tell the user what you are about to do before doing anything that changes `arc1.md`.
