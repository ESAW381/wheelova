"""Tier-1 tool upgrades for pages that are not in content_v2.UPGRADES (food wheel, pair generator). Nov 27 2026."""
UPD = "2026-11-27"

def apply(pages):
    by = {p["slug"]: p for p in pages}

    f = by["food-wheel"]
    f["updated"] = UPD
    f["multiPick"] = {"title": "Plan meals for the week", "help": "Picks several meals from the current list. No repeats gives you a different meal each day.", "button": "Plan meals", "n": 7}
    f["description"] = "Can't decide what to eat? Spin the food wheel for dinner, a cuisine, lunch or dessert, or plan a week of meals at once. Add your own favourites. Free."
    f["howTo"] = ["Pick a set: dinner ideas, cuisines, lunch, dessert, or cook-or-order.", "Remove anything you don't fancy or can't make, and add your own favourites.", "Spin for tonight, or use \"Plan meals for the week\" to get several meals at once."]
    for s in f["sections"]:
        if s["h2"] == "Make it work for your household":
            s["body"] = s["body"].replace("- **Plan the week.** Turn on **Remove winner** and spin five times for Monday to Friday; nothing repeats.",
                                          "- **Plan the week.** Use **Plan meals for the week** under the results, or turn on **Remove winner** and spin once per day.")
    i = next(k for k, s in enumerate(f["sections"]) if s["h2"] == "Make it work for your household")
    f["sections"].insert(i + 1, {"h2": "Plan a week of meals in one click", "body":
        "The **Plan meals for the week** box under the results picks several meals at once. Set how many days you're planning, keep **No repeats** ticked and press **Plan meals**. Read the list from top to bottom as Monday, Tuesday and so on, and **Copy** it into your shopping-list app.\n\n"
        "Why not just spin once a day? With the 12 dinner ideas and repeats allowed, a week of daily spins has about an **89% chance** of serving the same meal twice. Even over four days the chance is about **43%**. With No repeats, you can plan as many days as there are meals on the list, so add more meals for a longer plan.\n\n"
        "- **Leave a night off.** Plan six days from **Dinner ideas** and keep the seventh for takeaway or leftovers.\n"
        "- **Your own rotation.** Save your family's favourite meals under **My saved wheels**, then plan from that list each Sunday."})
    for q in f["faq"]:
        if q["q"] == "Can I plan meals for the week?":
            q["a"] = "Yes. Use \"Plan meals for the week\" under the results to pick several meals at once with no repeats, or turn on \"Remove winner\" and spin once a day."

    p = by["random-pair-generator"]
    p["updated"] = UPD
    p["title"] = "Random Pair Generator – Random Partners & Matchups | Wheelova"
    p["description"] = "Random pair and partner generator: paste names for random partners, match two lists, or make a round-robin schedule. Handles odd numbers. Free, no sign-up."
    p["subhead"] = "Paste names to make random partners, match two lists, or build a round-robin schedule."
    p["howTo"] = ["Paste or type the names, one per line. The list is saved in your browser.", "Choose random pairs, a round-robin schedule, or Match two lists (then fill in List B).", "Press Generate. Press it again for a fresh set, then copy the result."]
    p["sections"][0]["h2"] = "Random pairs or a round-robin schedule"
    p["sections"].insert(1, {"h2": "Match two lists", "body":
        "Sometimes the two sides of a pair come from different lists: mentees and mentors, students and project topics, players and characters. Choose **Match two lists** under Make, put the first group in **List A** and the second in **List B**, then press Generate. Each name in List A gets one item from List B, and both lists are shuffled first.\n\n"
        "| Lists | What happens |\n|---|---|\n"
        "| Same length | Every item in A gets a different item in B. |\n"
        "| List B is shorter | B items are shared out as evenly as possible. With 30 students and 6 topics, each topic goes to exactly 5 students. |\n"
        "| List B is longer | Every name in A gets a different item, and the extra B items are listed as \"Not matched\". |\n\n"
        "For a gift exchange inside one group, where nobody may draw their own name, use the [Secret Santa guide](/guides/secret-santa-draw-names) instead: that needs a different method."})
    p["faq"].insert(2, {"q": "Can I pair people from two different lists?", "a": "Yes. Choose \"Match two lists\", put one group in List A and the other in List B. Each name in A gets one item from B; if B is shorter, its items are shared out as evenly as possible."})
    p["faq"].insert(3, {"q": "Can I use it as a random partner generator for class?", "a": "Yes. Paste the class list, keep \"Random pairs\" and choose \"Make one trio\" so nobody is left without a partner. Press Generate again for new partners next lesson."})
