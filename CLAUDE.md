# Second Serve: project memory

Read `NEW_CHAT_PROMPT.md` first and follow it. Then `handofff.md` and the bible sections it lists.

## The golden rule (never forget)

Chapters are slow and stretched out, but they must never lag. Every scene earns its length: no idling, no re-explaining, no summary where a scene belongs. Nothing can feel artificial. Every chapter needs soul: characters act from what they want (bible "Soul sheet"). The hook at the end comes out of that soul. Target about 4,000 to 5,500 words of prose, with no padding.

## The conversations are the soul of chapters

Every interaction has a purpose, a distinct voice, and a reason for the characters to engage. Relationships grow through what people say, what they avoid saying, their disagreements, their humour, and the small ways they answer each other. Scenes and conversations flow into each other. Every character has a reason to speak, every scene a reason to exist, and every ending a hook that grows from what happened.

## Grounded tone (user, Nov 22)

- No status cards, no stat letters, no named power stages in the prose or after chapters. Growth shows through training results, match performance and coach feedback.
- Sho's mind is ahead of his body. His body earns what his mind knows: visible, measurable weaknesses in strength, stamina under match conditions, landing mechanics and repeated jumping, fixed over time by training on the page.

## Editorial pass on chapters 1 to 13 (user, Nov 23)

The user's editorial prompt is saved verbatim at `planning/editorial/EDITORIAL_REVISION_PROMPT.md`. It is the review prompt for these chapters and it is binding: read it in full, never from memory, and never paraphrase it in its place. In short: restore natural, human-feeling prose; fix repetitive patterns, filler micro-actions, over-polished dialogue, overexplaining and forced literary description by judgement, not by banning; keep every chapter's soul; trim only what is truly redundant (a modest 5 to 10%, not a quota); split a chapter only for a real narrative reason; continuity is non-negotiable; when a sentence already works, leave it alone.

How it is run:
- Goal: `planning/editorial/GOAL.md` (skill `editorial-goal`). Loop: `planning/editorial/LOOP.md` (skill `editorial-loop`). Checker rubric: skill `editorial-review`. Binding rules: `planning/editorial/loop-constraints.md`. Ledger: `planning/editorial/STATE.md`. Tools: `planning/editorial/tools/`.
- Phase 1 (assessment and proposed chapter map) is report-only and ends at a hard gate. Phase 2 starts only on the user's own message approving the map, then 1 chapter per iteration with a separate checker; per-chapter approval is on by default.
- For this pass the editorial prompt governs length: the 4,000 to 5,500 word target in the golden rule does not apply to chapters 1 to 13 here. "Never lag, never artificial, always soul" still stands.
- The standing hard style rules in `NEW_CHAT_PROMPT.md` (no dashes, digits for numbers, no negative parallelisms in any form) still apply until the user says otherwise. See `STATE.md` Flags.
- Chapter 14 (the Suga POV) is on hold until the user says whether these editorial rules apply to it.

## Skills in this repo

`.claude/skills/`: `editorial-review`, `editorial-goal` and `editorial-loop` (the editorial pass above), `systematic-debugging` (obra/superpowers), `goal-loop` (sickn33/antigravity-awesome-skills, from davidondrej/skills), and the loop skills from cobusgreyling/loop-engineering (`loop-verifier` is the maker/checker reviewer pattern). Use them when they fit: the strict report-only reviewer on every chapter is the checker.
