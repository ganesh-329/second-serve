# Shared brief for the Arc 1 revision planning agents ("Second Serve", a Haikyuu!! reincarnation fanfic)

## The job
Arc 3 (ch 30 to 45) is finished and Arc 4 is planned. Before Arc 4 is written, the author is revising Arc 1 (ch 1 to 15, `arc1.md`) and then Arc 2 (ch 16 to 29, `arc2.md`). This planning round is for **Arc 1 only**. Arc 2 gets its own round after Arc 1's revision is done.

The author reread the early chapters and says the soul is corrupted in most of them:
- The conversations aren't meaningful.
- Many have errors (canon, volleyball, continuity).
- Too much reads as AI writing.
- The pacing is too fast. Arc 1 chapters run about 2,300 to 4,000 words; Arc 3's run 5,000 to 6,500. Most could be extended a lot.

The author allows **more chapters** if the material needs them (the structure agent decides; renumbering of later chapters is then a mechanical job done once, later). Every report feeds a chapter-by-chapter revision plan for Arc 1.

## The golden rule (author, most important)
Chapters are slow and stretched out, but they must NEVER lag. Every scene earns its length: no idling, no re-explaining, no summary where a scene belongs. Nothing can feel artificial. Every chapter has soul: characters act from what they want (bible "Soul sheet"). The hook at the end of each chapter comes out of someone's soul.

## What a revision may and may not change
- KEEP every plot beat and every fact a later chapter (ch 16 to 45, and the Arc 4 plan) relies on: who knows what; the eye's firings and their costs; scores and results; bets, notebook lines, nicknames, promises; stat cards; planted threads (Oikawa's tells, Tanaka's spot, Mio's bets and door checks, etc.).
- If a fix needs a fact changed, FLAG it for the author (list every later chapter it touches). Never assume.
- MAY: rebuild scenes and conversations from scratch; add scenes inside the same stretch of time; slow down rallies that matter (serve, pass, set, hit, where, why); fix canon, volleyball and continuity errors; fix titles that break the style rules (e.g. "One touch" uses a spelled-out number; "Not a Team Yet" is a negative construction and title case).
- Canon is a starting point: Sho changes matches near him. Protected canon moments stay with their owners (Hinata and Kageyama's quick and their fight; Asahi's return and "call for the ball"; Noya's return; Ukai agreeing to coach; Kenma and Hinata; Tanaka's arc).

## Source files
- Story bible: `/home/user/second-serve/story bible.md`. Sections: "Master prompt", "Writing guide" ("How these people talk", "Artificial tells to cut on sight"), "Sho's place on the team", "Arc 1 outline", "Canon plot timeline" (Arc 1 rows), "Noun KB", "Original nouns" (Sho, Emperor's Eye ladder, Meta Vision ladder, stats, card template), "Canon and divergence", "Soul sheet", "Dialogue playbook" (line ~1052), "The ace path" (inside "Eyes as a weapon").
- Chapters: `/home/user/second-serve/arc1.md` (ch 1 to 15), `arc2.md` (ch 16 to 29), `arc3.md` (ch 30 to 45). Each chapter ends with a "**Continuity (ch N)**" block: read those first, they're fast.
- Voice and pace model: `arc3.md` ch 41 to 45 (ch 41 starts line 4104; ch 45 at 5368).
- Handoff with the author's hard rules and threads: `/home/user/second-serve/handofff.md`.
- Earlier planning (format and depth to match): `planning/arc3/*.md`, `planning/arc4/*.md`. Fact ledgers: `planning/arc3/09_continuity.md` (audit of ch 1 to 28) and `planning/arc4/08_continuity.md` (ch 30 to 45).
- Files use CRLF line endings; pipe through `tr -d '\r'` if needed.
- Web: WebSearch may work (load with ToolSearch "select:WebSearch,WebFetch"). WebFetch to haikyuu.fandom.com may be BLOCKED; try, and fall back to search snippets. Tag every canon fact [web: URL], [memory] or [unsure]. Never present memory as verified.

## Premise in brief
Matsumoto Satoshi: college ace (outside hitter, #5), Osaka gym; left ACL at 20 after training through 3 months of pain and telling nobody; 9 years a V.League video analyst; died at his desk at 3:14 a.m. rewinding tape, 29. Reborn as Kiyose Sho (15, 182 cm, Karasuno 1st year, class 1-5, later #13). Memories return in April when a stray ball hits him in the face (ch 1). He is one person with both lives; his family is his own. Before the hit, Sho quit every sport by 12. Shameless (Lloyd Frontera), cold analyst underneath, polite 15-year-old out loud; analyst jargon stays in his head. Anime brain (Naruto, One Piece, Bleach, Gintama; never saw Haikyuu). Sub ace and receiving outside hitter; Noya stays libero; Hinata stays the heart. Family: Mom (up at 4:40 making onigiri; doesn't ask, notices everything), Dad (quiet, "Mm", folds the newspaper small; dry: "Red car still on?"), Mio (10; pudding bets; checks his knees and forearms at the door when she thinks nobody sees, from ch 8; magnet on the fridge calendar).

## Story rules
- Sho is an ACE (outside hitter) being built. At least 1 line of the ace in every chapter.
- Emperor's Eye: dormant until the 3v3 (Hinata's 1st freak quick, ch 5), then partial awakening: fires on its own, a ghost of 1 player's next move about 0.2s ahead, never on command. Shows the hitter or setter, NEVER where the ball lands after contact. Nobody treats it as shocking; Sho never announces it (he privately calls it Observation Haki). Meta Vision: Film brain at start, Scanning from Golden Week (ch 13), overload freeze vs Nekoma (ch 14).
- Never explain the hand symbolism, the Satoshi parallels or the Hinata mirror in prose.
- Sho is shameless about himself, never cruel.

## Style rules (hard)
No em or en dashes. No negative parallelisms in any form ("Not X. Y.", "X, not Y", "It wasn't X. It was Y.", concession-then-pivot, "didn't X, he Y"). Numbers as digits, including "1st", "2nd", "the 1 who". Contractions; short paragraphs; plain specific words. Banned words: delve, crucial, seamless, robust, vibrant, testament, highlight, leverage, showcase, enhance, harness, unlock, realm, landscape, pivotal, intricate, foster, elevate (and similar AI vocabulary). Banned tics: "for a moment/second/while/long time", "said nothing", "didn't say anything", "didn't look at", "without looking", "without turning", "very quietly", "filed", "Something in his chest", "That was all". Avoid: runs of 1-line stoic paragraphs, narrator explaining subtext or feelings, adverbs naming a feeling, mirrored or topper exchanges, button endings, kids talking like writers, sitcom ping-pong, a simile on every gesture.

## Output format for every agent
- Write your FULL report to the file path your task gives you (markdown). Be concrete: chapter and line numbers, quotes, names, scores, scene ideas, SAMPLE dialogue lines (plain, real-sounding, no quips) and why.
- Use digits for numbers, no em dashes or en dashes, no "Not X. Y." constructions in your own prose.
- Do NOT edit arc1.md, arc2.md, arc3.md, the bible or the handoff. Report only.
- Your final message back: a tight summary under 600 words with the most important, concrete findings.

## POV chapters (author, added during planning)
The author wants a few surprise POV chapters in Arc 1 too ("a nice touch but not too much"). Follow the bible's "POV chapters" rules: 1 character per chapter, close third, past tense, their own vocabulary and soul; the story moves forward (new time, or a moment Sho can't see); the reader sees Sho from outside at least once; never 2 POV chapters in a row; title format "Chapter N: <title> (<character>)". Suggest at most 2 or 3 for Arc 1, each only where a moment truly needs that person's eyes, and say why that character and that moment.
