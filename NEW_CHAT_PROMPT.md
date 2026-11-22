You're co-writing "Second Serve", my Haikyuu!! reincarnation webnovel, with me. The repo is ganesh-329/second-serve and you work on branch claude/ecstatic-sagan-930qnw. Commit and push after every chapter, and never open a PR unless I ask.

## The job: revise ch 1 to 34 before Arc 4
Arc 3 (ch 35 to 50) is finished and Arc 4 (ch 51 to 72) is fully planned. We are NOT writing Arc 4 yet.

I reread the early chapters and the soul was corrupted in most of them: the conversations weren't meaningful, many had errors, too much read as AI writing, and the pacing was too fast. We're rebuilding them chapter by chapter, in order. We go to Arc 4 only when this is done.

**Done so far:** ch 1 to 13 are revised (Ball to the face, The wig, Dawn reps, The King, Eyes closed, Jackets, Blue castle, Bottle cap, Grand King, Guardian deity, The ace who left, 40 yen, Neighborhood). The chapter count grew by 5 (Option B), and everything is renumbered: Arc 1 is ch 1 to 18, Arc 2 ch 19 to 34, Arc 3 ch 35 to 50, Arc 4 ch 51 to 72. The old-to-new table is `planning/revision/CHAPTER_MAP.md`.

**Next:** ch 14 "Call for the ball" (Suga POV). The handoff's "Next" line has the details.

## The heart of it (my words)
THE CONVERSATIONS ARE THE SOUL OF CHAPTERS. ORCHESTRATE THE CHAPTERS BEAUTIFULLY.

Give every interaction a purpose, a distinct voice, and a reason for the characters to engage. Let relationships develop through what people say, what they avoid saying, their disagreements, their humour, and the small ways they respond to each other. Use occasional surprise POVs when they add a perspective the main narration can't provide (the 1st is ch 14, Suga). Above everything, make *Second Serve* feel like a story written by someone who understands and cares about its characters. Let chapters breathe. Let conversations carry the story. Give every character a reason to speak, every scene a reason to exist, and every ending a hook that grows naturally from what happened.

## The golden rule (most important)
Chapters are slow and stretched out, but they must never lag. Every scene earns its length: no idling, no re-explaining, no summary where a scene belongs. Nothing can feel artificial. Every chapter needs soul: characters act from what they want (Soul sheet). The hook at the end comes out of that soul. Target Arc 3 length (about 4,000 to 5,500 words of prose), with no padding.

## Read before you touch anything
- `handofff.md`: the hard rules, the status (every revised chapter has a line), the threads and the "Next" line.
- `story bible.md`: "Revision of ch 1 to 34" (my decisions) first, then Master prompt, Writing guide, Sho's place on the team, Original nouns (Sho, both power ladders, stats), Canon and divergence, Soul sheet, POV chapters, Dialogue playbook, and the Arc 1 and Arc 2 outlines.
- The planning reports in `planning/revision/`: 01 to 05 audits, 06 canon, 07 and 08 soul and conversations plans, 09 structure, 10 fact ledger. **They use the OLD chapter numbers; read them through CHAPTER_MAP.md.**
- The pace and voice model: `arc3.md` ch 46 to 50, plus the revised ch 1 to 6 in `arc1.md`.
- The Haikyuu wiki dump: `haikyuufandomcom-20200223-history.xml.7z` in the repo. Extract it into the scratchpad with py7zr in a venv, then split it into 1 text file per article (about 1,243). The manga chapter and match pages are empty stubs; character, team, episode and "List of matches" pages hold the detail.

## What a revision may and may not change
Keep every plot beat and every fact a later chapter relies on: who knows what, the eye's firings and costs (the ledger's section 2), scores and results, bets, notebook lines, nicknames, promises, planted threads (stat cards are retired, Nov 22). If a fix needs a fact changed, stop and ask me first, and list every later chapter it touches. You may rebuild scenes and conversations from scratch, add scenes inside the same stretch of time, slow down rallies that matter (serve, pass, set, hit, where, why), fix canon, volleyball and continuity errors, and fix titles that break the style rules.

My decisions (Nov 22): **grounded tone**, no status cards, letter grades or named power stages anywhere in or after chapters; growth shows through training results, match performance and coach feedback. **The body earns what the mind knows**: visible, measurable weaknesses in strength, stamina under match conditions, landing mechanics and repeated jumping, fixed over time by training on the page (bible "Body").

My decisions already made (Nov 13): exam pass line stays 30; Aone stuffs Sho twice in ch 23 and Sho tools a block with Aone in it; the Nekoma practice match is 3 games; Sho plays the wing (outside hitter), never a hidden opposite; Seijoh plays 2 more matches the afternoon it beats Karasuno; the Inter-High final is 22-25, 23-25; "Observation Haki" is a thought only, never said aloud.

## Story rules
- Sho is an ACE (outside hitter) being built. Receive, defense and the eye are the all-rounder layer of an ace. At least 1 line of the ace in every chapter.
- The eye in ch 1 to 26 is the partial awakening: it fires on its own, about a blink early, never on command. It shows the hitter's or setter's body, never where the ball lands; Sho's own tape memory turns a swing into a place. Nobody treats it as shocking; Sho never announces it. One forced fusion in ch 27.
- Never explain the hand symbolism, the Satoshi parallels or the Hinata mirror in prose.
- Sho is shameless about himself and never cruel. Out loud he's a polite 15-year-old; analyst jargon stays in his head. He never calls Tsukishima's blocks (ch 4: "Don't do that again.").
- Canon is a starting point: Sho changes matches near him. Protected canon moments stay with their owners.

## Style rules (hard)
- No em dashes or en dashes.
- No negative parallelisms in ANY form: no "Not X. Y.", "X, not Y", "It wasn't X. It was Y.", concession-then-pivot, or "didn't X, he Y". Say what is.
- Numbers as digits, including "1st", "2nd", "the 1 who...", "1 by 1".
- Contractions, short paragraphs, plain and specific words.
- Banned words: delve, crucial, seamless, robust, vibrant, testament, highlight, leverage, showcase, enhance, and the rest of the AI-word list in my preferences.
- Banned tics: "for a moment", "for a second", "for a while", "for a long time", "said nothing", "didn't say anything", "didn't look at", "without looking", "without turning", "very quietly", "filed", "Something in his chest", "That was all".
- Also avoid: runs of 1-line stoic paragraphs, the narrator explaining subtext or feelings, adverbs that name a feeling, mirrored or topper exchanges, button endings, kids talking like writers.
- Every chapter ends with a "**Continuity (ch N)**" bullet block that separates canon from invented details.

## Lessons from my corrections (don't repeat these)
- **Nobody can know what hasn't happened yet.** Tanaka can't mention Saturday's match at dawn before Hinata and Kageyama have asked for it. Check every line against the in-story clock.
- **Callbacks must be on the page.** If a character echoes words from earlier, those words must actually appear earlier in the text. A thought or reaction the reader can't decode (for example "He'd heard himself.") needs the setup visible.
- **Readable over clever.** If a beat leans on subtext, make sure a reader can follow it without knowing the plan.
- **Volleyball logic, strictly:** a team keeps serving only while it wins rallies; recompute every score and server; front and back row; the sub and libero rules.
- **Reviewers matter.** The strict reviewer caught real errors on every chapter: wrong servers, wrong hand, ages, objects that later chapters describe differently (the 1-sheet bank calendar, the red string on the key, the door-frame pencil marks).

## Workflow for every chapter
1. **Audit:** read the chapter's sections in the 01 to 05 audits, the 07 or 08 plan and the 10 ledger (old numbers), plus the current text.
2. **Plan:** what stays, what gets rebuilt, which scenes to add or slow down, the 2 or 3 main conversations with each person's want, and the hook.
3. **Draft** in the scratchpad.
4. **Grep** the draft for dashes, tics, negative parallelisms and spelled-out numbers, and fix them.
5. **Review:** a strict report-only reviewer agent on the draft (golden rule, canon, volleyball logic, continuity with every later chapter that relies on it, style).
6. **Fix** what it finds, or rewrite.
7. **Replace** the chapter in place in `arc1.md` or `arc2.md`, keeping CRLF line endings (a Python script that reads with newline='' works).
8. **Update** `handofff.md`: a "Revised:" line for the chapter, and the "Next" line.
9. **Commit** with the attribution lines and push.

Reply to me in plain, short, direct English. Check your own grammar. Don't paste back long summaries of what you wrote.

Start by reading the files, then finish ch 7.
