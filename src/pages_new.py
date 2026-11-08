# New tool pages added Nov 8 2026: random word wheel, drawing prompt wheel, food wheel.
# All word lists, prompts and food lists below are written for Wheelova.
from content_v2 import S_MDN, RANDOM_NOTE

NOUNS = ["apple", "bridge", "castle", "dragon", "forest", "guitar", "island", "jacket", "kitten", "lantern", "mountain", "notebook",
         "ocean", "pencil", "rocket", "sandwich", "teacher", "umbrella", "volcano", "window", "garden", "planet", "robot", "treasure"]
VERBS = ["jump", "whisper", "build", "chase", "dance", "explore", "float", "giggle", "hide", "invent", "juggle", "kick",
         "laugh", "melt", "paint", "race", "sail", "sneeze", "throw", "wander", "climb", "shout", "swim", "wobble"]
ADJECTIVES = ["brave", "shiny", "tiny", "enormous", "fuzzy", "grumpy", "sleepy", "noisy", "sparkly", "ancient", "clumsy", "gentle",
              "frozen", "hungry", "mysterious", "soggy", "spicy", "wobbly", "curious", "silly", "smooth", "rusty", "golden", "bouncy"]
SHORT = ["cat", "dog", "sun", "hat", "map", "pig", "bed", "cup", "fox", "jam", "log", "net", "pen", "rug", "web", "zip",
         "frog", "ship", "drum", "milk", "nest", "sock", "star", "tent"]
ANIMALS = ["elephant", "penguin", "giraffe", "octopus", "kangaroo", "hedgehog", "dolphin", "owl", "tiger", "zebra", "koala", "flamingo",
           "crocodile", "panda", "squirrel", "jellyfish", "camel", "parrot", "turtle", "wolf"]

EASY_DRAW = ["a cup of tea", "a house with a red door", "a smiling sun", "a pair of boots", "a slice of pizza", "a tree in autumn",
             "a bicycle", "a cat asleep", "a lighthouse", "a cactus in a pot", "a hot-air balloon", "a snowman", "a fish bowl", "a kite", "a key"]
CHARACTERS = ["a knight who is afraid of the dark", "a robot learning to bake", "a grandmother skateboarding", "a dragon with a cold",
              "a detective dog", "a wizard who lost their hat", "a pirate on holiday", "an astronaut gardener", "a shy monster",
              "a superhero with a boring power", "a frog prince waiting for a bus", "a giant who loves tiny things"]
SCENES = ["a market at sunrise", "a city under the sea", "a treehouse village", "a rainy bus stop at night", "a picnic on the moon",
          "a library that never ends", "a train crossing a desert", "a garden on a rooftop", "a snowy cabin", "a busy kitchen", "a castle made of clouds", "a beach after a storm"]
MASHUPS = ["a cat wearing a raincoat", "a teapot shaped like a whale", "a house on the back of a turtle", "a cactus playing the violin",
           "a snail with a castle for a shell", "a cloud raining sweets", "a lion made of leaves", "an umbrella growing flowers",
           "a fish riding a bicycle", "a mountain with a door in it", "a lamp that is also a jellyfish", "a bookshelf on legs"]

DINNER = ["Pasta", "Tacos", "Pizza", "Stir-fry", "Curry", "Burgers", "Soup", "Salad bowl", "Fried rice", "Roast chicken", "Fish and chips", "Omelette"]
CUISINES = ["Italian", "Mexican", "Indian", "Chinese", "Japanese", "Thai", "Lebanese", "Greek", "Korean", "Turkish", "Vietnamese", "American"]
LUNCH = ["Sandwich", "Wrap", "Soup", "Leftovers", "Noodles", "Salad", "Baked potato", "Quesadilla", "Rice bowl", "Pasta salad"]
DESSERT = ["Ice cream", "Brownies", "Fruit salad", "Cheesecake", "Pancakes", "Apple pie", "Cookies", "Rice pudding", "Chocolate mousse", "Waffles"]
HOME_OUT = ["Cook at home", "Order takeaway", "Eat out", "Leftovers night"]

NEW_PAGES = [
{
 "slug": "random-word-wheel", "key": "words", "nav": "Random Word Wheel", "updated": "2026-11-08", "upgraded": True,
 "title": "Random Word Wheel – Random Word Generator Wheel for Games & Class | Wheelova",
 "description": "Spin the random word wheel for a noun, verb, adjective, animal or short word. Free random word generator wheel for word games, writing prompts and spelling.",
 "h1": "Random Word Wheel", "subhead": "Spin for a random word: nouns, verbs, adjectives, animals or short words, or add your own.",
 "entries": NOUNS[:12],
 "variants": [{"label": "Nouns", "entries": NOUNS}, {"label": "Verbs", "entries": VERBS}, {"label": "Adjectives", "entries": ADJECTIVES},
              {"label": "Animals", "entries": ANIMALS}, {"label": "Short words", "entries": SHORT}],
 "resultLabel": "YOUR WORD", "popLabel": "YOUR WORD IS",
 "howTo": ["Pick a word list (nouns, verbs, adjectives, animals or short words), or paste your own words, one per line.", "Press SPIN.", "Use the word, then turn on Remove winner if each word should come up only once."],
 "sections": [
  {"h2": "What is a random word wheel?", "body":
   "A random word wheel puts a list of words on a spinner and picks one at random. It is a quick way to get a word you didn't choose yourself, which is the whole point in word games, writing warm-ups and vocabulary practice.\n\n"
   "The lists here are short and kid-friendly on purpose: every word is common, easy to picture and safe for a classroom. For your own vocabulary list, spelling words or a foreign-language set, paste them in or press **Import** to load a CSV file.\n\n" + RANDOM_NOTE},
  {"h2": "The word lists", "body":
   "| List | Words | Good for |\n|---|---|---|\n"
   "| Nouns | 24 everyday things and places | Story starters, drawing games, \"describe it\" rounds |\n"
   "| Verbs | 24 action words | Charades, acting games, sentence building |\n"
   "| Adjectives | 24 describing words | Creative writing, \"silly sentence\" games |\n"
   "| Animals | 20 animals | Younger children, quick-draw, guessing games |\n"
   "| Short words | 24 three- and four-letter words | Early readers, phonics and spelling practice |\n\n"
   "Combine wheels for more variety: spin an adjective, then a noun, and you get prompts like *a soggy castle* or *a curious robot*."},
  {"h2": "Word games to play with it", "body":
   "- **Charades:** spin the verb list and act the word out without speaking.\n"
   "- **Describe it:** spin a noun and describe it without saying the word; the first person to guess spins next.\n"
   "- **One-sentence story:** spin three times (adjective, noun, verb) and build a sentence that uses all three.\n"
   "- **Quick draw:** spin an animal or a noun and give everyone 30 seconds to sketch it. For ready-made scenes, try the [Drawing Prompt Wheel](/drawing-prompt-wheel).\n"
   "- **Spelling check:** spin the short words list and ask students to write the word, then reveal it."},
  {"h2": "Using it in class", "body":
   "Paste this week's spelling or vocabulary words and turn on **Remove winner** so every word comes up once before any repeats. Save the list under **My saved wheels** to reuse it next lesson, and press **F** for fullscreen on a projector. For picking students rather than words, use the [Name Picker Wheel](/name-picker-wheel); for a single letter, use the [Random Letter Generator](/random-letter-generator)."},
  {"h2": "Odds and repeats", "body":
   "Each word is an equal slice, so with 24 words every word has a 1 in 24 chance (about 4.2%) on each spin. With Remove winner off, a word can come up twice in a row; that is normal for a random spin. Type a word twice to make it twice as likely."}
 ],
 "faq": [
  {"q": "Can I use my own words?", "a": "Yes. Delete the sample words and type or paste yours, one per line, or press Import to load a CSV or text file."},
  {"q": "How do I stop the same word coming up again?", "a": "Turn on \"Remove winner after each spin\". Each word then leaves the wheel once it is picked."},
  {"q": "Are the word lists suitable for children?", "a": "Yes. The built-in lists use common, classroom-safe words. Check any list you paste yourself before using it with a class."},
  {"q": "Can I spin for two words at once?", "a": "The wheel picks one word per spin. Spin twice, or open the wheel in two tabs with different lists, for example adjectives and nouns."},
  {"q": "Does it work in other languages?", "a": "Yes. Paste words in any language; the wheel shows whatever you type."}
 ],
 "related": ["random-letter-generator", "drawing-prompt-wheel", "name-picker-wheel", "truth-or-dare-wheel"],
 "sources": [S_MDN],
},
{
 "slug": "drawing-prompt-wheel", "key": "draw", "nav": "Drawing Prompt Wheel", "updated": "2026-11-08", "upgraded": True,
 "title": "Drawing Prompt Wheel – Random Drawing Ideas Generator | Wheelova",
 "description": "Don't know what to draw? Spin the drawing prompt wheel for a random idea: easy objects, characters, scenes or silly mash-ups. Free, no sign-up.",
 "h1": "Drawing Prompt Wheel", "subhead": "Spin for something to draw: easy objects, characters, scenes or silly mash-ups.",
 "entries": EASY_DRAW[:10],
 "variants": [{"label": "Easy objects", "entries": EASY_DRAW}, {"label": "Characters", "entries": CHARACTERS}, {"label": "Scenes", "entries": SCENES}, {"label": "Silly mash-ups", "entries": MASHUPS}],
 "resultLabel": "DRAW THIS", "popLabel": "YOUR PROMPT",
 "howTo": ["Pick a prompt set: easy objects, characters, scenes or silly mash-ups.", "Press SPIN and read your prompt.", "Draw it. Turn on Remove winner to get a different prompt each time."],
 "sections": [
  {"h2": "How the drawing prompt wheel works", "body":
   "Each prompt is one slice of the wheel. Spin, and the wheel picks one at random, so you stop deciding what to draw and start drawing. The four sets go from simple to more imaginative:\n\n"
   "| Set | Prompts | Example | Good for |\n|---|---|---|---|\n"
   "| Easy objects | 15 | a cactus in a pot | Beginners, warm-ups, younger children |\n"
   "| Characters | 12 | a robot learning to bake | Character design, cartoons |\n"
   "| Scenes | 12 | a rainy bus stop at night | Backgrounds, perspective, mood |\n"
   "| Silly mash-ups | 12 | a teapot shaped like a whale | Creative thinking, parties |\n\n"
   "All prompts were written for Wheelova and avoid characters owned by film, game or TV companies, so they are safe to use in class or share online.\n\n" + RANDOM_NOTE},
  {"h2": "Ways to practise with it", "body":
   "- **Five-minute sketch:** spin, set a timer for five minutes, draw, repeat. Speed stops you overthinking.\n"
   "- **Daily drawing habit:** one spin a day from the same set; turn on **Remove winner** so you don't repeat a prompt until the list is done.\n"
   "- **Two-spin challenge:** spin a character, then a scene, and put the character in the scene.\n"
   "- **Style switch:** draw the same prompt three ways, for example in pencil, as a cartoon and with only three colours. The [Color Wheel](/color-wheel) can pick the colours for you."},
  {"h2": "In the classroom or at a party", "body":
   "Project the wheel (press **F** for fullscreen) and let a student spin. Everyone draws the same prompt, then compares how differently they saw it. At parties, the mash-ups set works well as a drawing-and-guessing game: one person draws, the others guess the prompt."},
  {"h2": "Make your own prompt list", "body":
   "Replace the prompts with your own, one per line: topics from a lesson, words in a language you're learning, or themes for an art challenge. Save the list under **My saved wheels** to reuse it, or share it with a link so a whole group gets the same wheel."}
 ],
 "faq": [
  {"q": "What should I draw when I'm out of ideas?", "a": "Spin the wheel and draw whatever it picks. Start with the Easy objects set if you're warming up, or Silly mash-ups if you want something unusual."},
  {"q": "Are the prompts good for kids?", "a": "Yes. All built-in prompts are family-friendly. The Easy objects set suits younger children best."},
  {"q": "Can I stop prompts repeating?", "a": "Turn on \"Remove winner after each spin\" and each prompt leaves the wheel after it is picked."},
  {"q": "Can I add my own prompts?", "a": "Yes. Type or paste them, one per line, or import a CSV file."},
  {"q": "Can I use the prompts for an art challenge online?", "a": "Yes. The prompts were written for Wheelova and don't use anyone else's characters. A credit link is appreciated but not required."}
 ],
 "related": ["random-word-wheel", "color-wheel", "decision-wheel", "truth-or-dare-wheel"],
 "sources": [S_MDN],
},
{
 "slug": "food-wheel", "key": "food", "nav": "Food Wheel", "updated": "2026-11-08", "upgraded": True,
 "title": "Food Wheel – What to Eat? Spin for Dinner Ideas | Wheelova",
 "description": "Can't decide what to eat? Spin the food wheel for dinner ideas, a cuisine, lunch or dessert, or add your own favourites. Free food spinner, no sign-up.",
 "h1": "Food Wheel", "subhead": "Can't decide what to eat? Spin for dinner, a cuisine, lunch or dessert.",
 "entries": DINNER,
 "variants": [{"label": "Dinner ideas", "entries": DINNER}, {"label": "Cuisines", "entries": CUISINES}, {"label": "Lunch", "entries": LUNCH},
              {"label": "Dessert", "entries": DESSERT}, {"label": "Cook or order?", "entries": HOME_OUT}],
 "resultLabel": "LET'S EAT", "popLabel": "TONIGHT IT'S",
 "howTo": ["Pick a set: dinner ideas, cuisines, lunch, dessert, or cook-or-order.", "Remove anything you don't fancy or can't make, and add your own favourites.", "Spin, and eat what the wheel says."],
 "sections": [
  {"h2": "What to eat? Let the wheel decide", "body":
   "\"What do you want to eat?\" \"I don't mind, you choose.\" The food wheel ends that loop. Put only options you would actually be happy with on the wheel, spin, and the decision is made. Because everyone watches the same spin, nobody has to be the one who chose.\n\n" + RANDOM_NOTE},
  {"h2": "The food sets", "body":
   "| Set | What's on it | Use it when |\n|---|---|---|\n"
   "| Dinner ideas | 12 everyday meals | You're cooking and need a plan |\n"
   "| Cuisines | 12 cuisines from around the world | You're ordering or eating out |\n"
   "| Lunch | 10 quick lunches | Packing lunch or working from home |\n"
   "| Dessert | 10 desserts | Someone said \"something sweet?\" |\n"
   "| Cook or order? | Cook, takeaway, eat out, leftovers | The first decision of the evening |\n\n"
   "A good two-step routine: spin **Cook or order?** first, then spin **Dinner ideas** or **Cuisines** depending on the answer."},
  {"h2": "Make it work for your household", "body":
   "- **Edit the list first.** Remove what you can't make, can't eat or don't have in the cupboard. A wheel is only as good as its options.\n"
   "- **Save your own wheel.** Type your family's ten favourite meals and save them under **My saved wheels**, for example as \"Weeknight dinners\".\n"
   "- **Weight the favourites.** Type a meal twice to make it twice as likely.\n"
   "- **Plan the week.** Turn on **Remove winner** and spin five times for Monday to Friday; nothing repeats.\n"
   "- **Agree before you spin.** In a group, everyone accepts the result first. If you're disappointed with what comes up, that tells you what you really wanted."},
  {"h2": "When not to use it", "body":
   "The wheel picks at random, so it can't account for allergies, dietary needs or what is in the fridge. Only put foods on the wheel that are safe and suitable for everyone eating. For other everyday choices, use the [Decision Wheel](/decision-wheel); for a quick yes or no (\"dessert tonight?\"), use the [Yes or No Wheel](/yes-or-no-wheel)."}
 ],
 "faq": [
  {"q": "How do I decide what to eat?", "a": "Put three to twelve meals you'd all be happy with on the wheel and spin. If the result disappoints you, pick the one you were hoping for: the spin showed you what you wanted."},
  {"q": "Can I add my own meals and restaurants?", "a": "Yes. Delete the sample list and type your own, one per line, then save it under My saved wheels."},
  {"q": "Can I plan meals for the week?", "a": "Yes. Turn on \"Remove winner after each spin\" and spin once per day, so no meal repeats that week."},
  {"q": "Is every option equally likely?", "a": "Yes. Each option is an equal slice. Type a favourite twice to make it twice as likely."},
  {"q": "Does it know about allergies or diets?", "a": "No. It only picks from the list you give it, so remove anything that isn't suitable before you spin."}
 ],
 "related": ["decision-wheel", "yes-or-no-wheel", "lucky-wheel", "mystery-wheel"],
 "sources": [S_MDN],
},
]
