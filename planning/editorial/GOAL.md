# Goal: editorial pass on Second Serve, chapters 1 to 13

Written Nov 23, 2026 in the 5-part contract format of the `goal-loop` skill. The user types `/goal` in front of the block below; Claude cannot set a goal itself and must not claim one is running unless the host confirms it.

The contract points at files instead of restating them, so it stays short. The user's prompt in `EDITORIAL_REVISION_PROMPT.md` is binding and is never summarised in place of the original.

```
**Objective:** Carry out the editorial revision of Second Serve chapters 1 to 13 exactly as the user specified in planning/editorial/EDITORIAL_REVISION_PROMPT.md: Phase 1 (assessment and proposed chapter map) first, then, only after the user approves the chapter map, Phase 2 (chapter-by-chapter revision).
**Read first:** CLAUDE.md; planning/editorial/EDITORIAL_REVISION_PROMPT.md (binding, verbatim); planning/editorial/STATE.md; planning/editorial/LOOP.md; planning/editorial/loop-constraints.md; NEW_CHAT_PROMPT.md (standing story and style rules); handofff.md; "story bible.md" (Revision of ch 1 to 34, Soul sheet, Original nouns); chapters 1 to 13 and their Continuity blocks in arc1.md; planning/revision/CHAPTER_MAP.md.
**Constraints:** Hard gate: do NOT start Phase 2 until the user's own message approves the chapter map. Edit only chapters 1 to 13 (and the files named in loop-constraints.md). Keep every Continuity fact, callback, score, timeline and canon divergence; flag contradictions in STATE.md instead of fixing them silently. When a sentence already works, leave it alone. No new scenes unless needed to repair a real narrative problem. Standing hard style rules in NEW_CHAT_PROMPT.md still apply (no dashes, digits for numbers, no negative parallelisms). Do not refactor anything outside the chapters. Do not open a PR.
**Validate:** `python3 -I planning/editorial/tools/chapter.py check` after any change to arc1.md (must print "round trip OK"); for each revised chapter `python3 -I planning/editorial/tools/lint.py <revised file>` and `python3 -I planning/editorial/tools/chapter.py facts N <revised file>` (every missing line explained in the change log), then a report-only checker verdict of APPROVE using the editorial-review skill.
**Document:** Write concise, targeted documentation for all changes: Phase 1 goes in planning/editorial/PHASE1_ASSESSMENT.md, every chapter gets planning/editorial/changelog/chNN.md, STATE.md and handofff.md are updated at every checkpoint.
**Checkpoints:** Work one chapter per checkpoint, commit and push to the branch after each, and give a one-line status each time: what is being done and whether it is on track.
**Stop when:** (a) Phase 1 is delivered and the chapter map is waiting for the user's approval; or (b) after approval, every chapter in the approved map is revised, checker APPROVE, Continuity updated, handoff updated and pushed; OR when any step needs the user (a continuity contradiction, a split or renumbering, a conflict between rules, 3 failed attempts on one chapter). Do not delete, skip, weaken or narrow any check, Continuity bullet or the checker rubric to make the goal pass.
```

## Why this shape

- The stop condition has 2 honest finish lines. Stopping at the approval gate after Phase 1 is correct behaviour, not a failure; the lifecycle state there is "unmet, waiting for the user".
- The Validate line is mechanical where it can be (round trip, lint, facts) and a separate checker agent where it can't be (voice, naturalness, continuity judgement). The maker never grades its own chapter.
- "Leave it alone when it works" and "no new scenes" are in the constraints because the user said rewriting is not improving.
