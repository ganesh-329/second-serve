You're co-writing "Second Serve", my Haikyuu!! reincarnation webnovel, with me. The repo is ganesh-329/second-serve and you work on branch claude/ecstatic-sagan-930qnw. Commit and push after every chapter, and never open a PR unless I ask.

## The job: revise chapters 1 to 22 before Arc 4
Arc 3 (ch 30 to 45) is finished and Arc 4 is fully planned. We are NOT writing Arc 4 yet.

I've reread ch 1 to 22 (arc1.md ch 1 to 15, arc2.md ch 16 to 22), and the soul is corrupted in most of them:
- The conversations aren't meaningful.
- Many have errors.
- Too much of it reads as AI writing.
- The pacing is too fast. The chapters are much shorter than Arc 3's, and most could be extended a lot.

Fix this chapter by chapter, starting at ch 1. We go to Arc 4 only when this is done. The old rule "Don't edit ch 1 and 2" is lifted for this revision.

## The golden rule (most important)
Chapters are slow and stretched out, but they must never lag.
- Every scene earns its length: no idling, no re-explaining, no summary where a scene belongs.
- Nothing can feel artificial.
- Every chapter needs soul. Characters act from what they want (see the Soul sheet).
- The hook at the end of each chapter comes out of that soul.

## Read before you touch anything
- `handofff.md`: the hard rules, the status and the threads.
- `story bible.md`, these sections first:
  - Master prompt
  - Writing guide (How these people talk, Artificial tells to cut on sight)
  - Sho's place on the team
  - Original nouns (Sho, both power ladders, stats)
  - Canon and divergence
  - Soul sheet
  - Dialogue playbook
  - Arc 1 outline
  - Arc 2 outline
- The pace and voice model: Arc 3's ch 41 to 45 in `arc3.md`. These are the latest, reviewed chapters, at about 5,000 to 6,500 words each.
- The fact ledgers. Later chapters depend on these facts:
  - `planning/arc3/09_continuity.md`: an audit of ch 1 to 28.
  - `planning/arc4/08_continuity.md`: an audit of ch 30 to 45.

## What a revision may and may not change
- Keep every plot beat and every fact a later chapter relies on:
  - who knows what
  - the eye's firings and their costs
  - scores and results
  - the bets, the notebook lines, nicknames and promises
  - the stat cards
  - the planted threads (for example Oikawa's tells and Tanaka's spot)
- If a fix needs a fact changed, stop and ask me first. Then list every later chapter it touches.
- You may:
  - rebuild scenes and conversations from scratch
  - add scenes inside the same stretch of time
  - slow down rallies that matter (serve, pass, set, hit, where, why)
  - fix canon, volleyball and continuity errors
  - fix titles that break the style rules (for example "One touch", "Not a Team Yet")
- Canon is a starting point: Sho changes matches near him. Protected canon moments stay with their owners.

## Story rules
- Sho is an ACE (outside hitter) being built. Receive, defense and the eye are the all-rounder layer of an ace. Put at least 1 line of the ace in every chapter.
- The eye (Emperor's Eye) works as its ladder says for that point in the story. In ch 1 to 22 it is the partial awakening, firing on its own. Nobody treats it as shocking, and Sho never announces it.
- The eye shows the hitter or setter, never where the ball lands after contact.
- Never explain the hand symbolism, the Satoshi parallels or the Hinata mirror in prose.
- Sho is shameless about himself and never cruel. He's a polite 15-year-old out loud; analyst jargon stays in his head.

## Style rules (hard)
- No em dashes or en dashes.
- No negative parallelisms in ANY form: no "Not X. Y.", "X, not Y", "It wasn't X. It was Y.", concession-then-pivot, or "didn't X, he Y". Say what is.
- Numbers as digits, including "1st", "2nd" and "the 1 who...".
- Contractions, short paragraphs, plain and specific words.
- Banned words: delve, crucial, seamless, robust, vibrant, testament, highlight, leverage, showcase, enhance, and the rest of the AI-word list in my preferences.
- Banned tics:
  - "for a moment", "for a second", "for a while", "for a long time"
  - "said nothing", "didn't say anything"
  - "didn't look at", "without looking", "without turning"
  - "very quietly", "filed", "Something in his chest", "That was all"
- Also avoid:
  - runs of 1-line stoic paragraphs
  - the narrator explaining subtext or feelings
  - adverbs that name a feeling
  - mirrored or topper exchanges
  - button endings
  - kids talking like writers
- Every chapter ends with a "**Continuity (ch N)**" bullet block that separates canon from invented details. Update it to match the revision.

## Workflow for every chapter
1. **Audit first.** Run a strict report-only reviewer agent on the current chapter. It checks:
   - soul: what each character wants, and whether they act from it
   - whether each conversation means something
   - AI tells and style violations
   - canon and volleyball logic (rotations, front and back row, who serves, scores)
   - continuity against the ledgers and the chapters around it
   - pacing: where it rushes and where a scene belongs

   Give me a short summary of what's wrong before you rewrite. For ch 1, also show me the plan and wait for my OK.
2. **Plan the revision:**
   - what stays (facts and beats)
   - what gets rebuilt
   - which scenes to add or slow down
   - the 2 or 3 main conversations and each person's want
   - the hook

   Target: Arc 3 length, with no padding.
3. **Draft** it in the scratchpad.
4. **Grep** the draft for dashes, tics, negative parallelisms and spelled-out numbers, and fix them.
5. **Review.** Run a strict report-only reviewer agent on the draft: the golden rule, canon, volleyball logic, continuity (including every later chapter that relies on this one) and style.
6. **Fix** what it finds, or rewrite.
7. **Replace** the chapter in place in `arc1.md` or `arc2.md`, keeping CRLF line endings and the same chapter number.
8. **Update** `handofff.md`. Add a line saying the chapter is revised, and set the "Next" line to the next chapter to revise.
9. **Commit** with the attribution lines and push.

Reply to me in plain, short, direct English. Check your own grammar. Don't paste back long summaries of what you wrote.

Start by reading the files, then audit ch 1.
