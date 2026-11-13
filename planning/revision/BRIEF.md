# Revision of ch 1 to 29: shared brief for planning agents

Repo: /home/user/second-serve (branch claude/ecstatic-sagan-930qnw). Report-only: write ONLY your own output file. Never edit arc1.md, arc2.md, arc3.md, the bible, the handoff or anything in planning/arc3 or planning/arc4.

## The job
The user has reread ch 1 to 29 (`arc1.md` ch 1 to 15, `arc2.md` ch 16 to 29) and says the soul is corrupted in most of them:
- The conversations aren't meaningful.
- Many have errors (canon, volleyball, continuity).
- Too much reads as AI writing.
- The pacing is too fast. Ch 1 to 15 run 2,200 to 4,800 words; Arc 3's model chapters (ch 41 to 45 in `arc3.md`) run 4,000 to 6,500 and feel slow without lagging.

Every chapter gets rebuilt, one at a time, starting at ch 1. Arc 3 (ch 30 to 45) is finished; Arc 4 is planned and not written. Your report feeds the revision plan and the bible update.

## The user's words (verbatim, the heart of it)
"THE CONVERSATIONS ARE THE SOUL OF CHAPTERS. ORCHESTRATE THE CHAPTERS BEAUTIFULLY."
"Give every interaction a purpose, a distinct voice, and a reason for the characters to engage. Let relationships develop through what people say, what they avoid saying, their disagreements, their humour, and the small ways they respond to each other. Orchestrate each chapter so its scenes and conversations flow naturally, with enough room for emotions and relationships to develop."
"Use occasional surprise POVs when they add a perspective that the main narration can't provide. Give those POVs their own character motivations and narrative purpose. You may increase the chapter count when the story genuinely needs more room." (If chapters are added, every later chapter number, outline, continuity reference and handoff shifts.)
"Make Second Serve feel like a story written by someone who understands and cares about its characters. Let chapters breathe. Let conversations carry the story. Give every character a reason to speak, every scene a reason to exist, and every ending a hook that grows naturally from what happened."

Golden rule: chapters are slow and stretched out, but never lag. Every scene earns its length: no idling, no re-explaining, no summary where a scene belongs. Nothing artificial. Every chapter has soul: characters act from what they want (bible "Soul sheet"). The end hook comes out of that soul.

## What a revision may and may not change
Keep every plot beat and every fact a later chapter relies on: who knows what; the eye's firings and their costs; scores and results; bets, notebook lines, nicknames, promises; stat cards; planted threads (Oikawa's tells, Tanaka's spot, etc). A fix that needs a fact changed must be flagged as "NEEDS USER OK" with every later chapter it touches.
Allowed: rebuild scenes and conversations from scratch; add scenes inside the same stretch of time; slow down rallies that matter (serve, pass, set, hit, where, why); fix canon, volleyball and continuity errors; fix titles that break style rules (e.g. "One touch", "Not a Team Yet": title case and the negative-parallel shape).

## Story rules
- Sho is an ACE (outside hitter) being built. Receive, defense and the eye are the all-rounder layer of an ace. At least 1 line of the ace in every chapter.
- The eye (Emperor's Eye): ch 1 to 22 is the partial awakening, firing on its own, about 0.2s, never on command. Nobody treats it as shocking; Sho never announces it. It shows the hitter or setter, never where the ball lands after contact. One forced fusion in ch 22 (see bible).
- Never explain the hand symbolism, the Satoshi parallels or the Hinata mirror in prose.
- Sho: shameless about himself, never cruel; a polite 15-year-old out loud; analyst jargon stays in his head.
- Canon is a starting point. Sho changes matches near him. Protected canon moments stay with their owners (bible "Canon and divergence").

## Style rules (hard)
No em or en dashes. No negative parallelisms in any form ("Not X. Y.", "X, not Y", "It wasn't X. It was Y.", concession-then-pivot, "didn't X, he Y"). Numbers as digits ("1st", "the 1 who"). Contractions, short paragraphs, plain words. Banned words: delve, crucial, seamless, robust, vibrant, testament, highlight, leverage, showcase, enhance, etc. Banned tics: "for a moment/second/while/long time", "said nothing", "didn't say anything", "didn't look at", "without looking", "without turning", "very quietly", "filed", "Something in his chest", "That was all". Avoid runs of 1-line stoic paragraphs, narrator explaining subtext or feelings, adverbs naming a feeling, mirrored/topper exchanges, button endings, kids talking like writers, sitcom ping-pong.

## Files to read
- `handofff.md` (rules, status, threads), `NEW_CHAT_PROMPT.md`.
- `story bible.md`: Master prompt; Writing guide (How these people talk; Artificial tells); Sho's place on the team; Arc 1 outline; Original nouns; Canon and divergence; Soul sheet; POV chapters; Arc 2 outline; Dialogue playbook. Also skim Arc 3 and Arc 4 outlines.
- Voice and pace model: `arc3.md` ch 41 to 45 (and the POV models ch 33 Kenma, ch 38 Ukai; arc2 ch 23 Mio, ch 27 Tanaka).
- Fact ledgers: `planning/arc3/09_continuity.md` (audit of ch 1 to 28), `planning/arc4/08_continuity.md` (audit of ch 30 to 45).
- Canon reference: the Haikyuu fandom wiki (Feb 2020 dump), one plain-text file per article in
  `/tmp/claude-0/-home-user-second-serve/a9e5a82e-325e-544e-8344-93df3079cc1a/scratchpad/wikipages/`
  with a title index at `.../scratchpad/wiki_index.txt` (format: `filename | title`). Some titles have duplicates with a numeric suffix; read the biggest. Use grep. Manga chapter pages are titled by chapter name (e.g. "Endings and Beginnings", "Karasuno High School Volleyball Club"); episode pages end in "(Episode)"; match pages look like "Karasuno vs. Aobajohsai (Practice Match)"; character pages like "Kiyoko Shimizu". Cite the wiki file for every canon claim; mark anything from memory as [memory, unverified].

Use CRLF-agnostic tools (`tr -d '\r'`) when reading the arc files. Chapter boundaries: `grep -n "^## Chapter" arc1.md arc2.md arc3.md`.
