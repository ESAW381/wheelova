# Content upgrades (round 1). Applied on top of pages.py by build.py.
AUTHOR = {"name": "Sajid Ali", "role": "Editor, Wheelova"}
UPDATED = "2026-10-21"

S_MDN = {"title": "MDN Web Docs — Crypto.getRandomValues()", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues"}
S_RANDOMORG = {"title": "RANDOM.ORG — Introduction to Randomness and Random Numbers", "url": "https://random.org/essay.html"}
S_NORVIG = {"title": "Peter Norvig — English Letter Frequency Counts (Google Books Ngrams)", "url": "https://norvig.com/mayzner.html"}
S_CBE = {"title": "Alvares et al. (2023), CBE—Life Sciences Education 22:ar51 — student perceptions of being called on in class", "url": "https://par.nsf.gov/servlets/purl/10482726"}

RANDOM_NOTE = ("Wheelova uses your browser's `crypto.getRandomValues()`. According to MDN, browsers implement it as a "
               "cryptographically secure pseudo-random generator seeded with system entropy — the same kind of source used for "
               "security features. It is unpredictable in practice, but it is not a physical \"true random\" device such as "
               "atmospheric-noise generators.")

UPGRADES = {
# ---------------------------------------------------------------- NUMBER GENERATOR
"random-number-generator": {
 "sections": [
  {"h2": "How this random number generator works", "body":
   "Pick a range, choose how many numbers you need, and press **Generate**. Every whole number from *From* to *To* has the same chance of being chosen.\n\n" + RANDOM_NOTE +
   "\n\nTo turn a random value into a number in your range, the tool scales it to the size of the range and rounds down. With ranges below a few million, any bias from this step is far too small to matter for games, classrooms or draws."},
  {"h2": "Pseudo-random vs. true random — what's the difference?", "body":
   "There are two broad kinds of random number generator:\n\n"
   "| | Pseudo-random (PRNG) | True random (TRNG) |\n|---|---|---|\n"
   "| Source | A mathematical algorithm | A physical process (e.g. atmospheric noise) |\n"
   "| Speed | Very fast | Slower |\n"
   "| Repeatable? | Yes, if you know the starting seed | No |\n"
   "| Typical use | Simulations, games, everyday picks | Lotteries, some security uses |\n\n"
   "Ordinary PRNGs (like many programming languages' default `random()` functions) can be predicted if someone knows the seed. A **cryptographically secure** PRNG, like the one browsers expose through `crypto.getRandomValues()`, is designed so that past output does not let anyone predict the next number. For picking a winner, a seat number or a game move, that is more than enough."},
  {"h2": "Repeats or no repeats?", "body":
   "- **No repeats** works like drawing numbered tickets from a hat: once a number is drawn, it can't come up again in the same batch. Use it for raffles, seat assignments, test-question order, or choosing several winners. You can't ask for more unique numbers than the range contains — 1–10 has only ten.\n"
   "- **Repeats allowed** works like rolling a die again and again: every draw is independent, so the same number can appear twice. Use it for dice games, simulations and practice problems."},
  {"h2": "What are the odds? A quick reference", "body":
   "With one number drawn from a range, every number has a chance of **1 ÷ (size of the range)**:\n\n"
   "| Range | Numbers | Chance of any one number |\n|---|---|---|\n"
   "| 1–6 | 6 | 1 in 6 (16.7%) |\n| 1–10 | 10 | 1 in 10 (10%) |\n| 1–20 | 20 | 1 in 20 (5%) |\n| 1–50 | 50 | 1 in 50 (2%) |\n| 1–100 | 100 | 1 in 100 (1%) |\n| 1–1000 | 1,000 | 1 in 1,000 (0.1%) |\n\n"
   "**Repeats are more common than people expect.** If you draw numbers from 1–100 *with* repeats allowed, the chance that at least two match is about 10% after 5 draws, about 37% after 10 and about 87% after 20 — the same maths as the \"birthday problem\". If repeats would spoil your draw, tick **No repeats**."},
  {"h2": "Worked examples", "body":
   "**Raffle with 250 tickets, 3 prizes.** Set 1 to 250, How many = 3, tick No repeats, and press Generate once. Read the winners in order — first number for first prize, and so on — and announce that order before you press the button.\n\n"
   "**Pick a random student by roll number.** Class of 32: set 1 to 32, How many = 1. For a fresh number each time without repeats across the lesson, use the [Name Picker Wheel](/name-picker-wheel) with \"remove winner\" instead.\n\n"
   "**Four-digit PIN for a game or puzzle.** Set 1000 to 9999, How many = 1. (Don't use generated numbers for real bank or account PINs — let your bank's own system create those.)\n\n"
   "**Shuffle question order for a quiz with 15 questions.** Set 1 to 15, How many = 15, No repeats on, Sort off. The result is a random order of all 15 questions."},
  {"h2": "Ideas for using random numbers", "body":
   "- **Classrooms** — question numbers, page numbers, seating, maths warm-ups (\"multiply the two numbers you get\").\n"
   "- **Games** — replace a lost die (1–6) or a 20-sided die (1–20), pick a level, set a score target.\n"
   "- **Giveaways** — draw ticket numbers live on screen. For named entrants, the [Raffle Wheel](/raffle-wheel) shows the draw visually.\n"
   "- **Everyday picks** — which restaurant on a numbered list, which chore, which movie from a ranked watchlist."},
  {"h2": "When not to use it", "body":
   "This generator is right for games, teaching, raffles and everyday decisions. It is **not** a certified gaming or lottery system, and it should not replace audited draw software where the law requires it. It also isn't meant for generating passwords or encryption keys — use a password manager or your platform's key-generation tools for that."}
 ],
 "faq": [
  {"q": "How do I pick a random number between 1 and 100?", "a": "Tap the 1–100 button (or set From to 1 and To to 100), keep How many at 1, and press Generate."},
  {"q": "Can I generate numbers without repeats?", "a": "Yes. Tick \"No repeats\". Each number then appears at most once in that batch."},
  {"q": "How many numbers can I generate at once?", "a": "Up to 1,000 per click. With No repeats on, the limit is also the size of your range."},
  {"q": "Is this random number generator truly random?", "a": "It uses the browser's cryptographically secure pseudo-random generator (crypto.getRandomValues), which is unpredictable in practice. It is not a physical true-random device, but it is far stronger than ordinary random() functions."},
  {"q": "Why did I get the same number twice in a row?", "a": "With repeats allowed, each draw is independent, so repeats happen naturally — from 1–10, two identical numbers in a row happen about 1 time in 10. Tick No repeats to prevent it within a batch."},
  {"q": "Can I use negative numbers?", "a": "Yes. Any whole numbers work, for example -50 to 50."},
  {"q": "Can I sort the results?", "a": "Yes. Tick \"Sort results\" to list them from smallest to largest."},
  {"q": "Is it OK to use for a lottery?", "a": "Use it for informal draws and games. Official lotteries and regulated prize draws usually require certified systems and rules that vary by country."}
 ],
 "sources": [S_MDN, S_RANDOMORG],
},
# ---------------------------------------------------------------- YES OR NO
"yes-or-no-wheel": {
 "sections": [
  {"h2": "What is a yes or no wheel?", "body":
   "A yes or no wheel is a spinner with two equal halves — **Yes** and **No**. Each spin lands on one of them at random, so it works like a coin flip you can watch. You can also add options such as **Maybe** or **Ask again**, or change the odds by adding more slices.\n\n" + RANDOM_NOTE},
  {"h2": "How the odds work", "body":
   "Every slice on the wheel is the same size, so the chance of an answer is simply *its slices ÷ total slices*:\n\n"
   "| Wheel | Chance of Yes | Chance of No | Other |\n|---|---|---|---|\n"
   "| Yes, No | 50% | 50% | — |\n| Yes, No, Maybe | 33.3% | 33.3% | Maybe 33.3% |\n| Yes, Yes, No | 66.7% | 33.3% | — |\n| Yes, No, No | 33.3% | 66.7% | — |\n| Yes, No, Ask again | 33.3% | 33.3% | Ask again 33.3% |\n\n"
   "**Streaks are normal.** With a 50/50 wheel, three of the same answer in a row happens one time in four (the first spin can be anything; the next two have to match it). Ten spins with no streak of three at all is actually less likely than getting one."},
  {"h2": "Best of three, five or seven", "body":
   "If one spin feels too sudden, play a series: the first answer to win the majority decides. A best of three ends after two spins half the time. Best of five gives a more \"settled\" feeling for bigger choices. The odds stay 50/50 either way — the extra spins only change how the decision feels."},
  {"h2": "Using the wheel to find out what you really want", "body":
   "A random answer can still be useful when the choice isn't really random. Spin, then notice your first reaction:\n\n"
   "- **Relief** when it says \"No\"? You probably didn't want to do it.\n"
   "- **Disappointment** when it says \"No\"? You likely wanted \"Yes\" all along.\n\n"
   "This is a reflection trick, not science — but it often settles small decisions faster than another list of pros and cons."},
  {"h2": "Good questions for a yes or no wheel", "body":
   "**Everyday:** Should I order takeaway tonight? Do I go to the gym today? Watch one more episode?\n\n"
   "**Party and classroom games:** Does this team get a bonus point? Do we play another round? Does the next person sing or dance?\n\n"
   "**Group tie-breaks:** When a vote is split exactly in half, agree before spinning that everyone accepts the result.\n\n"
   "Keep the wheel for choices where both answers are acceptable. For decisions about health, money, safety or law, get real information or advice first."},
  {"h2": "Yes or no wheel vs. coin flip", "body":
   "Both give a 50/50 answer. A wheel is easier to share on screen (classrooms, streams, video calls), can add a third option like Maybe, and can change the odds by adding slices — which a coin can't do. A physical coin is quicker when you're away from a screen."},
  {"h2": "Other ways to decide", "body":
   "For more than two options, use the [Decision Wheel](/decision-wheel). For a surprise answer hidden behind question marks, try the [Mystery Wheel](/mystery-wheel). To pick a number instead, use the [Random Number Generator](/random-number-generator)."}
 ],
 "faq": [
  {"q": "Is the yes or no wheel 50/50?", "a": "Yes. With the default two entries, Yes and No each have an equal 50% chance. Adding or repeating entries changes the odds."},
  {"q": "Can I add a Maybe option?", "a": "Yes. Tap the \"Yes / No / Maybe\" preset, or type Maybe on a new line. Each option then has a 1 in 3 chance."},
  {"q": "How do I make Yes more likely?", "a": "Add Yes more than once. With Yes, Yes, No the chance of Yes is 2 in 3 (about 67%)."},
  {"q": "Why do I keep getting the same answer?", "a": "Streaks are a normal part of randomness. With a 50/50 wheel, three identical answers in a row happen about one time in four."},
  {"q": "Can I use it in a classroom or on a stream?", "a": "Yes. It runs in any browser, works full-width on a projector, and needs no sign-up."},
  {"q": "Should I use a wheel for important decisions?", "a": "Use it to break ties between options you are already happy with. For serious decisions — health, money, legal matters — get proper information or advice first."}
 ],
 "sources": [S_MDN],
},
# ---------------------------------------------------------------- NAME PICKER
"name-picker-wheel": {
 "sections": [
  {"h2": "A random name picker for classrooms, teams and events", "body":
   "Paste a list of names, spin, and the wheel picks one at random. Because everyone can watch the wheel turn, the choice is visibly fair — nobody can say the teacher or host played favourites. Turn on **Remove winner** and each person is picked only once until the list runs out.\n\n" + RANDOM_NOTE},
  {"h2": "Using random calling in class", "body":
   "Calling on students at random (sometimes called \"cold calling\") is a common way to spread participation beyond the few who always raise their hands. Research on it is promising but mixed. A 2023 study of community-college biology classes (Alvares et al., *CBE—Life Sciences Education*) found that students in classes using **warm** random calling reported participating more and saw more of their peers participating than students in volunteer-only classes. Students in those classes were not more likely to report anxiety that interfered with learning — but more of them did report frustration (about 16% vs. 6%). The study was observational and at one college, so the authors call the results promising rather than conclusive.\n\n"
   "\"Warm\" is the important word. In practice that usually means:\n\n"
   "1. **Give think time first.** Ask the question, wait, and let students jot or discuss an answer before you spin.\n"
   "2. **Let pairs answer together.** Spin for a pair or table group rather than a single student.\n"
   "3. **Allow a pass or a phone-a-friend.** A student can pass once and you come back to them.\n"
   "4. **Respond kindly to wrong answers.** Thank them and build on the attempt.\n"
   "5. **Tell the class why** you call at random: everyone's thinking counts, not just the fastest hands."},
  {"h2": "How to keep the draw fair", "body":
   "- **One line per person.** A name typed twice gets two slices and double the chance.\n"
   "- **Check spellings.** \"Jon\" and \"John\" become two different people on the wheel.\n"
   "- **Use Remove winner** when everyone should get exactly one turn.\n"
   "- **Remember streaks happen.** With Remove winner off, the same name can come up twice in a row — that's randomness, not a bug.\n\n"
   "In a class of 30 with Remove winner off, each spin gives every student a 1 in 30 chance — about 3.3%. With Remove winner on, the second spin is 1 in 29, then 1 in 28, and so on, so every student is guaranteed a turn by spin 30."},
  {"h2": "Ideas for a name wheel", "body":
   "**Classroom:** who answers next, presentation order, classroom jobs for the week, reading partners, who chooses the end-of-lesson game.\n\n"
   "**Office and meetings:** who speaks first in stand-up, who takes notes, who picks the next team lunch spot, secret-gift partners.\n\n"
   "**Events and streams:** door-prize winners, audience volunteers, viewer shout-outs. For prize draws with many entrants, the [Raffle Wheel](/raffle-wheel) explains how to run a fair, recorded draw."},
  {"h2": "Presentation order in one minute", "body":
   "Paste the class list, turn on **Remove winner**, and spin until the wheel is empty. The **Results** list keeps the order each name came up — that's your running order. Screenshot it or copy it into your plan."},
  {"h2": "Picking groups instead of one person", "body":
   "To split the whole list into teams at once, use the [Random Team Generator](/random-team-generator). To create new names (for stories, games or examples) rather than pick from your own list, use the [Random Name Generator](/random-name-generator)."},
  {"h2": "Privacy", "body":
   "Names stay in your own browser's storage on this device. They are not uploaded or shared. To clear them, press **Clear**, or clear your browser's site data."}
 ],
 "faq": [
  {"q": "How many names can I add?", "a": "As many as you like. Labels shrink as the list grows; up to about 50 names stay easy to read on a projector."},
  {"q": "Can I stop the same name being picked twice?", "a": "Yes. Keep \"Remove winner after each spin\" on, or press \"Remove from wheel\" in the winner popup."},
  {"q": "Can I paste names from Excel or Google Sheets?", "a": "Yes. Copy a single column and paste it into the entry box — each cell becomes one line and one slice."},
  {"q": "Is random calling stressful for students?", "a": "It can be if it's done abruptly. Research suggests \"warm\" random calling — with think time, pair answers and the option to pass — increases participation without raising disruptive anxiety for most students."},
  {"q": "Can I use this as a wheel of names for a giveaway?", "a": "Yes. Enter each eligible person once, spin live, and keep Remove winner on for multiple prizes."},
  {"q": "Are the names I enter private?", "a": "Yes. Names are stored only in your own browser on this device. Nothing is uploaded."}
 ],
 "sources": [S_CBE, S_MDN],
},
# ---------------------------------------------------------------- TEAM GENERATOR
"random-team-generator": {
 "sections": [
  {"h2": "How the random team generator works", "body":
   "Paste your names, choose either **the number of teams** or **the number of people per team**, and press Generate. The list is shuffled, then people are dealt into teams one at a time, like dealing cards. That keeps team sizes within one person of each other.\n\n" + RANDOM_NOTE},
  {"h2": "Number of teams or people per team?", "body":
   "- **Number of teams** — when the activity needs a fixed number of groups (\"four stations\", \"three breakout rooms\").\n"
   "- **People per team** — when the task works best at a certain size (\"pairs\", \"groups of four\"). The generator works out how many teams that makes.\n\n"
   "Quick reference for common class sizes:\n\n"
   "| People | Pairs | Groups of 3 | Groups of 4 | Groups of 5 |\n|---|---|---|---|---|\n"
   "| 20 | 10 × 2 | 7 teams (3,3,3,3,3,3,2) | 5 × 4 | 4 × 5 |\n"
   "| 24 | 12 × 2 | 8 × 3 | 6 × 4 | 5 teams (5,5,5,5,4) |\n"
   "| 25 | 13 teams (12 × 2, one 1) | 9 teams (7 × 3, two of 2) | 7 teams (4 × 4, three of 3) | 5 × 5 |\n"
   "| 28 | 14 × 2 | 10 teams (8 × 3, two of 2) | 7 × 4 | 6 teams (4 × 5, two of 4) |\n"
   "| 30 | 15 × 2 | 10 × 3 | 8 teams (6 × 4, two of 3) | 6 × 5 |\n\n"
   "When the numbers don't divide evenly, the generator spreads the extra people so no team is more than one person bigger than another. If a team of one appears (for example 25 people in pairs), move that person into any pair to make a three."},
  {"h2": "What random teams are good for — and what they aren't", "body":
   "Random teams are **fair in process**: nobody picks, nobody is chosen last, and friendship groups get mixed. That's ideal for classroom projects, workshops, social games and mixers.\n\n"
   "Random teams are **not balanced by skill**. For a competitive match, generate the teams, then swap one or two people by hand, or seed the strongest players first (put one strong player in each team, then generate the rest)."},
  {"h2": "Seeding: keep certain people apart or together", "body":
   "The generator doesn't know who should be split up, so do it in two steps:\n\n"
   "1. **Separate.** Remove the people who must be on different teams (for example, team captains or two friends who distract each other) and place one in each team yourself.\n"
   "2. **Generate the rest.** Paste the remaining names, generate, then add your placed people to the teams.\n\n"
   "To keep a pair together, paste them as one line (\"Ana & Ben\"). They'll be dealt as one entry — note that this makes their team one person larger."},
  {"h2": "Ideas", "body":
   "**Classroom:** project groups, lab partners, reading circles, debate sides, station rotation.\n\n"
   "**PE and sports:** fair sides for a match, relay teams, tournament brackets — then pick who starts with the [Yes or No Wheel](/yes-or-no-wheel) or a coin.\n\n"
   "**Work:** breakout rooms, workshop tables, hackathon teams, lunch-roulette groups.\n\n"
   "**Game nights:** quiz teams, partners for card games, escape-room squads."},
  {"h2": "Tips for running groups in class", "body":
   "- **Generate in front of the class** so students see the teams weren't hand-picked.\n"
   "- **Give each team a role list** (leader, scribe, timekeeper, reporter) and let teams pick roles, or spin for them with the [Name Picker Wheel](/name-picker-wheel).\n"
   "- **Re-generate for each new project** so students work with different people over a term."},
  {"h2": "Privacy", "body":
   "The names you paste are saved only in your own browser on this device, so they're there next time. Nothing is uploaded."}
 ],
 "faq": [
  {"q": "How do I make random pairs?", "a": "Choose \"People per team\" and enter 2. With an odd number of people, the last team has one person — move them into any pair to make a group of three."},
  {"q": "How do I split a class into 4 groups?", "a": "Paste the class list, choose \"Number of teams\", enter 4, and press Generate."},
  {"q": "Are the teams equal in size?", "a": "As equal as the numbers allow — no team is more than one person larger than any other."},
  {"q": "Can I balance teams by skill?", "a": "Not automatically. Place your strongest players in different teams first, then generate the rest, or swap a few people after generating."},
  {"q": "Can I name the teams?", "a": "Teams are numbered. Copy the results and rename them wherever you paste them."},
  {"q": "Can I pick one person instead of making teams?", "a": "Yes — use the Name Picker Wheel."},
  {"q": "Are the names saved?", "a": "Yes, in your own browser only, so the list is there next time. Nothing is uploaded."}
 ],
 "sources": [S_MDN],
},
# ---------------------------------------------------------------- LETTER GENERATOR
"random-letter-generator": {
 "sections": [
  {"h2": "How the random letter generator works", "body":
   "Each letter is one equal slice of the wheel. With all 26 letters, every letter has a **1 in 26** chance — about 3.8% — on each spin. Choose a preset (vowels, consonants, or A–Z without the hardest letters), or edit the list to make your own.\n\n" + RANDOM_NOTE},
  {"h2": "Fair for games, different from real English", "body":
   "On this wheel every letter is equally likely. In real English text, letters are very uneven. In Peter Norvig's count of about 744 billion words from Google Books, **E** makes up about 12.5% of all letters and **Z** under 0.1%:\n\n"
   "| Most common | Share of letters | Least common | Share of letters |\n|---|---|---|---|\n"
   "| E | 12.49% | Z | 0.09% |\n| T | 9.28% | Q | 0.12% |\n| A | 8.04% | J | 0.16% |\n| O | 7.64% | X | 0.23% |\n| I | 7.57% | K | 0.54% |\n\n"
   "First letters of words are different again — the same source notes that **T** is the most common first letter and that E starts words far less often than it appears overall. That's why letters like Q, X and Z make word games much harder: very few common words start with them."},
  {"h2": "Which preset should I use?", "body":
   "| Preset | Letters | Good for |\n|---|---|---|\n"
   "| A–Z | 26 | Alphabet practice, fair draws, codes |\n"
   "| Vowels | A, E, I, O, U | Phonics, building words, vowel-sound games |\n"
   "| Consonants | 21 | Blending practice, consonant-vowel-consonant words |\n"
   "| No Q, X, Z | 23 | Categories-style games where every letter must be playable |\n\n"
   "For an even gentler game, also remove J, K, V and Y by deleting them from the list."},
  {"h2": "Word games to play with a random letter", "body":
   "**Categories (Scattergories-style).** Spin a letter. Everyone writes an animal, a country, a food, a name and a job starting with it in 60 seconds. Unique answers score a point.\n\n"
   "**One-minute word sprint.** Spin a letter and list as many words as you can that start with it. Longer words score extra.\n\n"
   "**Story chain.** Each sentence of a group story must start with the spun letter. Spin again for every new sentence.\n\n"
   "**Alphabet scavenger hunt.** Find an object in the room — or in a picture book — that starts with the letter.\n\n"
   "**Name game.** Spin a letter and use the [Random Name Generator](/random-name-generator) for inspiration, or invent a character whose first and last names start with it."},
  {"h2": "For teachers: phonics and spelling", "body":
   "- **Letter-sound warm-up** — spin, say the letter name and its sound, then a word that starts with it.\n"
   "- **Spelling practice** — spin a letter and ask for a spelling-list word containing it.\n"
   "- **No repeats across a lesson** — turn on **Remove winner** so you work through the alphabet without repeating letters.\n"
   "- **Projector-friendly** — the wheel fills the screen width on a classroom display."},
  {"h2": "Other alphabets and characters", "body":
   "The wheel accepts any characters, one per line. You can make a wheel for another alphabet, a set of musical notes (A–G), Greek letters for maths, or digits and letters for a puzzle code."}
 ],
 "faq": [
  {"q": "Is every letter equally likely?", "a": "Yes, as long as each letter appears once in the list. Each of the 26 letters has a 1 in 26 (about 3.8%) chance per spin."},
  {"q": "Can I generate a random letter without repeats?", "a": "Yes. Turn on \"Remove winner after each spin\" so each letter comes up only once."},
  {"q": "How do I remove hard letters like Q, X and Z?", "a": "Tap the \"No Q, X, Z\" preset, or delete any letter from the list."},
  {"q": "Which letter is most common in English?", "a": "E — about 12.5% of letters in a large Google Books count. T is the most common first letter of words."},
  {"q": "Can I use another alphabet?", "a": "Yes. Type any letters or characters you like, one per line."},
  {"q": "Can I pick a vowel or a consonant?", "a": "Yes. Use the Vowels or Consonants preset."}
 ],
 "sources": [S_NORVIG, S_MDN],
},
}

# ================================================================ ROUND 2
S_NBER = {"title": "Levitt (2016), NBER Working Paper 22487 — Heads or Tails: The Impact of a Coin Toss on Major Life Decisions", "url": "https://www.nber.org/digest/oct16/change-or-not-change-just-flip-coin"}
S_UTMB = {"title": "UTMB Digital Accessibility — Color blindness", "url": "https://www.utmb.edu/accessibility/digital/100-days-of-a11y/100-days-article/days-of-a11y/2024/04/03/3.-color-blindness"}
S_UNM49 = {"title": "UN Statistics Division — Standard country or area codes (M49)", "url": "https://unstats.un.org/unsd/methodology/m49/"}
S_TNW = {"title": "The Next Web (June 2017) — Google adds a virtual fidget spinner to search", "url": "https://thenextweb.com/news/google-virtual-fidget-spinner-search"}
S_CMS = {"title": "CMS — Prize competitions and free prize draws: Gambling Commission guidance (UK)", "url": "https://cms.law/en/gbr/legal-updates/prize-competitions-and-free-prize-draws-new-guidance-1"}
S_AMOE = {"title": "Mondaq — The importance of a valid sweepstakes AMOE (US)", "url": "https://www.mondaq.com/unitedstates/dodd-frank-consumer-protection-act/1336530/the-importance-of-a-valid-sweepstakes-amoe"}

UPGRADES.update({
# ---------------------------------------------------------------- COLOR
"color-wheel": {
 "sections": [
  {"h2": "How the random color generator works", "body":
   "Each color on your list becomes one equal slice, painted in that real color. Spin, and the wheel stops on one at random; the popup shows the color name, a large swatch and its **hex code** (for example `#E53935` for red), so you can copy it straight into a design tool, a slide or a craft project.\n\n" + RANDOM_NOTE},
  {"h2": "Which colors are painted, and with which codes", "body":
   "These names are drawn in their real color. Type any of them, one per line:\n\n"
   "| Color | Hex | Color | Hex | Color | Hex |\n|---|---|---|---|---|---|\n"
   "| Red | `#E53935` | Orange | `#FB8C00` | Yellow | `#FDD835` |\n| Green | `#43A047` | Blue | `#1E88E5` | Indigo | `#3949AB` |\n| Violet | `#8E24AA` | Purple | `#7B1FA2` | Pink | `#EC407A` |\n| Brown | `#6D4C41` | Black | `#212121` | White | `#FAFAFA` |\n| Gray | `#9E9E9E` | Teal | `#00897B` | Cyan | `#00ACC1` |\n| Navy | `#1A237E` | Maroon | `#800000` | Gold | `#D4AF37` |\n| Lavender | `#B39DDB` | Mint | `#98E2C6` | Coral | `#FF7F6B` |\n\n"
   "Silver, beige, turquoise, magenta, olive, lime, peach and sky blue work too. Any other word still spins — it just uses the standard Wheelova colors instead of a real swatch."},
  {"h2": "What is a hex code?", "body":
   "A hex code describes a color for screens using three pairs of characters: the amount of **red**, **green** and **blue** light, each from `00` (none) to `FF` (full). `#FF0000` is pure red, `#000000` is black and `#FFFFFF` is white. Paste a hex code into Canva, Figma, PowerPoint, Google Slides or CSS to get exactly the same color. Printed colors (paint, fabric, ink) can look slightly different from the screen, so treat the code as a close guide for physical projects."},
  {"h2": "Which preset should I use?", "body":
   "| Preset | Colors | Chance of each | Good for |\n|---|---|---|---|\n"
   "| Rainbow | 7 | 1 in 7 (14.3%) | Kids' games, art lessons, the classic ROYGBIV order |\n"
   "| Basic colors | 12 | 1 in 12 (8.3%) | Scavenger hunts, outfit or theme days |\n"
   "| Primary | 3 | 1 in 3 (33.3%) | Early-years colour learning, quick team colours |\n"
   "| Pastels | 6 | 1 in 6 (16.7%) | Design prompts, party themes, nail or craft ideas |\n\n"
   "The rainbow's seven colors come from Isaac Newton, who named seven bands in the spectrum — partly to match the seven notes of a musical scale. The real spectrum is continuous, which is why some people struggle to see a separate indigo."},
  {"h2": "Ideas for a random color", "body":
   "**Art and design.** Spin a main color for a drawing challenge, or spin twice for a two-color palette. Designers can use the hex code as a starting point and build lighter and darker shades around it.\n\n"
   "**Classroom.** \"Find something in the room that is this color\", color-word spelling, or sorting games for younger children.\n\n"
   "**Parties and teams.** Assign team colours, pick the colour theme for a birthday, or play \"wear something this colour tomorrow\".\n\n"
   "**Everyday.** Choose a nail polish, a phone wallpaper, a gift-wrap colour or the colour of the week."},
  {"h2": "Playing with people who are color-blind", "body":
   "Some players may not tell certain colors apart. As many as 1 in 12 men and about 1 in 200 women have some form of color vision deficiency, most often red–green. The wheel always shows the **color name** on each slice and in the popup, so nobody has to rely on the swatch alone. For games, avoid putting only red and green — or only blue and purple — on the same wheel."},
  {"h2": "Is this a color theory wheel?", "body":
   "No. This page picks a color at random. A color theory wheel shows how hues relate — complementary, analogous, triadic — and is used to build matching palettes. Use this tool when you want chance to choose, and a palette tool when you want colors that match."}
 ],
 "faq": [
  {"q": "How do I get a random color with its hex code?", "a": "Spin the wheel. The popup shows the color name, a swatch and its hex code, ready to copy."},
  {"q": "Can I add my own colors?", "a": "Yes. Type any color name on a new line. Names in the table above are painted in their real color."},
  {"q": "Is each color equally likely?", "a": "Yes, as long as each color appears once. With the 7 rainbow colors, each has a 1 in 7 chance."},
  {"q": "Can I pick colors without repeats?", "a": "Yes. Turn on \"Remove winner after each spin\" so each color is used once."},
  {"q": "Why does indigo look so close to blue?", "a": "The spectrum is continuous; Newton named seven bands partly to match the musical scale. Indigo sits between blue and violet and is hard for many people to see as separate."},
  {"q": "Will the hex code match my paint or fabric?", "a": "Closely, but not exactly. Screens mix light while paint and ink mix pigment, so printed colors can look slightly different."}
 ],
 "sources": [S_UTMB, S_MDN],
},
# ---------------------------------------------------------------- COUNTRY
"random-country-generator": {
 "sections": [
  {"h2": "How the random country generator works", "body":
   "Every country on the list is one equal slice of the wheel. With all 193 countries, each one has a 1 in 193 chance (about 0.5%) on every spin. Pick a region to narrow it down, or turn on **Remove winner** to work through countries without repeats.\n\n" + RANDOM_NOTE},
  {"h2": "Which countries are on the wheel?", "body":
   "The default list is the **193 member states of the United Nations**, grouped by the UN's M49 regions. The UN also has two **observer states** — the Holy See (Vatican City) and the State of Palestine — which aren't on the default list. Some places that govern themselves but aren't UN members, such as Taiwan and Kosovo, aren't included either.\n\n"
   "There is no single official answer to \"how many countries are there?\" — it depends on who is counting. If your game or lesson needs a different list, type extra names in or delete ones you don't want."},
  {"h2": "Odds by region", "body":
   "Because regions have different numbers of countries, spinning **all 193** doesn't give each region the same chance:\n\n"
   "| Region (UN M49) | Countries | Chance a spin lands here |\n|---|---|---|\n"
   "| Africa | 54 | 28.0% |\n| Asia | 47 | 24.4% |\n| Europe | 43 | 22.3% |\n| Americas | 35 | 18.1% |\n| Oceania | 14 | 7.3% |\n\n"
   "If you want every continent to have an equal chance, spin a region first — make a quick wheel with the five region names — then use that region's preset."},
  {"h2": "Why some countries are in \"unexpected\" regions", "body":
   "The UN grouping follows statistical convention, not everyday usage. On this wheel **Cyprus, Turkey, Armenia, Azerbaijan and Georgia** are in Asia; **Russia** is in Europe; **Egypt** is in Africa; and the **Americas** covers North, Central and South America plus the Caribbean together. The wheel follows the UN so the lists are consistent and checkable."},
  {"h2": "Geography games and lesson ideas", "body":
   "**Map hunt.** Spin a country; the first person to find it on a map scores a point. Make it harder by hiding labels.\n\n"
   "**Capital, flag, language.** Spin, then name the capital, describe the flag and name a main language. One point each.\n\n"
   "**Twenty questions.** One person spins secretly and the others ask yes-or-no questions to guess the country.\n\n"
   "**Research cards.** Each student spins a country and makes a one-page fact card: population, currency, a famous landmark, a traditional food.\n\n"
   "**Around the world in a term.** Turn on Remove winner and spin one country per lesson so the class never repeats."},
  {"h2": "Travel and food ideas", "body":
   "- **Dream-trip planning** — spin for a destination, then research the best time to visit and three things to see.\n"
   "- **Cooking challenge** — cook a dish from the country you land on; spin again if ingredients are impossible to find.\n"
   "- **Film or book club** — watch a film or read a book from the spun country this month.\n"
   "- **Language taster** — learn \"hello\" and \"thank you\" in a main language of the country."},
  {"h2": "Related tools", "body":
   "For US states instead of countries, use the [Random State Generator](/random-state-generator). To split a class into groups that each research a country, use the [Random Team Generator](/random-team-generator)."}
 ],
 "faq": [
  {"q": "How many countries are on the wheel?", "a": "All 193 UN member states when \"All 193 countries\" is selected."},
  {"q": "Why isn't Taiwan, Kosovo or Palestine on the list?", "a": "The default list uses UN membership. Palestine and the Holy See are UN observer states; Taiwan and Kosovo aren't UN members. You can add any of them by typing the name on a new line."},
  {"q": "Can I pick a random country from one continent?", "a": "Yes. Choose Africa, Americas, Asia, Europe or Oceania above the list."},
  {"q": "Does each continent have the same chance?", "a": "Not when spinning all 193 — Africa has the most countries (28% of spins), Oceania the fewest (7.3%). Spin a region first if you want equal chances."},
  {"q": "Can I avoid getting the same country twice?", "a": "Yes. Turn on \"Remove winner after each spin\"."},
  {"q": "Why is Turkey listed in Asia?", "a": "The wheel follows the UN M49 regions, which place Turkey, Cyprus, Armenia, Azerbaijan and Georgia in Western Asia."}
 ],
 "sources": [S_UNM49, S_MDN],
},
# ---------------------------------------------------------------- SPINNER
"spinner": {
 "sections": [
  {"h2": "A simple online spinner", "body":
   "Choose 2 to 20 numbered slices and spin. It works like the cardboard spinner in a board game — but it can't bend, wobble or favour one side, and it keeps a list of every result. Type words into the entry box to turn it into a custom spinner for names, tasks or prizes.\n\n" + RANDOM_NOTE},
  {"h2": "Looking for the spinner from Google search?", "body":
   "In 2017 Google added a small spinner to its search results, with a fidget-spinner mode and a number mode. This page is an independent alternative to that idea, not Google's tool. It adds a few things a quick search widget doesn't: up to 20 slices, your own words instead of numbers, a results history, sound on or off, fullscreen for a classroom projector, and a share link."},
  {"h2": "Odds for each spinner size", "body":
   "Every slice is the same size, so each number has a chance of **1 ÷ slices**. The last column shows how many spins it takes, on average, before every number has come up at least once — handy for games where everyone needs a turn:\n\n"
   "| Slices | Chance per number | Average spins to see every number |\n|---|---|---|\n"
   "| 2 | 50% | 3 |\n| 4 | 25% | 8.3 |\n| 6 | 16.7% | 14.7 |\n| 8 | 12.5% | 21.7 |\n| 10 | 10% | 29.3 |\n| 20 | 5% | 72 |\n\n"
   "That last column surprises people: with a six-slice spinner it typically takes about 15 spins, not 6, before all six numbers appear. If everyone must get a turn quickly, turn on **Remove winner** instead."},
  {"h2": "Spinner vs. dice", "body":
   "A 6-slice spinner gives exactly the same odds as a standard die: 1 in 6 for each number. A spinner is easier to see on a shared screen and can't roll off the table, and you can make sizes that dice don't come in — a 5-slice or 7-slice spinner, for example. For two dice added together, though, a single spinner isn't the same: totals like 7 are more common than 2 or 12. Spin twice and add the results to copy two dice."},
  {"h2": "Ways to use the spinner", "body":
   "**Board games.** Replace a lost spinner or die. Snakes and Ladders, Twister-style games and homemade board games all work.\n\n"
   "**Classroom.** Spin a question number from a worksheet, a page number, a times table, or which group presents next.\n\n"
   "**Fitness.** Spin for the number of reps, rounds or minutes. Write exercise names in the entry box for a workout spinner.\n\n"
   "**Family decisions.** Number the options — which film, which chore, who goes first — and spin."},
  {"h2": "Need bigger numbers?", "body":
   "For ranges like 1–100 as a wheel, use the [Random Number Wheel](/number-wheel). For one or many numbers as a list — with or without repeats — use the [Random Number Generator](/random-number-generator)."}
 ],
 "faq": [
  {"q": "How many slices can the spinner have?", "a": "Choose 2 to 20 from the menu. For more, type your own entries into the list."},
  {"q": "Is this Google's spinner?", "a": "No. It's an independent spinner that works the same basic way, with extra options such as words, history and fullscreen."},
  {"q": "Is a 6-slice spinner the same as a die?", "a": "Yes for a single die — each number has a 1 in 6 chance. For two dice added together, spin twice and add the results."},
  {"q": "Can I put words on the spinner?", "a": "Yes. Type anything into the entry box, one per line, and each line becomes a slice."},
  {"q": "Does it work on phones?", "a": "Yes. It runs in any modern mobile browser with no app to install."},
  {"q": "Is the spinner random?", "a": "Yes. The stop point is chosen with your browser's cryptographically secure random generator, and each spin is independent."}
 ],
 "sources": [S_TNW, S_MDN],
},
# ---------------------------------------------------------------- RAFFLE
"raffle-wheel": {
 "sections": [
  {"h2": "How the raffle wheel works", "body":
   "Each line on the list is one entry and one equal slice. Spin to draw a winner; with **Remove winner** on, that entry leaves the wheel so it can't win again. The **Results** list records every winner in order for the session.\n\n" + RANDOM_NOTE},
  {"h2": "Run a fair draw in six steps", "body":
   "1. **Write the rules first.** Who can enter, how many entries each person gets, the closing time, the prizes and how winners will be contacted.\n"
   "2. **Close entries** at the stated time, then build the list. Remove duplicates and anyone who doesn't qualify.\n"
   "3. **Say the numbers out loud.** \"We have 214 valid entries and 3 prizes.\"\n"
   "4. **Announce the prize order** before the first spin — smallest prize first, or grand prize first.\n"
   "5. **Spin live** on screen, in a stream, or on a recorded video, with Remove winner on.\n"
   "6. **Keep a record.** Screenshot the entry count and the Results list, and keep it until prizes are delivered.\n\n"
   "If a winner doesn't respond within the time in your rules, spin again for a replacement and record that too."},
  {"h2": "Tickets or names?", "body":
   "- **One entry each:** paste names, one per line.\n"
   "- **Multiple tickets:** paste **ticket numbers**, not names. Someone with five tickets then has five slices — exactly the odds they paid for. The \"Tickets 1–100\" preset gives you numbered lines to start from.\n\n"
   "For very large draws (thousands of tickets), the [Random Number Generator](/random-number-generator) can draw several winning ticket numbers in one click with No repeats on."},
  {"h2": "What are my chances of winning?", "body":
   "With equal entries and no repeat winners, the chance of winning at least one prize is:\n\n"
   "| Entries in the draw | Your tickets | Prizes | Your chance |\n|---|---|---|---|\n"
   "| 100 | 1 | 1 | 1.0% |\n| 100 | 3 | 1 | 3.0% |\n| 100 | 3 | 3 | 8.8% |\n| 100 | 10 | 3 | 27.3% |\n| 250 | 5 | 1 | 2.0% |\n| 250 | 5 | 3 | 5.9% |\n| 500 | 20 | 5 | 18.5% |\n\n"
   "More prizes help everyone a little, but buying more tickets is the only thing that raises *your* share relative to others."},
  {"h2": "Social media giveaways", "body":
   "1. Export or copy the comments or entries (most platforms and tools let you copy usernames).\n"
   "2. Remove duplicates, the host's own account, and entries that don't meet your rules (for example, missing a required tag).\n"
   "3. Paste the usernames here, one per line, and spin live — a screen recording is the easiest proof.\n"
   "4. Check the winner still meets the rules before announcing.\n\n"
   "Each platform has its own promotion rules, and some require you to state that the giveaway isn't sponsored or endorsed by them. Read them before you post."},
  {"h2": "Is a random draw legal?", "body":
   "A fair wheel makes the **pick** fair; it doesn't make the **promotion** legal. Rules depend on your country:\n\n"
   "- In the **United States**, a promotion that combines a prize, chance and a required payment is generally treated as an illegal lottery. That's why sweepstakes usually offer a free \"alternative method of entry\" and say \"no purchase necessary\".\n"
   "- In the **United Kingdom**, the Gambling Commission's guidance says free prize draws must offer a genuinely free entry route that is publicised and treated equally with paid entries; otherwise the draw may be a lottery that needs a licence.\n"
   "- Charity raffles often have their own rules and registration requirements.\n\n"
   "This is general information, not legal advice. For a business promotion with valuable prizes, check local rules or ask a professional."}
 ],
 "faq": [
  {"q": "How many entries can the raffle wheel handle?", "a": "Hundreds work well. Labels shrink as the list grows; for thousands of tickets, the Random Number Generator is easier."},
  {"q": "How do I draw several winners?", "a": "Keep \"Remove winner\" on and spin once per prize, in the order you announced."},
  {"q": "Should I enter names or ticket numbers?", "a": "Names when everyone has one entry; ticket numbers when people can have more than one, so each ticket gets its own slice."},
  {"q": "Can people verify the result?", "a": "Spin live or record your screen, and keep a screenshot of the entry count and the Results list. Verifiable draw receipts are planned but not available yet."},
  {"q": "What if a winner doesn't reply?", "a": "Follow your published rules: after the deadline, spin again for a replacement and keep a record of it."},
  {"q": "Does using a wheel make my giveaway legal?", "a": "No. The wheel makes the pick fair, but giveaway and lottery rules depend on your country and platform. Check them before you launch."}
 ],
 "sources": [S_AMOE, S_CMS, S_MDN],
},
# ---------------------------------------------------------------- DECISION
"decision-wheel": {
 "sections": [
  {"h2": "How the decision wheel works", "body":
   "Put your options on the wheel — anything from restaurants to weekend plans — and spin. Every option is an equal slice, so each has the same chance. Use the presets for common choices, or type your own.\n\n" + RANDOM_NOTE},
  {"h2": "Does letting chance decide actually help?", "body":
   "There is some interesting evidence. In a 2016 study, economist Steven Levitt invited people who were stuck on a decision to flip a virtual coin on his website, with heads meaning \"make the change\". Over 20,000 flips were recorded, and participants were surveyed two and six months later. People who got heads were about **25% more likely** to make the change. And people who made a change — quitting a job, ending a relationship, breaking a habit — reported being happier six months later than those who stayed put.\n\n"
   "The study has limits: participants were volunteers from a website, and happiness was self-reported. But it suggests that when people are genuinely torn, a random nudge can help them act — and that many of us wait too long before making a change."},
  {"h2": "When to use a decision wheel — and when not to", "body":
   "| Good fit | Not a good fit |\n|---|---|\n"
   "| Every option is acceptable | One option is clearly better on the facts |\n"
   "| You've spent longer deciding than the choice deserves | The decision affects health, safety, money or the law |\n"
   "| A group can't agree and needs a fair tie-break | Someone would be harmed by one of the outcomes |\n"
   "| You want to find out what you really prefer | You need a reason you can explain later |"},
  {"h2": "Five ways to decide better with a wheel", "body":
   "1. **Only add options you'd accept.** If you'd refuse an outcome, take it off before spinning.\n"
   "2. **Weight what matters.** Enter a favourite twice to double its chance.\n"
   "3. **Use the disappointment test.** If the result makes you hope for a re-spin, you've learned which option you actually wanted — go with that.\n"
   "4. **Agree before you spin.** In a group, everyone agrees to accept the result first. That's what makes it fair.\n"
   "5. **Narrow it down.** With many options, turn on Remove winner and spin to *eliminate* until two are left, then spin once more."},
  {"h2": "Popular decision wheels", "body":
   "**What to eat:** pizza, burger, biryani, sushi, tacos, pasta, salad, noodles — or your local favourites.\n\n"
   "**What to watch:** comedy, action, drama, horror, sci-fi, romance, animation, documentary.\n\n"
   "**Weekend plans:** stay in, eat out, hike, visit friends, shopping, movie night.\n\n"
   "**Who does it:** names of housemates or family members for chores, driving or paying.\n\n"
   "For a single question, the [Yes or No Wheel](/yes-or-no-wheel) is quicker. For hidden outcomes, try the [Mystery Wheel](/mystery-wheel)."},
  {"h2": "Decision wheel for groups and teams", "body":
   "Teams use decision wheels to choose who presents first, which task to tackle next, or where to go for a team lunch. Share your screen, spin, and the result is visible to everyone — no one can claim the choice was rigged. To divide people into groups rather than choose an option, use the [Random Team Generator](/random-team-generator)."}
 ],
 "faq": [
  {"q": "How does a decision wheel help me decide?", "a": "It breaks ties between options you'd accept, saves time, and your reaction to the result often shows which option you really wanted."},
  {"q": "Can I make one option more likely?", "a": "Yes. Enter it more than once — each copy is another equal slice."},
  {"q": "Is there evidence that random decisions help?", "a": "A 2016 study by Steven Levitt found people who were nudged by a coin flip into making a change reported being happier six months later. It used volunteers and self-reported happiness, so treat it as suggestive."},
  {"q": "How many options can I add?", "a": "As many as you like, but 3–12 options are easiest to read and decide between."},
  {"q": "Is it fair for a group decision?", "a": "Yes, if everyone agrees the list and to accept the result before spinning. The result is chosen at random and everyone can watch."},
  {"q": "Should I use it for big life decisions?", "a": "Use it to break a deadlock between options you're genuinely happy with. For decisions about health, money or legal matters, get proper information or advice first."}
 ],
 "sources": [S_NBER, S_MDN],
},
})

# ================================================================ ROUND 3
S_SSA = {"title": "U.S. Social Security Administration — Olivia and Liam remain most popular baby names for 2024", "url": "https://www.ssa.gov/blog/en/posts/2025-05-09.html"}
S_CENSUS_NAMES = {"title": "U.S. Census Bureau — Frequently occurring surnames from the 2010 Census", "url": "https://census.gov/topics/population/genealogy/data/2010_surnames.html"}
S_CENSUS_REG = {"title": "U.S. Census Bureau — Census regions and divisions", "url": "https://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf"}
S_NFL = {"title": "NFL.com — Teams", "url": "https://www.nfl.com/teams/"}
S_NBA = {"title": "NBA.com — Teams", "url": "https://www.nba.com/teams"}
S_MLB = {"title": "MLB.com — Teams", "url": "https://www.mlb.com/team"}

def _draft(n, league):
    return ("Use **Remove winner** so every person gets a different team. With " + str(n) + " teams and Remove winner off, repeats come quickly — "
            "on average it takes about " + {32: "130", 30: "120"}[n] + " spins before every team has come up at least once. With Remove winner on, "
            "it takes exactly " + str(n) + ". For a draft order, first spin the managers' names on the [Name Picker Wheel](/name-picker-wheel), then spin " + league + " teams in that order.")

UPGRADES.update({
# ---------------------------------------------------------------- LUCKY
"lucky-wheel": {
 "sections": [
  {"h2": "How the lucky wheel works", "body":
   "Every prize you add is one equal slice. Spin, and the wheel stops on a prize at random. To make a prize rarer or more common, change how many slices it has — that's the only lever, and it's completely transparent to players.\n\n" + RANDOM_NOTE},
  {"h2": "Design your odds", "body":
   "The chance of a prize is **its slices ÷ total slices**. Some example setups:\n\n"
   "| Wheel | Grand prize chance | Try again chance |\n|---|---|---|\n"
   "| 8 slices, 1 grand prize | 1 in 8 (12.5%) | — |\n"
   "| 8 slices, 1 grand prize, 2 try again | 12.5% | 25% |\n"
   "| 12 slices, 1 grand prize, 4 try again | 8.3% | 33.3% |\n"
   "| 20 slices, 1 grand prize, 6 try again | 5% | 30% |\n\n"
   "A good rule of thumb for events: keep \"try again\" under a third of the wheel, so most spins still feel like a win."},
  {"h2": "Budgeting prizes for an event", "body":
   "Expected prize use is simple: **spins × chance**. If 200 people spin a wheel where \"Free drink\" is 2 of 8 slices (25%), expect about 50 free drinks — but plan for some extra, because randomness can run above average. With Remove winner on, each prize can be won only once, which caps your cost exactly but changes the odds as prizes disappear."},
  {"h2": "Lucky wheel ideas", "body":
   "**Shops and market stalls:** small discounts, free samples, a mystery bag, one rare voucher.\n\n"
   "**Classrooms:** homework pass, choose the music, line leader, sit anywhere, extra break minutes.\n\n"
   "**Birthday parties:** party favours, silly forfeits, who opens the next present.\n\n"
   "**Streams and online events:** shout-outs, small prizes, viewer-chosen challenges. Use **Embed** to put the wheel on your page or into OBS."},
  {"h2": "Being fair to players", "body":
   "- **Show the wheel before anyone spins**, so players can see every prize and how many slices each has.\n"
   "- **Don't change the wheel mid-event** without telling people.\n"
   "- **Real prizes = real rules.** For giveaways open to the public, check local promotion and sweepstakes rules first. See the [Raffle Wheel](/raffle-wheel) guide for more on fair draws."},
  {"h2": "Not affiliated with any TV show", "body":
   "Wheelova is an independent random wheel you fill with your own prizes. It isn't connected to any game show, casino or brand."}
 ],
 "faq": [
  {"q": "How do I make the grand prize rare?", "a": "Add more slices of other prizes or \"Try again\". With one grand prize among 20 slices, the chance is 5%."},
  {"q": "Can I remove a prize once it's won?", "a": "Yes. Press \"Remove from wheel\" in the winner popup, or turn on \"Remove winner after each spin\"."},
  {"q": "How many of each prize will I give away?", "a": "On average, number of spins × chance. 200 spins on a 25% prize means about 50 — plan for a few extra."},
  {"q": "Can I put the lucky wheel on my website or stream?", "a": "Yes. Press Embed to get code for a website or an OBS browser source."},
  {"q": "Is this the same as Wheel of Fortune?", "a": "No. Wheelova is a free random wheel you fill with your own prizes; it isn't connected to any TV show."}
 ],
 "sources": [S_MDN],
},
# ---------------------------------------------------------------- MYSTERY
"mystery-wheel": {
 "sections": [
  {"h2": "How the mystery wheel works", "body":
   "It's a normal random wheel with the labels hidden. Every slice shows **?**, so players can't see where the good or bad outcomes sit. When the wheel stops, the popup reveals the result.\n\n" + RANDOM_NOTE},
  {"h2": "Why hide the outcomes?", "body":
   "On a visible wheel, players watch the pointer slow down and know what's coming a second early. Hiding the labels keeps the suspense until the reveal — which is the whole fun of a challenge wheel, a prize reveal or a game-show moment in class. The odds don't change: every slice still has an equal chance."},
  {"h2": "Set it up without spoiling it", "body":
   "1. Type the outcomes into the list **before** sharing your screen or turning the screen toward players.\n"
   "2. Press **Shuffle** so even you don't know the order.\n"
   "3. Scroll so only the wheel is visible, or press the **fullscreen** button.\n"
   "4. Spin. The result appears only in the popup."},
  {"h2": "Mystery wheel ideas", "body":
   "**Party challenges:** sing a chorus, do an impression, swap seats, tell a joke, free pass.\n\n"
   "**Classroom:** hidden quiz questions, a mystery reward, a surprise brain-break activity, which topic comes next.\n\n"
   "**Date night or weekends:** hidden activities or restaurants — spin to find out where you're going.\n\n"
   "**Streams:** viewers spin a mystery challenge or prize; add it to OBS with **Embed**."},
  {"h2": "Mix good and bad on purpose", "body":
   "A mystery wheel works best with a mix: a few great outcomes, a few silly ones and a couple of \"free pass\" slices. If one outcome would genuinely upset someone, leave it off — random doesn't mean anything goes. For classes and kids, keep every slice age-appropriate."}
 ],
 "faq": [
  {"q": "Can players see the entries?", "a": "Not on the wheel — slices show \"?\". The entry list below the wheel still shows them, so set it up before players look or use fullscreen."},
  {"q": "Does hiding the labels change the odds?", "a": "No. Every slice still has an equal chance; only the labels are hidden."},
  {"q": "Can I remove an outcome once it's revealed?", "a": "Yes. Press \"Remove from wheel\" or turn on \"Remove winner after each spin\"."},
  {"q": "Can I share a mystery wheel?", "a": "Yes. Share link and Embed keep the slices hidden for whoever opens them."}
 ],
 "sources": [S_MDN],
},
# ---------------------------------------------------------------- NUMBER WHEEL
"number-wheel": {
 "sections": [
  {"h2": "How the number wheel works", "body":
   "Choose a range, and every whole number in it becomes one equal slice. Spin, and the wheel stops on one at random. It's the visual version of a random number generator — better when people are watching, like a raffle, a bingo call or a classroom game.\n\n" + RANDOM_NOTE},
  {"h2": "Number wheel or number generator?", "body":
   "| Use the number wheel when… | Use the [number generator](/random-number-generator) when… |\n|---|---|\n"
   "| People are watching the draw | You just need the result |\n"
   "| The range is up to a few hundred | The range is huge (e.g. 1–1,000,000) |\n"
   "| You draw one number at a time | You want many numbers at once |\n"
   "| The spin itself is part of the fun | You want to copy a list |"},
  {"h2": "Odds and repeats", "body":
   "Each number has a chance of **1 ÷ (size of the range)**: 10% on 1–10, 1% on 1–100.\n\n"
   "- **Remove winner off:** numbers can repeat, like rolling a die. Repeats come sooner than people expect.\n"
   "- **Remove winner on:** each number appears once, like drawing tickets from a hat — the right choice for raffles and bingo."},
  {"h2": "Bingo caller", "body":
   "- **US-style bingo** uses 75 numbers: set From 1, To 75.\n"
   "- **UK-style bingo** uses 90 numbers: set From 1, To 90.\n\n"
   "Turn **Remove winner** on so no number is called twice, and keep the Results list visible as your called-numbers board. Any single number has about a 6.7% chance of appearing in the first five calls of a 75-ball game."},
  {"h2": "Classroom ideas", "body":
   "**Times tables:** spin two numbers from 1–12 and multiply.\n\n"
   "**Place value:** spin 0–9 three times to build a three-digit number.\n\n"
   "**Rounding and estimating:** spin 1–1,000 and round to the nearest ten or hundred.\n\n"
   "**Student numbers:** give each student a number and spin to choose who answers — or use the [Name Picker Wheel](/name-picker-wheel) with real names."},
  {"h2": "Make your own number lists", "body":
   "The entry box accepts any numbers, one per line. Use only even numbers, negative numbers (−10 to 10), decimals for a measurement game, or a custom list like seat numbers. Up to 500 numbers can be generated with the From/To fields."}
 ],
 "faq": [
  {"q": "What is the biggest range I can use?", "a": "Up to 500 numbers in one wheel (for example 1–500). For bigger ranges, use the Random Number Generator."},
  {"q": "Can I use it as a bingo caller?", "a": "Yes. Set 1–75 or 1–90, turn on Remove winner, and spin for each call."},
  {"q": "Can I use negative numbers or skip numbers?", "a": "Yes. Type any numbers you want into the entry box, one per line."},
  {"q": "Is every number equally likely?", "a": "Yes, as long as each number appears once. Slices are equal and the stop point is random."},
  {"q": "Can I draw several numbers in a row without repeats?", "a": "Yes. Turn on \"Remove winner after each spin\" and keep spinning."}
 ],
 "sources": [S_MDN],
},
# ---------------------------------------------------------------- NAME GENERATOR
"random-name-generator": {
 "sections": [
  {"h2": "How the random name generator works", "body":
   "Choose female, male or any names, how many you want, and whether to add a last name. Each click draws first names and surnames at random from Wheelova's built-in lists, with no duplicates in a single batch.\n\n" + RANDOM_NOTE},
  {"h2": "Name generator vs. name picker", "body":
   "This page **creates** names. If you already have a list of real people — a class, a team, giveaway entrants — and want to pick one of them, use the [Name Picker Wheel](/name-picker-wheel) instead."},
  {"h2": "Where the names come from", "body":
   "The first-name lists focus on names that are common in English-speaking countries today, plus widely used South Asian, Middle Eastern and East Asian names. Many of them — Olivia, Emma, Mia, Sophia, Liam, Noah, Oliver, James, Lucas — appear in the U.S. Social Security Administration's most popular baby names for 2024, where Olivia and Liam were number one.\n\n"
   "The surname list starts with the most common surnames in the 2010 U.S. Census — Smith, Johnson, Williams, Brown, Jones and Garcia — and adds common surnames from other countries. The lists are illustrative: they're built to produce realistic-sounding names, not to reflect how often each name occurs in a population."},
  {"h2": "Ideas", "body":
   "**Writers:** names for side characters, especially when you need a lot of them. Generate ten and pick the one that fits.\n\n"
   "**Games and role-play:** quick names for NPCs, players or characters in a tabletop campaign.\n\n"
   "**Teachers:** names for word problems and examples, so worksheets don't use real students.\n\n"
   "**Developers and designers:** placeholder names for mock-ups, demos and test data — clearly fake, but realistic."},
  {"h2": "A note on real people", "body":
   "Generated full names are random combinations, but some will match real people. Don't use a generated name to imply that a real person said or did something, and don't use generated names to impersonate anyone."}
 ],
 "faq": [
  {"q": "Can I generate full names?", "a": "Yes. Keep \"Add last name\" ticked to get first and last names."},
  {"q": "How many names can I generate at once?", "a": "Up to 100 per click, with no duplicates in a single batch."},
  {"q": "Can I filter by gender?", "a": "Yes — choose female, male or any."},
  {"q": "Are these real people's names?", "a": "They're random combinations of common first names and surnames. Some may match real people by coincidence."},
  {"q": "What were the most popular baby names in 2024?", "a": "In the U.S., Olivia and Liam, according to the Social Security Administration."},
  {"q": "Can I pick a name from my own list?", "a": "Yes — use the Name Picker Wheel."}
 ],
 "sources": [S_SSA, S_CENSUS_NAMES, S_MDN],
},
# ---------------------------------------------------------------- STATE
"random-state-generator": {
 "sections": [
  {"h2": "How the random state generator works", "body":
   "All 50 US states are on the wheel, one equal slice each — a 1 in 50 (2%) chance per spin. Choose a region to narrow it down, or add Washington, D.C. with the \"50 states + DC\" preset.\n\n" + RANDOM_NOTE},
  {"h2": "The four Census regions", "body":
   "The regions follow the U.S. Census Bureau. Because they have different numbers of states, spinning all 50 doesn't give each region the same chance:\n\n"
   "| Region | States | Chance a spin lands here |\n|---|---|---|\n"
   "| South | 16 | 32% |\n| West | 13 | 26% |\n| Midwest | 12 | 24% |\n| Northeast | 9 | 18% |\n\n"
   "Delaware, Maryland and West Virginia are in the **South** in the Census grouping, which surprises some people."},
  {"h2": "Is Washington, D.C. a state?", "body":
   "No. Washington, D.C. is a federal district, not a state, so it isn't on the default wheel. Use the \"50 states + DC\" preset if your game counts it. US territories such as Puerto Rico and Guam aren't included either — type them in if you need them."},
  {"h2": "Geography games and lessons", "body":
   "**State capitals:** spin a state and name its capital. Keep score over ten rounds.\n\n"
   "**Neighbours:** spin a state and list every state that borders it.\n\n"
   "**Fact cards:** each student spins a state and researches its nickname, flag, largest city and one famous landmark.\n\n"
   "**50-state challenge:** turn on Remove winner and spin one state per lesson until all 50 are covered."},
  {"h2": "Road trips and travel", "body":
   "- **Next destination:** spin for a road-trip state, or spin within your region for a shorter trip.\n"
   "- **License-plate game:** spin a state and see who spots its plate first.\n"
   "- **Bucket list:** remove states you've visited from the list and spin for the next one."}
 ],
 "faq": [
  {"q": "Is Washington, D.C. included?", "a": "Not by default, because it isn't a state. Choose \"50 states + DC\" to add it."},
  {"q": "Can I spin only one region?", "a": "Yes. Choose Northeast, Midwest, South or West above the list."},
  {"q": "Does each region have the same chance?", "a": "No. The South has 16 states (32% of spins) and the Northeast 9 (18%). Spin a region first if you want equal chances."},
  {"q": "Can I avoid repeats?", "a": "Yes. Turn on \"Remove winner after each spin\"."},
  {"q": "Can I add Puerto Rico or other territories?", "a": "Yes. Type any extra names on new lines."}
 ],
 "sources": [S_CENSUS_REG, S_MDN],
},
# ---------------------------------------------------------------- NFL
"random-nfl-team-generator": {
 "sections": [
  {"h2": "How the NFL team wheel works", "body":
   "All 32 NFL teams are on the wheel, one equal slice each — a 1 in 32 (3.1%) chance per spin. Narrow it to the AFC, the NFC or a single division with the presets.\n\n" + RANDOM_NOTE},
  {"h2": "How the NFL is organized", "body":
   "The NFL has **32 teams** in two conferences of 16: the **AFC** and the **NFC**. Each conference has four divisions — East, North, South and West — of four teams each. Since 2021, each team plays a 17-game regular season.\n\n"
   "| Preset | Teams | Chance per team |\n|---|---|---|\n| All teams | 32 | 3.1% |\n| AFC or NFC | 16 | 6.25% |\n| One division | 4 | 25% |"},
  {"h2": "Every manager gets a different team", "body": _draft(32, "NFL")},
  {"h2": "Ideas", "body":
   "**Madden challenges:** spin your franchise team, or spin a division and rebuild its weakest team.\n\n"
   "**Office pools and game days:** give everyone a random team for the season or the weekend.\n\n"
   "**Watch parties:** each guest spins a team to cheer for.\n\n"
   "**Trivia:** spin a team, then name its city, stadium or division rival."},
  {"h2": "Keeping the list current", "body":
   "Team names on the wheel match the teams listed on NFL.com at the time of our last update. If a team relocates or rebrands, edit the entry or tell us at support@wheelova.com."}
 ],
 "faq": [
  {"q": "How many NFL teams are on the wheel?", "a": "All 32 by default. Pick AFC, NFC or a division to narrow it down."},
  {"q": "Can each person get a different team?", "a": "Yes. Turn on \"Remove winner after each spin\"."},
  {"q": "How do I randomize a fantasy draft order?", "a": "Spin managers' names on the Name Picker Wheel with Remove winner on; the order they come up is the draft order."},
  {"q": "Is this affiliated with the NFL?", "a": "No. Wheelova is an independent tool; team names are used only to identify the teams."}
 ],
 "sources": [S_NFL, S_MDN],
},
# ---------------------------------------------------------------- NBA
"random-nba-team-generator": {
 "sections": [
  {"h2": "How the NBA team wheel works", "body":
   "All 30 NBA teams are on the wheel, one equal slice each — a 1 in 30 (3.3%) chance per spin. Choose a conference or a division to narrow it down.\n\n" + RANDOM_NOTE},
  {"h2": "How the NBA is organized", "body":
   "The NBA has **30 teams**: 15 in the **Eastern Conference** and 15 in the **Western Conference**. Each conference has three divisions of five teams. Each team plays an 82-game regular season.\n\n"
   "| Preset | Teams | Chance per team |\n|---|---|---|\n| All teams | 30 | 3.3% |\n| Eastern or Western | 15 | 6.7% |\n| One division | 5 | 20% |\n\n"
   "One team on the list plays outside the United States: the **Toronto Raptors**, in Canada."},
  {"h2": "Every player gets a different team", "body": _draft(30, "NBA")},
  {"h2": "Ideas", "body":
   "**NBA 2K challenges:** spin a team for a MyNBA rebuild, or spin a division and take its last-place team.\n\n"
   "**Watch parties and brackets:** each person spins a team to follow through the season.\n\n"
   "**Classroom and trivia:** spin a team and name its city, arena or division."},
  {"h2": "Keeping the list current", "body":
   "Team names match NBA.com at the time of our last update. The NBA has discussed adding teams in the future; if the league expands or a team moves, edit the list or tell us at support@wheelova.com."}
 ],
 "faq": [
  {"q": "How many NBA teams are on the wheel?", "a": "All 30 by default. Choose a conference or division to narrow it."},
  {"q": "Can each person get a different team?", "a": "Yes. Turn on \"Remove winner after each spin\"."},
  {"q": "Which conference is each team in?", "a": "Use the Eastern Conference or Western Conference presets — each loads that conference's 15 teams."},
  {"q": "Is this affiliated with the NBA?", "a": "No. Wheelova is an independent tool; team names are used only to identify the teams."}
 ],
 "sources": [S_NBA, S_MDN],
},
# ---------------------------------------------------------------- MLB
"random-mlb-team-generator": {
 "sections": [
  {"h2": "How the MLB team wheel works", "body":
   "All 30 MLB teams are on the wheel, one equal slice each — a 1 in 30 (3.3%) chance per spin. Choose the American League, the National League or a division to narrow it down.\n\n" + RANDOM_NOTE},
  {"h2": "How MLB is organized", "body":
   "Major League Baseball has **30 teams**: 15 in the **American League (AL)** and 15 in the **National League (NL)**, each split into East, Central and West divisions of five. Each team plays a 162-game regular season.\n\n"
   "| Preset | Teams | Chance per team |\n|---|---|---|\n| All teams | 30 | 3.3% |\n| AL or NL | 15 | 6.7% |\n| One division | 5 | 20% |\n\n"
   "The A's appear as **Athletics**, the name the club has used since leaving Oakland. The **Toronto Blue Jays** are the one team based outside the United States."},
  {"h2": "Everyone gets a different team", "body": _draft(30, "MLB")},
  {"h2": "Ideas", "body":
   "**MLB The Show:** spin a team for a franchise or Road to the Show challenge.\n\n"
   "**Office pools:** assign every coworker a random team for the season.\n\n"
   "**Ballpark bucket list:** spin the next stadium to visit, and remove ones you've already seen.\n\n"
   "**Trivia nights:** spin a team, then name its city, ballpark or division."},
  {"h2": "Keeping the list current", "body":
   "Team names match MLB.com at the time of our last update. If a team moves or renames, edit the entry or tell us at support@wheelova.com."}
 ],
 "faq": [
  {"q": "How many MLB teams are on the wheel?", "a": "All 30 by default. Choose a league or division to narrow it."},
  {"q": "Why does it say Athletics instead of Oakland Athletics?", "a": "The club uses the name Athletics since leaving Oakland, and that's how it's listed by MLB."},
  {"q": "Can each person get a different team?", "a": "Yes. Turn on \"Remove winner after each spin\"."},
  {"q": "Is this affiliated with MLB?", "a": "No. Wheelova is an independent tool; team names are used only to identify the teams."}
 ],
 "sources": [S_MLB, S_MDN],
},
})

# Full-list tables generated from data
from data import NFL, NBA, MLB, STATES
def _tbl(groups, col1):
    rows = "".join(f"| {k} | {', '.join(v)} |\n" for k, v in groups.items())
    return f"| {col1} | Teams |\n|---|---|\n" + rows
_STATE_T = "| Region | States |\n|---|---|\n" + "".join(f"| {k} ({len(v)}) | {', '.join(v)} |\n" for k, v in STATES.items())
for _slug, _h, _body in [
    ("random-nfl-team-generator", "All 32 NFL teams by division", _tbl(NFL, "Division")),
    ("random-nba-team-generator", "All 30 NBA teams by division", _tbl(NBA, "Division")),
    ("random-mlb-team-generator", "All 30 MLB teams by division", _tbl(MLB, "Division")),
    ("random-state-generator", "All 50 states by region", _STATE_T),
]:
    UPGRADES[_slug]["sections"].insert(2, {"h2": _h, "body": _body})
