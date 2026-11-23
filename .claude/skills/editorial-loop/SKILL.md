---
name: editorial-loop
description: The loop that carries out the Second Serve editorial pass: Phase 1 assessment, then (after the user approves the chapter map) one chapter per iteration through plan, build, test, reflect, improve with a separate checker. Use when running or resuming the editorial pass.
user_invocable: true
---

# Editorial loop

Full procedure: `planning/editorial/LOOP.md`. Binding rules: `planning/editorial/loop-constraints.md` (read it at the start of every run, as the `loop-constraints` skill requires). State: `planning/editorial/STATE.md`. Tools: `planning/editorial/tools/` (`python3 -I ... chapter.py stats | extract | replace | check | facts`, `lint.py`).

## Every run starts the same way

1. Read `loop-constraints.md` and `STATE.md`. If `paused: yes`, stop and say so.
2. Read `EDITORIAL_REVISION_PROMPT.md` again. Do not work from memory of it.
3. Decide the step from `STATE.md`:
   - `phase: 1`, assessment not started: run Phase 1, then stop (the approval gate).
   - `phase: 1`, assessment delivered: wait for the user's approval. Do nothing else.
   - `phase: 2`, `structure_approved: yes`: take the next `queued` chapter.
4. Tell the user what you are about to do before you change `arc1.md`.

## One chapter (Phase 2)

Plan, build, test, reflect, improve, deliver, in the order set out in `LOOP.md`:

- **Plan:** extract the chapter, read its Phase 1 entry and Continuity block and the next chapter's opening, grep later chapters for callbacks, write the must-survive list.
- **Build (maker):** the smallest edits that repair real problems. When a sentence works, leave it alone. No new scenes. Continuity additions only; contradictions go to `STATE.md` Flags. Use `systematic-debugging` when something fails: find the cause before changing text. Use the `minimal-fix` stance: the smallest change, never a rewrite for its own sake.
- **Test:** `lint.py`, `chapter.py stats` (word delta), `chapter.py facts N <file>`, then the checker: a separate report-only agent given the `editorial-review` skill, the revised chapter, the original, the must-survive list and the mechanical results. The maker never approves its own chapter.
- **Reflect and improve:** on REJECT, repair the cause and re-test. Maximum 3 attempts; then mark `escalated` and stop.
- **Deliver:** `revised/chNN.md` (the complete revised chapter) and `changelog/chNN.md` (significant cuts, structural changes, continuity adjustments, flags), update `STATE.md`, commit and push. In `per-chapter` mode stop for the user's OK, then `chapter.py replace N`, `chapter.py check`, update `handofff.md`, commit and push. Never open a PR.

## Speaking to the user

Plain, short, direct English. After each chapter: what changed (word delta, what was cut and why), what the checker found, what was flagged, what is waiting on them. Do not paste the chapter back into chat; give the path, and the change log.

## Do not

- Start Phase 2 without the user's own approval of the chapter map.
- Touch chapter 14 or later, `arc2.md`, `arc3.md` or the bible (except approved renumbering).
- Split or renumber without the user's OK on the list of affected files.
- Weaken a check or drop a Continuity bullet to get an APPROVE.
- Treat a quiet, ordinary scene as a useless one.
