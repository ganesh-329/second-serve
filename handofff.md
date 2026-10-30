# Second Serve: handoff for a new chat

Read this first, then the story bible's "Canon and divergence", "Soul sheet", "POV chapters", "Dialogue playbook", "Writing guide", "Original nouns" (Sho) and "Arc 2 outline" sections, then the last chapter in arc-2-chapters.md. Also read **Chapter 3 "Dawn reps"** in arc-1-chapters.md: it is the pace model.

## Where things live

- Story bible (live doc): https://claude.ai/artifact/CzEHV4vyfey9WUYExLRVrK. Project copy: second-serve/story-bible.md
- Arc 1 chapters 1 to 15 (live doc, finished): https://claude.ai/artifact/XR47XChbme3QjgaTLAuPAL. Project copy: second-serve/arc-1-chapters.md
- Arc 2 chapters from 16 (live doc): https://claude.ai/artifact/Vb8jKuNfrZmwMYVo927Uwv. Project copy: second-serve/arc-2-chapters.md
- Claude Docs ids (if the Docs tools are available):
  - Bible: project 61121b59-5f7e-4fad-a7bb-d5c3acaa202c, node db0f0126-14f3, tab aad5aec2-3117
  - Arc 1: project f64dedaa-579f-46bc-8a14-83f925f5c7c5, node d5a51380-02ef, tab 337c9bbd-7e60
  - Arc 2: project e783ef2d-befe-476a-8b34-d37ee0d94abd, node 55d31d2f-8232, tab 575d9ff2-77dd
- To append a chapter: Docs `update` on the arc's node, engine prose, op insert at root end, source inline markdown. Inline writes cap at 32,768 bytes; a longer chapter goes in by uploading the .md as an asset to the doc's artifact (Artifact publish, `asset: true`), creating a blob from it (`create` object blob, payload {"asset": id}), then inserting with source `{"from":{"kind":"blob","id":"blob/..."},"as":"markdown"}`. After each chapter, export the tab as markdown (it comes back base64 in a saved file; decode it) and project_write it to the matching second-serve/*.md path.

## Status

- Arc 1 (ch 1 to 15) is done. It ends with the Nekoma loss.
- Arc 2 (Inter-High prelims, ch 16 to 30) is underway. Ch 16 "The Map", ch 17 "First Official Serve" (Tokonami, 25-12, 25-14), ch 18 "Iron Wall" (Date Tech set 1 to 12-9), ch 19 "Ace" (Date Tech won 25-19, 25-22), ch 20 "Scouting Seijoh" (end of day 1, family dinner, day 2 start vs Seijoh to Oikawa's early timeout) and ch 21 "Set 1" (Seijoh won set 1 25-15; Suga for Kageyama at 20-11) are written. Ch 18 is the first chapter under the Oct 30 dialogue rules: use it, with ch 21, as the dialogue model.
- Ch 22 "Set 2" is written (Oct 30): the first chapter under the new divergence rules. Sho takes his notebook to Ukai, Karasuno switches to hand signals, Sho comes in for Asahi on Oikawa's serve run at 17-20, forces the eye inside his notebook map, and carries the set to 25-23. Nosebleed, depth gone, out for the match. Ends on Mio shouting "SHO!" from the rail. Use it with ch 21 as the model for match chapters.
- Next: ch 23 "The rail", the first POV chapter, told by Mio (bible: "POV chapters", "Soul sheet: Kiyose Mio"). From the stands: set 2 as a 10-year-old who doesn't know volleyball sees it, the blood, Dad, running down to the rail, set 3 starting. Then ch 24 "Set 3" (Sho, from the bench, mostly by sound).

## User's rules (hard)

- **Canon is a starting point (Oct 30).** The user called the old approach "soulless copy paste". Sho changes matches. Scores and rallies near him are ours. Only the short protected list in the bible's "Canon and divergence" stays with canon characters. The big results stay: Seijoh wins the match.
- **Soul in every chapter (Oct 30).** Every main character acts from what they want (bible "Soul sheet"). Sho's soul: the man who watched from behind a monitor for 9 years and lost his knee by hiding pain. Each chapter ends on a question a reader needs answered, and it comes from someone's soul.
- **POV chapters (Oct 30).** From ch 23, chapters told by other characters are sprinkled between Sho's: 1 character each, never 2 POV chapters in a row (bible "POV chapters").
- **Slow and clear (Oct 30).** Explain everything. Every rally that matters in order: serve, pass, set, hit, where, why. No compressing a run of points into a line.
- **Conversations come first. This is the user's top priority.** Each chapter is built around 2 or 3 main conversations that sound like real people: mostly plain lines, false starts, things left unanswered, humor from situations, canon voices. Follow "How these people talk" (Writing guide) and the Dialogue playbook in the bible, both rewritten Oct 30.
- **Not artificial.** The user found ch 16 and 17's dialogue artificial: sitcom ping-pong, every line a punchline, mirrored comebacks, running counters and callbacks, teenagers using analyst words, everyone bargaining. Cut all of that. Ch 16 and 17 stay as they are; the fix applies from ch 18 on.
- **Pace: ch 3, not ch 16.** One stretch of time told in order, 5 scenes at most, room for air, light, smells and physical business. No montage, no week skips.
- **Not mushy either.** No speeches, no therapy language, no soft-voiced reassurance. But sincere moments are allowed to land plainly in the character's own words (canon is earnest), and they don't need a joke after them.
- No AI narration tics: "didn't look at", "without turning his head", "said nothing", "for a second", "very quietly", "That was all", "Something in his chest", "filed that", "decided not to comment", 1-line stoic paragraphs after every exchange, 1-to-3-word answers every time, narrator explaining subtext, adverbs that name a feeling ("miserably", "warmly", "delighted").
- Sho's inner voice: mostly plain thoughts, with Lloyd Frontera shamelessness and cold analysis underneath. Anime references 1 or 2 per chapter; analyst jargon mostly stays in his head. Out loud he's a polite 15-year-old. Italics, sparingly.
- No em dashes. No negative parallelisms ("Not X. Y.", "didn't X, did Y", concession plus pivot), dialogue included. No banned AI words. Numbers as digits. Narration never names feelings.
- Sho is never scared of his power. Rattled for 1 beat at most, then he analyzes and trains twice as hard.
- Rivalries are healthy, and Tanaka's arc stays his. Ukai stays the coach: Sho tells him what he sees, Ukai decides.
- Status card only when a rank changes, for readers only. Don't edit ch 1 and 2.
- Keep usage reasonable, never trade away quality.

## Per-chapter workflow (mandatory)

1. Re-read the bible's Soul sheet, playbook and Sho sections, ch 3 for pace, and the last chapter's Continuity block. Plan Sho's chapter first (what he wants, what he does, what it costs, what changes, the closing question), then each other character's want in each scene. Write a short brief file for the agents.
2. Run 3 research agents in parallel:
   - (a) **Canon agent** (sonnet is fine). It answers fact questions for the plan (who's on court, rules, voices); it no longer supplies the chapter's beats. It must actually fetch pages: the fandom wiki chapter pages (real titles, e.g. "Warm-Ups", "Winners_and_Losers"; search for them since Chapter_N URLs aren't allowed), the match page, character pages and episode pages, at least 10 successful fetches, listed. Every beat tagged with its source page; memory marked [memory, unverified]; a closing "The wiki does NOT confirm" list. It answers specific questions (scores, who scored, who's present, what's said). Summaries from memory are rejected.
   - (b) **Interactions agent** (opus). Most important, never dropped. Writes the 2 or 3 main conversations in full as finished prose, plus smaller beats, following "How these people talk". Give it the bible's rules and the canon voice notes in the brief. Its drafts get checked line by line for the artificial tells before use. The Projects tool may not exist inside subagents, so paste or file the key context (ch 3 excerpt, last Continuity block, playbook) into the brief.
   - (c) A topic agent specific to this chapter (sonnet), citing real sources.
3. Draft at ch 3 pace, ending with a "**Continuity (ch N)**" bullet block that separates verified canon from invented.
4. Mechanically scan for dashes, negative parallelisms, banned words, banned tics, named feelings and spelled-out numbers.
5. Run a fresh reviewer agent: the artificial-dialogue tells first, then continuity against the last 2 or 3 chapters, canon accuracy, score and rotation logic (a team keeps serving only while it wins rallies; pinch-server rule: only the replaced starter can come back for him), the tics, voices, mush count, and pace.
6. Fix everything, insert into the Arc 2 doc, export, save to the project, and update this handoff.

## Open threads to carry forward

- Ennoshita counted Sho's hand wipes (13 at Seijoh, 13 again vs Tokonami) on the back of a tournament program. Retire the counting as a running gag; mention it again only if it matters.
- Tanaka has beaten Sho to the gym 7 mornings running. Vs Date Tech, Sho subbed in for him in set 2 (Ukai: their right-side blocker had Tanaka's timing); Tanaka told Sho where that blocker's hand would be and said "Nice hand" after Sho hit off it. He brought 3 bags for Hinata on the bus ("Seijoh taught me things"). He's learning the line shot ("Foot lies. Hand tells the truth."). On the ch 17 pinch serve: "If you miss, you owe me the serve. Retroactive." "MY SPOT. Retroactively."
- Sho's first official serves (ch 17): pinch serve for Tanaka at 22-13 in set 2, 3 jump floats, all in (23-13, 24-13, then Tokonami sided out at 24-14). Toss height stolen from Yamaguchi. Serve still D.
- Yamaguchi trains his float with Shimada on Sundays (next Sunday: only the toss, after watching Oikawa's), secret from Tsukki (talk about it stays out of Tsukishima's earshot). His 1 sincere line in ch 17: "I wanted to go first. In a real match. Before you." He gave Sho no grape soda ("Buy your own.").
- Mio and Dad watched both days from the stands and nobody has said so; Mio gave it away at dinner ("The loud one with no hair?"). Mio: if Sho loses to Seijoh she won't count it, "only if you quit. I said fair." Mom said to thank Tanaka for the katsu compliment; Sho did. Dad moved his fan to dry Sho's jersey.
- Mio claims the pudding bet is now 3 ("It's interest."); Sho hasn't agreed. Her magnet sits on August. Mio and Dad secretly came to watch the Tokonami match (Dad folding his newspaper small, Mio standing on her seat); Sho saw them, did nothing, and nobody has mentioned it. Dad's schedule is under the fish magnet.
- Asahi meat bun ledger is at "That's 3". Noya's debt notebook is "mostly drawings of Kiyoko-san". Sho invented a "Kobayashi" story for Asahi.
- Oikawa knows Sho's name now but prefers "Tall-kun". At the sink on day 2 he listed Sho's day 1 back to him and said Sho turns his chin toward the blocker's hand right before he jumps: "When you look at the hand, they'll move it." Ukai on scouting a setter: "Not at him. At them. When all of them look good, that's him." Notebook: "watch the hitters" under Oikawa. Kuroo calls him "notebook".
- Date Tech: Aone (unnamed to Sho, "the big one") pointed at Asahi in the hallway, pushes his hands over the net (Tsukishima asked about it), and looked up at Karasuno's 飛べ banner after his match. Futakuchi: "Be ready for the rematch." Sho crossed "read" out of "read and commit" in the notebook.
- Notebook bracket: Tokonami crossed out; Karasuno's box now has 2 dots; Oikawa starred, "dangerous" underlined twice.
- Sho's rules: 2 checks max ("setter's hands, then the hitter, then feet"). For the eye, "Don't ask it. Be ready for both." It did not fire in ch 17. He calls it Observation Haki.
- Last status card (ch 13): Power C, Jump B, Speed C, Stamina B, Reception D, Serve D, Block E, Set E, Mentality B, Shamelessness S, Emperor's Eye: Partial awakening, Meta Vision: Scanning. Age 15, 182 cm, #13.

- Ch 21 threads: Tanaka slapped his face in the 2nd timeout ("I wasn't playing right. That's on me.") and hit a straight spike down the line; he hit Sho on the shoulder once and said nothing else. Kageyama sat next to Sho after the sub (Suga asked Sho to give him water and not tell him what he did); "Hinata was late" (Sho thought: He wasn't); Kageyama: "He talks to them. Every time." and, at the set break, "When I'm back, I'll set you so many you'll be sick of hitting." Suga to Kageyama: "I don't know yet!", "I was scared out there... I still didn't want to come off." "You were sitting right there. It helped." Oikawa sat alone with a towel over his head and looked at Suga. Sho's notebook under Seijoh now has 4 lines (watch the hitters; end guy moves the outside hand late after the hitter looks; Kindaichi goes with H on the fast one, reads the plain one; Suga: finger, their middle late). Sho caught his own chin turning toward a hand he wasn't hitting. Mio stood on her seat behind the Seijoh girls and sat down when they screamed for Oikawa; nobody has said anything about her or Dad.
- Dialogue lessons from the ch 21 review: keep timeouts short (30 seconds, a few lines), no Ukai slogans or quips at the end of an explanation, no mirrored lines, no Sho solving a canon problem, check back-row and front-row logic and the side-out count whenever a team is serving or blocking.

- Ch 22 threads: Ukai to Sho at the break: "Next time you see something, you tell me right then... You don't sit on it." "...Good eye." After the set: "You knew it was costing you, and you kept going." "Yes." "I saw you miss that one. And I left you on. So we're both going to talk about it. Later." That talk is owed (ch 26 or Ukai's POV in ch 29). Kageyama asked Tsukishima, Tanaka, Asahi and Sho what toss they want; Sho: "Flat. Out to the antenna." Kageyama left carton milk on Sho's knee: "Drink it." Oikawa: waved 2 fingers at Sho at 8-4, stayed on the left to block him at 24-23, got tooled, "Rude." Tsukishima noticed first: "Your eyes are red." Tanaka: "You LOOKED at him!" Noya: "Do it again!" Hinata: "WE BLOCKED HIM!", later stood in front of Sho without talking. Asahi twisted his towel watching the rotation; he's back on for set 3.
- Sho's eye: one-time forced fusion (bible note under Meta Vision). Depth comes back properly only the next morning. He chose it with Satoshi's knee in his head (*3 months is what took the knee. This is 1 set.*) and told nobody. The arc asks whether that was smart.
- Network note: in Claude Code cloud sessions the fandom wiki is blocked; WebSearch works. Allow haikyuu.fandom.com in the environment's network settings for proper canon fetches.
