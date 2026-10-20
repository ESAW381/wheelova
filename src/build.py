import json, re, html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES, MDN

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dist")
V = "5"
SITE = "https://wheelova.com"
BY = {p["slug"]: p for p in PAGES}
NAV = [("name-picker-wheel", "Name Picker"), ("yes-or-no-wheel", "Yes or No"), ("random-number-generator", "Number Generator"), ("random-team-generator", "Team Generator"), ("wheels", "All tools")]
POPULAR = ["yes-or-no-wheel", "name-picker-wheel", "random-number-generator", "random-team-generator", "spinner", "decision-wheel", "random-letter-generator", "color-wheel", "random-name-generator", "random-country-generator", "raffle-wheel", "lucky-wheel", "mystery-wheel", "number-wheel", "random-state-generator", "random-nfl-team-generator", "random-nba-team-generator", "random-mlb-team-generator"]
CLUSTERS = [("Decisions", ["yes-or-no-wheel", "decision-wheel", "mystery-wheel", "lucky-wheel"]), ("Names & groups", ["name-picker-wheel", "random-team-generator", "random-name-generator", "random-letter-generator"]), ("Numbers & chance", ["random-number-generator", "number-wheel", "spinner"]), ("Giveaways", ["raffle-wheel"]), ("Geography", ["random-country-generator", "random-state-generator"]), ("Sports", ["random-nfl-team-generator", "random-nba-team-generator", "random-mlb-team-generator"]), ("Colors", ["color-wheel"])]
DOTS = ["#7C6CF2", "#E2603B", "#14A37F", "#2F7BF6", "#D94F8A", "#E0A21B"]
e = html.escape

def md(s):
    s = e(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\((/[^)]*)\)", r'<a href="\2">\1</a>', s)
    out, lst = [], None
    for line in s.split("\n"):
        m1, m2 = re.match(r"^- (.*)", line), re.match(r"^\d+\. (.*)", line)
        tag = "ul" if m1 else "ol" if m2 else None
        if tag:
            if lst != tag:
                if lst: out.append(f"</{lst}>")
                out.append(f"<{tag}>"); lst = tag
            out.append(f"<li>{(m1 or m2).group(1)}</li>")
        else:
            if lst: out.append(f"</{lst}>"); lst = None
            if line.strip(): out.append(f"<p>{line}</p>")
    if lst: out.append(f"</{lst}>")
    return "\n".join(out)

def plain(s):
    return re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s).replace("**", "").replace("`", "")

def navhtml(path):
    cur = ' aria-current="page"'
    return ''.join('<a href="/%s"%s>%s</a>' % (s, cur if '/'+s==path else '', n) for s, n in NAV)

def head(title, desc, path, ld, ogtitle=None):
    url = SITE + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0A0A0C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Wheelova">
<meta property="og:title" content="{e(ogtitle or title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Inter+Tight:wght@600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script>try{{var t=localStorage.getItem("wv_theme")||(matchMedia("(prefers-color-scheme: light)").matches?"light":"dark");document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<link rel="stylesheet" href="/app.css?v={V}">
<script defer src="/_vercel/insights/script.js"></script>
</head>
<body>
<header><div class="hd">
<a class="logo" href="/"><svg width="26" height="26" viewBox="0 0 26 26" aria-hidden="true"><circle cx="13" cy="13" r="11" fill="none" stroke="#6E56F0" stroke-width="2.4"/><path d="M13 2v11l8 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>Wheelova</a>
<button class="theme" id="theme" type="button" aria-label="Switch to light mode"><svg class="moon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="sun" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
<button class="burger" id="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path class="b1" d="M4 7h16"/><path class="b2" d="M4 12h16"/><path class="b3" d="M4 17h16"/></svg></button>
<nav id="mnav" aria-label="Main">{navhtml(path)}</nav>
</div></header>
"""

POP = """
<div class="pop" id="pop" role="dialog" aria-modal="true" aria-labelledby="popwin"><div class="popc">
<div class="lbl" id="poplbl">WE HAVE A WINNER</div><div class="popswatch" id="popswatch" aria-hidden="true"></div><div class="win" id="popwin"></div><div class="pophex" id="pophex"></div>
<div class="acts"><button class="pbtn" id="popremove" type="button">Remove from wheel</button><button class="pbtn pri" id="popclose" type="button">Close</button></div>
</div></div>
"""

def footer():
    pop = "".join(f'<a href="/{s}">{e(BY[s]["nav"])}</a>' for s in POPULAR[:6])
    more = "".join(f'<a href="/{s}">{e(BY[s]["nav"])}</a>' for s in POPULAR[6:12])
    return f"""<footer><div class="ft">
<div style="flex:1 1 240px;color:var(--mu2)">© 2026 Wheelova. Free random wheel spinner.</div>
<div><span class="h">Popular wheels</span>{pop}</div>
<div><span class="h">More wheels</span>{more}<a href="/wheels">All wheels</a></div>
<div><span class="h">Wheelova</span><a href="/">Spin the Wheel</a><a href="/about">About</a><a href="/privacy">Privacy</a><a href="/terms">Terms</a></div>
</div></footer>
"""

def tool(controls="", default_label="Entries"):
    return f"""<div class="tool" id="tool">
<div class="stage">
<div class="wheelbox">
<div class="pointer" aria-hidden="true"></div>
<canvas id="wheel" width="960" height="960" role="img" aria-label="Spinning wheel"></canvas>
<button class="spinbtn" id="spin" type="button" aria-label="Spin the wheel">SPIN</button>
</div>
<div class="result" id="result" aria-live="polite"><div class="hint">Press SPIN or the Space bar</div></div>
</div>
<aside>
<div class="card">
<div class="row">
<label for="entries" style="font-weight:600;color:var(--hi)">{default_label} <span id="count" style="color:var(--mu2);font-weight:500"></span></label>
<div style="display:flex;gap:6px"><button class="btn" id="shuffle" type="button">Shuffle</button><button class="btn" id="sort" type="button">Sort</button><button class="btn" id="clear" type="button">Clear</button></div>
</div>
{controls}
<textarea id="entries" spellcheck="false" aria-describedby="entries-help"></textarea>
<p class="small" id="entries-help">One entry per line. Saved in your browser automatically.</p>
<button class="toggle" id="remove" type="button" aria-pressed="false"><span class="sw" aria-hidden="true"></span>Remove winner after each spin</button>
<button class="toggle" id="sound" type="button" aria-pressed="true"><span class="sw" aria-hidden="true"></span>Sound</button>
</div>
<div class="card">
<div style="font-weight:600;color:var(--hi)">Results <span id="rcount" style="color:var(--mu2);font-weight:500">· 0</span></div>
<ol id="history" style="margin:10px 0 0;padding-left:20px;color:var(--mu);max-height:160px;overflow:auto"></ol>
</div>
</aside>
</div>"""

def card(slug, i):
    p = BY[slug]; c = DOTS[i % len(DOTS)]
    return f'<a class="tpl" href="/{slug}"><span class="dot" style="background:conic-gradient({c} 0 25%,#2A2A36 0 50%,{c} 0 75%,#2A2A36 0)"></span><span><b>{e(p["h1"])}</b><span>{e(p["subhead"])}</span></span></a>'

def scripts(p, cfg):
    if p.get("tool"):
        g = {"type": p["tool"]}
        if p["tool"] == "team": g["sample"] = p["sample"]
        if p["tool"] == "name": g["data"] = p["data"]
        return f'<script>window.WG={json.dumps(g, ensure_ascii=False)}</script>\n<script src="/gen.js?v={V}"></script>'
    return f'<script>window.WV={json.dumps(cfg, ensure_ascii=False)}</script>\n<script src="/app.js?v={V}"></script>'

def gentool(p):
    t = p["tool"]
    if t == "number":
        ctr = """<div class="gq">""" + "".join(f'<button class="chip" type="button" data-range="{r}">{r.replace("-", "–")}</button>' for r in ["1-10", "1-20", "1-50", "1-100", "1-1000", "1-6"]) + """</div>
<div class="nrow"><label>From<input id="nmin" type="number" inputmode="numeric" value="1"></label><label>To<input id="nmax" type="number" inputmode="numeric" value="100"></label><label>How many<input id="ncount" type="number" inputmode="numeric" value="1" min="1" max="1000"></label></div>
<label class="ck"><input id="nuniq" type="checkbox" checked> No repeats</label><label class="ck"><input id="nsort" type="checkbox"> Sort results</label>"""
    elif t == "team":
        ctr = """<label for="tnames" style="font-weight:600;color:var(--hi)">Names <span id="tcount" style="color:var(--mu2);font-weight:500"></span></label>
<textarea id="tnames" spellcheck="false" style="min-height:200px"></textarea>
<div class="nrow"><label>Split by<select id="tmode" style="width:170px"><option value="teams">Number of teams</option><option value="size">People per team</option></select></label><label>Number<input id="tnum" type="number" inputmode="numeric" value="3" min="1"></label></div>"""
    else:
        ctr = """<div class="nrow"><label>Names<select id="ngender" style="width:130px"><option value="any">Any</option><option value="female">Female</option><option value="male">Male</option></select></label><label>How many<input id="ncount" type="number" inputmode="numeric" value="10" min="1" max="100"></label></div>
<label class="ck"><input id="nfull" type="checkbox" checked> Add last name</label>"""
    return f"""<div class="tool gtool" id="tool">
<div class="card gctl">{ctr}
<button class="gbtn" id="ggo" type="button">Generate</button>
<p class="err" id="gerr" role="alert"></p>
</div>
<div class="stage gres">
<div class="row" style="width:100%"><span id="gcount" style="color:var(--mu2);font-size:14px"></span><button class="btn" id="gcopy" type="button">Copy</button></div>
<div class="gout" id="gout" aria-live="polite"></div>
{'' if t == "team" else '<div style="width:100%"><div style="font-weight:600;color:var(--hi);font-size:14px">Recent</div><ol id="ghist" class="ghist"></ol></div>'}
</div>
</div>"""

def page(p):
    path = "/" + p["slug"]
    controls = ""
    if p.get("variants"):
        controls += '<div class="chips" id="variants" aria-label="Presets"></div>'
    if p.get("numberRange"):
        controls += '<div class="nrow"><label>From<input id="nmin" type="number" inputmode="numeric" value="1"></label><label>To<input id="nmax" type="number" inputmode="numeric" value="100"></label><button class="btn" id="ngo" type="button" style="height:40px">Make wheel</button></div><p class="err" id="nerr" role="alert"></p>'
    if p.get("spinnerCount"):
        opts = "".join(f'<option value="{n}"{" selected" if n==6 else ""}>{n} slices</option>' for n in range(2, 21))
        controls += f'<div class="nrow"><label>Number of slices<select id="scount" style="width:150px">{opts}</select></label></div>'
    cfg = {k: p[k] for k in ("entries", "variants", "mode", "colorMap", "removeWinner", "resultLabel", "popLabel", "key") if k in p}
    faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in p["faq"]]}
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "name": p["h1"], "url": SITE + path, "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": p["description"], "publisher": {"@type": "Organization", "name": "Wheelova", "url": SITE + "/"}},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Wheelova", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Wheels", "item": SITE + "/wheels"}, {"@type": "ListItem", "position": 3, "name": p["h1"], "item": SITE + path}]},
        faq_ld]}
    steps = "".join(f'<div><span class="n">{i+1:02d}</span><p>{md(s)[3:-4]}</p></div>' for i, s in enumerate(p["howTo"]))
    secs = "".join(f'<h2>{e(s["h2"])}</h2>\n{md(s["body"])}\n' for s in p["sections"])
    faqs = "".join(f'<details><summary>{e(f["q"])}</summary><p>{e(f["a"])}</p></details>' for f in p["faq"])
    rel = "".join(card(s, i) for i, s in enumerate(p["related"]))
    srcs = "".join(f' List source: <a href="{x["url"]}" rel="noopener">{e(x["title"])}</a>.' for x in p.get("sources", []))
    return head(p["title"], p["description"], path, ld) + f"""
<main>
<div class="wrap hero">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Wheelova</a> / <a href="/wheels">Wheels</a> / <span aria-current="page">{e(p["h1"])}</span></nav>
<h1>{e(p["h1"])}</h1>
<p class="sub1">{e(p["subhead"])}</p>
{gentool(p) if p.get("tool") else tool(controls)}
</div>

<section id="how"><div class="wrap">
<h2 style="margin-bottom:24px">How to use the {e(p["h1"].lower().replace("random ", "").replace("online ", ""))}</h2>
<div class="steps3">{steps}</div>
</div></section>

<section><div class="wrap prose">
{secs}
</div></section>

<section id="faq"><div class="wrap" style="max-width:860px">
<h2 style="margin-bottom:12px">Questions</h2>
{faqs}
</div></section>

<section><div class="wrap">
<h2 style="margin-bottom:20px">Related wheels</h2>
<div class="grid">{rel}</div>
<p class="src">Randomness: Wheelova uses the browser's <a href="{MDN["url"]}" rel="noopener">crypto.getRandomValues()</a> (MDN Web Docs).{srcs}</p>
</div></section>
</main>
{POP}
{footer()}
{scripts(p, cfg)}
</body>
</html>
"""

def hub():
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "All Wheelova wheels", "url": SITE + "/wheels", "hasPart": [{"@type": "WebPage", "name": BY[s]["h1"], "url": f"{SITE}/{s}"} for s in POPULAR]}
    cards = "".join(f'<h2 style="margin:36px 0 16px">{e(c)}</h2><div class="grid">' + "".join(card(s, i) for i, s in enumerate(ss)) + '</div>' for c, ss in CLUSTERS)
    return head("All Tools – Random Wheels & Generators | Wheelova", "Every Wheelova tool: yes or no wheel, name picker, random number and team generators, country, state and sports team wheels, and more. All free.", "/wheels", ld) + f"""
<main><div class="wrap hero">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Wheelova</a> / <span aria-current="page">Wheels</span></nav>
<h1>All wheels &amp; generators</h1>
<p class="sub1">Pick a ready-made wheel, or <a href="/">build your own on the homepage</a>.</p>
{cards}
</div></main>
{footer()}
<script>(function(){{var b=document.getElementById('burger'),n=document.getElementById('mnav');b.onclick=function(){{var o=!n.classList.contains('open');n.classList.toggle('open',o);b.setAttribute('aria-expanded',o)}};var t=document.getElementById('theme'),r=document.documentElement;t.onclick=function(){{var v=r.getAttribute('data-theme')==='light'?'dark':'light';r.setAttribute('data-theme',v);try{{localStorage.setItem('wv_theme',v)}}catch(e){{}}}}}})();</script>
</body>
</html>
"""

def home():
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    main = re.search(r"<main>[\s\S]*?</main>", src).group(0)
    ld = json.loads(re.search(r'<script type="application/ld\+json">\s*([\s\S]*?)\s*</script>', src).group(1))
    popular = "".join(card(s, i) for i, s in enumerate(POPULAR))
    main = main.replace('<section id="features">', f'<section id="popular"><div class="wrap">\n<h2>Popular wheels</h2>\n<p style="margin:0 0 28px;color:var(--mu)">Ready-made wheels with their own presets and guides.</p>\n<div class="grid">{popular}</div>\n</div></section>\n\n<section id="features">', 1)
    main = main.replace("<h2>A ready-made wheel for everything</h2>", "<h2>Quick templates</h2>")
    t = re.search(r"<title>(.*?)</title>", src).group(1)
    d = re.search(r'<meta name="description" content="(.*?)">', src).group(1)
    return head(html.unescape(t), html.unescape(d), "/", ld, "Wheelova – Spin the Wheel. Trust the result.") + main + POP + footer() + f'<script src="/app.js?v={V}"></script>\n</body>\n</html>\n'

import shutil; shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
files = {"index.html": home(), "wheels.html": hub()}
for p in PAGES:
    files[p["slug"] + ".html"] = page(p)
for name, body in files.items():
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(body)
for f in ["app.css", "app.js", "gen.js", "about.html", "privacy.html", "terms.html", "favicon.svg", "robots.txt"]:
    open(os.path.join(OUT, f), "w", encoding="utf-8").write(open(os.path.join(ROOT, f), encoding="utf-8").read())
urls = ["", "wheels"] + [p["slug"] for p in PAGES] + ["about", "privacy", "terms"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}/{u}</loc><lastmod>2026-10-21</lastmod></url>" for u in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
print("built", len(files), "pages +", len(urls), "sitemap urls")
