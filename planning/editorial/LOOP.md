# Loop: how the editorial pass is run

Cadence: manual, 1 chapter per iteration, level L1 (human-gated). It follows the user's Loop operating cadence (Plan, Build, Test, Reflect, Improve) with the maker/checker split from the `loop-verifier` skill. State lives in `STATE.md`; binding rules live in `loop-constraints.md`.

Skills used: `editorial-loop` (this procedure), `editorial-review` (the checker's rubric), `loop-constraints`, `loop-verifier`, `systematic-debugging` (when a check fails or a contradiction appears, find the cause before changing text), `minimal-fix` (the smallest edit that repairs the problem).

## Phase 1: assessment (one iteration, report-only)

1. Read `loop-constraints.md` and `STATE.md`. If `paused: yes`, stop.
2. Read `EDITORIAL_REVISION_PROMPT.md`, then every chapter 1 to 13 with its Continuity block, in order. Run `chapter.py stats`.
3. Write `PHASE1_ASSESSMENT.md` with the 3 parts the user asked for: A overall diagnosis (honest, no generic praise, with quoted examples of each artificial pattern and where momentum is lost), B chapter-by-chapter (central purpose; what works; what feels prolonged or artificial; what to preserve; light edit, moderate condensation or structural change; whether a split would genuinely help), C proposed chapter map (what stays, what splits and where, why).
4. Run the checker (a report-only agent with the `editorial-review` rubric) on the assessment itself: are the claims quoted, and does every proposed split have a real narrative reason?
5. Update `STATE.md`, commit, push, tell the user, and STOP. Phase 2 does not begin until the user's own message approves the chapter map.

## Phase 2: one chapter per iteration

Pre-flight each time: `STATE.md` says `structure_approved: yes`, `paused: no`, and the chapter's status is `queued`.

1. **Plan.** `chapter.py extract N <scratchpad dir>`. Read the chapter's Phase 1 entry, its Continuity block, the next chapter's opening, and grep later chapters (arc1, arc2, arc3, bible, handoff) for callbacks to it. Write the list of facts that must survive.
2. **Build.** Edit the prose with the smallest changes that repair real problems (artificial patterns A to E, overexplaining, micro-actions, polished dialogue, redundancy). Keep sentences that work. Do not add scenes. Additions to the Continuity block are allowed; deletions are not. Contradictions go to STATE.md "Flags", not into the text.
3. **Test, mechanical.** `lint.py`; `chapter.py stats` for the word delta; `chapter.py facts N <revised>`. Explain every missing line (replaced, moved, or cut with a reason) in the change log.
4. **Test, checker.** Spawn a report-only agent with the `editorial-review` rubric and the chapter's must-survive list. It never edits and is never the maker. Verdict: APPROVE, REJECT (numbered findings) or ESCALATE_HUMAN.
5. **Reflect and improve.** On REJECT, fix the cause and re-run steps 3 and 4. Maximum 3 attempts per chapter; after that, mark the chapter `escalated` and stop for the user.
6. **Deliver.** Save the complete revised chapter to `revised/chNN.md` and the change log to `changelog/chNN.md` (significant cuts, structural changes, continuity adjustments, flags). Update `STATE.md`.
   - If `chapter_approval: per-chapter` (the default), commit and push these files, show the user the paths and the change log, and STOP. When the user says OK, run `chapter.py replace N ...`, run `chapter.py check`, update `handofff.md`, commit and push.
   - If `chapter_approval: batch`, replace in `arc1.md` after checker APPROVE, then continue to the next chapter.
7. Always: commit and push after each chapter. Never open a PR.

## Splits and renumbering (their own iteration)

Only if the approved map contains a split. A split renumbers every later chapter and every reference to it (arc1, arc2, arc3, the bible, `handofff.md`, `planning/revision/CHAPTER_MAP.md`, Continuity labels, "Next" lines, the Arc 4 plan). Before doing it, list every file and reference that changes and get the user's OK on the list. Do the split as 1 commit, run `chapter.py check`, and update `CHAPTER_MAP.md` without losing rows.

## Budget and kill switch

- One chapter per iteration; a chapter that needs more than 3 attempts is escalated, not retried.
- Kill switch: `paused: yes` in `STATE.md`; stop immediately and say so.
- Never mark the goal achieved because budget is nearly spent. Summarise, record what is left in `STATE.md`, and stop.
