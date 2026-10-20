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
