# /faq — Wheelova help & FAQ. Answers describe only what the product actually does.
FAQ_PAGE = {
 "slug": "faq",
 "title": "Wheelova FAQ – Randomness, Saving, Sharing & Embeds",
 "desc": "Answers about Wheelova: is the wheel truly random, can it be rigged, how saving and share links work, embedding in websites and OBS, and classroom use.",
 "h1": "Frequently asked questions",
 "sub": "How the wheel picks, where your entries are kept, and how to share, embed and present it.",
 "sections": [
  ("Randomness and fairness", "random", [
   ("Is the wheel truly random?",
    "Yes, in the way that matters for games, lessons and draws. Every spin uses your browser's `crypto.getRandomValues()`, which [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues) describes as a cryptographically secure pseudo-random generator seeded with system entropy. "
    "The random number decides how far the wheel turns, and the winner is whichever slice stops under the pointer. Each spin is independent of the last one. "
    "We tested this with 1,000,000 spins per wheel: see the [fairness study](/is-the-wheel-random) for the results and raw data."),
   ("Does every entry have the same chance?",
    "Yes, as long as each entry appears once. All slices are the same size, so with 8 unique entries each has a 1 in 8 (12.5%) chance. "
    "If you type the same entry twice, it gets two slices and twice the chance. That is how you weight the wheel on purpose."),
   ("Why did I get the same result twice in a row?",
    "Because each spin is independent, repeats are normal. With 2 entries, the same result comes up twice in a row half the time. With 10 entries, it happens on 1 spin in 10. "
    "If you want each entry to win only once, turn on **Remove winner after each spin**."),
   ("I spun several times and one entry came up more than the others. Is something wrong?",
    "Probably not. Over a handful of spins, uneven results are expected. Spin a 4-slice wheel 20 times and you will rarely see exactly 5 of each. "
    "The counts only even out over hundreds or thousands of spins."),
   ("Is the Shuffle button random too?",
    "Yes. Shuffle reorders your list with the Fisher–Yates method, using the same secure random source. It changes where entries sit on the wheel, not their chances: equal slices stay equal."),
   ("Can the wheel be rigged?",
    "Wheelova has no hidden setting that chooses a winner in advance, and the result is never decided by entry position or name. "
    "But whoever controls the device controls the list, so for public draws, show the full list on screen before you spin, keep duplicates out unless everyone agreed to them, and spin live or record the screen."),
  ]),
  ("Using the wheel", "use", [
   ("How do I use Wheelova?",
    "Type or paste your entries into the box, one per line, then press **Spin** or the Space bar. The winner appears in a pop-up and in the Results list. "
    "Ready-made wheels, such as the [Yes or No Wheel](/yes-or-no-wheel) or the [Name Picker Wheel](/name-picker-wheel), come with their own entries and presets."),
   ("How many entries can I add?",
    "There is no fixed limit. Text gets smaller as you add more, so up to about 50 entries reads well on a projector. Share links carry up to 1,000 entries."),
   ("Can I change how long the wheel spins?",
    "Yes. Open **Settings** under the entries box and choose Fast, Normal or Slow. Your choice is saved in your browser. If your device is set to reduce motion, the wheel stops almost instantly whatever you choose."),
   ("Can I change the text in the winner pop-up?",
    "Yes. In **Settings**, type your own heading, for example \"Today's presenter\" or \"Congratulations!\". Leave it empty to use the default."),
   ("Can I turn off the sound?",
    "Yes. Use the **Sound** switch under the entries. Custom sounds and music are not available."),
   ("Can I use more than one wheel at a time?",
    "Each wheel page keeps its own list, so you can open the [Name Picker Wheel](/name-picker-wheel) and the [Decision Wheel](/decision-wheel) in two tabs and use both. "
    "Two tabs of the same page share one saved list."),
  ]),
  ("Saving and privacy", "save", [
   ("Do I need an account?",
    "No. There is nothing to sign up for. Open the page and spin."),
   ("How is my wheel saved?",
    "Your entries save automatically in your own browser (local storage) each time you type. They are there when you come back on the same device and browser."),
   ("Can I open my wheel on another device?",
    "Not automatically, because nothing is stored on our servers. Use **Share link** to copy a link with your entries inside it, and open that link on the other device."),
   ("Why did my entries disappear?",
    "Usually because the browser's site data was cleared, or you used a private window, which forgets everything when closed. To keep a list safe, save its share link somewhere."),
   ("Is my data private?",
    "Your entries never leave your device unless you create a share link. A share link carries the entries inside it (encoded, not encrypted), so anyone with the link can read them; we never store them. "
    "The wheel and your entries are masked from our analytics tool, and it is not loaded at all on shared-wheel links. Read the [privacy policy](/privacy) for the details."),
  ]),
  ("Sharing and embedding", "share", [
   ("How do I share a wheel?",
    "Press **Share link** and copy the link. Anyone who opens it sees your wheel with the same entries, and their changes do not affect your copy. Because the entries are readable by anyone who has the link, avoid sharing lists with private information."),
   ("Why doesn't my shared link update when I change my wheel?",
    "The entries are stored inside the link itself, so a link is a snapshot. After you edit the wheel, create a new link."),
   ("Can I put the wheel on my website or blog?",
    "Yes. Press **Embed** and copy the code into your page's HTML. It shows a working wheel with your entries and a small credit link."),
   ("Can I embed the wheel in Google Sites?",
    "Yes. In Google Sites, choose **Insert → Embed → Embed code**, paste the code from Wheelova's **Embed** button, and resize the box so the whole wheel shows."),
   ("Can I use the wheel in OBS or a live stream?",
    "Yes. Press **Embed**, copy just the web address inside `src=\"…\"`, then add a **Browser** source in OBS with that address. Set the size to about 560 × 560. "
    "Click into the source with **Interact** to spin it during the stream."),
   ("Can I put the wheel in Google Slides or PowerPoint?",
    "Slides cannot run a live wheel inside the presentation. The simplest option is a link on your slide that opens the wheel, then **fullscreen mode** (press F) to present it."),
  ]),
  ("Classroom and giveaways", "class", [
   ("How can I use the wheel in class?",
    "Paste your class list into the [Name Picker Wheel](/name-picker-wheel) and leave **Remove winner** on so every student gets a turn. Press F for fullscreen on the projector. "
    "Teachers also use it for presentation order, groups (try the [Random Team Generator](/random-team-generator)) and quick quiz games."),
   ("How do I pick a winner from survey or form responses?",
    "Export the responses to a spreadsheet (Google Forms can send them to Google Sheets), copy the column of names or emails, and paste it into the [Raffle Wheel](/raffle-wheel). Remove duplicates first if each person should have one chance."),
   ("Can I use Wheelova for an official giveaway?",
    "You can use it to pick the winner fairly and visibly. Whether your giveaway is legal is a separate question: rules for prize draws differ by country and by social platform, so check them before you launch. The [Raffle Wheel](/raffle-wheel) guide covers running a fair draw."),
  ]),
  ("Devices and browsers", "devices", [
   ("Which devices and browsers work?",
    "Any recent version of Chrome, Safari, Edge or Firefox, on phones, tablets and computers. Nothing to install."),
   ("Why isn't true fullscreen available on iPhone?",
    "iPhone browsers don't let websites enter true fullscreen. On iPhone, fullscreen mode enlarges the wheel to fill the browser window instead."),
   ("Can I add Wheelova to my phone's home screen?",
    "Yes. In Safari, tap **Share → Add to Home Screen**. In Chrome on Android, open the menu and tap **Add to Home screen**. It opens like an app, but it needs an internet connection."),
  ]),
  ("About Wheelova", "about", [
   ("Is Wheelova free?",
    "Yes. Every tool is free with no sign-up and no ads at the moment. If that changes, the [privacy policy](/privacy) will be updated first."),
   ("Who makes Wheelova?",
    "Wheelova is an independent site. Guides are written and reviewed by Sajid Ali, Editor. Read more on the [About page](/about)."),
   ("How do I report a problem or suggest a feature?",
    "Email [support@wheelova.com](mailto:support@wheelova.com). Corrections to our guides are welcome too."),
  ]),
 ],
}
