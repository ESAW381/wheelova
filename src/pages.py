# Wheelova tool pages — content as data. One dict per page.
MDN = {"title": "Crypto.getRandomValues() — MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues"}

COLOR_MAP = {"red":"#E53935","orange":"#FB8C00","yellow":"#FDD835","green":"#43A047","blue":"#1E88E5","indigo":"#3949AB","violet":"#8E24AA","purple":"#7B1FA2","pink":"#EC407A","brown":"#6D4C41","black":"#212121","white":"#FAFAFA","gray":"#9E9E9E","grey":"#9E9E9E","cyan":"#00ACC1","teal":"#00897B","lime":"#C0CA33","gold":"#D4AF37","silver":"#BDBDBD","navy":"#1A237E","maroon":"#800000","beige":"#D7C4A3","turquoise":"#26C6DA","magenta":"#D81B60","olive":"#808000","peach":"#FFB38A","lavender":"#B39DDB","mint":"#98E2C6","coral":"#FF7F6B","sky blue":"#87CEEB"}

PAGES = [
{
 "slug":"yes-or-no-wheel","key":"yesno","nav":"Yes or No",
 "title":"Yes or No Wheel – Spin for a Random Answer | Wheelova",
 "description":"Spin the Yes or No wheel for an instant random answer. Add Maybe, weight your odds with extra slices, or ask again. Free, no sign-up.",
 "h1":"Yes or No Wheel","subhead":"Ask a question, spin, and let the wheel answer yes or no.",
 "entries":["Yes","No"],
 "variants":[{"label":"Yes / No","entries":["Yes","No"]},{"label":"Yes / No / Maybe","entries":["Yes","No","Maybe"]},{"label":"Yes / No / Ask again","entries":["Yes","No","Ask again"]},{"label":"Definitely / Probably / Probably not / No way","entries":["Definitely","Probably","Probably not","No way"]}],
 "resultLabel":"THE ANSWER IS","popLabel":"THE WHEEL SAYS",
 "howTo":["Think of a yes-or-no question.","Press SPIN (or the Space bar).","Read the answer in the popup — spin again for best of three."],
 "sections":[
  {"h2":"What is a yes or no wheel?","body":"A yes or no wheel is a two-slice spinner: one half says **Yes**, the other says **No**. Each spin picks one at random, so it works like a coin flip you can watch. It is useful when two options feel equally good and you just need something to break the tie."},
  {"h2":"Good ways to use it","body":"- **Small daily decisions** — \"Should I order dessert?\" \"Do I go to the gym tonight?\"\n- **Party and classroom games** — a quick yes/no round keeps a game moving without anyone choosing.\n- **Best of three** — spin three times and go with the majority if one spin feels too sudden.\n- **Check your gut** — if you feel disappointed when the wheel says \"No\", you probably wanted \"Yes\". That reaction is often the real answer."},
  {"h2":"Changing the odds","body":"Every slice on the wheel has the same size, so each entry has the same chance. To make \"Yes\" more likely, add it twice: with **Yes, Yes, No** the chance of yes is 2 in 3 (about 67%). Adding **Maybe** turns it into three equal options, each 1 in 3."},
  {"h2":"Is the answer really random?","body":"Yes. Wheelova picks the stopping point using your browser's cryptographically secure random number generator (`crypto.getRandomValues`), which is designed to be unpredictable. Each spin is independent, so getting \"Yes\" three times in a row is normal — just like flipping heads three times."}
 ],
 "faq":[
  {"q":"Is the yes or no wheel 50/50?","a":"Yes, with the default two entries each answer has an equal 50% chance. Adding or repeating entries changes the odds."},
  {"q":"Can I add a Maybe option?","a":"Yes. Tap the \"Yes / No / Maybe\" preset above the entry box, or type Maybe on a new line."},
  {"q":"Should I use a wheel for important decisions?","a":"Use it to break ties between options you are already happy with. For serious decisions — health, money, legal matters — get proper information or advice first."},
  {"q":"Does it save my entries?","a":"Yes, entries are saved in your own browser so they are there when you come back. Nothing is sent to a server."}
 ],
 "related":["decision-wheel","spinner","mystery-wheel","number-wheel"]
},
{
 "slug":"name-picker-wheel","key":"names","nav":"Name Picker",
 "title":"Random Name Picker Wheel – Spin to Pick a Name | Wheelova",
 "description":"Paste a list of names and spin the wheel to pick one at random. Remove each winner automatically for fair turns. Free for classrooms and teams.",
 "h1":"Random Name Picker Wheel","subhead":"Paste your list of names, spin, and pick someone at random — fairly.",
 "entries":["Ayesha","Ben","Chloe","Daniyal","Emma","Faisal","Grace","Hamza","Isabella","Jack"],
 "removeWinner":True,
 "variants":[{"label":"10 sample names","entries":["Ayesha","Ben","Chloe","Daniyal","Emma","Faisal","Grace","Hamza","Isabella","Jack"]},{"label":"Team A / Team B","entries":["Team A","Team B"]},{"label":"Group 1–6","entries":["Group 1","Group 2","Group 3","Group 4","Group 5","Group 6"]}],
 "howTo":["Paste or type names, one per line (copy a column straight from a spreadsheet).","Leave \"Remove winner after each spin\" on so nobody is picked twice.","Spin. The picked name disappears from the wheel for the next turn."],
 "sections":[
  {"h2":"A wheel of names for any group","body":"A name picker wheel turns a list of people into slices of a wheel and picks one at random when you spin. Because everyone can see the wheel turn, the choice feels fair — nobody can say the teacher or host played favourites."},
  {"h2":"Classroom ideas","body":"- **Cold calling without the stress** — spin to choose who answers next, and remove each student so everyone gets a turn.\n- **Presentation order** — spin repeatedly and write the names down in the order they come up.\n- **Classroom jobs** — use one wheel for names and spin once per job each week.\n- **Reading partners** — spin two names at a time to form pairs."},
  {"h2":"Teams, offices and events","body":"Use it to decide who speaks first in a stand-up, who takes the next task, or who wins a door prize. For a raffle or giveaway with many entrants, the [Raffle Wheel](/raffle-wheel) page explains how to run the draw fairly."},
  {"h2":"How to keep it fair","body":"- Enter each person **once** — a name typed twice has double the chance.\n- Check spelling, so the same person isn't listed twice under two spellings.\n- Turn on **Remove winner** when each person should be picked only once.\n- Wheelova picks with your browser's cryptographically secure random number generator, so the result can't be predicted."}
 ],
 "faq":[
  {"q":"How many names can I add?","a":"As many as you like. Labels get smaller as the list grows; up to about 50 names stay easy to read."},
  {"q":"Can I stop the same name being picked twice?","a":"Yes. Keep \"Remove winner after each spin\" switched on, or press \"Remove from wheel\" in the winner popup."},
  {"q":"Can I paste names from Excel or Google Sheets?","a":"Yes. Copy a single column and paste it into the entry box — each cell becomes one line and one slice."},
  {"q":"Are the names I enter private?","a":"Yes. Names are stored only in your own browser. Nothing is uploaded."}
 ],
 "related":["raffle-wheel","decision-wheel","letter-wheel","number-wheel"]
},
{
 "slug":"number-wheel","key":"numbers","nav":"Numbers",
 "title":"Random Number Wheel – Spin a Number 1–100 or Any Range | Wheelova",
 "description":"Spin a random number wheel from 1–10, 1–100 or any range you choose. Great for raffles, bingo, games and maths lessons. Free, no sign-up.",
 "h1":"Random Number Wheel","subhead":"Pick a range, spin, and get a random number.",
 "entries":[str(i) for i in range(1,11)],
 "numberRange":True,
 "variants":[{"label":"1–10","entries":[str(i) for i in range(1,11)]},{"label":"1–20","entries":[str(i) for i in range(1,21)]},{"label":"1–50","entries":[str(i) for i in range(1,51)]},{"label":"1–100","entries":[str(i) for i in range(1,101)]},{"label":"Dice 1–6","entries":[str(i) for i in range(1,7)]}],
 "resultLabel":"YOUR NUMBER","popLabel":"YOUR NUMBER IS",
 "howTo":["Choose a preset or type your own From and To numbers, then press Make wheel.","Press SPIN.","Turn on \"Remove winner\" if a number shouldn't come up twice (like a raffle or bingo)."],
 "sections":[
  {"h2":"How the number wheel works","body":"Each number in your range becomes one equal slice. With 1–10 every number has a 1 in 10 (10%) chance; with 1–100 it is 1 in 100 (1%). The wheel stops at a point chosen by your browser's cryptographically secure random number generator."},
  {"h2":"With or without repeats","body":"Leave **Remove winner** off and the same number can come up again — like rolling a die. Turn it on and each number can only be drawn once — like pulling tickets from a hat. Use \"no repeats\" for raffles, bingo calls and seat numbers."},
  {"h2":"Ideas for using a number wheel","body":"- **Raffle tickets** — set the range to your ticket numbers (for example 1–250) and draw winners.\n- **Bingo** — 1–75 or 1–90 with Remove winner on.\n- **Maths practice** — spin two numbers and multiply, add or compare them.\n- **Games** — pick a page, a level, or how many steps to move.\n- **Picking a seat or table** — number the seats and spin."},
  {"h2":"Need a quick 2–20 spinner instead?","body":"For a simple spinner with a handful of numbered slices, try the [Online Spinner](/spinner), where you choose how many slices you want."}
 ],
 "faq":[
  {"q":"What is the biggest range I can use?","a":"Up to 500 numbers in one wheel (for example 1–500). Larger ranges are hard to read on a wheel."},
  {"q":"Can I use negative numbers or skip numbers?","a":"Yes. Type any numbers you want into the entry box, one per line — for example only even numbers, or -5 to 5."},
  {"q":"Is every number equally likely?","a":"Yes, as long as each number appears once. Slices are equal in size and the stop point is chosen at random."},
  {"q":"Can I draw several numbers in a row without repeats?","a":"Yes. Turn on \"Remove winner after each spin\" and keep spinning; each result leaves the wheel."}
 ],
 "related":["spinner","raffle-wheel","letter-wheel","yes-or-no-wheel"]
},
{
 "slug":"color-wheel","key":"colors","nav":"Colors",
 "title":"Color Wheel Spinner – Spin for a Random Color | Wheelova",
 "description":"Spin the color wheel to pick a random color. Every slice is painted its real color. Use the rainbow, basics or your own list. Free, no sign-up.",
 "h1":"Color Wheel Spinner","subhead":"Spin to pick a random color — each slice shows the real color.",
 "entries":["Red","Orange","Yellow","Green","Blue","Indigo","Violet"],
 "mode":"color","colorMap":COLOR_MAP,
 "variants":[{"label":"Rainbow (7)","entries":["Red","Orange","Yellow","Green","Blue","Indigo","Violet"]},{"label":"Basic colors (12)","entries":["Red","Orange","Yellow","Green","Blue","Purple","Pink","Brown","Black","White","Gray","Teal"]},{"label":"Primary (3)","entries":["Red","Yellow","Blue"]},{"label":"Pastels","entries":["Peach","Lavender","Mint","Sky Blue","Coral","Beige"]}],
 "resultLabel":"YOUR COLOR","popLabel":"YOUR COLOR IS",
 "howTo":["Pick a preset or type color names, one per line.","Press SPIN.","See the color name and swatch in the popup."],
 "sections":[
  {"h2":"Which colors are painted?","body":"Common color names are drawn in their real color: red, orange, yellow, green, blue, indigo, violet, purple, pink, brown, black, white, gray, cyan, teal, lime, gold, silver, navy, maroon, beige, turquoise, magenta, olive, peach, lavender, mint, coral and sky blue. Any other word you type still works — it just uses the standard wheel colors."},
  {"h2":"Ideas for a random color","body":"- **Art and drawing challenges** — spin a color you must use as the main one.\n- **Kids' games** — \"find something in the room that is this color\".\n- **Outfit or theme days** — let the wheel choose the color of the week.\n- **Party games** — color-themed teams or Twister-style moves."},
  {"h2":"Is this a color theory wheel?","body":"No — this is a random **picker**. A color theory wheel shows how hues relate (complementary, analogous and so on). If you need a palette generator or design tool, use a dedicated color-theory tool; use this page when you want chance to choose a color."}
 ],
 "faq":[
  {"q":"Can I add my own colors?","a":"Yes. Type any color name on a new line. Names in the list above are painted in their real color."},
  {"q":"Can I pick a color without repeats?","a":"Yes. Turn on \"Remove winner after each spin\" so each color is used once."},
  {"q":"Is each color equally likely?","a":"Yes, as long as each color appears once in the list."}
 ],
 "related":["letter-wheel","mystery-wheel","decision-wheel","spinner"]
},
{
 "slug":"spinner","key":"spinner","nav":"Spinner",
 "title":"Online Spinner – Free Number Spinner from 2 to 20 Slices | Wheelova",
 "description":"A simple online spinner: choose 2 to 20 numbered slices and spin. Use it for board games, turns and quick random picks. Free, works on any phone.",
 "h1":"Online Spinner","subhead":"Choose how many slices you need, then spin.",
 "entries":["1","2","3","4","5","6"],
 "spinnerCount":True,
 "resultLabel":"YOU SPUN","popLabel":"YOU SPUN",
 "howTo":["Choose the number of slices (2–20).","Press SPIN or tap the wheel.","Spin again any time — results are listed under Results."],
 "sections":[
  {"h2":"A spinner for games and quick picks","body":"This is a plain numbered spinner, like the cardboard spinner in a board game. Pick how many slices you want and spin. If you were searching for the number spinner that appears in web search results, this works the same way — with a results history, sound on/off and no ads covering the wheel."},
  {"h2":"Ways to use it","body":"- **Board games** — replace a lost spinner or die.\n- **Turn order** — give each player a number and spin.\n- **Lessons** — spin a question number or a page number.\n- **Fitness** — spin for the number of reps or rounds."},
  {"h2":"Want words instead of numbers?","body":"Type anything you like into the entry box below — names, tasks or prizes — and the spinner becomes a custom wheel. For bigger number ranges such as 1–100, use the [Random Number Wheel](/number-wheel)."}
 ],
 "faq":[
  {"q":"How many slices can the spinner have?","a":"Choose 2 to 20 slices from the menu. For more, type your own entries in the list."},
  {"q":"Does it work on phones?","a":"Yes. It runs in any modern mobile browser with no app to install."},
  {"q":"Is it random?","a":"Yes. The stop point is chosen with your browser's cryptographically secure random number generator."}
 ],
 "related":["number-wheel","yes-or-no-wheel","decision-wheel","mystery-wheel"]
},
{
 "slug":"decision-wheel","key":"decision","nav":"Decision Wheel",
 "title":"Decision Wheel – Spin to Decide Between Options | Wheelova",
 "description":"Can't decide? Put your options on the decision wheel and spin. Free decision maker for food, plans, movies and tie-breaks. No sign-up needed.",
 "h1":"Decision Wheel","subhead":"Put your options on the wheel and let it decide.",
 "entries":["Option 1","Option 2","Option 3","Option 4"],
 "variants":[{"label":"What to eat","entries":["Pizza","Burger","Biryani","Sushi","Tacos","Pasta","Salad","Noodles"]},{"label":"Movie genre","entries":["Comedy","Action","Drama","Horror","Sci-fi","Romance","Animation","Documentary"]},{"label":"Weekend plan","entries":["Stay in","Go out to eat","Hike","Visit friends","Shopping","Movie night"]},{"label":"Who pays?","entries":["Me","You","Split it"]}],
 "howTo":["Replace the sample options with your own, one per line.","Spin.","Not happy with the answer? That tells you which option you really wanted."],
 "sections":[
  {"h2":"When a decision wheel helps","body":"A decision wheel is most useful when every option is acceptable and the hard part is simply choosing. Instead of debating dinner for 20 minutes, list the places everyone is fine with and spin once."},
  {"h2":"Make better decisions with it","body":"- **Only add options you'd accept.** If you'd refuse the result, take it off the wheel first.\n- **Weight what matters.** Add your favourite twice to double its chance.\n- **Use the \"disappointment test\".** If you hope for a re-spin, you've learned what you actually prefer.\n- **Agree first.** In a group, agree to accept the result before spinning — it saves the argument."},
  {"h2":"Popular decision wheels","body":"Use the presets above for food, movies or weekend plans, or try the [Yes or No Wheel](/yes-or-no-wheel) for single questions."}
 ],
 "faq":[
  {"q":"Can I make one option more likely?","a":"Yes. Enter it more than once — each copy is another equal slice."},
  {"q":"How many options can I add?","a":"As many as you like, but 3–12 options are easiest to read and decide between."},
  {"q":"Is it fair for a group decision?","a":"Yes, if everyone agrees on the list beforehand. The result is chosen at random by your browser, and everyone can watch it."}
 ],
 "related":["yes-or-no-wheel","name-picker-wheel","mystery-wheel","lucky-wheel"]
},
{
 "slug":"raffle-wheel","key":"raffle","nav":"Raffle Wheel",
 "title":"Raffle Wheel – Pick Raffle & Giveaway Winners Online | Wheelova",
 "description":"Run a raffle or giveaway draw with a spinning wheel. Paste entrants or ticket numbers, remove each winner, and spin live. Free, no sign-up.",
 "h1":"Raffle Wheel","subhead":"Draw raffle and giveaway winners live, in front of everyone.",
 "entries":["Ticket 001","Ticket 002","Ticket 003","Ticket 004","Ticket 005","Ticket 006","Ticket 007","Ticket 008"],
 "removeWinner":True,
 "variants":[{"label":"Tickets 1–50","entries":[f"Ticket {i:03d}" for i in range(1,51)]},{"label":"Tickets 1–100","entries":[f"Ticket {i:03d}" for i in range(1,101)]},{"label":"Prize tiers","entries":["Grand prize","Second prize","Third prize"]}],
 "howTo":["Paste entrants' names or ticket numbers, one per line.","Keep \"Remove winner\" on so nobody wins twice.","Spin once for each prize, starting with the smallest prize or the grand prize — announce your order first."],
 "sections":[
  {"h2":"How to run a fair draw","body":"1. **Close entries** before you spin, and say how many entries there are.\n2. **Check for duplicates** — one line per valid entry (or per ticket bought).\n3. **Announce the order** of prizes before the first spin.\n4. **Spin live** on screen or stream so everyone can see.\n5. **Record the results** — the Results list keeps every winner of the session; take a screenshot for your records."},
  {"h2":"Tickets vs. names","body":"If people can buy several tickets, enter **ticket numbers**, not names — someone with three tickets then has three slices, which is fair. If everyone has one entry, names are simpler."},
  {"h2":"Giveaway rules","body":"A random wheel picks a winner fairly, but it doesn't make a giveaway legal by itself. Rules on raffles, sweepstakes and prize draws differ by country and platform (for example, some places require a free way to enter). Check the rules that apply to you and to the social network you run it on."}
 ],
 "faq":[
  {"q":"How many entrants can the raffle wheel handle?","a":"Hundreds of entries work. Labels shrink as the list grows, but the draw stays random."},
  {"q":"Can I draw several winners?","a":"Yes. Leave \"Remove winner\" on and spin once per prize; each winner leaves the wheel."},
  {"q":"Can people verify the result?","a":"Spin live so everyone can watch, and screenshot the Results list. Verifiable draw receipts are planned but not available yet."}
 ],
 "related":["name-picker-wheel","number-wheel","lucky-wheel","decision-wheel"]
},
{
 "slug":"lucky-wheel","key":"lucky","nav":"Lucky Wheel",
 "title":"Lucky Wheel – Spin to Win Prizes Online | Wheelova",
 "description":"Make a lucky wheel with your own prizes and spin to win. Use it for parties, shop events, classrooms and online games. Free, no sign-up.",
 "h1":"Lucky Wheel","subhead":"Add your prizes, spin, and see what luck brings.",
 "entries":["10% off","Free drink","Try again","Sticker","Free dessert","Mystery gift","Try again","Grand prize"],
 "variants":[{"label":"Shop prizes","entries":["10% off","Free drink","Try again","Sticker","Free dessert","Mystery gift","Try again","Grand prize"]},{"label":"Party forfeits","entries":["Sing a song","Tell a joke","Dance for 10 seconds","Do an impression","Skip a turn","Pick someone else"]},{"label":"Classroom rewards","entries":["Sit anywhere","Homework pass","Choose the music","Line leader","Extra 5 minutes break","Sticker"]}],
 "resultLabel":"YOU GOT","popLabel":"YOU WON",
 "howTo":["Replace the sample prizes with your own.","Repeat a prize to make it more common (e.g. several \"Try again\" slices).","Spin and hand out the prize."],
 "sections":[
  {"h2":"Setting the odds","body":"Each slice is the same size, so the chance of a prize equals how many slices it has, divided by the total. With 8 slices and one \"Grand prize\", the chance of winning it is 1 in 8 (12.5%). To make it rarer, add more small prizes or \"Try again\" slices."},
  {"h2":"Ideas for a lucky wheel","body":"- **Shop or market stall events** — small discounts and freebies.\n- **Birthday parties** — party favours or fun forfeits.\n- **Classrooms** — reward wheel for good work.\n- **Streams and online events** — viewers win shout-outs or small prizes."},
  {"h2":"Be clear about prizes","body":"If real prizes are involved, tell people the odds and the prize list in advance. For giveaways open to the public, check local promotion and sweepstakes rules first."}
 ],
 "faq":[
  {"q":"How do I make the grand prize rare?","a":"Add more slices of other prizes or \"Try again\". With one grand prize among 20 slices, the chance is 5%."},
  {"q":"Can I remove a prize once it's won?","a":"Yes. Press \"Remove from wheel\" in the winner popup, or turn on \"Remove winner after each spin\"."},
  {"q":"Is this the same as Wheel of Fortune?","a":"No. Wheelova is a free random wheel you fill with your own prizes; it isn't connected to any TV show."}
 ],
 "related":["raffle-wheel","mystery-wheel","decision-wheel","name-picker-wheel"]
},
{
 "slug":"mystery-wheel","key":"mystery","nav":"Mystery Wheel",
 "title":"Mystery Wheel – Hidden Spin Wheel with Surprise Results | Wheelova",
 "description":"A mystery wheel hides every slice behind a question mark. Spin to reveal the surprise. Great for games, challenges and prize reveals. Free.",
 "h1":"Mystery Wheel","subhead":"Every slice is hidden. Spin to reveal the surprise.",
 "entries":["Do 10 jumping jacks","Tell a secret","Swap seats","Sing a chorus","Free pass","Speak in an accent","Compliment someone","Mystery prize"],
 "mode":"mystery",
 "resultLabel":"REVEALED","popLabel":"THE MYSTERY IS",
 "howTo":["Type the hidden outcomes, one per line (the list box shows them — hide the screen from players while you type).","Every slice on the wheel shows \"?\".","Spin — the result is revealed only in the popup."],
 "sections":[
  {"h2":"How the mystery wheel works","body":"It works like any other random wheel, except the labels are hidden. Players see only question marks, so nobody knows where the good or bad outcomes are. The result appears when the wheel stops."},
  {"h2":"Ideas","body":"- **Challenge wheel** — fun tasks or dares for parties.\n- **Prize reveal** — hide prizes for a classroom or stream.\n- **Surprise date night** — hidden activities or restaurants.\n- **Mystery lesson starter** — hidden questions or topics."},
  {"h2":"Keep it secret","body":"The entry list is visible while you edit it. Set the wheel up before sharing your screen, or scroll down past the list so only the wheel is visible."}
 ],
 "faq":[
  {"q":"Can players see the entries?","a":"Not on the wheel — slices show \"?\". The entry box below still lists them, so set it up before players look."},
  {"q":"Can I remove an outcome once it's revealed?","a":"Yes. Press \"Remove from wheel\" or turn on \"Remove winner after each spin\"."},
  {"q":"Is the result random?","a":"Yes, chosen with your browser's cryptographically secure random number generator."}
 ],
 "related":["lucky-wheel","decision-wheel","yes-or-no-wheel","color-wheel"]
},
{
 "slug":"letter-wheel","key":"letters","nav":"Letter Wheel",
 "title":"Random Letter Wheel – Spin the Alphabet A to Z | Wheelova",
 "description":"Spin the letter wheel to pick a random letter from A to Z. Choose vowels only, consonants, or remove hard letters. Great for word games. Free.",
 "h1":"Random Letter Wheel","subhead":"Spin to pick a random letter of the alphabet.",
 "entries":list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
 "variants":[{"label":"A–Z","entries":list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")},{"label":"Vowels","entries":list("AEIOU")},{"label":"Consonants","entries":list("BCDFGHJKLMNPQRSTVWXYZ")},{"label":"No Q, X, Z","entries":list("ABCDEFGHIJKLMNOPRSTUVWY")}],
 "resultLabel":"YOUR LETTER","popLabel":"YOUR LETTER IS",
 "howTo":["Choose A–Z, vowels, consonants, or edit the list.","Spin.","Turn on \"Remove winner\" to go through letters without repeats."],
 "sections":[
  {"h2":"Word game ideas","body":"- **Categories game** — spin a letter, then name an animal, a city and a food that start with it.\n- **Spelling practice** — spin a letter and list as many words as you can in one minute.\n- **Storytelling** — every sentence must start with the spun letter.\n- **Alphabet scavenger hunt** — find an object starting with the letter."},
  {"h2":"Removing tricky letters","body":"Letters like Q, X and Z have very few common starting words, which can stall a game. Use the \"No Q, X, Z\" preset, or delete any letter from the list."},
  {"h2":"Every letter has the same chance","body":"With all 26 letters, each one has a 1 in 26 chance (about 3.8%). In real English, letters are not used equally often — so this wheel is fair for games, not a model of how often letters appear in words."}
 ],
 "faq":[
  {"q":"Can I use other alphabets?","a":"Yes. Type any letters or characters you like, one per line."},
  {"q":"Can I avoid repeating letters?","a":"Yes. Turn on \"Remove winner after each spin\"."},
  {"q":"Is each letter equally likely?","a":"Yes, as long as each letter appears once in the list."}
 ],
 "related":["number-wheel","color-wheel","name-picker-wheel","spinner"]
},
]

# ---------------- Batch 2 ----------------
from data import COUNTRIES, STATES, NFL, NBA, NBA_CONF, MLB, NAMES, flat

def _variants(groups, all_label):
    v = [{"label": all_label, "entries": flat(groups)}]
    v += [{"label": k, "entries": groups[k]} for k in groups]
    return v

UN_SRC = {"title": "UN Statistics Division — Standard country or area codes (M49)", "url": "https://unstats.un.org/unsd/methodology/m49/"}
CENSUS_SRC = {"title": "U.S. Census Bureau — Census regions and divisions", "url": "https://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf"}

PAGES += [
{
 "slug":"random-number-generator","key":"rng","nav":"Number Generator","tool":"number",
 "title":"Random Number Generator – Pick Numbers 1–100 or Any Range | Wheelova",
 "description":"Free random number generator. Pick one or many numbers in any range, with or without repeats, sorted or not. Copy the results in one click.",
 "h1":"Random Number Generator","subhead":"Pick one number or a whole list, in any range, with or without repeats.",
 "howTo":["Set the range with From and To (or tap a quick range).","Choose how many numbers you want, and whether repeats are allowed.","Press Generate. Copy the results with one click."],
 "sections":[
  {"h2":"How this random number generator works","body":"Each number in your range has the same chance of being picked. The numbers come from your browser's cryptographically secure random number generator (`crypto.getRandomValues`) — the same kind of source browsers use for security features."},
  {"h2":"Repeats or no repeats?","body":"- **No repeats (unique)** — like drawing tickets from a hat. Use it for raffles, lottery-style draws, seat numbers or picking several winners. You can't ask for more unique numbers than the range contains.\n- **Repeats allowed** — like rolling a die many times. Use it for games, dice simulations and practice problems."},
  {"h2":"Common ranges","body":"- **1–10** — quick choices, games, \"pick a number\".\n- **1–100** — percentages, classroom questions, raffles.\n- **1–6** — a standard die. For a visual version, try the [Random Number Wheel](/number-wheel).\n- **Any range** — use negative numbers or big ranges, such as 1000–9999 for a four-digit code."},
  {"h2":"What it isn't for","body":"This tool is fine for games, classrooms, raffles and everyday choices. It is not a certified lottery system or a replacement for audited draw software where the law requires one."}
 ],
 "faq":[
  {"q":"How do I pick a random number between 1 and 100?","a":"Set From to 1 and To to 100 (or tap the 1–100 button), keep How many at 1, and press Generate."},
  {"q":"Can I generate numbers without repeats?","a":"Yes. Tick \"No repeats\". Each number then appears at most once in your results."},
  {"q":"How many numbers can I generate at once?","a":"Up to 1,000 per click."},
  {"q":"Is it truly random?","a":"It uses the browser's cryptographically secure random number generator, which is designed to be unpredictable. Each click is independent of the last."}
 ],
 "related":["number-wheel","spinner","raffle-wheel","random-team-generator"]
},
{
 "slug":"random-team-generator","key":"teams","nav":"Team Generator","tool":"team",
 "title":"Random Team Generator – Split Names into Random Groups | Wheelova",
 "description":"Paste a list of names and split them into random teams or groups in one click. Choose the number of teams or people per team. Free, no sign-up.",
 "h1":"Random Team Generator","subhead":"Paste your names and split them into fair, random teams.",
 "sample":["Ayesha","Ben","Chloe","Daniyal","Emma","Faisal","Grace","Hamza","Isabella","Jack","Kiran","Lena"],
 "howTo":["Paste names, one per line.","Choose the number of teams, or how many people per team.","Press Generate. Not happy? Press it again to reshuffle."],
 "sections":[
  {"h2":"How the teams are made","body":"The list is shuffled with your browser's cryptographically secure random number generator, then people are dealt into teams one by one, like dealing cards. That keeps team sizes within one person of each other — with 13 people in 3 teams you get 5, 4 and 4."},
  {"h2":"Number of teams vs. people per team","body":"- **Number of teams** — \"split my class into 4 groups\".\n- **People per team** — \"make pairs\" (2) or \"groups of 5\". The last team may be one smaller if the numbers don't divide evenly."},
  {"h2":"Ideas","body":"- **Classrooms** — project groups, reading circles, seating.\n- **Sports and PE** — fair sides for a match.\n- **Work** — breakout rooms, workshop tables, hackathon teams.\n- **Game nights** — quiz teams or partners for card games."},
  {"h2":"Keeping teams fair","body":"Random teams are fair in the sense that nobody chooses them — but they don't balance skill. If you need balanced ability, generate the teams, then swap one or two people by hand. Enter each person once so nobody appears in two teams."}
 ],
 "faq":[
  {"q":"How do I make random pairs?","a":"Choose \"People per team\" and enter 2. With an odd number of people, the last team has one person — move them into any pair to make a group of three."},
  {"q":"Can I name the teams?","a":"Teams are numbered Team 1, Team 2 and so on. Copy the results and rename them wherever you paste them."},
  {"q":"Are the names saved?","a":"Yes, in your own browser only, so the list is there next time. Nothing is uploaded."},
  {"q":"Can I pick one person instead of making teams?","a":"Yes — use the [Name Picker Wheel](/name-picker-wheel)."}
 ],
 "related":["name-picker-wheel","random-name-generator","random-number-generator","decision-wheel"]
},
{
 "slug":"random-name-generator","key":"namegen","nav":"Name Generator","tool":"name",
 "title":"Random Name Generator – Generate First & Full Names | Wheelova",
 "description":"Generate random first names or full names in one click. Choose female, male or any, and up to 100 names at once. Great for characters, games and test data.",
 "h1":"Random Name Generator","subhead":"Generate random first names or full names in one click.",
 "data":NAMES,
 "howTo":["Choose female, male or any names.","Choose how many names and whether to add a last name.","Press Generate and copy the list."],
 "sections":[
  {"h2":"Name generator vs. name picker","body":"This page **creates** names from a built-in list. If you already have a list of real people and want to choose one of them, use the [Name Picker Wheel](/name-picker-wheel) instead."},
  {"h2":"Where the names come from","body":"The generator mixes common first names and surnames used in English-speaking countries, plus some widely used South Asian, Middle Eastern and East Asian names. It is a fun, illustrative list — not a statistical sample of any population."},
  {"h2":"Ideas","body":"- **Writers** — names for side characters.\n- **Games and role-play** — quick NPC or player names.\n- **Teachers** — names for word problems and examples.\n- **Developers and designers** — placeholder names for mock-ups and test data."},
  {"h2":"A note on real people","body":"Generated full names are random combinations, but some will match real people. Don't use them to imply that a real person said or did something."}
 ],
 "faq":[
  {"q":"Can I generate full names?","a":"Yes. Keep \"Add last name\" ticked to get first + last names."},
  {"q":"How many names can I generate?","a":"Up to 100 per click, with no duplicates in a single batch."},
  {"q":"Can I filter by gender?","a":"Yes — choose female, male, or any."}
 ],
 "related":["name-picker-wheel","random-team-generator","random-letter-generator","random-country-generator"]
},
{
 "slug":"random-country-generator","key":"countries","nav":"Country Generator",
 "title":"Random Country Generator – Spin the Wheel of Countries | Wheelova",
 "description":"Spin to pick a random country from all 193 UN member states, or filter by Africa, Americas, Asia, Europe or Oceania. Free country wheel for games and lessons.",
 "h1":"Random Country Generator","subhead":"Spin to pick a random country — all 193 UN members, or one region.",
 "entries":flat(COUNTRIES),"variants":_variants(COUNTRIES,"All 193 countries"),
 "resultLabel":"YOUR COUNTRY","popLabel":"YOUR COUNTRY IS",
 "howTo":["Choose all countries or one region.","Spin the wheel.","Turn on \"Remove winner\" to go through countries without repeats."],
 "sections":[
  {"h2":"Which countries are included?","body":"The list contains the 193 member states of the United Nations, grouped by the UN's M49 regions: Africa (54), the Americas (35), Asia (47), Europe (43) and Oceania (14). Observer states and territories (for example Palestine, the Holy See, Taiwan or Kosovo) are not on the default list — add them yourself if your game needs them."},
  {"h2":"Ideas for a random country","body":"- **Geography lessons** — find it on a map, name the capital, or describe the flag.\n- **Travel inspiration** — spin for a dream destination to research.\n- **Cooking challenge** — cook a dish from the country you spin.\n- **Quiz nights** — one country per round, teams answer questions about it."},
  {"h2":"About the regions","body":"The UN groups some countries differently from everyday usage — for example, Cyprus, Turkey, Armenia, Azerbaijan and Georgia are in Asia, and Russia is in Europe. The wheel follows the UN grouping so the lists are consistent."}
 ],
 "faq":[
  {"q":"How many countries are on the wheel?","a":"All 193 UN member states when \"All 193 countries\" is selected."},
  {"q":"Can I pick a country from one continent?","a":"Yes. Choose Africa, Americas, Asia, Europe or Oceania above the list."},
  {"q":"Can I add territories?","a":"Yes. Type any extra names into the list, one per line."}
 ],
 "sources":[UN_SRC],
 "related":["random-state-generator","random-name-generator","random-letter-generator","decision-wheel"]
},
{
 "slug":"random-state-generator","key":"states","nav":"State Generator",
 "title":"Random State Generator – Spin a Random US State | Wheelova",
 "description":"Pick a random US state from all 50, or by region: Northeast, Midwest, South or West. Free state wheel for road trips, lessons and games.",
 "h1":"Random State Generator","subhead":"Spin to pick one of the 50 US states — or one region.",
 "entries":flat(STATES),"variants":_variants(STATES,"All 50 states")+[{"label":"50 states + DC","entries":flat(STATES)+["District of Columbia"]}],
 "resultLabel":"YOUR STATE","popLabel":"YOUR STATE IS",
 "howTo":["Choose all states or a region.","Spin.","Turn on \"Remove winner\" to visit every state once."],
 "sections":[
  {"h2":"Regions on this wheel","body":"The regions follow the U.S. Census Bureau: **Northeast** (9 states), **Midwest** (12), **South** (16) and **West** (13). Washington, D.C. is not a state; add it with the \"50 states + DC\" preset."},
  {"h2":"Ideas","body":"- **Road-trip planning** — spin for your next destination.\n- **US geography lessons** — capital, nickname, neighbouring states.\n- **License-plate or trivia games** — one state per round.\n- **Writing prompts** — set a story in the state you spin."}
 ],
 "faq":[
  {"q":"Is Washington, D.C. included?","a":"Not by default, because it isn't a state. Choose \"50 states + DC\" to add it."},
  {"q":"Can I spin only one region?","a":"Yes. Choose Northeast, Midwest, South or West above the list."}
 ],
 "sources":[CENSUS_SRC],
 "related":["random-country-generator","random-nfl-team-generator","decision-wheel","random-number-generator"]
},
{
 "slug":"random-nfl-team-generator","key":"nfl","nav":"NFL Teams",
 "title":"Random NFL Team Generator – Spin the NFL Team Wheel | Wheelova",
 "description":"Spin to pick a random NFL team from all 32, or by AFC, NFC or division. Free NFL team wheel for fantasy drafts, Madden picks and watch parties.",
 "h1":"Random NFL Team Generator","subhead":"Spin to pick one of the 32 NFL teams.",
 "entries":flat(NFL),"variants":[{"label":"All 32 teams","entries":flat(NFL)},{"label":"AFC","entries":[t for k,v in NFL.items() if k.startswith("AFC") for t in v]},{"label":"NFC","entries":[t for k,v in NFL.items() if k.startswith("NFC") for t in v]}]+[{"label":k,"entries":v} for k,v in NFL.items()],
 "resultLabel":"YOUR TEAM","popLabel":"YOUR TEAM IS",
 "howTo":["Choose all teams, a conference or a division.","Spin.","Use \"Remove winner\" so each person gets a different team."],
 "sections":[
  {"h2":"What's on the wheel","body":"All 32 current NFL teams: 16 in the AFC and 16 in the NFC, each split into East, North, South and West divisions of four teams."},
  {"h2":"Ideas","body":"- **Madden and video games** — let the wheel choose your team for a challenge run.\n- **Office pools and parties** — give everyone a random team for the season or a game day.\n- **Fantasy football** — randomize draft order with the [Name Picker Wheel](/name-picker-wheel), then spin a team for each manager.\n- **Trivia** — answer questions about the team you spin."}
 ],
 "faq":[
  {"q":"How many NFL teams are on the wheel?","a":"All 32 teams by default. Pick AFC, NFC or a division to narrow it down."},
  {"q":"Can each person get a different team?","a":"Yes. Turn on \"Remove winner after each spin\"."},
  {"q":"Is this affiliated with the NFL?","a":"No. Wheelova is an independent tool; team names are used only to identify the teams."}
 ],
 "related":["random-nba-team-generator","random-mlb-team-generator","random-team-generator","random-state-generator"]
},
{
 "slug":"random-nba-team-generator","key":"nba","nav":"NBA Teams",
 "title":"Random NBA Team Generator – Spin the NBA Team Wheel | Wheelova",
 "description":"Spin to pick a random NBA team from all 30, or by Eastern or Western Conference and division. Free NBA team wheel for 2K, drafts and games.",
 "h1":"Random NBA Team Generator","subhead":"Spin to pick one of the 30 NBA teams.",
 "entries":flat(NBA),"variants":[{"label":"All 30 teams","entries":flat(NBA)}]+[{"label":c+" Conference","entries":[t for d in ds for t in NBA[d]]} for c,ds in NBA_CONF.items()]+[{"label":k,"entries":v} for k,v in NBA.items()],
 "resultLabel":"YOUR TEAM","popLabel":"YOUR TEAM IS",
 "howTo":["Choose all teams, a conference or a division.","Spin.","Turn on \"Remove winner\" for a draft-style pick."],
 "sections":[
  {"h2":"What's on the wheel","body":"All 30 current NBA teams — 15 in the Eastern Conference and 15 in the Western Conference, in six divisions of five teams."},
  {"h2":"Ideas","body":"- **NBA 2K challenges** — spin your team for a rebuild or a random franchise.\n- **Watch parties** — everyone spins a team to cheer for.\n- **Classrooms and trivia** — spin a team, then name its city or arena."}
 ],
 "faq":[
  {"q":"How many NBA teams are on the wheel?","a":"All 30 by default. Choose a conference or division to narrow it."},
  {"q":"Is this affiliated with the NBA?","a":"No. Wheelova is an independent tool; team names are used only to identify the teams."}
 ],
 "related":["random-nfl-team-generator","random-mlb-team-generator","random-team-generator","number-wheel"]
},
{
 "slug":"random-mlb-team-generator","key":"mlb","nav":"MLB Teams",
 "title":"Random MLB Team Generator – Spin the MLB Team Wheel | Wheelova",
 "description":"Spin to pick a random MLB team from all 30, or by American or National League and division. Free MLB team wheel for MLB The Show, pools and games.",
 "h1":"Random MLB Team Generator","subhead":"Spin to pick one of the 30 MLB teams.",
 "entries":flat(MLB),"variants":[{"label":"All 30 teams","entries":flat(MLB)},{"label":"American League","entries":[t for k,v in MLB.items() if k.startswith("AL") for t in v]},{"label":"National League","entries":[t for k,v in MLB.items() if k.startswith("NL") for t in v]}]+[{"label":k,"entries":v} for k,v in MLB.items()],
 "resultLabel":"YOUR TEAM","popLabel":"YOUR TEAM IS",
 "howTo":["Choose all teams, a league or a division.","Spin.","Turn on \"Remove winner\" so nobody gets the same team."],
 "sections":[
  {"h2":"What's on the wheel","body":"All 30 current MLB teams: 15 in the American League and 15 in the National League, in six divisions of five. The A's appear as \"Athletics\", the name the club uses since leaving Oakland."},
  {"h2":"Ideas","body":"- **MLB The Show** — spin a team for a franchise or Road to the Show challenge.\n- **Office pools** — assign random teams for the season.\n- **Ballpark bucket list** — spin the next stadium to visit."}
 ],
 "faq":[
  {"q":"How many MLB teams are on the wheel?","a":"All 30 by default. Choose a league or division to narrow it."},
  {"q":"Is this affiliated with MLB?","a":"No. Wheelova is an independent tool; team names are used only to identify the teams."}
 ],
 "related":["random-nfl-team-generator","random-nba-team-generator","random-team-generator","random-state-generator"]
},
]

# Retargets
for p in PAGES:
    if p["slug"] == "letter-wheel":
        p.update({"slug":"random-letter-generator","nav":"Letter Generator",
          "title":"Random Letter Generator – Spin the Alphabet Wheel A–Z | Wheelova",
          "description":"Random letter generator: spin the alphabet wheel to pick a letter from A to Z. Vowels only, consonants, or no hard letters. Free for word games.",
          "h1":"Random Letter Generator","subhead":"Spin the alphabet wheel to pick a random letter."})
    if p["slug"] == "color-wheel":
        p.update({"nav":"Color Generator",
          "title":"Random Color Generator & Color Wheel Picker | Wheelova",
          "description":"Spin the color wheel picker for a random color, shown with its hex code. Rainbow, basic, primary or pastel colors, or your own list. Free.",
          "h1":"Random Color Generator","subhead":"Spin the color wheel to pick a random color — with its hex code."})

for p in PAGES:
    p["related"] = ["random-letter-generator" if r == "letter-wheel" else r for r in p["related"]]

# ---------------- Batch 3: Truth or Dare, Coin flip, Dice roller ----------------
TOD = {
"kids": {
 "Truth": ["What's your favourite food, and what's the worst food you've ever tried?","If you could have any animal as a pet, what would it be?","What's the funniest thing that's happened to you at school?","If you could be any superhero, who would you be?","What's something you're really good at?","What's your favourite thing to do on a weekend?","If you could visit any place in the world, where would you go?","What's the silliest thing you've ever done?","Who is your best friend, and why?","What's your favourite book or film, and why?","If you could invent something, what would it be?","What's the best present you've ever received?","What are you scared of?","If you were a teacher for a day, what would you teach?","What's your favourite joke?","What would you do if you were invisible for a day?","What's something nice someone did for you recently?","If you could have any job, what would it be?","What's your favourite game to play?","What's one thing you'd like to learn this year?"],
 "Dare": ["Do your best animal impression for 10 seconds.","Hop on one foot five times.","Say the alphabet backwards as far as you can.","Make the silliest face you can and hold it for five seconds.","Speak like a robot until your next turn.","Do five jumping jacks.","Sing the first line of your favourite song.","Pretend to be a news reporter for 20 seconds.","Walk like a penguin across the room.","Tell a joke — if nobody laughs, tell another.","Balance a book on your head for 10 seconds.","Do your best dance move.","Say a tongue twister three times fast.","Act out your favourite animal without making a sound.","Give everyone a compliment.","Draw a picture with your eyes closed.","Spin around three times, then try to walk in a straight line.","Pretend you're a statue until someone makes you laugh.","Talk in a whisper until your next turn.","Do your best impression of a teacher (kindly!)."]
},
"teens": {
 "Truth": ["What's the most embarrassing thing that's happened to you in public?","What's a song you secretly love but would never admit to?","What's the last thing you searched for on your phone?","What's your biggest pet peeve?","Who in this room would survive longest in a zombie apocalypse?","What's the weirdest dream you've ever had?","What's a habit you're trying to break?","What's the best advice you've ever been given?","If you could swap lives with anyone for a day, who would it be?","What's a rule you think is completely pointless?","What's your most unpopular opinion?","What's the worst haircut you've ever had?","What's the most useless talent you have?","What's one thing you'd change about yourself?","What's the most childish thing you still do?","Which app do you spend the most time on?","What's a goal you have for this year?","What's the funniest text you've ever sent by mistake?","Who was your first celebrity crush?","What's something you're proud of but rarely talk about?"],
 "Dare": ["Let the group pick a song for you to sing the chorus of.","Talk in an accent of the group's choice until your next turn.","Do 10 push-ups (or 10 squats).","Let someone draw a moustache on your hand.","Tell a story using only song titles.","Do your best runway walk across the room.","Strike your best selfie pose and hold it for five seconds.","Speak only in questions until your next turn.","Do an impression of someone in the group — they choose who.","Try to lick your elbow.","Hold a plank for 30 seconds.","Let the group choose your phone wallpaper for the next hour.","Say something nice about every person here.","Recite a poem the group picks, dramatically.","Do your best evil laugh.","Let the group give you a new nickname until your next turn.","Act out a famous movie scene without words.","Keep your eyes closed until your next turn.","Invent a new handshake with the person on your left.","Describe your day as if you were a sports commentator."]
},
}

PAGES += [
{
 "slug":"truth-or-dare-wheel","key":"tod","nav":"Truth or Dare",
 "title":"Truth or Dare Wheel – Spin for a Truth or Dare Question | Wheelova",
 "description":"Spin the Truth or Dare wheel and get a random question or dare. Kids and teen/party decks with 80 clean prompts, or add your own. Free, no sign-up.",
 "h1":"Truth or Dare Wheel","subhead":"Spin, land on Truth or Dare, and get a random prompt to answer or do.",
 "entries":["Truth","Dare","Truth","Dare","Truth","Dare"],
 "variants":[{"label":"Truth / Dare (equal)","entries":["Truth","Dare","Truth","Dare","Truth","Dare"]},{"label":"More truths","entries":["Truth","Dare","Truth","Truth","Dare","Truth"]},{"label":"More dares","entries":["Dare","Truth","Dare","Dare","Truth","Dare"]}],
 "prompts":TOD,"resultLabel":"YOU GOT","popLabel":"YOU GOT",
 "howTo":["Choose a deck: Kids or Teens & party.","Spin to land on Truth or Dare.","Read the prompt in the popup — answer the truth or do the dare, then pass to the next player."],
 "sections":[],"faq":[],"related":["yes-or-no-wheel","mystery-wheel","decision-wheel","name-picker-wheel"]
},
{
 "slug":"coin-flip","key":"coin","nav":"Coin Flip","tool":"coin",
 "title":"Flip a Coin – Free Online Coin Flip, Heads or Tails | Wheelova",
 "description":"Flip a coin online for heads or tails. Flip once or up to 100 times, see the tally and longest streak. Fair, instant and free — no sign-up.",
 "h1":"Flip a Coin","howTitle":"How to flip a coin online","subhead":"Heads or tails? Flip once, or flip many times and see the tally.",
 "howTo":["Press Flip (or the Space bar).","Choose how many flips if you want more than one.","Read the result and the running heads/tails tally."],
 "sections":[],"faq":[],"related":["yes-or-no-wheel","dice-roller","random-number-generator","decision-wheel"]
},
{
 "slug":"dice-roller","key":"dice","nav":"Dice Roller","tool":"dice",
 "title":"Dice Roller – Roll Virtual Dice Online (d4 to d20) | Wheelova",
 "description":"Roll 1 to 6 virtual dice online — d4, d6, d8, d10, d12 or d20. See each die and the total. Free dice roller for board games, D&D and class.",
 "h1":"Dice Roller","subhead":"Roll up to six dice — d4, d6, d8, d10, d12 or d20 — and see the total.",
 "howTo":["Choose how many dice and how many sides.","Press Roll (or the Space bar).","See each die and the total. Recent rolls are listed below."],
 "sections":[],"faq":[],"related":["coin-flip","spinner","random-number-generator","number-wheel"]
},
]
