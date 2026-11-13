# 06 Canon reference and canon check, ch 1 to 29

Report only. Source: the Feb 2020 fandom wiki dump. Every file named below sits in
`/tmp/claude-0/-home-user-second-serve/a9e5a82e-325e-544e-8344-93df3079cc1a/scratchpad/wikipages/` (written `W:` below).
Anything marked **[memory, unverified]** comes from my own memory of the series, not from the dump.

**What the dump can and can't do.** The manga chapter pages for ch 2 to 75 are empty stubs: title and navigation only, no plot (for example `W:The_King_of_The_Court.txt`, `W:Vs._the_Great_King.txt`, `W:The_Defeated.txt`). The two match pages are stubs too (`W:Karasuno_vs._Aobajohsai_(Practice_Match).txt` is 180 bytes). There's no Nekoma practice match page, no Neighborhood Association page and no Interhigh Preliminaries page. Most of the usable detail is in:
- the team pages: `W:Aobajohsai_High.txt`, `W:Nekoma_High.txt`, `W:Date_Tech_High.txt`, `W:Karasuno_High.txt`, `W:Tokonami_High.txt`
- `W:List_of_Matches.txt`, `W:Timeline.txt`
- the episode summaries in `W:Episode_Guide.txt`
- the character pages

About 55 pages were read in all. Line numbers below refer to the arc files with CR stripped (`tr -d '\r'`), which matches what `grep -n` gives on the originals.

---

## Part 4 first: canon errors found in our chapters

I checked these against the deliberate divergences in the bible ("Canon and divergence", the Arc 1 and Arc 2 outlines) and each chapter's Continuity block. Only accidental errors are listed. They're ordered by how much they matter.

### A. Hard errors (canon says otherwise; fix in the rebuild)

1. **Seijoh's "next match" after Karasuno is wrong** (arc2.md 4649, 4885, 5056, 5231)
   - What we wrote: Oikawa says "We play Ushiwaka next. Shiratorizawa." and "So I'll fix the looking thing tonight." Ukai says "The night before he plays Ushijima."
   - Canon: Seijoh played 3 matches on day 2 (Karasuno, then the quarterfinal vs Senseki, then the semifinal vs Johzenji) and the final vs Shiratorizawa on day 3 (`W:Aobajohsai_High.txt`: "one game on the first day, three on the second, one on the third"; `W:List_of_Matches.txt`).
   - So when Oikawa is at the sink, Seijoh still has 2 matches to play that same afternoon.
   - Fix: "We play again in an hour" and "Shiratorizawa tomorrow, if we get there". Ukai's line becomes "the day before he plays Ushijima", or "with 2 matches left today".
   - The "tonight" in the tell trade can stay if the tell is aimed at the final.
   - Touches ch 25 and 26 only. Ch 28's "Monday's final" fits a day-3 final.

2. **Inter-High final score** (arc2.md 5609 and Continuity 5884)
   - What we wrote: Aoba Johsai "pushed the 1st set to deuce".
   - Canon: Shiratorizawa won 25-22, 25-23. Neither set went to deuce (`W:List_of_Matches.txt`, `W:Aobajohsai_High.txt`).
   - Fix: "lost both sets by 3 or fewer", or "22-25, 23-25". The Continuity note says the scores are unverified; they're on the wiki.

3. **Exam pass mark** (arc2.md 6033 "Below 30"; 6067 and 6069 "It's 11 more than 30"; Continuity 6345)
   - Canon: "The passing grade for exams is 40 points. Students who fail their final exams must take weekend supplementary classes and a supplementary exam for each failed subject... The passing grade for supplementary exams is 80 points, and students must take them until they pass" (`W:Karasuno_High.txt`, Academics).
   - With a 40 line, Sho's Classical 41 is 1 point clear, which is more dramatic.
   - **NEEDS USER OK.** Sho's 41, Ukai's "11 more than 30" and Arc 3 ch 30 "Red pen" (exams, Classical) all lean on the number. Check every reference to 30 in arc3.md ch 30 to 32 before changing it.

4. **Number of Nekoma games** (arc1.md 5514 "They still took all 4."; 5598 "Pieces of 4 games."; Continuity 5659 and 5665)
   - Canon: 3 games, the match plus 2 rematches, all won 2-0 by Nekoma (`W:Nekoma_High.txt` "Practice Matches": 25-22, 25-23 / 25-22, 26-24 / 27-25, 32-30).
   - The prose at 5498 says "They played 2 more", which makes 3. Ukai's "Held it for 3 games" (5526) is right.
   - Fix: "They still took all 3", or "all 6 sets".
   - Our ch 15 Continuity block has no rematch scores. Canon's are 25-22, 26-24 and 27-25, 32-30. "Every one of them close" fits.
   - Check later chapters (arc3 ch 33 Kenma POV, ch 29's "May Nekoma page") for any "4 games" or "4 sets".

### B. Volleyball-rule problems

5. **Libero comes back in with no rally in between** (arc2.md 4300 area, ch 24 text line 225 of the chapter: "Tsukishima came back on as the rotation brought his spot to the front row, and Noya ran off and in again for Hinata at the back." Same in Continuity 4518: "18-20 (... Noya in for Hinata)")
   - Under FIVB, which Japanese high school play follows, there has to be a completed rally between 2 libero replacements [memory, unverified: FIVB rule 19.3.2.6]. The dump has no rules page that covers this.
   - So Noya can't leave for Tsukishima and come straight back in for Hinata in the same stoppage. He comes in for Hinata after the next rally (after Tanaka's 1st serve).
   - It's 1 sentence: "Noya waited out Tanaka's 1st serve and came back in for Hinata."
   - Ch 22 is clean. At 23-22, Tsukishima comes back on and Noya stays off (arc2.md 3353 area).

6. **Back-row Hinata under Yamaguchi's pinch serve** (ch 24)
   - The text handles it legally: Hinata goes back on for Yamaguchi at the next dead ball, which is his 2nd and last entry of the set.
   - Keep in mind for the rebuild: Hinata can't be taken off again in set 3, because he has used his re-entry.
   - Yamaguchi can't come in again in set 3 either.

7. **"Pinch-server rule"** (Continuity 1159, ch 17: "Ukai then sent Tanaka back in for the last rally (pinch-server rule)")
   - No rule sends a pinch server off. Tanaka coming back is Ukai's choice, and it uses Tanaka's 1 re-entry for set 2.
   - Fix the note. If the prose says "rule", fix that too. The text at 1006 ("Ukai lifted the number paddle") is fine.

### C. Softer mismatches (canon detail differs; low risk, worth fixing while rebuilding)

8. **Kageyama's first toss to Hinata: Thursday** (arc1.md ch 4, about 963 to 1000; Continuity 1361)
   - The wiki puts it on "the morning of the day before their game", the game being Saturday, which makes it Friday (`W:Tobio_Kageyama_1097.txt`, "Club Entrance").
   - The wording is loose ("Hinata trains hard the following days. So, in the morning of the day before their game..."). Either move it to Friday or leave it as a quiet change.

9. **Kuroo in set 1 vs Nekoma** (arc1.md ch 14; Continuity 5313 "Kuroo then blocked Asahi, 13-12")
   - `W:Tetsur_Kuroo_949.txt`: "Kuroo doesn't play much until late into the second set... he attacks back with a personal time difference he'd perfected with Kenma."
   - Kuroo is a starting middle blocker, so a set 1 block is possible, but canon saves his entrance (the paused quick, needling Hinata) for late set 2.
   - Option: give the 13-12 block to Inuoka or Yamamoto and keep Kuroo's net duel for ch 15, where we already have it.

10. **Seijoh's order of matches on day 1** (ch 20)
    - Correct as written: Karasuno watched Seijoh beat Oomisaki 25-14, 25-12 on day 1 (`W:List_of_Matches.txt`). Episode Guide ep 18: "Aobajōsai is up 24-13 in their 1st round match first set."
    - Seijoh had a bye in round 1 (`W:Aobajohsai_High.txt`: "exempt from the first round"). So "Seijoh's first match" is really their round 2, Karasuno's round 2 slot.

11. **Kageyama's apology to Hinata after the Seijoh loss** (ch 24 to 26)
    - Canon: after the loss, Kageyama apologized to Hinata for the last toss, taking the blame. In ch 79 Hinata gives that apology as his reason for wanting to hit with his eyes open (`W:Sh_y_Hinata_839.txt` and `W:Tobio_Kageyama_1097.txt`, Relationships).
    - Our chapters move Hinata's motive to Sho's dinner observation (ch 26, ch 27 Continuity notes the divergence). Fine, but the apology itself never appears.
    - It's a canon beat that belongs to them. Consider putting it in the rebuild of ch 24 (handshake or bench) or ch 26. It also gives ch 27's "I want to see" a 2nd root that is theirs.

12. **"Send" and "bring"** (ch 21 Continuity 2879; ch 22)
    - The wiki says Suga came up with "saying 'bring it' and 'send it'" for the combo (`W:K_shi_Sugawara_553.txt`, Personality). So they are spoken calls, and they're Suga's idea.
    - The anime summary says Oikawa "figures out the secret signals Kageyama and Hinata use for their quick strike" in set 1 (`W:Episode_Guide.txt`, ep 20).
    - Our ch 22 (Sho catches the spoken calls; Ukai switches to hand signals) is a deliberate bible divergence, so it stays. Two small fixes:
      - The ch 21 note "the wiki doesn't say whether they are spoken" is out of date.
      - Since Suga invented the calls, Ukai checking with Suga at the set break ("Did you say anything?" "No.") gets more bite if Suga says the calls were his.

13. **Shimada's look** (arc1.md 3727 area: "thin, with glasses and black hair... SHIMADA MART")
    - The wiki gives no appearance for Shimada (`W:Makoto_Shimada.txt`, empty section) and gives Takinoue "blonde messy hair and brown eyes" (`W:Y_suke_Takinoue.txt`).
    - The blond on Takinoue matches. Shimada's glasses are [memory, unverified]; I can't confirm either way.

14. **The roster has 12 numbers, and Sho is 13** (bible "Open question"; ch 13)
    - Canon Karasuno is numbered 1 to 12 (`W:Karasuno_High.txt` member table).
    - Whether an Inter-High prelim roster can register a 13th player isn't on the wiki. [memory, unverified: Japanese high school tournaments register 12 players.]
    - If that's right, Sho's place on the Inter-High bench in ch 16 to 24 is itself a canon break. That needs a decision from the user. **NEEDS USER OK** if anything changes. Touches ch 16 to 24, and Kinoshita or Narita's place on the bench.

15. **Oikawa's jersey in the practice match**
    - The wiki says he wore "the green #13 jersey he wore during a practice match with Karasuno in Chapter 14" (`W:T_ru_Oikawa_1128.txt`, Appearance).
    - Our ch 7 and 8 never give his number, so there's no error. If the rebuild has Sho read a number off him, it's 13. Kunimi wears 13 at the Inter-High (`W:Aobajohsai_High.txt`).

### D. Checked and correct (no action)

- **3v3:** 2-0, 25-23, 25-21, Hinata's side (`W:Hinata_Kageyama_and_Tanaka_vs._Tsukishima_Yamaguchi_and_Sawamura.txt`). Daichi's penalty, the 5 a.m. practices, the key from Tanaka, Suga noticing the key (`W:K_shi_Sugawara_553.txt`). Kiyoko only appears on match day in the manga (`W:Kiyoko_Shimizu.txt`); our ch 4 matches. Jackets from Kiyoko after the match (`W:Tadashi_Yamaguchi_889.txt`).
- **Seijoh practice match:** 25-13, 22-25, 23-25, Karasuno wins 2-1 (`W:Aobajohsai_High.txt`). Our "set 2 25-22 (inferred)" is confirmed. Ennoshita was the regular in canon (`W:Chikara_Ennoshita.txt`).
- **Noya's suspension:** 1 week from school, 1 month from the club, a vase broken near the vice principal (`W:Y_Nishinoya_1215.txt`).
- **Neighborhood match:** 4 alumni came; Suga and Noya join the Association side; Asahi fills the last spot (`W:Episode_Guide.txt` ep 9). Our ch 10 and 11 match.
- **Lev was not at the Nekoma match** (`W:Lev_Haiba.txt`: "He was not present at the practice match between Nekoma and Karasuno, due to his lack of experience"). Inuoka is #7, a 1st-year middle blocker (`W:S_Inuoka.txt`).
- **Inter-High scores:** Tokonami 25-12, 25-14; Date Tech 25-19, 25-22; Seijoh 15-25, 25-23, 31-33 (`W:List_of_Matches.txt`).
- **Date Tech numbers:** Kamasaki #1, Moniwa #2 (captain), Futakuchi #6, Aone #7 (`W:Date_Tech_High.txt`). Our "the number 6" and "the number 1" are right.
- **Seijoh numbers:** Matsukawa #2, Hanamaki #3, Iwaizumi #4, Watari #7 (libero), Kindaichi #12, Kunimi #13 (`W:Aobajohsai_High.txt`).
- **Oikawa:** right knee brace, from overwork (`W:T_ru_Oikawa_1128.txt`). He once nearly hit Kageyama for asking about the serve.
- **Ukai:** headband, smokes, Sakanoshita, setter #2 eight years ago (`W:Keishin_Ukai.txt`).
- **Takeda:** teaches modern Japanese literature; favorite food nikujaga (`W:Ittetsu_Takeda.txt`). Ch 16's nikujaga joke lands.
- **Tsukishima's favorite food** is strawberry shortcake (`W:Kei_Tsukishima.txt`). Ch 4's bribe is canon-true.
- **The Fukurodani Academy Group** is Fukurodani, Nekoma, Shinzen and Ubugawa (`W:Nekoma_High.txt`). Ch 29 is right.
- **Ukai coaching only until Nekoma**, then staying on after it (`W:Episode_Guide.txt` ep 10, 13).
- **Rotation bookkeeping in ch 22's 17-20 to 25-23 run:** I re-derived it and it holds. Sho goes 5, 4, 3, 2, then serves at 24-23. Oikawa front-left facing Sho at right front at 23-23 is consistent.

---

## Part 1: Canon events by our chapter

Dates: an official timeline puts the series in 2012 (`W:Timeline.txt`):
- April: Hinata enrolls; Seijoh practice match.
- May: Nekoma practice match.
- June: Karasuno loses to Seijoh in Inter-High round 3; Hinata turns 16.
- July: Tokyo training camp.
- August: Spring High round-1 qualifiers.

### Ch 1 to 2: club day 1 and the wig (canon ch 1 to 2; ep 1 to 2)
- Hinata walks into the gym, finds Kageyama, and they argue.
- Daichi, Suga and Tanaka arrive and recognize Kageyama from watching his junior high games. Hinata shouts that he'll be Karasuno's ace (`W:Tobio_Kageyama_1097.txt`).
- They ignore Daichi. The vice principal ("dean") comes in and scolds Daichi.
- Hinata challenges Kageyama to serve at him. Kageyama's serve is one Tanaka says he couldn't receive.
- On the next serve the ball bounces off Hinata's face into the vice principal and knocks his wig off.
- Daichi throws them out with their forms: the team is short of players but doesn't want people who won't be teammates. Kageyama says he'd rather do everything alone (same page).
- Outside, they challenge the club to a match. Tanaka plays on their side. Condition: if they lose, Kageyama never plays setter while Daichi is captain (same page; `W:Sh_y_Hinata_839.txt`).
- Tanaka at the window: morning practice starts at 7:00. They decide to come at 5 a.m. (same page).
- Daichi turns it into a 3-on-3: Hinata, Kageyama and Tanaka against the new 1st years plus Daichi (`W:The_Formidable_Ally_(Episode).txt`).
- In the manga Kiyoko hands Daichi the registration forms on day 1, then isn't seen again until the 3v3 (`W:Kiyoko_Shimizu.txt`).

### Ch 3: dawn practices (canon ch 3 to 4; ep 2 to 3)
- Tanaka arrives with the key and lets them in (`W:Tobio_Kageyama_1097.txt`). Suga caught on because Tanaka, who's always late, asked for the key (`W:K_shi_Sugawara_553.txt`).
- Suga helps. Kageyama refuses to toss to Hinata.
- Kageyama, at a vending machine, overhears Hinata telling Suga he wants to beat him (`W:Tobio_Kageyama_1097.txt`).
- They practice by the soccer field until dark. Tsukishima and Yamaguchi turn up.
  - Yamaguchi: "Geh, t-shirts? It's cold out!" and tells them Tsukishima is 188 cm (`W:Tadashi_Yamaguchi_889.txt`).
  - Tsukishima brings up "King of the Court" and offers to throw the game. Kageyama grabs his collar.
  - Hinata jumps for a ball Tsukishima holds up.
  - Walking home, Tsukishima: "Uselessly hot-blooded people irritate me" (`W:Kei_Tsukishima.txt`).
- By the morning of the day before the game, Hinata can take Kageyama's receives. Kageyama finally tosses to him (`W:Tobio_Kageyama_1097.txt`). The anime has Tanaka also help with receive and spiking (`W:The_Formidable_Ally_(Episode).txt`).

### Ch 4 to 6: the 3v3 (canon ch 5 to 9; ep 4 to 5)
- **Sides:** Hinata, Kageyama and Tanaka vs Tsukishima, Yamaguchi and Daichi. **2-0, 25-23, 25-21** (`W:Hinata_Kageyama_and_Tanaka_vs._Tsukishima_Yamaguchi_and_Sawamura.txt`).
- **Order** (`W:Tobio_Kageyama_1097.txt`, `W:Tadashi_Yamaguchi_889.txt`, `W:Kei_Tsukishima.txt`):
  - On match day they race to the gym.
  - Before the start, Tsukishima talks loudly about who to block first. Yamaguchi: "Tsukki, they can hear you."
  - Tanaka scores 1st off Kageyama's toss. Tsukishima blocks Hinata again and again and keeps up "King".
  - Hinata defends Kageyama when Tsukishima brings up the junior-high toss nobody went for.
  - Yamaguchi serves into the net.
  - Hinata cuts in front and Kageyama sets him on instinct; the spike goes out.
  - Kageyama explains a quick badly. Suga tells him to match Hinata's movement; Kageyama tells Hinata to jump his highest and fastest.
  - Hinata hits it with his eyes closed. The next tries hit his face. Kageyama smiles; Hinata yells about his cheek.
  - Then quicks land and Hinata becomes a decoy for Tanaka. Tsukishima pulls Yamaguchi into the block; Hinata runs to the other side.
- **After:** Daichi tells Tsukishima "they made you play seriously". The handshake turns into a quarrel. Kiyoko brings the jackets. Tanaka teaches Hinata and Kageyama hand signals (`W:Tadashi_Yamaguchi_889.txt`).
- Takeda arrives with the Seijoh practice match. The condition: Kageyama sets the whole match (`W:A_Coward_s_Anxiety_(Episode).txt`).
- **Jerseys:** jackets now. Numbered jerseys at Golden Week (`W:Decision_(Episode).txt`).

### Ch 7 to 8: Seijoh practice match (canon ch 10 to 14; ep 6 to 7)
- **Result:** Seijoh 25-13, 22-25, 23-25. Karasuno wins 2-1 (`W:Aobajohsai_High.txt`).
- **Karasuno lineup:** Ennoshita played as a regular in place of the absent Asahi and Noya (`W:Chikara_Ennoshita.txt`). The other 5 are [memory, unverified]: Daichi, Tanaka, Tsukishima, Hinata, Kageyama. In the fic, Sho takes Ennoshita's spot, a bible choice.
- **Before the match:** Kindaichi keeps calling Kageyama "King". 2 Seijoh players badmouth Karasuno in the hallway; Tanaka and Tsukishima scare them; Daichi reprimands (`W:Kei_Tsukishima.txt`).
- Kiyoko's encouragement makes Hinata worse (`W:Kiyoko_Shimizu.txt`).
- Hinata meets Kindaichi by the toilets and names him "turnip head" (`W:Y_tar_Kindaichi.txt`).
- **Set 1:** Hinata's mistakes. **Set 2:** the quick works. Kageyama says the setter on court isn't their real one (`W:Episode_Guide.txt` ep 6).
- **Set 3, Oikawa's entry:** he comes on as a pinch server and aims at Tsukishima's receive. Seijoh close the gap until Daichi changes the formation (ep 7).
  - His jersey is a green #13 (`W:T_ru_Oikawa_1128.txt`).
  - 24-21 and the subbing-for-Kunimi detail are from the bible; the wiki doesn't confirm them [memory].
- **Afterwards:** Oikawa warns that next time Seijoh start with "all of its aces" (ep 7). Seijoh's coach calls Tsukishima "a clever blocker, despite being somewhat lacking in drive" (`W:Kei_Tsukishima.txt`).
- After the match, Kunimi smacks Kindaichi's arm when he says it hurts that Kageyama says "we" with his new team (`W:Akira_Kunimi.txt`).

### Ch 9: Nishinoya's return (canon ch 15 to 16; ep 8)
- Ukai, still just the shop clerk, gives Tanaka, Hinata and Kageyama free popsicles despite Tanaka's insult (`W:Keishin_Ukai.txt`).
- Kageyama reveals the Shiratorizawa rejection [bible; wiki ep 8 summary has none].
- Noya runs in and receives Kageyama's serve perfectly. He learns Asahi isn't back and storms out (`W:Episode_Guide.txt` ep 8).
- When Hinata calls him "senpai" and "awesome", Noya offers ice cream (`W:Y_Nishinoya_1215.txt`). His favorite is Garigari-kun, soda flavor.
- **History:** at the start of March Asahi stopped coming. Noya went after him and knocked into the vice principal, who broke a vase. 1 week of school suspension and a 1-month club ban (same page).
- Asahi stayed away "for a month" after Date Tech (`W:Asahi_Azumane_81.txt`).

### Ch 10: Asahi's history; Ukai becomes coach (canon ch 17 to 19; ep 8 to 9)
- **Asahi:** against Date Tech every spike was blocked. He blamed himself, more so because Noya didn't.
  - The fight. Noya's line: "Don't you DARE give up on the shots I've worked so hard to receive... I'm not allowed to attack... I have no intention of blaming you... But to just accept defeat so selfishly... That's something I cannot forgive!!"
  - The next day Asahi skipped the club, argued with Noya again and quit (`W:Asahi_Azumane_81.txt`; `W:Y_Nishinoya_1215.txt` quotes).
- **Suga and Asahi:** "murky" after the Date Tech loss; they patch it up at the Neighborhood match (`W:K_shi_Sugawara_553.txt`).
- **Ukai:** Takeda begs again and again, hoping the Ukai name will open doors (`W:Keishin_Ukai.txt`, `W:Ittetsu_Takeda.txt`).
  - Ukai agrees once he hears about the Nekoma match, but "only until the practice match is finished".
  - He then sets up the Neighborhood match to see the players (`W:Episode_Guide.txt` ep 9).
  - He only coached at first to beat Nekoma (`W:Keishin_Ukai.txt`).

### Ch 11 to 12: Neighborhood Association match (canon ch 20 to 24; ep 9 to 10)
- **Neighborhood side:** only 4 association players came. Suga and Noya went to their side, and Asahi filled the last spot (`W:Episode_Guide.txt` ep 9). Ukai coaches.
  - Shimada Makoto: 26, 177.7 cm, wing spiker. Old Karasuno #11, wing spiker and pinch server. Shimada Mart (`W:Makoto_Shimada.txt`, `W:Karasuno_High.txt`).
  - Takinoue Yusuke: 26, 185.6 cm, middle blocker. Old #9. Takinoue Electronics; his manga captions advertise a sale (`W:Y_suke_Takinoue.txt`).
  - Uchizawa Hidenori: 28, 176.3 cm (`W:Hidenori_Uchizawa.txt` infobox).
- **Karasuno side:** the canon triple block on Asahi is Kageyama, Tanaka and Tsukishima (ep 9). The other 3 are [memory, unverified].
- **What happens:** Asahi gets past the triple block and gets his confidence back. Hinata and Kageyama's quick shocks Ukai, who weighs Kageyama's skill against Suga's trust and experience (ep 10).
  - Hinata is distracted comparing himself to Asahi, has a mishap, and Kageyama talks him into the decoy role (ep 10).
  - Noya: "So one more time, call out for the toss! Ace!" and "that 2 cm gap between the ball and the floor is the ace's lifeline" (`W:Y_Nishinoya_1215.txt`).
- **Result:** the Association wins. Set scores aren't on the wiki; the bible's 2-0 is [memory].
- Shimada's jump float serve is canon (`W:Episode_Guide.txt` ep 14; `W:Karasuno_High.txt`).

### Ch 13: Golden Week camp (canon ch 25 to 28; ep 11)
- **Dates:** not on the wiki. [memory, unverified: the last days of Golden Week, about May 2 to 6, with the Nekoma match on the last day.] `W:Timeline.txt` only says May.
- Ukai hesitates over the starting setter and picks Kageyama (ep 11 in `W:Episode_Guide.txt`; `W:Decision_(Episode).txt`).
- **Starting lineup vs Nekoma:** Daichi, Noya, Asahi, Tanaka, Tsukishima, Kageyama, Hinata (`W:Decision_(Episode).txt`).
- **Jerseys handed out:** Hinata gets #10, the Little Giant's number; Karasuno's only Nationals team (same page).
- **Numbers** (`W:Karasuno_High.txt`): Daichi 1, Suga 2, Asahi 3, Noya 4, Tanaka 5, Ennoshita 6, Kinoshita 7, Narita 8, Kageyama 9, Hinata 10, Tsukishima 11, Yamaguchi 12.
- **Hinata meets Kenma** after getting lost on a run. Kenma is playing a game and says he's lost too. He says he doesn't like volleyball or dislike it: he hates getting tired, but his friends play. Kuroo collects him. Kenma: "see you soon" (`W:Kenma_Kozume_501.txt`).
- **The stories of Ikkei's old training** come at camp (ep 11: "Surprising backstories of the upperclassmen"). Ennoshita, Narita and Kinoshita quit over Ikkei's training and came back to find him hospitalized: "the Ungrateful Second Years" (`W:Chikara_Ennoshita.txt`).
- **Nekoma before the match:** they beat Tsukinokizawa 2-0 (25-21, 25-13). Kuroo calls Kenma "our backbone, brain and heart" (`W:Tetsur_Kuroo_949.txt`, `W:Nekoma_High.txt`).
- Hinata doesn't recognize Noya after the bath (hair down, 10 cm shorter) (`W:Y_Nishinoya_1215.txt`).

### Ch 14 to 15: Nekoma practice match (canon ch 27 to 34; ep 11 to 13)
- **Scores:** 25-22, 25-23; rematch 1: 25-22, 26-24; rematch 2: 27-25, 32-30. Nekoma win all 3 (`W:Nekoma_High.txt`).
- **Nekoma roster** (`W:Nekoma_High.txt`):

| # | Player | Year and position |
| --- | --- | --- |
| 1 | Kuroo | 3rd, captain, middle blocker |
| 2 | Kai | 3rd, vice captain, wing spiker |
| 3 | Yaku | 3rd, libero |
| 4 | Yamamoto | 2nd, wing spiker, ace |
| 5 | Kenma | 2nd, setter |
| 6 | Fukunaga | 2nd, wing spiker |
| 7 | Inuoka | 1st, middle blocker |
| 8 | Teshiro | 1st, setter |
| 11 | Lev | absent |
| 12 | Shibayama | 1st, libero |

- **Coach:** Nekomata. Nekoma's chant is the blood line (`W:Nekoma_High.txt`).
- **Line-up outside:** Tanaka and Yamamoto clash. Yaku breaks it up; he and Suga apologize to each other and bond (`W:Morisuke_Yaku.txt`).
- Hinata sees Kenma and asks why he didn't say. Kenma: you didn't ask, and he'd seen "Karasuno" on Hinata's shirt (`W:Kenma_Kozume_501.txt`).
- Daichi and Kuroo shake hands; Kuroo notes Daichi is "the cunning type" (`W:Tetsur_Kuroo_949.txt`).
- **Set 1** (`W:Kenma_Kozume_501.txt`, `W:Episode_Guide.txt` ep 12):
  - Kenma serves 1st. The quick makes it 1-0.
  - Nekoma timeout. Kenma: narrow Hinata's range; Inuoka chases him.
  - Inuoka gets touches. Kenma dumps.
  - Kenma reads Tsukishima as a thinker and fools him by glancing right and setting the other way.
  - Inuoka blocks the quick clean. Nekoma 25-22.
- **Set 2:**
  - Kageyama teaches Hinata to hit straight and use his eyes for gaps. Hinata changes his path in mid-air (1 goes long) (ep 12).
  - Kuroo plays little until late in the set, needles Hinata, and hits his paused quick with Kenma (`W:Tetsur_Kuroo_949.txt`).
  - Nekoma 25-23 (ep 13).
- **After:** Ukai agrees to stay as full-time coach (ep 13). Kuroo tells Tsukishima he's "not like a high school student at all". He and Daichi shake hands again, both squeezing hard (`W:Tetsur_Kuroo_949.txt`).
  - Inuoka and Hinata praise each other in gibberish. Hinata: "Inuoka is really awesome!!" (`W:S_Inuoka.txt`).
  - Kenma tells Hinata he looks forward to a real match (`W:Kenma_Kozume_501.txt`). The promise to meet at Nationals is in ep 13.
- **Ukai on Kenma:** he "can show his real skills because of Nekoma's stable receives" (`W:Kenma_Kozume_501.txt`).

### Ch 16: between Nekoma and the prelims (canon ch 35 to 36; ep 14)
- The bracket comes out. Final practices on back-row attacks and signals.
- Yamaguchi secretly asks Shimada for jump float help so he won't be the only 1st year who can't contribute (`W:Episode_Guide.txt` ep 14).
- Kiyoko fixes and washes the old banner, "Take to the Skies" (`W:Kiyoko_Shimizu.txt`, `W:Karasuno_High.txt`).
- Ukai's lines (`W:Keishin_Ukai.txt`, ch 35):
  - "'This is the final ball!' Think that at all times..."
  - "If you only pay attention to what's 'above', you'll get tripped up from below."

### Ch 17: Tokonami (canon ch 37 to 40; ep 15 to 16)
- **Score:** 25-12, 25-14 (`W:List_of_Matches.txt`).
- **Before the match:** rumors of the "Flightless Crows" / "Fallen Champions" (`W:Karasuno_High.txt`).
- Daichi meets Ikejiri (#4 wing spiker), from Izumitate Middle School. They'd promised to meet on court (`W:Daichi_Sawamura_167.txt`, `W:Hayato_Ikejiri.txt`).
- Ukai: "it's a matter of who breaks out of it faster" (`W:Keishin_Ukai.txt`, ch 39).
- **The match:** Karasuno take the 1st 3 points. Tanaka's celebrating earns a warning (`W:Ry_nosuke_Tanaka_762.txt`).
- Ikejiri remembers Daichi's junior-high speech. Afterwards he tells Daichi to keep winning for Tokonami (ep 16).
- **Tokonami roster** (`W:Tokonami_High.txt`): Komaki #1, Sakurai #2 (libero), Shibuya #10; Chaya, Haga (setter), Tamagawa; Ikejiri.

### Ch 18 to 19: Date Tech (canon ch 41 to 47; ep 16 to 18)
- **Score:** 25-19, 25-22 (`W:List_of_Matches.txt`, `W:Date_Tech_High.txt`). The anime summary says "25-21" for set 1 (`W:Episode_Guide.txt` ep 17). Use the manga number.
- **Date Tech** (`W:Date_Tech_High.txt`): highest blocking rate in the country, "Date's Iron Wall" banner. Strategy: a strong serve to break the formation, then block the return. A chant people want to join in with.
- **Set 1:** Ukai's plan is to make Hinata stand out. When Aone keeps up, Kageyama goes to Asahi (ep 16).
- **Set 2:** a double rotation moves Hinata away from #7, so Asahi faces Aone. At 24-22 Hinata rotates out, and it's on Asahi (ep 17).
- **Noya's foot save** (`W:Y_Nishinoya_1215.txt`, Abilities).
- **Aone:** "high, fast, and expansive wall". Ukai: "He stays calm and avoids tunnel vision" (`W:Takanobu_Aone.txt`). He shakes Hinata's hand after (same page).
- **Futakuchi:** "Hey, what was that? He's supposed to get dejected." (`W:Kenji_Futakuchi.txt`).
- Leaving, they see Seijoh up 24-13 in set 1 of their 1st match (ep 17).

### Ch 20 to 24: Seijoh at the Inter-High (canon ch 48 to 69; ep 18 to 24)
- **Score:** 15-25, 25-23, 31-33 (`W:List_of_Matches.txt`). Day 2 of 3 for Seijoh (`W:Aobajohsai_High.txt`).
- **Day 1:** Karasuno watch Oikawa's serves and sets against Oomisaki (25-14, 25-12) and are shaken (ep 18).
- **Day 2 opening:** Oikawa's setter dump, then Kageyama's own dump makes it 2-1 (ep 18).
- **Set 1:** Seijoh pull away. Oikawa works out the quick's signals; Kageyama panics and sets too fast (ep 19).
  - "With no timeouts left for this set, Ukai has no choice but to sub Sugawara in" (ep 19). Seijoh take the set.
- **Set 2:** Karasuno lead through Suga's tactics, but Oikawa's serve is still a problem (ep 20).
  - Kageyama comes back and "attempts to communicate with each of his teammates and learns how to accommodate the different attackers". He syncs with Tsukishima (ep 21).
  - Oikawa remembers his jealousy of Kageyama and his goal of beating Ushijima.
  - Ukai at the set: "Seijoh is vastly better in terms of experience and technique..." (`W:Keishin_Ukai.txt`, ep 21).
- **Set 3:** Seijoh pull ahead. **Yamaguchi's pinch serve is a service error**, but it calms the team and they catch up (ep 22).
  - Shimada and Takinoue are in the stands. Shimada (ep 23): "Serving is the only time you're alone..." and "this chance to feel this regret... will definitely make him stronger" (`W:Makoto_Shimada.txt`).
  - The wiki doesn't give the score at Yamaguchi's serve. The bible's 15-15 is [memory].
- **Deuce:** Kageyama sees Kunimi's changed attitude (Kunimi's "true strength lies in his late game plays", `W:Akira_Kunimi.txt`).
  - Kageyama despairs; Hinata reminds him he's on Karasuno now. Oikawa sees he is no longer the Solitary King.
  - Ukai: Oikawa "still managed to find the smallest gap and pulled off a feint".
  - **Seijoh block Hinata's quick at the end.** 31-33 (ep 24; `W:Keishin_Ukai.txt` quotes).
- **Oikawa on the serve:** his coach lets him take time and breaks alone to recover his focus (`W:T_ru_Oikawa_1128.txt`).

### Ch 25 to 26: after the loss; the dinner (canon ch 69; ep 24)
- **Takeda's speech:** "Isn't losing difficult for all of you? ... If you stay on your hands and knees, that proves that you are weak." (`W:Ittetsu_Takeda.txt`, ep 24). The setting isn't given.
- **Ukai at dinner, which he pays for:** "Eat... eat... a little at a time... but be sure... to grow stronger." (`W:Keishin_Ukai.txt`, ep 24).
- **Kageyama apologizes to Hinata** for the last toss (`W:Sh_y_Hinata_839.txt`; see error 11).
- **Seijoh's day continues:** they beat Senseki (?, 25-22) and Johzenji, then lose the final to Shiratorizawa 22-25, 23-25 (`W:List_of_Matches.txt`).

### Ch 27 to 28: aftermath; the 3rd years stay (canon ch 70 to 71; ep 25; S2 ep 1)
- The 3rd years must decide whether to retire. Hinata and Kageyama vent in the gym. The prelim winner is announced. 1st real practice for Spring High (ep 25).
- Kiyoko "was reluctant to step down from the club after the Interhigh" (`W:Kiyoko_Shimizu.txt`). Suga stays with the others "even when most third years choose to retire" (`W:K_shi_Sugawara_553.txt`).
- Ukai (S2 ep 2): "Don't forget the frustration... you don't need to hold onto the feeling of losing. Hurry up and wipe that away!" (`W:Keishin_Ukai.txt`).
- Noya starts practicing tosses with Suga after the Seijoh loss (`W:Y_Nishinoya_1215.txt`). That's a free beat for ch 27 to 29.

### Ch 29: the Tokyo invite, exams, Yachi (canon ch 72 to 78; S2 ep 1 to 3)
- **The invite:** Takeda "barges in" during practice with news of Nekoma's camp (S2 ep 1, `W:Episode_Guide.txt`). Our message by phone is a deliberate change (bible ch 28).
- Hinata and Kageyama, lost on a run, meet Ushijima (S2 ep 1).
- **Exams:**
  - Hinata, Kageyama, Noya and Tanaka panic. Daichi vows the whole team goes and makes them study. The 2nd years study at Tanaka's house. Tsukishima is a reluctant tutor; Yachi helps (S2 ep 2).
  - Pass mark 40. Make-up exams on a weekend, pass mark 80 (`W:Karasuno_High.txt`).
  - Takeda wanted "supplementary exams and lessons" to come before club events (`W:Ittetsu_Takeda.txt`).
  - Hinata says he's never scored double digits on a high school test (`W:Sh_y_Hinata_816.txt`). Ennoshita has never failed (`W:Chikara_Ennoshita.txt`).
- **The make-up:** Hinata and Kageyama fail, take the make-up, and Saeko drives them to Tokyo, arriving late (S2 ep 3, `W:Saeko_Tanaka.txt`).
- **Yachi:**
  - 1st year, class 5, 149.7 cm (`W:Hitoka_Yachi.txt`). Kiyoko recruited her "after the first tournament" (`W:Karasuno_High.txt`).
  - She hears Takeda and Ukai say there's no bus money. Her mother pushes back. Hinata's "Townsperson B" talk. She makes a donations poster from photos of the quick. She tutors Hinata and Kageyama; they fail anyway (`W:Hitoka_Yachi.txt`).
  - She calls Tanaka in to break up their eyes-open fight (canon ch 82, Arc 3).
- **The camps:**
  - The 1st Tokyo matches include Shinzen (Eikichi touches the quick) (S2 ep 3).
  - Later "Karasuno arrives at Saitama for the training camp" (S2 ep 7).
  - Timeline: "July: Tokyo training camp" (`W:Timeline.txt`). The fic's "August at Shinzen" for the Saitama camp is [memory, unverified].

---

## Part 2: Voices and facts

Year is the 2012 school year. Heights are April figures. Sources are the character infoboxes unless noted otherwise.

| Who | Year, class, # , position, height | Voice and habits | Key ties |
| --- | --- | --- | --- |
| Hinata Shoyo | 1st, class 1; #10; middle blocker and decoy; 162.8 cm | Loud, cheerful, a natural schmoozer. Hides behind teammates when scared, then challenges. Tanaka calls him "Number One Shortie"; Oikawa and Kuroo call him "Chibi-chan" / "Shrimp"; Kageyama calls him "dumbass" (boke) (`W:Sh_y_Hinata_816.txt`) | Kageyama; idolizes the Little Giant; befriends Kenma and Aone |
| Kageyama Tobio | 1st, class 3; #9; setter; 180.6 cm | Blunt, short answers, flustered by praise [memory]. Calls Hinata "boke"; calls Suga and Daichi "-san". Likes pork curry with an egg; milk [memory] (`W:Tobio_Kageyama_1097.txt`) | Learned to serve by watching Oikawa; respects Suga as a teacher |
| Sawamura Daichi | 3rd, class 4; #1; captain, wing spiker, defensive specialist; 176.8 cm | Kind, patient, terrifying when angry. Mature; mocks Asahi's lack of "ace-like presence" (`W:Daichi_Sawamura.txt`, `_167`) | Suga (close friends, the only one who can lecture him); Ikejiri; recruited Kiyoko |
| Sugawara Koshi | 3rd, class 4; #2; vice captain, setter, pinch server; 174.3 cm | Soothing; Kageyama's "handler". Watches from the bench and gives tips; gets stressed and overthinks on court. Thought up "bring it" and "send it". Likes super-spicy mapo tofu (`W:K_shi_Sugawara_553.txt`, `_552`) | Daichi; Asahi (setter-hitter bond "built over time"); Yaku (fellow caretakers) |
| Azumane Asahi | 3rd, class 3; #3; ace; 184.7 cm | Gentle, "glass heart", looks older and scary. Rumors (gang leader, 5 years in high school) (`W:Asahi_Azumane.txt`, `_81`) | Noya (foils; "slightly scared of Noya"); Daichi teases him; Suga |
| Nishinoya Yu | 2nd, class 3; #4; libero; 159.3 cm | Loud, impulsive, no filter. Names his moves (Rolling Thunder). Focused and calm in games. Shy with new girls. Can't explain receiving [bible]. Chidoriyama, best libero award (`W:Y_Nishinoya_1215.txt`) | Asahi; Tanaka (Kiyoko guard); Hinata |
| Tanaka Ryunosuke | 2nd, class 1; #5; wing spiker; 177.2 cm | Loud, hot-headed, looks like a delinquent, protective of the 1st years. Spins his shirt after points in practice. "If you look down on us like that, we'll chew you up and spit you out." Likes melon bread (`W:Ry_nosuke_Tanaka_762.txt`) | Noya; sister Saeko; Yamamoto |
| Tsukishima Kei | 1st, class 4; #11; middle blocker; 188.3 cm | Blunt needler; "King"; "Uselessly hot-blooded people irritate me." Respects only the 3rd years. Headphones; strawberry shortcake (`W:Kei_Tsukishima.txt`) | Yamaguchi ("Tsukki"); brother Akiteru (Arc 3) |
| Yamaguchi Tadashi | 1st, class 4; #12; middle blocker and pinch server; 179.5 cm | Shy, snickers along with Tsukki, apologizes ("Sorry, Tsukki"). Works in secret on the jump float with Shimada (`W:Tadashi_Yamaguchi_889.txt`) | Tsukishima saved him from bullies |
| Ennoshita Chikara | 2nd, class 4; #6; wing spiker (mostly left); 175.4 cm | Quiet, gentle smile; the only 2nd year who can control Tanaka and Noya. Analytical; next captain; never failed a test (`W:Chikara_Ennoshita.txt`) | Narita and Kinoshita ("Ungrateful Second Years") |
| Narita Kazuhito | 2nd; #8; middle blocker; 180.2 cm | Shaved head; hardly characterized (`W:Kazuhito_Narita.txt`) | Never seen apart from Ennoshita or Kinoshita |
| Kinoshita Hisashi | 2nd, class 2; #7; wing spiker and pinch server; 174.7 cm | Anxious about his ability; sly ("Don't take off your shirt, baldy!") (`W:Hisashi_Kinoshita.txt`) | Narita, Ennoshita |
| Shimizu Kiyoko | 3rd, class 2; manager; 166.2 cm | Quiet, scolds Tanaka and Noya when they go too far; ex-hurdler. Wears black tights from habit; ignored Oikawa (`W:Kiyoko_Shimizu.txt`) | The 3rd years (Daichi recruited her) |
| Ukai Keishin | 26; ex-setter #2, not a regular; 178.2 cm | Dyed blond hair, headband, 2 left-ear piercings, smokes. Runs the shop and the farm at dawn. Calls the kids "hyperactive ones and simpletons". Grandson of Ikkei (`W:Keishin_Ukai.txt`) | Takeda; Nekomata; Naoi ("Benchwarmers Club") |
| Takeda Ittetsu | 29; modern Japanese literature teacher; 166.5 cm | Polite, persistent, bows 90 degrees, clumsy, makes speeches. "I'm good at getting on my knees and begging." (`W:Ittetsu_Takeda.txt`) | Ukai |
| Oikawa Toru | 3rd; #1 (#13 in the practice match); captain and setter; 184.3 cm | Cheerful remark, then a menacing afterthought. Calls Kageyama "Tobio-chan", Hinata "Chibi-chan", Suga "Mr. Refreshing", Ushijima "Ushiwaka-chan". Takes Mondays off; right knee brace (`W:T_ru_Oikawa_1128.txt`, `W:K_shi_Sugawara_552.txt`) | Iwaizumi ("Iwa-chan"); hates "geniuses" |
| Iwaizumi Hajime | 3rd, class 5; #4; vice captain, ace; 179.3 cm | Stubborn, reliable, violent with Oikawa (balls to the head), supportive of Kageyama. Calls Oikawa "Assikawa" / "Shittykawa" (`W:Hajime_Iwaizumi.txt`, `W:T_ru_Oikawa_1128.txt`) | Oikawa's childhood friend |
| Kindaichi Yutaro | 1st; #12; middle blocker; 189.2 cm | Competitive, stubborn; stiff "thank you" when Oikawa praises him. "Turnip head" (`W:Y_tar_Kindaichi.txt`) | Kunimi; ex-teammate of Kageyama |
| Kunimi Akira | 1st, class 6; #13; wing spiker; 182.8 cm | Lazy-quiet, saves energy, strong late in matches. Hates "go all out" (`W:Akira_Kunimi.txt`) | Kindaichi |
| Kozume Kenma | 2nd, class 3; #5; setter; 169.2 cm | Quiet, avoids people, "brain"; dump-shot expert. Calls Kuroo "Kuro" (`W:Kenma_Kozume_501.txt`) | Kuroo (neighbor); Hinata (texts) |
| Kuroo Tetsuro | 3rd, class 5; #1; captain, middle blocker; 187.7 cm | Scheming "provocation expert" with a loud laugh. Treats younger players as kids ("Ah, youth"). Calls Hinata "Chibi-chan" (`W:Tetsur_Kuroo_949.txt`, `W:Sh_y_Hinata_816.txt`) | Kenma; Daichi (crushing handshakes) |
| Yaku Morisuke | 3rd, class 5; #3; libero; 165.2 cm | Parental, a "demon senpai", touchy about height; receives Asahi's spike after seeing it once (`W:Morisuke_Yaku.txt`) | Suga; Lev (later) |
| Inuoka So | 1st, class 1; #7; middle blocker; 185.3 cm | Bright, bouncy like Hinata; most agile on Nekoma; "I won't lose when it comes to attacking!" (`W:S_Inuoka.txt`) | Shibayama; Hinata |
| Aone Takanobu | 2nd; #7 (Inter-High); middle blocker; 191.8 cm | Almost silent; "locks on" to aces; kind and shy; no eyebrows (`W:Takanobu_Aone.txt`) | Hinata (handshake, friendship); Futakuchi |
| Futakuchi Kenji | 2nd; #6 (Inter-High); wing spiker; 184.2 cm | Easygoing provoker, argues with Kamasaki; Moniwa calls him a problem kohai (`W:Kenji_Futakuchi.txt`, `W:Date_Tech_High.txt`) | Aone; Kamasaki; Moniwa |
| Shimada Makoto | 26; ex-#11; wing spiker and pinch server; 177.7 cm | Talks about gravity, being alone at the serve, and Ikkei's "To enjoy competitive activities, you need to be good" (`W:Makoto_Shimada.txt`) | Yamaguchi (mentor); Takinoue |
| Takinoue Yusuke | 26; ex-#9; middle blocker; 185.6 cm | Upbeat, confident; explains rules to girls in the stands; stung at being called "old man"; bangs water bottles to cheer (`W:Y_suke_Takinoue.txt`) | Shimada |

---

## Part 3: Volleyball rules as they apply

From the wiki:
- **6 a side, 3 touches,** no one touches twice in a row, rally scoring, and the team that wins the rally serves (`W:Volleyball.txt`).
- **The libero** is "exclusively defensive". Can't block, spike or play at the net, can't be captain, wears a contrasting jersey. Can replace any player, but not the player about to serve, and not during a rally. A player designated libero can't play other roles that match (`W:Positions.txt`, `W:Volleyball.txt`). Noya never serves in canon, which fits FIVB [memory].
- **Positions:** setter; wing spikers (left/outside and right/opposite); 2 middles; libero; pinch servers (serve controllers and power servers). In canon the jump float is a pinch-server weapon (`W:Positions.txt`).
- **Set lengths in canon:**
  - Practice matches and Inter-High prelims are best of 3, and the 3rd set goes to 25 (Seijoh practice set 3 23-25; Inter-High 31-33) (`W:Aobajohsai_High.txt`, `W:List_of_Matches.txt`).
  - The Spring High Miyagi final is best of 5, with set 5 played to 15 (21-19) (`W:List_of_Matches.txt`).
- **Timeouts:** Karasuno had 2 in set 1 vs Seijoh and had used both before the Suga sub ("no timeouts left") (`W:Episode_Guide.txt` ep 19). That fits 2 per set.

From memory, all **[memory, unverified]**, because the dump has no rules page:
- **Rotation** is clockwise on each side-out. Order is fixed per set; the lineup can be reset between sets.
- **Overlap:** at the serve, each front-row player must be in front of the matching back-row player, and each player must be correctly left or right of the side neighbors. The server is exempt.
- **Back-row attack:** take off behind the 3 m line when contacting the ball above the net.
- **Libero:** no attacking above the net. A finger set by the libero in front of the 3 m line can't be attacked above the net. A completed rally is needed between 2 libero replacements. Re-designating a libero for the rest of the match is in the bible.
- **Substitutions:** 6 per team per set. A starter may leave and re-enter once per set, only in their own spot. A sub enters once per set, only for that starter, and can only be replaced by that starter.
- **Technical timeouts:** FIVB had them at 8 and 16 until 2015; I don't think Japanese high school play used them in 2012, and the canon matches don't seem to show any.
- **Deciding set:** 15 in a best-of-5. The Inter-High prelims are best of 3 with set 3 to 25, as the canon scores show.
- **Roster:** Japanese high school tournaments are believed to register 12 players. See error 14.

---

## Part 5: The wiki does NOT confirm

- Any detail of manga ch 2 to 75 beyond what the character and team pages and the anime summaries give; the chapter pages are empty.
- The Neighborhood match score (the bible's 2-0, 25-19 and the rest), the Karasuno side's full lineup, and Uchizawa's or a "4th alumnus's" role.
- Golden Week dates (May 2 to 6) and the date of the Nekoma match.
- Oikawa subbing for Kunimi, the 24-21 score at his entry, and his serve type beyond "jump serve".
- The score at Yamaguchi's pinch serve (15-15 in the bible), the exact blockers on the last quick, and every in-set score except the finals.
- Whether "bring it" and "send it" stayed spoken in set 2, or how Karasuno fixed them in canon.
- Where and in what words Takeda gave his speech (dinner, hall or gym).
- The Inter-High dates and weekdays (our Saturday, Sunday and Monday).
- The 1st Tokyo trip's venue (our "at Fukurodani") and the Saitama camp month (our "August").
- Whether an Inter-High roster can hold a 13th player, and whether any technical timeouts were used.
- The year of Oikawa's knee injury (our "2nd year").
- Shimada's glasses and hair; Takinoue calling Ukai "Kei-chan".
- Kageyama and milk, and the Shiratorizawa entrance-exam detail (the bible has it; the wiki dump doesn't show it).
- The Kenma and Hinata "next time / fun" exchange; Kuroo's "we'll see you in Tokyo".
- The bible timeline's Spring High final scores: it says 18-25 for set 3; the wiki says 20-25 (`W:List_of_Matches.txt`). That's outside ch 1 to 29 but should be fixed in the bible.
