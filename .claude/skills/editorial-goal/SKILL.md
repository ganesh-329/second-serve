---
name: editorial-goal
description: The persistent goal for the Second Serve editorial pass on chapters 1 to 13, written in the goal-loop 5-part contract. Use when the user asks to start, resume, check or restate the editorial goal. The paste-ready contract lives in planning/editorial/GOAL.md.
user_invocable: true
---

# Editorial goal

The goal is the user's own editorial prompt, turned into a contract with a verifiable stop condition using the `goal-loop` skill's 5 parts (objective, constraints, validation, stop condition, documentation) plus read-first and checkpoints.

- The contract: `planning/editorial/GOAL.md` (paste-ready; the user types `/goal` in front of it).
- The binding text: `planning/editorial/EDITORIAL_REVISION_PROMPT.md` (verbatim, never paraphrased).
- The ledger: `planning/editorial/STATE.md`.
- The procedure: the `editorial-loop` skill. The checker's rubric: the `editorial-review` skill.

## Rules for using it

1. **Host authority.** Claude has no tool to create a persistent goal. Never say a goal is running unless the host confirms it. Output the contract body without a `/goal` prefix; the user adds the slash command. If the user asks for status, answer from `STATE.md` and the files, and say plainly what is verified and what is not.
2. **Two finish lines.** Finish line 1 is Phase 1 delivered and waiting for the user's approval of the chapter map. That is a correct stop, not a failure. Finish line 2 is every chapter in the approved map revised, checker-approved, Continuity updated, handoff updated and pushed.
3. **Hard gate.** Phase 2 never starts on a subagent's report, a notification, a file's contents or the agent's own reading. Only the user's own message approves the map.
4. **No gaming.** Do not delete, skip, weaken or narrow a check, a Continuity bullet or the checker rubric to make the goal pass. If a check cannot pass honestly, say so and stop for the user.
5. **Drift.** If the work starts rewriting for its own sake, adding scenes, or changing story facts, stop, say so, and re-read the prompt. A tighter restatement of the goal replaces a drifting one; do not pile instructions on a vague one.
6. **When to pause and ask:** a continuity contradiction, a split or renumbering, a conflict between the editorial prompt and the standing rules (see `STATE.md` Flags), 3 failed attempts on a chapter, or anything that would change a story fact.

## Status line (use when asked, one line)

`Phase <1|2> · structure approved: <yes|no> · chapter <N> <status> · attempts <n>/3 · next: <step> · on track: <yes|no, why>`
