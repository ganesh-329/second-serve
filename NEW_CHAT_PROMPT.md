You're co-writing "Second Serve", my Haikyuu!! reincarnation webnovel, with me. The repo is ganesh-329/second-serve and you work on branch claude/ecstatic-sagan-930qnw. Commit and push after every chapter, and never open a PR unless I ask.

## The job: revise Arc 1 and Arc 2 (ch 1 to 29) before Arc 4
Arc 3 (ch 30 to 45, `arc3.md`) is finished and is my preferred style. Arc 4 is planned but on hold.
- Done (in `arc1.md`): ch 1 to 8. Unrevised chapters are headed "## Old chapter N: title".
- **Next: ch 9 "Grand King" (from "Old chapter 8").** Then the rest of Arc 1, then Arc 2 (`arc2.md`, ch 16 to 29), which gets its own short planning round first.
- Read `handofff.md` (status, threads, my rules) and `planning/arc1/BRIEF.md` (every "Author direction" at the bottom). The research is in `planning/arc1/` (01a/01b audits, 02 canon, 03 continuity lock list, 04 soul, 05 matches, 06 shameless, 07 voices, 10 structure). The structure plan's chapter splits and +7 renumber NO LONGER apply (see light touch below); renumber once at the end from the real list.
- Canon source: the full wiki dump `haikyuufandomcom-20200223-history.xml.7z` in the repo. Rebuild it with `planning/tools/README.md` (needs `pip install py7zr`). Canon is reference only: things change because of Sho.

## LIGHT TOUCH (most important, learned the hard way)
My first revisions of ch 1 to 7 stretched the chapters, rewrote them from scratch, and made them worse: flatter, less funny, new errors. So:
- **If a chapter doesn't need revision, leave it.** Start from the OLD text. Keep its flow, humor, narration and charm.
- **Change the conversations** (sitcom ping-pong, quips and toppers, Sho's cocky lines, out-of-voice lines, canon talks told as summary that should be spoken) and **fix real errors** (canon, volleyball logic, rotation and serve order, continuity, the eye's rules, banned tics).
- **Stretch only where a scene truly needs it.** Never pad for a word count. No unnecessary conversations; don't skip important ones.
- **Always evaluate** the revised chapter against the old one before it goes in: more readable? more soul? anything lost? If anything got worse, fix that first.
- Keep Sho's inner voice alive (shameless, funny, 1 or 2 anime references a chapter in his head); his spoken lines stay plain and polite.

## The golden rule
Chapters are slow and stretched out where it matters, but they must never lag. Every scene earns its length: no idling, no re-explaining, no summary where a scene belongs. Nothing can feel artificial. Every chapter needs soul: characters act from what they want (bible "Soul sheet"). The hook at the end comes out of that soul.

## Story rules
- Sho is an ACE (outside hitter) being built: at least 1 line of the ace per chapter.
- The eye in ch 1 to 22: partial awakening, fires on its own, shows the hitter's or setter's body (never where the ball lands), never announced aloud (Observation Haki stays in his head), nobody treats it as shocking. Sho is never scared of his power.
- Never explain the hand symbolism, the Satoshi parallels or the Hinata mirror in prose. Sho never says Satoshi/Matsumoto/"past life" aloud in Arc 1.
- Shameless = plain, polite asks; asks again once after a no; copies openly; reports his own failures flatly. Never quips, pitches, roasting or winning every exchange.
- Keep every fact later chapters rely on (`planning/arc1/03_continuity.md`). If a fix needs a fact changed, ask me first.

## Style rules (hard)
- No em or en dashes. No negative parallelisms in any form ("Not X. Y.", "X, not Y", "didn't X, he Y", concession then pivot).
- **Numbers:** digits for counts and measures ("1 year", "3 steps", "1st year"). **The word "one" stays a word when it isn't a count:** "the one", "this one", "the next one", "no one", "one of them", "one by one", "Can I hit one?". Never "the 1 I'm going to beat".
- Banned words: delve, crucial, seamless, robust, vibrant, testament, highlight, leverage, showcase, enhance, and the rest of my AI-word list.
- Banned tics: "for a moment/second/while/long time", "said nothing", "didn't say anything", "didn't look at", "without looking", "without turning", "very quietly", "filed", "Something in his chest", "That was all". Avoid narrator explaining feelings, feeling adverbs, and-chains, button endings, simile overload, kids talking like writers.
- Every chapter ends with a "**Continuity (ch N)**" block separating canon from invented details.

## Workflow per chapter (keep it lean)
1. Read the old chapter and its spec/audit notes. Tell me in a few lines what's wrong and what you'll change.
2. Edit the old text in the scratchpad (targeted replacements, not a rewrite).
3. Grep for dashes, tics, negative parallelisms, numbers and the "one" rule.
4. Evaluate it against the old version honestly. Use a reviewer agent only when a chapter has match logic or big changes.
5. Replace it in `arc1.md`/`arc2.md` with CRLF line endings and its new chapter number; update `handofff.md`; commit and push.

Reply to me in plain, short, direct English. Start by reading the files, then do ch 9.
