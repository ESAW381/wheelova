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
  {"h2":"Is the answer really random?","body":"Yes. Wheelova picks the stopping point using your browser's built-in cryptographically secure random number generator (`crypto.getRandomValues`), not a predictable formula. Each spin is independent, so getting \"Yes\" three times in a row is normal — just like flipping heads three times."}
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
