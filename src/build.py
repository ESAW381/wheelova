import json, re, html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES, MDN
from content_v2 import UPGRADES, AUTHOR, UPDATED
for _p in PAGES:
    if _p['slug'] in UPGRADES:
        _p.update(UPGRADES[_p['slug']]); _p['upgraded'] = True

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dist")
V = "18"
SITE = "https://wheelova.com"
BY = {p["slug"]: p for p in PAGES}
NAV = [("name-picker-wheel", "Name Picker"), ("yes-or-no-wheel", "Yes or No"), ("random-number-generator", "Number Generator"), ("random-team-generator", "Team Generator"), ("wheels", "All tools")]
POPULAR = ["yes-or-no-wheel", "name-picker-wheel", "random-number-generator", "random-team-generator", "spinner", "decision-wheel", "truth-or-dare-wheel", "coin-flip", "dice-roller", "random-letter-generator", "color-wheel", "random-name-generator", "random-country-generator", "raffle-wheel", "lucky-wheel", "mystery-wheel", "number-wheel", "random-state-generator", "random-nfl-team-generator", "random-nba-team-generator", "random-mlb-team-generator"]
CLUSTERS = [("Decisions", ["yes-or-no-wheel", "decision-wheel", "coin-flip"]), ("Games & parties", ["truth-or-dare-wheel", "dice-roller", "lucky-wheel", "mystery-wheel"]), ("Names & groups", ["name-picker-wheel", "random-team-generator", "random-name-generator", "random-letter-generator"]), ("Numbers & chance", ["random-number-generator", "number-wheel", "spinner", "dice-roller", "coin-flip"]), ("Giveaways", ["raffle-wheel"]), ("Geography", ["random-country-generator", "random-state-generator"]), ("Sports", ["random-nfl-team-generator", "random-nba-team-generator", "random-mlb-team-generator"]), ("Colors", ["color-wheel"])]
DOTS = ["#6E56F0", "#E11D48", "#F59E0B", "#16A34A", "#2563EB", "#DB2777", "#0D9488", "#EA580C"]
e = html.escape

def md(s):
    s = e(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\((/[^)]*)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\[([^\]]+)\]\(((?:https?://|mailto:)[^)]*)\)", r'<a href="\2" rel="noopener">\1</a>', s)
    out, lst, tbl = [], None, []
    def flush():
        if not tbl: return
        rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in tbl if not re.match(r"^\|?\s*-", r.strip("| ").strip() or "-") or "|" not in r]
        rows = [r for r in rows if not all(re.fullmatch(r"-+", c) for c in r)]
        h, body = rows[0], rows[1:]
        out.append('<div class="tw"><table><thead><tr>' + "".join(f"<th>{c}</th>" for c in h) + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table></div>")
        tbl.clear()
    for line in s.split("\n"):
        if line.startswith("|"):
            if lst: out.append(f"</{lst}>"); lst = None
            tbl.append(line); continue
        flush()
        if line.startswith("## "):
            if lst: out.append(f"</{lst}>"); lst = None
            out.append(f"<h2>{line[3:]}</h2>"); continue
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
    flush()
    if lst: out.append(f"</{lst}>")
    s2 = "\n".join(out)
    return re.sub(r"(?<![\w*])\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s2)

def plain(s):
    return re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s).replace("**", "").replace("`", "")

def navhtml(path):
    cur = ' aria-current="page"'
    return ''.join('<a href="/%s"%s>%s</a>' % (s, cur if '/'+s==path else '', n) for s, n in NAV)

from pages_es import ES, UI as ES_UI, JS as ES_JS, NAV_ES
ALT = {}
for _p in ES:
    _en = "/" + _p["en"] if _p["en"] else "/"
    ALT[_en] = ALT["/" + _p["slug"]] = {"en": _en, "es": "/" + _p["slug"]}
def hreflang(path):
    a = ALT.get(path)
    if not a: return ""
    u = lambda x: SITE + (x if x != "/" else "/")
    return "".join(f'\n<link rel="alternate" hreflang="{k}" href="{u(v)}">' for k, v in (("en", a["en"]), ("es", a["es"]), ("x-default", a["en"])))

def head(title, desc, path, ld, ogtitle=None):
    url = SITE + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">{hreflang(path)}
<meta name="theme-color" content="#0A0A0C">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Wheelova">
<meta property="og:title" content="{e(ogtitle or title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/icons/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Wheelova — spin the wheel, trust the result">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/icons/og-image.png">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/inter-tight.woff2" as="font" type="font/woff2" crossorigin>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script>try{{var t=localStorage.getItem("wv_theme")||(matchMedia("(prefers-color-scheme: light)").matches?"light":"dark");document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<link rel="stylesheet" href="/app.css?v={V}">
<script defer src="/_vercel/insights/script.js"></script>
</head>
<body>
<header><div class="hd">
<a class="logo" href="/"><svg width="28" height="28" viewBox="0 0 64 64" aria-hidden="true"><path d="M32 35 L32 9 A26 26 0 0 1 58 35 Z" fill="#6E56F0"/><path d="M32 35 L58 35 A26 26 0 0 1 32 61 Z" fill="#E11D48"/><path d="M32 35 L32 61 A26 26 0 0 1 6 35 Z" fill="#F59E0B"/><path d="M32 35 L6 35 A26 26 0 0 1 32 9 Z" fill="#16A34A"/><circle cx="32" cy="35" r="6.5" fill="#FFFFFF"/><path d="M25 2 H39 L32 14 Z" fill="currentColor"/></svg>Wheelova</a>
<button class="theme" id="theme" type="button" aria-label="Switch to light mode"><svg class="moon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="sun" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
<button class="burger" id="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path class="b1" d="M4 7h16"/><path class="b2" d="M4 12h16"/><path class="b3" d="M4 17h16"/></svg></button>
<nav id="mnav" aria-label="Main">{navhtml(path)}</nav>
</div></header>
"""

SHARE = """
<div class="pop" id="sharepop" role="dialog" aria-modal="true" aria-labelledby="sharettl"><div class="popc sharec">
<div class="lbl" id="sharettl">SHARE THIS WHEEL</div>
<p class="sharehelp" id="sharehelp">Anyone with this link opens the wheel with your entries. Nothing is stored on our server — the entries are inside the link.</p>
<label class="sharelbl" for="shareurl">Link</label>
<div class="sharefield"><input id="shareurl" readonly><button class="pbtn pri" id="sharecopy" type="button">Copy</button></div>
<div id="embedwrap"><label class="sharelbl" for="embedcode">Embed code — paste into your website, blog or OBS browser source</label>
<textarea id="embedcode" readonly rows="5"></textarea><button class="pbtn" id="embedcopy" type="button">Copy embed code</button></div>
<p class="sharewarn" id="sharewarn" hidden></p>
<div class="acts"><button class="pbtn" id="shareclose" type="button">Close</button></div>
</div></div>
"""

POP = """
<div class="pop" id="pop" role="dialog" aria-modal="true" aria-labelledby="popwin"><div class="popc">
<div class="lbl" id="poplbl">WE HAVE A WINNER</div><div class="popswatch" id="popswatch" aria-hidden="true"></div><div class="win" id="popwin"></div><div class="popprompt" id="popprompt"></div><div class="pophex" id="pophex"></div>
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
<button class="fsbtn" id="fsbtn" type="button" aria-label="Fullscreen" title="Fullscreen (F)"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path class="fs-in" d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/><path class="fs-out" d="M9 4v5H4M15 4v5h5M9 20v-5H4M15 20v-5h5"/></svg></button>
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
<div class="sharenote" id="sharenote" hidden><span>You opened a shared wheel.</span><button class="linkbtn" id="mylist" type="button">Back to my list</button></div>
<textarea id="entries" spellcheck="false" aria-describedby="entries-help"></textarea>
<p class="small" id="entries-help">One entry per line. Saved in your browser automatically.</p>
<button class="toggle" id="remove" type="button" aria-pressed="false"><span class="sw" aria-hidden="true"></span>Remove winner after each spin</button>
<button class="toggle" id="sound" type="button" aria-pressed="true"><span class="sw" aria-hidden="true"></span>Sound</button>
<div class="sharerow"><button class="btn" id="sharebtn" type="button"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>Share link</button><button class="btn" id="embedbtn" type="button"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5"/></svg>Embed</button></div>
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

def byline(p):
    if not p.get("upgraded"): return ""
    return f'<p class="byline">Written by <span>{e(AUTHOR["name"])}</span>, {e(AUTHOR["role"])} · Last updated <time datetime="{UPDATED}">October 21, 2026</time></p>'

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
    elif t == "coin":
        ctr = """<div class="nrow"><label>How many flips<select id="ccount" style="width:150px"><option>1</option><option>5</option><option>10</option><option>20</option><option>50</option><option>100</option></select></label></div>"""
    elif t == "dice":
        ctr = """<div class="nrow"><label>Dice<select id="dcount" style="width:110px">""" + "".join(f'<option{" selected" if n==2 else ""}>{n}</option>' for n in range(1,7)) + """</select></label><label>Sides<select id="dsides" style="width:110px">""" + "".join(f'<option value="{s}"{" selected" if s==6 else ""}>d{s}</option>' for s in (4,6,8,10,12,20)) + """</select></label></div>"""
    else:
        ctr = """<div class="nrow"><label>Names<select id="ngender" style="width:130px"><option value="any">Any</option><option value="female">Female</option><option value="male">Male</option></select></label><label>How many<input id="ncount" type="number" inputmode="numeric" value="10" min="1" max="100"></label></div>
<label class="ck"><input id="nfull" type="checkbox" checked> Add last name</label>"""
    return f"""<div class="tool gtool" id="tool">
<div class="card gctl">{ctr}
<button class="gbtn" id="ggo" type="button">{ {"coin": "Flip", "dice": "Roll"}.get(t, "Generate") }</button>
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
    if p.get("prompts"):
        controls += '<div class="nrow"><label>Deck<select id="tddeck" style="width:190px"><option value="kids">Kids</option><option value="teens">Teens &amp; party</option></select></label></div>'
    if p.get("spinnerCount"):
        opts = "".join(f'<option value="{n}"{" selected" if n==6 else ""}>{n} slices</option>' for n in range(2, 21))
        controls += f'<div class="nrow"><label>Number of slices<select id="scount" style="width:150px">{opts}</select></label></div>'
    cfg = {k: p[k] for k in ("entries", "variants", "mode", "colorMap", "removeWinner", "resultLabel", "popLabel", "key", "prompts") if k in p}
    faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in p["faq"]]}
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "name": p["h1"], "url": SITE + path, "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": p["description"], "publisher": {"@type": "Organization", "name": "Wheelova", "url": SITE + "/"}},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Wheelova", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Wheels", "item": SITE + "/wheels"}, {"@type": "ListItem", "position": 3, "name": p["h1"], "item": SITE + path}]},
        faq_ld] + ([{"@type": "WebPage", "@id": SITE + path + "#page", "url": SITE + path, "name": p["h1"], "dateModified": UPDATED, "author": {"@type": "Person", "name": AUTHOR["name"]}, "publisher": {"@type": "Organization", "name": "Wheelova", "url": SITE + "/"}}] if p.get("upgraded") else [])}
    steps = "".join(f'<div><span class="n">{i+1:02d}</span><p>{md(s)[3:-4]}</p></div>' for i, s in enumerate(p["howTo"]))
    secs = "".join(f'<h2>{e(s["h2"])}</h2>\n{md(s["body"])}\n' for s in p["sections"])
    faqs = "".join(f'<details><summary>{e(f["q"])}</summary><p>{e(f["a"])}</p></details>' for f in p["faq"])
    rel = "".join(card(s, i) for i, s in enumerate(p["related"]))
    _s = [x for x in p.get("sources", []) if x["url"] != MDN["url"]]
    srcs = (" Sources: " + "; ".join(f'<a href="{x["url"]}" rel="noopener">{e(x["title"])}</a>' for x in _s) + ".") if _s else ""
    return head(p["title"], p["description"], path, ld) + f"""
<main>
<div class="wrap hero">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Wheelova</a> / <a href="/wheels">Wheels</a> / <span aria-current="page">{e(p["h1"])}</span></nav>
<h1>{e(p["h1"])}</h1>
<p class="sub1">{e(p["subhead"])}</p>
{gentool(p) if p.get("tool") else tool(controls)}
</div>

<section id="how"><div class="wrap">
<h2 style="margin-bottom:24px">{e(p.get("howTitle") or "How to use the " + p["h1"].lower().replace("random ", "").replace("online ", ""))}</h2>
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
{byline(p)}
</div></section>
</main>
{POP}{SHARE if not p.get("tool") else ""}
{footer()}
{scripts(p, cfg)}
</body>
</html>
"""

CHROME_JS = """<script>(function(){var lg=document.querySelector('.logo');lg.addEventListener('click',function(){try{localStorage.removeItem('wv_entries_home2')}catch(e){}});var b=document.getElementById('burger'),n=document.getElementById('mnav');b.onclick=function(){var o=!n.classList.contains('open');n.classList.toggle('open',o);b.setAttribute('aria-expanded',o)};var t=document.getElementById('theme'),r=document.documentElement;t.onclick=function(){var v=r.getAttribute('data-theme')==='light'?'dark':'light';r.setAttribute('data-theme',v);try{localStorage.setItem('wv_theme',v)}catch(e){}}})();</script>"""

def simple(slug, title, desc, h1, sub, body, noindex=False):
    path = "/" + slug
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": h1, "url": SITE + path}
    h = head(title, desc, path, ld)
    if noindex:
        h = h.replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"', 1)
    return h + f"""
<main><div class="wrap hero">
<h1>{e(h1)}</h1>
<p class="sub1">{sub}</p>
</div>
<section style="padding-top:32px"><div class="wrap prose">
{md(body)}
</div></section>
</main>
{footer()}
{CHROME_JS}
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
{CHROME_JS}
</body>
</html>
"""

HOME_CFG = {"key": "home2", "entries": ["Emma", "Liam", "Olivia", "Noah", "Ava", "James", "Sophia", "Oliver", "Mia", "Lucas"],
            "palette": ["#6E56F0", "#E11D48", "#F59E0B", "#16A34A", "#2563EB", "#DB2777", "#0D9488", "#EA580C"]}

def home():
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    main = re.search(r"<main>[\s\S]*?</main>", src).group(0)
    ld = json.loads(re.search(r'<script type="application/ld\+json">\s*([\s\S]*?)\s*</script>', src).group(1))
    ld["@graph"].insert(0, {"@type": "Organization", "name": "Wheelova", "url": SITE + "/", "logo": SITE + "/icons/icon-512.png"})
    popular = "".join(card(s, i) for i, s in enumerate(POPULAR[:8]))
    main = main.replace('<section id="features">', f'<section id="popular"><div class="wrap">\n<h2>Popular wheels</h2>\n<p style="margin:0 0 28px;color:var(--mu)">Ready-made wheels with their own presets and guides.</p>\n<div class="grid">{popular}</div>\n<p style="margin-top:24px"><a class="more" href="/wheels">See all {len(PAGES)} tools →</a></p>\n</div></section>\n\n<section id="features">', 1)
    main = re.sub(r'<section id="wheels">[\s\S]*?</section>\s*', '', main, count=1)
    t = re.search(r"<title>(.*?)</title>", src).group(1)
    d = re.search(r'<meta name="description" content="(.*?)">', src).group(1)
    return head(html.unescape(t), html.unescape(d), "/", ld, "Wheelova – Spin the Wheel. Trust the result.") + main + POP + SHARE + footer() + '<script>window.WV=' + json.dumps(HOME_CFG) + '</script>\n' + f'<script src="/app.js?v={V}"></script>\n</body>\n</html>\n'

BY.update({x["slug"]: x for x in ES})

def es_page(p):
    U = ES_UI
    q = dict(p); q["upgraded"] = True
    q["howTitle"] = "Cómo usar la " + p["h1"][0].lower() + p["h1"][1:]
    path = "/" + p["slug"]
    h = page(q)
    h = h.replace("window.WV=" + json.dumps({k: q[k] for k in ("entries", "variants", "mode", "colorMap", "removeWinner", "resultLabel", "popLabel", "key", "prompts") if k in q}, ensure_ascii=False),
                  "window.WV=" + json.dumps(dict({k: q[k] for k in ("entries", "variants", "removeWinner", "resultLabel", "popLabel", "key", "palette") if k in q}, t=ES_JS), ensure_ascii=False), 1)
    nav = "".join('<a href="/%s"%s%s>%s</a>' % (sl, ' aria-current="page"' if "/" + sl == path else "", ' hreflang="en" lang="en"' if sl == "" else "", n) for sl, n in NAV_ES)
    h = re.sub(r'<nav id="mnav" aria-label="Main">[\s\S]*?</nav>', f'<nav id="mnav" aria-label="Principal">{nav}</nav>', h, count=1)
    crumbs = f'<a href="/es">Wheelova</a> / <span aria-current="page">{e(p["h1"])}</span>' if p["slug"] != "es" else '<span aria-current="page">Wheelova</span>'
    h = re.sub(r'(<nav class="crumbs" aria-label=")Breadcrumb(">)[\s\S]*?(</nav>)', lambda m: m.group(1) + "Ruta de navegación" + m.group(2) + crumbs + m.group(3), h, count=1)
    h = h.replace('"name": "Wheels", "item": "' + SITE + '/wheels"', '"name": "Ruleta aleatoria", "item": "' + SITE + '/es"')
    if p["slug"] == "es":
        h = h.replace(', {"@type": "ListItem", "position": 3, "name": "Ruleta aleatoria", "item": "' + SITE + '/es"}', '')
    h = re.sub(r'<footer>[\s\S]*?</footer>', '<footer><div class="ft"><div style="flex:1 1 240px;color:var(--mu2)">© 2026 Wheelova. Ruleta aleatoria gratis.</div><div><span class="h">Ruletas</span>' + "".join(f'<a href="/{x["slug"]}">{e(x["nav"])}</a>' for x in ES) + '</div><div><span class="h">Wheelova</span><a href="/" hreflang="en" lang="en">English</a><a href="/about">About</a><a href="/privacy">Privacy</a><a href="/terms">Terms</a></div></div></footer>', h, count=1)
    R = [('<html lang="en">', '<html lang="es">'),
         ('aria-label="Switch to light mode"', 'aria-label="' + ES_JS["tolight"] + '"'), ('aria-label="Open menu"', 'aria-label="Abrir menú"'),
         ('aria-label="Fullscreen" title="Fullscreen (F)"', 'aria-label="Pantalla completa" title="Pantalla completa (F)"'),
         ('aria-label="Spinning wheel"', 'aria-label="Ruleta"'), ('aria-label="Spin the wheel">SPIN<', 'aria-label="' + U["spin_aria"] + '">' + U["spin"] + '<'),
         ('Press SPIN or the Space bar', U["spin_hint"]), ('>Entries <span id="count"', '>' + U["entries"] + ' <span id="count"'),
         ('>Shuffle<', '>' + U["shuffle"] + '<'), ('>Sort<', '>' + U["sort"] + '<'), ('>Clear<', '>' + U["clear"] + '<'),
         ('aria-label="Presets"', 'aria-label="Ajustes rápidos"'),
         ('You opened a shared wheel.', U["shared_note"]), ('Back to my list', U["my_list"]),
         ('One entry per line. Saved in your browser automatically.', U["help"]),
         ('Remove winner after each spin', U["remove"]), ('</span>Sound<', '</span>' + U["sound"] + '<'),
         ('Share link</button>', U["share"] + '</button>'), ('Embed</button>', U["embed"] + '</button>'),
         ('>Results <span id="rcount"', '>' + U["results"] + ' <span id="rcount"'),
         ('WE HAVE A WINNER', ES_JS["pop"]), ('>Remove from wheel<', '>' + U["pop_remove"] + '<'), ('>Close<', '>' + U["close"] + '<'),
         ('SHARE THIS WHEEL', U["share_title"]),
         ('Anyone with this link opens the wheel with your entries. Nothing is stored on our server — the entries are inside the link.', U["share_help"]),
         ('for="shareurl">Link<', 'for="shareurl">' + U["link"] + '<'), ('id="sharecopy" type="button">Copy<', 'id="sharecopy" type="button">' + U["copy"] + '<'),
         ('Embed code — paste into your website, blog or OBS browser source', U["embed_label"]), ('>Copy embed code<', '>' + U["copy_embed"] + '<'),
         ('margin-bottom:12px">Questions<', 'margin-bottom:12px">' + U["faq"] + '<'), ('margin-bottom:20px">Related wheels<', 'margin-bottom:20px">' + U["related"] + '<'),
         ('Written by <span>', 'Escrito por <span>'), ('Editor, Wheelova', 'editor de Wheelova'), ('Last updated <time', 'Actualizado el <time'), ('>October 21, 2026<', '>21 de octubre de 2026<'),
         ("Wheelova – Spin the wheel, trust the result", "Wheelova – Gira la ruleta, confía en el resultado"),
         ('content="Wheelova — spin the wheel, trust the result"', 'content="Wheelova — gira la ruleta"'),
         ]
    for a, b in R:
        h = h.replace(a, b)
    h = re.sub(r'<p class="src">Randomness:.*?(?= Sources:|</p>)', '<p class="src">' + U["rand_src"], h, count=1).replace(" Sources: ", " " + U["sources"] + " ")
    h = h.replace('<meta property="og:type"', '<meta property="og:locale" content="es_ES">\n<meta property="og:type"', 1)
    return h

import shutil; shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
from static_pages import STATIC
files = {"index.html": home(), "wheels.html": hub()}
for s in STATIC:
    files[s["slug"] + ".html"] = simple(**s)
for p in PAGES:
    files[p["slug"] + ".html"] = page(p)
for p in ES:
    files[p["slug"] + ".html"] = es_page(p)
os.makedirs(os.path.join(OUT, "es"), exist_ok=True)
for name, body in files.items():
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(body)
for f in ["app.css", "app.js", "gen.js", "embed.js", "embed.html", "favicon.svg", "robots.txt", "site.webmanifest"]:
    open(os.path.join(OUT, f), "w", encoding="utf-8").write(open(os.path.join(ROOT, f), encoding="utf-8").read())
shutil.copy(os.path.join(ROOT, "favicon.ico"), OUT)
shutil.copytree(os.path.join(ROOT, "icons"), os.path.join(OUT, "icons"))
shutil.copytree(os.path.join(ROOT, "fonts"), os.path.join(OUT, "fonts"))
import hashlib, datetime
LM_PATH = os.path.join(ROOT, "src", "lastmod.json")
try: LM = json.load(open(LM_PATH))
except Exception: LM = {}
TODAY = datetime.date.today().isoformat()
urls = ["", "wheels"] + [p["slug"] for p in PAGES] + [p["slug"] for p in ES] + [s["slug"] for s in STATIC if s["slug"] != "404"]
for u in urls:
    body = files["index.html" if u == "" else u + ".html"]
    m = re.search(r"<main>[\s\S]*?</main>", body)
    hsh = hashlib.sha1((m.group(0) if m else body).encode()).hexdigest()[:12]
    if LM.get(u, {}).get("h") != hsh:
        LM[u] = {"h": hsh, "d": TODAY if u in LM else LM.get(u, {}).get("d", "2026-10-21")}
json.dump(LM, open(LM_PATH, "w"), indent=0, sort_keys=True)
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}/{u}</loc><lastmod>{LM[u]['d']}</lastmod></url>" for u in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
print("built", len(files), "pages +", len(urls), "sitemap urls")
