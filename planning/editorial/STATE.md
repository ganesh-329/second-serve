# Editorial pass state

Last updated: Nov 23, 2026. This file is the loop's ledger. Keep it true; never let it replace looking at the actual chapters.

```
phase: 1                      # 1 = assessment (report-only), 2 = revision
structure_approved: no        # only the user's own message can set this to yes
chapter_approval: per-chapter # per-chapter | batch (user's choice; per-chapter is the safe default)
paused: no                    # kill switch: yes = stop immediately and say so
assessment: drafted, checker review pending   # planning/editorial/PHASE1_ASSESSMENT.md
```

## Baseline (chapter.py stats, Nov 23, before the pass)

Words of prose, heading and scene breaks excluded. 5 to 10% off the total is the user's orientation (about 50,300 to 53,100), not a quota.

| Ch | Title | Words | Phase 1 verdict | Status | Checker attempts | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ball to the face | 5,575 | | queued | 0 | |
| 2 | The wig | 4,611 | | queued | 0 | |
| 3 | Dawn reps | 4,802 | | queued | 0 | |
| 4 | The King | 4,814 | | queued | 0 | |
| 5 | Eyes closed | 3,345 | | queued | 0 | |
| 6 | Jackets | 3,600 | | queued | 0 | |
| 7 | Blue castle | 4,847 | | queued | 0 | |
| 8 | Bottle cap | 4,435 | | queued | 0 | |
| 9 | Grand King | 4,620 | | queued | 0 | |
| 10 | Guardian deity | 4,079 | | queued | 0 | |
| 11 | The ace who left | 3,949 | | queued | 0 | |
| 12 | 40 yen | 3,807 | | queued | 0 | |
| 13 | Neighborhood | 3,411 | | queued | 0 | |
| | **Total** | **55,895** | | | | |

Status values: `queued`, `drafting`, `checking`, `awaiting-user-ok`, `done`, `escalated`.

## Flags (for the user; the loop does not resolve these itself)

1. **Length rule conflict.** The golden rule in `CLAUDE.md` and `NEW_CHAT_PROMPT.md` says chapters are "slow and stretched" at about 4,000 to 5,500 words. The editorial prompt asks for a modest reduction. For the chapters 1 to 13 pass the editorial prompt governs (recorded in `CLAUDE.md`). Open: does the same apply to chapter 14 onward?
2. **Style rule conflict.** The user's standing hard rule bans negative parallelisms ("Not X. Y.", "It wasn't X. It was Y.") in any form. The editorial prompt says not to ban such constructions mechanically. The loop keeps the standing ban and treats the editorial prompt's "don't ban mechanically" as applying to the other repetition patterns (A to E). Open: confirm or change.
3. **Chapter 14 (Suga POV) is on hold.** The next planned chapter was ch 14. The loop does not write it until the user says whether the editorial rules apply to it.
4. **Recent chapters grew under the old rule.** Chapters 7 to 13 were rebuilt Nov 22 to the old golden rule and added scenes (for example the tape reach test in ch 12, the pickup-rotation work and the extra rallies in ch 13). Phase 1 should judge those additions against the new rules, not assume they stay.
5. **Splits renumber everything.** Any approved split shifts ch 14 to 72 and every cross-reference. It needs its own OK on the list of affected files (see `LOOP.md`).
6. **Facts check is a prompt, not a gate.** `chapter.py facts` flags quoted lines and scores from a chapter's Continuity block that are missing from a revised file. It has about 10% noise (a dialogue tag splitting a quoted line, a bullet quoting another chapter or a replaced line), so every flagged line gets a judgement in the change log.

## Open continuity contradictions found so far

None logged by the pass yet. Known carried-over notes from the Nov 22 revisions live in `handofff.md` and the Continuity blocks.

## Log

- Nov 23: editorial prompt saved verbatim; goal, loop, constraints, state and the review skill created; `chapter.py` and `lint.py` added under `tools/`. Phase 1 not started (waiting for the user to start it).
- Nov 23 (later): user said go. Phase 1 assessment drafted from a full read of ch 1 to 6, measurements across all 13 chapters (`tools/patterns.py`) and re-reads of ch 7 to 13; checker review running. Stopped at the approval gate: no chapter edited, `structure_approved` still no.
