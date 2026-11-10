from data import COUNTRIES
import json, re, html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES, MDN
from pages_new import NEW_PAGES
PAGES += NEW_PAGES
# Phase 2 (Nov 10 2026): contextual Related blocks. names <-> teams <-> raffle; number <-> decision <-> yes/no.
for _slug, _rel in {
    "name-picker-wheel": ["random-team-generator", "raffle-wheel", "random-number-generator", "decision-wheel"],
    "random-team-generator": ["name-picker-wheel", "raffle-wheel", "random-number-generator", "decision-wheel"],
    "raffle-wheel": ["name-picker-wheel", "random-team-generator", "lucky-wheel", "random-number-generator"],
    "random-number-generator": ["decision-wheel", "yes-or-no-wheel", "number-wheel", "name-picker-wheel"],
    "decision-wheel": ["yes-or-no-wheel", "random-number-generator", "lucky-wheel", "food-wheel"],
    "yes-or-no-wheel": ["decision-wheel", "random-number-generator", "coin-flip", "lucky-wheel"],
    "lucky-wheel": ["raffle-wheel", "decision-wheel", "yes-or-no-wheel", "name-picker-wheel"],
}.items():
    next(x for x in PAGES if x["slug"] == _slug)["related"] = _rel
for _slug, _new in (("decision-wheel", "food-wheel"), ("random-letter-generator", "random-word-wheel"), ("color-wheel", "drawing-prompt-wheel")):
    _pg = next(x for x in PAGES if x["slug"] == _slug); _pg["related"] = [_new] + [r for r in _pg["related"] if r != _new][:3]
from content_v2 import UPGRADES, AUTHOR, UPDATED
for _p in PAGES:
    if _p['slug'] in UPGRADES:
        _p.update(UPGRADES[_p['slug']]); _p['upgraded'] = True

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dist")
V = "38"
SITE = "https://wheelova.com"
BY = {p["slug"]: p for p in PAGES}
NAV = [("name-picker-wheel", "Name Picker"), ("yes-or-no-wheel", "Yes or No"), ("random-number-generator", "Number Generator"), ("random-team-generator", "Team Generator"), ("wheels", "All tools")]
CORE = ["name-picker-wheel", "yes-or-no-wheel", "random-number-generator", "random-team-generator", "decision-wheel", "raffle-wheel", "lucky-wheel"]
POPULAR = ["yes-or-no-wheel", "name-picker-wheel", "random-number-generator", "random-team-generator", "spinner", "decision-wheel", "truth-or-dare-wheel", "coin-flip", "dice-roller", "random-letter-generator", "color-wheel", "random-name-generator", "random-country-generator", "raffle-wheel", "lucky-wheel", "mystery-wheel", "number-wheel", "random-state-generator", "random-nfl-team-generator", "random-nba-team-generator", "random-mlb-team-generator", "flag-quiz", "random-pair-generator"]
CLUSTERS = [("Decisions", ["yes-or-no-wheel", "decision-wheel", "food-wheel", "coin-flip"]), ("Games & parties", ["truth-or-dare-wheel", "dice-roller", "lucky-wheel", "mystery-wheel"]), ("Names & groups", ["name-picker-wheel", "random-team-generator", "random-pair-generator", "random-name-generator", "random-letter-generator"]), ("Numbers & chance", ["random-number-generator", "number-wheel", "spinner", "dice-roller", "coin-flip"]), ("Giveaways", ["raffle-wheel"]), ("Geography", ["random-country-generator", "flag-quiz", "random-state-generator"]), ("Sports", ["random-nfl-team-generator", "random-nba-team-generator", "random-mlb-team-generator"]), ("Words & creativity", ["random-word-wheel", "drawing-prompt-wheel", "random-letter-generator"]), ("Colors", ["color-wheel"])]
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
        if line.startswith("&gt;"):
            if lst and lst != "blockquote": out.append(f"</{lst}>"); lst = None
            if lst != "blockquote": out.append('<blockquote class="quote">'); lst = "blockquote"
            t = line[4:].strip()
            if t: out.append(f"<p>{t}</p>")
            continue
        m1, m2 = re.match(r"^- (.*)", line), re.match(r"^(\d+)\. (.*)", line)
        tag = "ul" if m1 else "ol" if m2 else None
        if tag:
            if lst != tag:
                if lst: out.append(f"</{lst}>")
                st = int(m2.group(1)) if m2 else 1
                out.append(f'<{tag} start="{st}">' if tag == "ol" and st != 1 else f"<{tag}>"); lst = tag
            out.append(f"<li>{m1.group(1) if m1 else m2.group(2)}</li>")
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
from pages_fr import FR, JS as FR_JS, NAV_FR
from pages_vi import VI, JS as VI_JS, NAV_VI, R as VI_R
ALT = {}
for _lang, _list in (("es", ES), ("fr", FR), ("vi", VI)):
    for _p in _list:
        _en = "/" + _p["en"] if _p["en"] else "/"
        grp = ALT.get(_en) or {"en": _en}
        grp[_lang] = "/" + _p["slug"]
        for _k in grp.values(): ALT[_k] = grp
def hreflang(path):
    a = ALT.get(path)
    if not a: return ""
    u = lambda x: SITE + (x if x != "/" else "/")
    return "".join(f'\n<link rel="alternate" hreflang="{k}" href="{u(v)}">' for k, v in [(l, a[l]) for l in ("en", "es", "fr", "vi") if l in a] + [("x-default", a["en"])])

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
<script src="/consent.js?v={V}" defer></script>
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
<div class="pop" id="sharepop" data-clarity-mask="true" role="dialog" aria-modal="true" aria-labelledby="sharettl"><div class="popc sharec">
<div class="lbl" id="sharettl">SHARE THIS WHEEL</div>
<p class="sharehelp" id="sharehelp">Anyone with this link can see your entries: they are encoded inside the link (not encrypted). Nothing is stored on our server, but the link stays in browser history and wherever you paste it, so avoid sharing private lists.</p>
<label class="sharelbl" for="shareurl">Link</label>
<div class="sharefield"><input id="shareurl" readonly><button class="pbtn pri" id="sharecopy" type="button">Copy</button></div>
<div id="embedwrap"><label class="sharelbl" for="embedcode">Embed code — paste into your website, blog or OBS browser source</label>
<textarea id="embedcode" readonly rows="5"></textarea><button class="pbtn" id="embedcopy" type="button">Copy embed code</button><p class="ekeep">Keep the credit link so others can find the wheel.</p></div>
<p class="sharewarn" id="sharewarn" hidden></p>
<div class="acts"><button class="pbtn" id="shareclose" type="button">Close</button></div>
</div></div>
"""

POP = """
<div class="pop" id="pop" data-clarity-mask="true" role="dialog" aria-modal="true" aria-labelledby="popwin"><div class="popc">
<div class="lbl" id="poplbl">WE HAVE A WINNER</div><div class="popswatch" id="popswatch" aria-hidden="true"></div><img class="popflag" id="popflag" hidden alt="" width="96" height="72"><div class="win" id="popwin"></div><div class="popprompt" id="popprompt"></div><div class="pophex" id="pophex"></div>
<div class="acts"><button class="pbtn" id="popremove" type="button">Remove from wheel</button><button class="pbtn pri" id="popclose" type="button">Close</button></div>
</div></div>
"""

LOGO_SVG = '''<svg width="28" height="28" viewBox="0 0 64 64" aria-hidden="true"><path d="M32 35 L32 9 A26 26 0 0 1 58 35 Z" fill="#6E56F0"/><path d="M32 35 L58 35 A26 26 0 0 1 32 61 Z" fill="#E11D48"/><path d="M32 35 L32 61 A26 26 0 0 1 6 35 Z" fill="#F59E0B"/><path d="M32 35 L6 35 A26 26 0 0 1 32 9 Z" fill="#16A34A"/><circle cx="32" cy="35" r="6.5" fill="#FFFFFF"/><path d="M25 2 H39 L32 14 Z" fill="currentColor"/></svg>'''
def fbrand(home, tag, copy):
    return f'<div class="fbrand"><a class="flogo" href="{home}">{LOGO_SVG}Wheelova</a><p class="ftag">{tag}</p><p class="fcopy">{copy}</p></div>'

def footer():
    pop = "".join(f'<a href="/{s}">{e(BY[s]["nav"])}</a>' for s in CORE)
    more = "".join(f'<a href="/{s}">{e(BY[s]["nav"])}</a>' for s in [x["slug"] for x in PAGES if x["slug"] not in CORE])
    return f"""<footer><div class="ft">
{fbrand("/", "Spin the wheel. Trust the result.", "© 2026 Wheelova. Free random wheel spinner.")}
<div><span class="h">Popular tools</span>{pop}<a href="/wheels">All tools</a></div>
<div class="fmore"><span class="h">More tools</span>{more}</div>
<div><span class="h">Wheelova</span><a href="/">Spin the Wheel</a><a href="/faq">FAQ</a><a href="/guides">Guides</a><a href="/embed-a-wheel">Embed a wheel</a><a href="/is-the-wheel-random">Fairness study</a><a href="/about">About</a><a href="/privacy">Privacy</a><a href="/terms">Terms</a><a href="#cookies" data-wvcookies>Cookie settings</a></div>
<div><span class="h">Languages</span><a href="/es" hreflang="es" lang="es">Español</a><a href="/fr" hreflang="fr" lang="fr">Français</a><a href="/vi" hreflang="vi" lang="vi">Tiếng Việt</a></div>
</div></footer>
"""

def tool(controls="", default_label="Entries"):
    return f"""<div class="tool" id="tool" data-clarity-mask="true">
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
<div class="row enthead">
<label for="entries" class="entttl" style="font-weight:600;color:var(--hi)">{default_label} <span id="count" style="color:var(--mu2);font-weight:500"></span></label>
<div class="entacts"><button class="btn" id="shuffle" type="button">Shuffle</button><button class="btn" id="sort" type="button">Sort</button><button class="btn" id="clear" type="button">Clear</button><button class="btn" id="impbtn" type="button">Import</button><input type="file" id="impfile" accept=".csv,.tsv,.txt,text/csv,text/plain" hidden></div>
</div>
{controls}
<div class="sharenote" id="sharenote" hidden><span>You're viewing a shared wheel. Your own saved list is untouched.</span><span class="snacts"><button class="linkbtn" id="savesh" type="button">Keep this as my list</button><button class="linkbtn" id="mylist" type="button">Back to my list</button></span></div>
<div class="impcol" id="impcol" hidden><label>Column<select id="impsel"></select></label><label class="ck"><input type="checkbox" id="imphdr" checked> First row is a header</label><button class="btn" id="impok" type="button">Use column</button><button class="linkbtn" id="impno" type="button">Cancel</button></div><textarea id="entries" spellcheck="false" aria-describedby="entries-help"></textarea>
<p class="small" id="entries-help">One entry per line. Saved in your browser automatically.</p>
<button class="toggle" id="remove" type="button" aria-pressed="false"><span class="sw" aria-hidden="true"></span>Remove winner after each spin</button>
<button class="toggle" id="sound" type="button" aria-pressed="true"><span class="sw" aria-hidden="true"></span>Sound</button>
<details class="wset"><summary>Settings</summary><div class="wsetb"><label>Spin speed<select id="wspeed"><option value="fast">Fast</option><option value="normal">Normal</option><option value="slow">Slow</option></select></label><label>Wheel colors<select id="wcolors"><option value="default">Wheelova</option><option value="pastel">Pastel</option><option value="ocean">Ocean</option><option value="sunset">Sunset</option><option value="forest">Forest</option><option value="mono">Grayscale</option><option value="safe">Color-blind friendly</option><option value="custom">Custom…</option></select></label><div class="wcust" id="wcust" hidden><input type="color" aria-label="Color 1"><input type="color" aria-label="Color 2"><input type="color" aria-label="Color 3"><input type="color" aria-label="Color 4"><input type="color" aria-label="Color 5"><input type="color" aria-label="Color 6"></div><label>Winner pop-up heading<input id="wmsg" maxlength="60" placeholder="WE HAVE A WINNER"></label><label class="ck"><input id="wspeak" type="checkbox"> Read the result aloud</label></div></details>
<div class="sharerow"><button class="btn" id="sharebtn" type="button"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>Share link</button><button class="btn" id="embedbtn" type="button"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5"/></svg>Embed</button></div>
<details class="wset" id="wsaves"><summary>My saved wheels</summary><div class="wsetb"><div class="wsrow"><input id="wsname" maxlength="40" placeholder="Name, e.g. Period 3" aria-label="Name for this wheel"><button class="btn" id="wssave" type="button">Save list</button></div><ul class="wslist" id="wslist"></ul><p class="small" id="wsempty">Save this list under a name to switch between classes or groups. Stored only in this browser.</p></div></details>
</div>
<div class="card">
<div class="row"><div style="font-weight:600;color:var(--hi)">Results <span id="rcount" style="color:var(--mu2);font-weight:500">· 0</span></div><div class="resacts" id="resacts" hidden><button class="btn" id="rcopy" type="button">Copy</button><button class="btn" id="rcsv" type="button">CSV</button></div></div>
<ol id="history" style="margin:10px 0 0;padding-left:20px;color:var(--mu);max-height:160px;overflow:auto"></ol>
</div>
</aside>
<div class="wtoast" id="wtoast" role="status" aria-live="polite" hidden><span id="wtmsg"></span><button class="linkbtn" id="wtundo" type="button">Undo</button></div>
</div>"""

def embed_line(p):
    """English wheel pages only: a plain link to the embed generator under Related tools."""
    if lang_of(p["slug"]) != "en" or p.get("tool"):
        return ""
    return '<p class="embedline">Want this wheel on your own site, blog or stream? <a href="/embed-a-wheel">Embed a wheel</a> in a minute, free.</p>\n'

def card(slug, i):
    p = BY[slug]; c = DOTS[i % len(DOTS)]
    return f'<a class="tpl" href="/{slug}"><span class="dot" style="background:conic-gradient({c} 0 25%,#2A2A36 0 50%,{c} 0 75%,#2A2A36 0)"></span><span><b>{e(p["h1"])}</b><span>{e(p["subhead"])}</span></span></a>'

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def endate(d): y, m, dd = map(int, d.split("-")); return f"{MONTHS[m-1]} {dd}, {y}"
def byline(p):
    if not p.get("upgraded"): return ""
    d = p.get("updated", UPDATED)
    return f'<p class="byline">Written by <span>{e(AUTHOR["name"])}</span>, {e(AUTHOR["role"])} · Last updated <time datetime="{d}">{endate(d)}</time></p>'

# Embed credit link: plain <a> outside the iframe in the copied snippet, pointing at the tool the wheel came from.
EMBED_ANCHOR = {
 "": "Spin the wheel", "name-picker-wheel": "Random name picker", "yes-or-no-wheel": "Yes or no wheel", "number-wheel": "Random number wheel",
 "color-wheel": "Random color wheel", "spinner": "Online spinner", "decision-wheel": "Decision wheel", "raffle-wheel": "Raffle wheel",
 "lucky-wheel": "Lucky prize wheel", "mystery-wheel": "Mystery wheel", "random-letter-generator": "Random letter wheel",
 "random-country-generator": "Random country wheel", "random-state-generator": "Random US state wheel",
 "random-nfl-team-generator": "Random NFL team wheel", "random-nba-team-generator": "Random NBA team wheel", "random-mlb-team-generator": "Random MLB team wheel",
 "truth-or-dare-wheel": "Truth or dare wheel", "random-word-wheel": "Random word wheel", "drawing-prompt-wheel": "Drawing prompt wheel", "food-wheel": "Food wheel",
 "es": "Ruleta aleatoria", "es/ruleta-de-nombres": "Ruleta de nombres", "es/ruleta-si-o-no": "Ruleta sí o no", "es/ruleta-de-sorteo": "Ruleta de sorteo",
 "es/ruleta-de-decisiones": "Ruleta de decisiones", "es/ruleta-de-colores": "Ruleta de colores", "es/ruleta-de-numeros": "Ruleta de números",
 "fr": "Roue aléatoire", "vi": "Vòng quay may mắn",
}
EMBED_BY = {"en": "by Wheelova", "es": "de Wheelova", "fr": "par Wheelova", "vi": "của Wheelova"}
EMBED_KEEP = {"en": "Keep the credit link so others can find the wheel.", "es": "Mantén el enlace de crédito para que otros puedan encontrar la ruleta.",
              "fr": "Gardez le lien de crédit pour que d'autres puissent trouver la roue.", "vi": "Hãy giữ liên kết ghi công để người khác cũng tìm được vòng quay."}
def lang_of(slug): return "es" if slug == "es" or slug.startswith("es/") else "fr" if slug == "fr" else "vi" if slug == "vi" else "en"
def embed_meta(slug):
    l = lang_of(slug)
    return '<script>window.WVA=' + json.dumps({"a": EMBED_ANCHOR.get(slug, EMBED_ANCHOR[""]), "p": "/" + slug, "by": EMBED_BY[l]}, ensure_ascii=False) + '</script>\n'

def scripts(p, cfg):
    if p.get("tool") == "flagquiz":
        iso = json.load(open(os.path.join(ROOT, "src", "country_iso.json"), encoding="utf-8"))
        return f'<script>window.WQ={json.dumps({"regions": COUNTRIES, "iso": iso}, ensure_ascii=False)}</script>\n<script src="/rng.js?v={V}" defer></script>\n<script src="/quiz.js?v={V}" defer></script>'
    if p.get("tool"):
        g = {"type": p["tool"]}
        if p["tool"] in ("team", "pair"): g["sample"] = p["sample"]
        if p["tool"] == "name": g["data"] = p["data"]
        return f'<script>window.WG={json.dumps(g, ensure_ascii=False)}</script>\n<script src="/rng.js?v={V}" defer></script>\n<script src="/gen.js?v={V}" defer></script>'
    return embed_meta(p["slug"]) + f'<script>window.WV={json.dumps(cfg, ensure_ascii=False)}</script>\n<script src="/rng.js?v={V}" defer></script>\n<script src="/app.js?v={V}" defer></script>'

def gentool(p):
    t = p["tool"]
    if t == "flagquiz":
        regs = "".join(f'<option value="{r}">{r} ({len(v)})</option>' for r, v in COUNTRIES.items())
        return f"""<div class="tool qtool" id="tool">
<div class="card qsetup"><div class="nrow"><label>Region<select id="qregion" style="width:190px"><option value="all">All countries (193)</option>{regs}</select></label><label>Flags<select id="qcount" style="width:140px"><option value="10">10 flags</option><option value="20">20 flags</option><option value="50">50 flags</option><option value="all">All in region</option></select></label></div>
<button class="gbtn" id="qstart" type="button">Start quiz</button></div>
<div class="stage qstage">
<div id="qplay" hidden>
<div class="qtop"><span id="qprog"></span><span>Score <b id="qscore">0</b> · Streak <b id="qstreak">0</b></span></div>
<div class="qflagbox"><img id="qflag" alt="" width="320" height="240"></div>
<div class="qopts" id="qopts"></div>
<p class="qfb" id="qfeedback" aria-live="polite"></p>
<button class="gbtn" id="qnext" type="button" hidden>Next flag</button>
</div>
<div id="qresult" hidden><div class="lbl">YOUR SCORE</div><div class="qbig" id="rscore"></div><p class="qsub"><span id="rpct"></span> correct · best streak <span id="rstreak"></span> · <span id="rbest"></span></p>
<div class="qacts"><button class="gbtn" id="qagain" type="button">Play again</button><button class="btn" id="qretry" type="button">Retry missed flags</button></div>
<div id="rmissedwrap"><div style="font-weight:600;color:var(--hi);margin:18px 0 8px">Flags you missed</div><ul class="qmissed" id="rmissed"></ul></div></div>
<div class="qintro" id="qintro"><div class="qflagbox"><img src="/flags/un.svg" alt="" width="320" height="240" onerror="this.style.display='none'"></div><p>Choose a region and press <b>Start quiz</b>.</p></div>
</div>
</div>"""
    if t == "number":
        ctr = """<div class="gq">""" + "".join(f'<button class="chip" type="button" data-range="{r}">{r.replace("-", "–")}</button>' for r in ["1-10", "1-20", "1-50", "1-100", "1-1000", "1-6"]) + """</div>
<div class="nrow"><label>From<input id="nmin" type="number" inputmode="numeric" value="1"></label><label>To<input id="nmax" type="number" inputmode="numeric" value="100"></label><label>How many<input id="ncount" type="number" inputmode="numeric" value="1" min="1" max="1000"></label></div>
<label class="ck"><input id="nuniq" type="checkbox" checked> No repeats</label><label class="ck"><input id="nsort" type="checkbox"> Sort results</label>"""
    elif t == "team":
        ctr = """<label for="tnames" style="font-weight:600;color:var(--hi)">Names <span id="tcount" style="color:var(--mu2);font-weight:500"></span></label>
<textarea id="tnames" spellcheck="false" style="min-height:200px"></textarea>
<div class="nrow"><label>Split by<select id="tmode" style="width:170px"><option value="teams">Number of teams</option><option value="size">People per team</option></select></label><label>Number<input id="tnum" type="number" inputmode="numeric" value="3" min="1"></label></div>"""
    elif t == "pair":
        ctr = """<label for="pnames" style="font-weight:600;color:var(--hi)">Names <span id="pcount" style="color:var(--mu2);font-weight:500"></span></label>
<textarea id="pnames" spellcheck="false" style="min-height:200px"></textarea>
<div class="nrow"><label>Make<select id="pmode" style="width:200px"><option value="pairs">Random pairs</option><option value="rr">Round-robin schedule</option></select></label><label>Odd number<select id="podd" style="width:170px"><option value="trio">Make one trio</option><option value="bye">One sits out</option></select></label></div>"""
    elif t == "coin":
        ctr = """<div class="nrow"><label>How many flips<select id="ccount" style="width:150px"><option>1</option><option>5</option><option>10</option><option>20</option><option>50</option><option>100</option></select></label></div>"""
    elif t == "dice":
        ctr = """<div class="nrow"><label>Dice<select id="dcount" style="width:110px">""" + "".join(f'<option{" selected" if n==2 else ""}>{n}</option>' for n in range(1,7)) + """</select></label><label>Sides<select id="dsides" style="width:110px">""" + "".join(f'<option value="{s}"{" selected" if s==6 else ""}>d{s}</option>' for s in (4,6,8,10,12,20)) + """</select></label></div>"""
    else:
        ctr = """<div class="nrow"><label>Names<select id="ngender" style="width:130px"><option value="any">Any</option><option value="female">Female</option><option value="male">Male</option></select></label><label>How many<input id="ncount" type="number" inputmode="numeric" value="10" min="1" max="100"></label></div>
<label class="ck"><input id="nfull" type="checkbox" checked> Add last name</label>"""
    return f"""<div class="tool gtool" id="tool" data-clarity-mask="true">
<div class="card gctl">{ctr}
<button class="gbtn" id="ggo" type="button">{ {"coin": "Flip", "dice": "Roll"}.get(t, "Generate") }</button>
<p class="err" id="gerr" role="alert"></p>
</div>
<div class="stage gres">
<div class="row" style="width:100%"><span id="gcount" style="color:var(--mu2);font-size:14px"></span><button class="btn" id="gcopy" type="button">Copy</button></div>
<div class="gout" id="gout" aria-live="polite"></div>
{'' if t in ("team",) else '<div style="width:100%"><div style="font-weight:600;color:var(--hi);font-size:14px">Recent</div><ol id="ghist" class="ghist"></ol></div>'}
</div>
</div>"""

MULTI_TXT = {
 "en": dict(fs="Fullscreen", exitfs="Exit fullscreen", add="+ Add wheel", region="Multiple wheels", tabs="Wheels", name="Wheel name", entries="Entries", rem="Remove winner after each spin", all="Spin all wheels", delw="Remove this wheel",
            hint="Click a wheel to spin just that one, or press Space to spin all. Saved only in this browser.", res="Results", copy="Copy", clear="Clear"),
 "es": dict(fs="Pantalla completa", exitfs="Salir de pantalla completa", add="+ Añadir ruleta", region="Varias ruletas", tabs="Ruletas", name="Nombre de la ruleta", entries="Opciones", rem="Quitar al ganador después de cada giro", all="Girar todas las ruletas", delw="Quitar esta ruleta",
            hint="Haz clic en una ruleta para girar solo esa, o pulsa la barra espaciadora para girar todas. Se guarda solo en este navegador.", res="Resultados", copy="Copiar", clear="Borrar"),
 "fr": dict(fs="Plein écran", exitfs="Quitter le plein écran", add="+ Ajouter une roue", region="Plusieurs roues", tabs="Roues", name="Nom de la roue", entries="Choix", rem="Retirer le gagnant après chaque tour", all="Faire tourner toutes les roues", delw="Supprimer cette roue",
            hint="Cliquez sur une roue pour ne faire tourner qu'elle, ou appuyez sur Espace pour toutes les faire tourner. Enregistré uniquement dans ce navigateur.", res="Résultats", copy="Copier", clear="Effacer"),
 "vi": dict(fs="Toàn màn hình", exitfs="Thoát toàn màn hình", add="+ Thêm vòng quay", region="Nhiều vòng quay", tabs="Các vòng quay", name="Tên vòng quay", entries="Lựa chọn", rem="Loại kết quả sau mỗi lượt quay", all="Quay tất cả", delw="Xóa vòng quay này",
            hint="Bấm vào một vòng quay để chỉ quay vòng đó, hoặc nhấn phím cách để quay tất cả. Chỉ lưu trong trình duyệt này.", res="Kết quả", copy="Sao chép", clear="Xóa"),
}
MULTI_PAGES = {"name-picker-wheel": "en", "es": "es", "fr": "fr", "vi": "vi"}
HELP_P = '<p class="small" id="entries-help">One entry per line. Saved in your browser automatically.</p>'

def multi_section(lang):
    M = MULTI_TXT[lang]
    return ('<section id="multi" class="multi" hidden data-clarity-mask="true" aria-label="' + M["region"] + '">'
            '<div class="mfsbar"><button type="button" class="btn mallbtn mfsall" id="mfsall">' + M["all"] + '</button>'
            '<button type="button" class="fsbtn mfsbtn" id="mfs" aria-label="' + M["fs"] + '" title="' + M["fs"] + ' (F)"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path class="fs-in" d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/><path class="fs-out" d="M9 4v5H4M15 4v5h5M9 20v-5H4M15 20v-5h5"/></svg></button></div>'
            '<div class="mlayout">'
            '<div class="mgrid" id="mgrid"></div>'
            '<div class="card mpanel">'
            '<div class="mtabs" id="mtabs" role="tablist" aria-label="' + M["tabs"] + '"></div>'
            '<label class="mtl">' + M["name"] + '<input id="mtitle" maxlength="40"></label>'
            '<label for="mta" class="mtl">' + M["entries"] + ' <span id="mcnt" class="mcnt"></span></label>'
            '<textarea id="mta" rows="8" spellcheck="false"></textarea>'
            '<label class="ck"><input type="checkbox" id="mrem"> ' + M["rem"] + '</label>'
            '<button type="button" class="btn mallbtn" id="mall">' + M["all"] + '</button>'
            '<div class="mrow"><button type="button" class="btn" id="madd">' + M["add"] + '</button><button type="button" class="linkbtn" id="mdel">' + M["delw"] + '</button></div>'
            '<p class="small">' + M["hint"] + '</p>'
            '<div class="mlogwrap" id="mlogwrap" hidden><div class="mloghead"><b>' + M["res"] + '</b><span><button type="button" class="linkbtn" id="mcopy">' + M["copy"] + '</button> <button type="button" class="linkbtn" id="mclear">' + M["clear"] + '</button></span></div><ol class="mlog" id="mlog"></ol></div>'
            '</div></div></section>\n<script src="/multi.js?v=' + V + '" defer></script>')

def add_wheel_btn(html_, lang):
    return html_.replace(HELP_P, HELP_P + '<button type="button" class="btn addwheel" id="npadd">' + MULTI_TXT[lang]["add"] + '</button>', 1)

def multi_wrap(p, toolhtml):
    """'+ Add wheel' under the entries box turns the page into 2-6 wheels side by side (multi.js). Name Picker + language homepages."""
    lang = MULTI_PAGES.get(p["slug"])
    if not lang:
        return toolhtml
    return '<div id="npone">' + add_wheel_btn(toolhtml, lang) + '</div>\n' + multi_section(lang)

def page(p):
    path = "/" + p["slug"]
    controls = ""
    if p.get("variants"):
        controls += '<div class="chips" id="variants" aria-label="Presets"></div>'
    if p.get("numberRange"):
        controls += '<div class="nrow"><label>From<input id="nmin" type="number" inputmode="numeric" value="1"></label><label>To<input id="nmax" type="number" inputmode="numeric" value="100"></label><button class="btn" id="ngo" type="button" style="height:40px">Make wheel</button></div><p class="err" id="nerr" role="alert"></p>'
    if p.get("prompts"):
        controls += '<div class="nrow"><label>Deck<select id="tddeck" style="width:190px"><option value="kids">Kids</option><option value="teens">Teens &amp; party</option></select></label></div>'
    if p.get("flags"):
        controls += '<div class="nrow"><label>Show<select id="wflag" style="width:170px"><option value="both">Flag &amp; name</option><option value="name">Name only</option><option value="flag">Flag only</option></select></label></div>'
    if p.get("spinnerCount"):
        opts = "".join(f'<option value="{n}"{" selected" if n==6 else ""}>{n} slices</option>' for n in range(2, 21))
        controls += f'<div class="nrow"><label>Number of slices<select id="scount" style="width:150px">{opts}</select></label></div>'
    cfg = {k: p[k] for k in ("entries", "variants", "mode", "colorMap", "removeWinner", "resultLabel", "popLabel", "key", "prompts", "flags") if k in p}
    faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in p["faq"]]}
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "name": p["h1"], "url": SITE + path, "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": p["description"], "publisher": {"@type": "Organization", "name": "Wheelova", "url": SITE + "/"}},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Wheelova", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Wheels", "item": SITE + "/wheels"}, {"@type": "ListItem", "position": 3, "name": p["h1"], "item": SITE + path}]},
        faq_ld] + ([{"@type": "WebPage", "@id": SITE + path + "#page", "url": SITE + path, "name": p["h1"], "dateModified": p.get("updated", UPDATED), "author": {"@type": "Person", "name": AUTHOR["name"]}, "publisher": {"@type": "Organization", "name": "Wheelova", "url": SITE + "/"}}] if p.get("upgraded") else [])}
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
{multi_wrap(p, gentool(p) if p.get("tool") else tool(controls))}
</div>

{('<div class="wrap"><a class="guidecta" href="/' + GUIDE_FOR[p["slug"]]["slug"] + '"><b>Guide:</b> ' + e(GUIDE_FOR[p["slug"]]["h1"][0].upper() + GUIDE_FOR[p["slug"]]["h1"][1:]) + ' →</a></div>') if p["slug"] in GUIDE_FOR else ''}
<section id="how"><div class="wrap">
<h2 style="margin-bottom:24px">{e(p.get("howTitle") or "How to use the " + re.sub(r"\b(nfl|nba|mlb)\b", lambda m: m.group(1).upper(), p["h1"].lower().replace("random ", "").replace("online ", "")))}</h2>
<div class="steps3">{steps}</div>
</div></section>

<section><div class="wrap prose">
{secs}
</div></section>

<section id="faq"><div class="wrap" style="max-width:860px">
<h2 style="margin-bottom:12px">Questions</h2>
{faqs}
<p style="margin-top:18px"><a class="more" href="/faq">More questions? Read the full FAQ →</a></p>
</div></section>

<section><div class="wrap">
<h2 style="margin-bottom:20px">Related tools</h2>
<div class="grid">{rel}</div>
{embed_line(p)}<p class="src">Randomness: Wheelova uses the browser's <a href="{MDN["url"]}" rel="noopener">crypto.getRandomValues()</a> (MDN Web Docs).{srcs}</p>
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

from faq import FAQ_PAGE
def faq_page():
    F = FAQ_PAGE; path = "/faq"
    allq = [(q, a) for _, _, qs in F["sections"] for q, a in qs]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "FAQPage", "url": SITE + path, "name": F["h1"], "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in allq]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Wheelova", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "FAQ", "item": SITE + path}]},
        {"@type": "WebPage", "@id": SITE + path + "#page", "url": SITE + path, "name": F["h1"], "dateModified": UPDATED, "author": {"@type": "Person", "name": AUTHOR["name"]}, "publisher": {"@type": "Organization", "name": "Wheelova", "url": SITE + "/"}}]}
    toc = "".join(f'<a class="chip" href="#{sid}">{e(t)}</a>' for t, sid, _ in F["sections"])
    body = "".join(f'<h2 id="{sid}" style="margin:44px 0 12px">{e(t)}</h2>' + "".join(f'<details><summary>{e(q)}</summary>{md(a)}</details>' for q, a in qs) for t, sid, qs in F["sections"])
    return head(F["title"], F["desc"], path, ld) + f"""
<main><div class="wrap hero">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Wheelova</a> / <span aria-current="page">FAQ</span></nav>
<h1>{e(F["h1"])}</h1>
<p class="sub1">{e(F["sub"])}</p>
<div class="chips faqtoc">{toc}</div>
</div>
<section id="faq" style="padding-top:8px"><div class="wrap" style="max-width:860px">
{body}
<p class="src" style="margin-top:40px">Didn't find your answer? Email <a href="mailto:support@wheelova.com">support@wheelova.com</a>.</p>
<p class="byline">Written by <span>{e(AUTHOR["name"])}</span>, {e(AUTHOR["role"])} · Last updated <time datetime="{UPDATED}">October 21, 2026</time></p>
</div></section>
</main>
{footer()}
{CHROME_JS}
</body>
</html>
"""

import study
def study_page():
    path = "/" + study.SLUG
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": study.H1, "description": study.DESC, "url": SITE + path, "datePublished": study.DATE_ISO, "dateModified": study.DATE_ISO, "image": SITE + "/icons/og-image.png", "author": {"@type": "Person", "name": AUTHOR["name"]}, "publisher": {"@type": "Organization", "name": "Wheelova", "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/icons/icon-512.png"}}},
        {"@type": "Dataset", "name": "Wheelova spin fairness test: 1,000,000 spins per wheel", "description": "Raw results of 1,000,000 simulated spins of Wheelova's spin code on 2-entry and 10-entry wheels, one digit per spin.", "url": SITE + path, "creator": {"@type": "Organization", "name": "Wheelova"}, "license": "https://creativecommons.org/licenses/by/4.0/", "isAccessibleForFree": True, "distribution": [{"@type": "DataDownload", "encodingFormat": "text/plain", "contentUrl": SITE + "/data/fairness/ten-entries-1m-spins.txt"}, {"@type": "DataDownload", "encodingFormat": "text/plain", "contentUrl": SITE + "/data/fairness/two-entries-1m-spins.txt"}]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Wheelova", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Fairness study", "item": SITE + path}]}]}
    return head(study.TITLE, study.DESC, path, ld, "We spun an online wheel 1,000,000 times. Is it random?") + f"""
<main><div class="wrap hero">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Wheelova</a> / <span aria-current="page">Fairness study</span></nav>
<h1>{e(study.H1)}</h1>
<p class="sub1">{e(study.SUB)}</p>
<p class="byline" style="margin-top:14px">By <span>{e(AUTHOR["name"])}</span>, {e(AUTHOR["role"])} · Published <time datetime="{study.DATE_ISO}">{study.DATE_TXT}</time></p>
</div>
<section style="padding-top:24px"><div class="wrap prose study">
{study.body()}
</div></section>
</main>
{footer()}
{CHROME_JS}
</body>
</html>
"""

from guides import TEACHER, GIVEAWAY, RNG_GUIDE
GUIDES = [TEACHER, GIVEAWAY, RNG_GUIDE]
GUIDE_FOR = {"lucky-wheel": GIVEAWAY, "name-picker-wheel": TEACHER, "random-team-generator": TEACHER, "raffle-wheel": GIVEAWAY, "random-number-generator": RNG_GUIDE, "number-wheel": RNG_GUIDE, "dice-roller": RNG_GUIDE}
def guide_page(G):
    path = "/" + G["slug"]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": G["h1"], "description": G["desc"], "url": SITE + path, "datePublished": G.get("date", "2026-10-23"), "dateModified": G.get("date", "2026-10-23"), "image": SITE + "/icons/og-image.png", "author": {"@type": "Person", "name": AUTHOR["name"]}, "publisher": {"@type": "Organization", "name": "Wheelova", "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/icons/icon-512.png"}}},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Wheelova", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Guides", "item": SITE + "/guides"}, {"@type": "ListItem", "position": 3, "name": G["h1"], "item": SITE + path}]}]}
    return head(G["title"], G["desc"], path, ld) + f"""
<main><div class="wrap hero">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Wheelova</a> / <a href="/guides">Guides</a> / <span aria-current="page">{e(G["h1"])}</span></nav>
<h1>{e(G["h1"])}</h1>
<p class="sub1">{e(G["sub"])}</p>
<p class="byline" style="margin-top:14px">By <span>{e(AUTHOR["name"])}</span>, {e(AUTHOR["role"])} · Published <time datetime="{G.get('date', '2026-10-23')}">{G.get('date_txt', 'October 23, 2026')}</time></p>
</div>
<section style="padding-top:24px"><div class="wrap prose study">
{md(G["body"])}
</div></section>
</main>
{footer()}
{CHROME_JS}
</body>
</html>
"""

def guides_hub():
    path = "/guides"
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Wheelova guides", "url": SITE + path, "hasPart": [{"@type": "Article", "name": G["h1"], "url": SITE + "/" + G["slug"]} for G in GUIDES] + [{"@type": "Article", "name": study.H1, "url": SITE + "/" + study.SLUG}]}
    items = [(G["slug"], G["h1"], G["sub"]) for G in GUIDES] + [(study.SLUG, study.H1, study.SUB)]
    cards = "".join(f'<a class="tpl" href="/{sl}"><span class="dot" style="background:conic-gradient({DOTS[i]} 0 25%,#2A2A36 0 50%,{DOTS[i]} 0 75%,#2A2A36 0)"></span><span><b>{e(h)}</b><span>{e(sb)}</span></span></a>' for i, (sl, h, sb) in enumerate(items))
    return head("Guides – Classroom, Giveaways & Fair Random Picks | Wheelova", "Practical guides for teachers and giveaway hosts, plus our 1,000,000-spin fairness study.", path, ld) + f"""
<main><div class="wrap hero">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Wheelova</a> / <span aria-current="page">Guides</span></nav>
<h1>Guides</h1>
<p class="sub1">Practical help for classrooms, giveaways and fair random picks.</p>
<div class="prose" style="margin-top:20px;max-width:760px"><p>These guides explain how to use random picking well: fairly, transparently and without wasting class or event time. Each one is written and checked by our editor, links to the tool it describes, and states its limits. For example, the giveaway guide is general guidance, not legal advice.</p>
<ul><li><b>Teachers:</b> 25 practical classroom uses for a name picker, with a free printable.</li><li><b>Giveaway hosts:</b> a step-by-step process from rules to winner announcement, with a rules template.</li><li><b>Curious how randomness works:</b> a plain-English guide to random number generators, seeds and the modulo-bias mistake.</li><li><b>Anyone who doubts the wheel:</b> our fairness study, with 1,000,000 spins per wheel and the raw data.</li></ul>
<p>Want a wheel on your own site? See <a href="/embed-a-wheel">how to embed a wheel</a>. Questions about how Wheelova works are answered in the <a href="/faq">FAQ</a>.</p></div>
<div class="grid" style="margin-top:28px">{cards}</div>
</div></main>
{footer()}
{CHROME_JS}
</body>
</html>
"""

import embedpage as EP
def embed_page():
    path = "/" + EP.SLUG
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "name": "Wheelova embeddable spin wheel", "url": SITE + path, "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": EP.DESC, "publisher": {"@type": "Organization", "name": "Wheelova", "url": SITE + "/"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in EP.FAQ]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Wheelova", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Embed a wheel", "item": SITE + path}]}]}
    faqs = "".join(f'<details><summary>{e(q)}</summary>{md(a)}</details>' for q, a in EP.FAQ)
    return head(EP.TITLE, EP.DESC, path, ld) + f"""
<main><div class="wrap hero">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Wheelova</a> / <span aria-current="page">Embed a wheel</span></nav>
<h1>{e(EP.H1)}</h1>
<p class="sub1">{e(EP.SUB)}</p>
{EP.TOOL}
</div>
<section><div class="wrap prose">
{md(EP.BODY)}
</div></section>
<section id="faq"><div class="wrap" style="max-width:860px">
<h2 style="margin-bottom:12px">Questions</h2>
{faqs}
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
<div class="prose" style="margin-top:20px;max-width:760px"><p>Every tool here is free, works in your browser without an account, and uses your browser's cryptographically secure random number source (we tested it with <a href="/is-the-wheel-random">1,000,000 spins per wheel</a>). Wheels let you watch the result land; generators give you a list you can copy.</p>
<ul><li><b>Decisions:</b> yes or no answers, choosing between options, what to eat, and coin flips.</li><li><b>Games &amp; parties:</b> truth or dare, dice, prize and mystery wheels.</li><li><b>Names &amp; groups:</b> pick a name, split a class into teams, or generate new names and letters.</li><li><b>Numbers &amp; chance:</b> random numbers as a list or a wheel, plus a spinner.</li><li><b>Giveaways:</b> draw winners live with the raffle wheel.</li><li><b>Geography:</b> random countries and states, and a flag quiz.</li><li><b>Sports:</b> random NFL, NBA and MLB teams, by conference or division.</li><li><b>Words &amp; creativity:</b> random words, drawing prompts and letters.</li><li><b>Colors:</b> random colours with hex codes.</li></ul></div>
{cards}
</div></main>
{footer()}
{CHROME_JS}
</body>
</html>
"""

HOME_CFG = {"key": "home2", "entries": ["Emma", "Liam", "Olivia", "Noah", "Ava", "James", "Sophia", "Oliver", "Mia", "Lucas"],
            "palette": ["#6E56F0", "#E11D48", "#F59E0B", "#16A34A", "#2563EB", "#DB2777", "#0D9488", "#EA580C"]}

FEATURED = """<section class="featured"><div class="wrap"><span class="fh">Featured on</span>
<a href="https://launchstag.com/p/wheelova" target="_blank" rel="noopener"><img src="https://launchstag.com/badge-light.svg" alt="Featured on Launchstag" width="198" height="62" loading="lazy" decoding="async"></a>
<a href="https://tools.cafe" target="_blank" rel="noopener"><img src="https://tools.cafe/b/light.svg" alt="Featured on tools.cafe" width="256" height="80" loading="lazy" decoding="async"></a>
<a href="https://launchbuff.com/products/wheelova-n778wi" target="_blank" rel="noopener noreferrer" title="Featured on LaunchBuff"><img src="https://launchbuff.com/badge-featured-dark.svg" alt="Featured on LaunchBuff" width="256" height="80" loading="lazy" decoding="async"></a>
</div></section>
"""
def home():
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    main = re.search(r"<main>[\s\S]*?</main>", src).group(0)
    ld = json.loads(re.search(r'<script type="application/ld\+json">\s*([\s\S]*?)\s*</script>', src).group(1))
    ld["@graph"].insert(0, {"@type": "Organization", "name": "Wheelova", "url": SITE + "/", "logo": SITE + "/icons/icon-512.png"})
    popular = "".join(card(s, i) for i, s in enumerate(CORE + ["spinner"]))
    main = main.replace('<section id="features">', f'<section id="popular"><div class="wrap">\n<h2>Popular tools</h2>\n<p style="margin:0 0 28px;color:var(--mu)">Ready-made wheels and generators with their own presets and guides.</p>\n<div class="grid">{popular}</div>\n<p style="margin-top:24px"><a class="more" href="/wheels">See all {len(PAGES)} tools →</a></p>\n</div></section>\n\n<section id="features">', 1)
    main = re.sub(r'<section id="wheels">[\s\S]*?</section>\s*', '', main, count=1)
    main = add_wheel_btn(main, "en")
    _toast = re.search(r'<div class="wtoast" id="wtoast"[^\n]*</div>\n</div>', main).group(0)
    main = main.replace(_toast, _toast + '\n' + multi_section("en"), 1)
    t = re.search(r"<title>(.*?)</title>", src).group(1)
    d = re.search(r'<meta name="description" content="(.*?)">', src).group(1)
    return head(html.unescape(t), html.unescape(d), "/", ld, "Wheelova – Spin the Wheel. Trust the result.") + main + FEATURED + POP + SHARE + footer() + embed_meta("") + '<script>window.WV=' + json.dumps(HOME_CFG) + '</script>\n' + f'<script src="/rng.js?v={V}" defer></script>\n<script src="/app.js?v={V}" defer></script>\n</body>\n</html>\n'

BY.update({x["slug"]: x for x in ES})

def es_page(p):
    U = ES_UI
    q = dict(p); q["upgraded"] = True
    q["howTitle"] = "Cómo usar la " + p["h1"][0].lower() + p["h1"][1:]
    path = "/" + p["slug"]
    h = page(q)
    h = h.replace("window.WV=" + json.dumps({k: q[k] for k in ("entries", "variants", "mode", "colorMap", "removeWinner", "resultLabel", "popLabel", "key", "prompts") if k in q}, ensure_ascii=False),
                  "window.WV=" + json.dumps(dict({k: q[k] for k in ("entries", "variants", "removeWinner", "resultLabel", "popLabel", "key", "palette", "mode", "colorMap") if k in q}, t=ES_JS), ensure_ascii=False), 1)
    nav = "".join('<a href="/%s"%s%s>%s</a>' % (sl, ' aria-current="page"' if "/" + sl == path else "", ' hreflang="en" lang="en"' if sl == "" else "", n) for sl, n in NAV_ES)
    h = re.sub(r'<nav id="mnav" aria-label="Main">[\s\S]*?</nav>', f'<nav id="mnav" aria-label="Principal">{nav}</nav>', h, count=1)
    crumbs = f'<a href="/es">Wheelova</a> / <span aria-current="page">{e(p["h1"])}</span>' if p["slug"] != "es" else '<span aria-current="page">Wheelova</span>'
    h = re.sub(r'(<nav class="crumbs" aria-label=")Breadcrumb(">)[\s\S]*?(</nav>)', lambda m: m.group(1) + "Ruta de navegación" + m.group(2) + crumbs + m.group(3), h, count=1)
    h = h.replace('"name": "Wheels", "item": "' + SITE + '/wheels"', '"name": "Ruleta aleatoria", "item": "' + SITE + '/es"')
    if p["slug"] == "es":
        h = h.replace(', {"@type": "ListItem", "position": 3, "name": "Ruleta aleatoria", "item": "' + SITE + '/es"}', '')
    h = re.sub(r'<footer>[\s\S]*?</footer>', '<footer><div class="ft">' + fbrand("/es", "Gira la ruleta. Confía en el resultado.", "© 2026 Wheelova. Ruleta aleatoria gratis.") + '<div><span class="h">Ruletas</span>' + "".join(f'<a href="/{x["slug"]}">{e(x["nav"])}</a>' for x in ES) + '</div><div><span class="h">Wheelova</span><a href="/" hreflang="en" lang="en">English</a><a href="/fr" hreflang="fr" lang="fr">Français</a><a href="/vi" hreflang="vi" lang="vi">Tiếng Việt</a><a href="/about">About</a><a href="/privacy">Privacy</a><a href="/terms">Terms</a><a href="#cookies" data-wvcookies>Cookies</a></div></div></footer>', h, count=1)
    R = [('<html lang="en">', '<html lang="es">'),
         ('aria-label="Switch to light mode"', 'aria-label="' + ES_JS["tolight"] + '"'), ('aria-label="Open menu"', 'aria-label="Abrir menú"'),
         ('aria-label="Fullscreen" title="Fullscreen (F)"', 'aria-label="Pantalla completa" title="Pantalla completa (F)"'),
         ('aria-label="Spinning wheel"', 'aria-label="Ruleta"'), ('aria-label="Spin the wheel">SPIN<', 'aria-label="' + U["spin_aria"] + '">' + U["spin"] + '<'),
         ('Press SPIN or the Space bar', U["spin_hint"]), ('>Entries <span id="count"', '>' + U["entries"] + ' <span id="count"'),
         ('>Shuffle<', '>' + U["shuffle"] + '<'), ('>Sort<', '>' + U["sort"] + '<'), ('>Clear<', '>' + U["clear"] + '<'),
         ('aria-label="Presets"', 'aria-label="Ajustes rápidos"'),
         ("You're viewing a shared wheel. Your own saved list is untouched.", "Estás viendo una ruleta compartida. Tu lista guardada no se ha modificado."), ('Back to my list', U["my_list"]), ('>Keep this as my list<', '>Guardar como mi lista<'),
         ('<summary>My saved wheels</summary>', '<summary>Mis ruletas guardadas</summary>'), ('placeholder="Name, e.g. Period 3" aria-label="Name for this wheel"', 'placeholder="Nombre, p. ej. 3.º B" aria-label="Nombre para esta ruleta"'),
         ('>Save list<', '>Guardar lista<'), ('Save this list under a name to switch between classes or groups. Stored only in this browser.', 'Guarda esta lista con un nombre para cambiar entre clases o grupos. Solo se guarda en este navegador.'),
         ('id="rcopy" type="button">Copy<', 'id="rcopy" type="button">Copiar<'), ('>Undo<', '>Deshacer<'),
         ('One entry per line. Saved in your browser automatically.', U["help"]),
         ('Remove winner after each spin', U["remove"]),
         ('<summary>Settings</summary>', '<summary>Ajustes</summary>'), ('<label>Spin speed<', '<label>Velocidad de giro<'), ('<label>Wheel colors<', '<label>Colores de la ruleta<'), ('id="impbtn" type="button">Import<', 'id="impbtn" type="button">Importar<'), ('<label>Column<', '<label>Columna<'), ('> First row is a header<', '> La primera fila es un encabezado<'), ('type="button">Use column<', 'type="button">Usar columna<'), ('id="impno" type="button">Cancel<', 'id="impno" type="button">Cancelar<'), ('>Grayscale<', '>Escala de grises<'), ('>Color-blind friendly<', '>Apta para daltónicos<'), ('>Custom…<', '>Personalizados…<'), ('>Ocean<', '>Océano<'), ('>Sunset<', '>Atardecer<'), ('>Forest<', '>Bosque<'), ('aria-label="Color ', 'aria-label="Color '), ('> Read the result aloud<', '> Leer el resultado en voz alta<'), ('>Fast<', '>Rápida<'), ('>Slow<', '>Lenta<'), ('Winner pop-up heading<input id="wmsg" maxlength="60" placeholder="WE HAVE A WINNER"', 'Título de la ventana del ganador<input id="wmsg" maxlength="60" placeholder="¡TENEMOS GANADOR!"'), ('</span>Sound<', '</span>' + U["sound"] + '<'),
         ('Share link</button>', U["share"] + '</button>'), ('<label>From<input id="nmin"', '<label>Desde<input id="nmin"'), ('<label>To<input id="nmax"', '<label>Hasta<input id="nmax"'), ('style="height:40px">Make wheel<', 'style="height:40px">Crear ruleta<'), ('Embed</button>', U["embed"] + '</button>'),
         ('>Results <span id="rcount"', '>' + U["results"] + ' <span id="rcount"'),
         ('WE HAVE A WINNER', ES_JS["pop"]), ('>Remove from wheel<', '>' + U["pop_remove"] + '<'), ('>Close<', '>' + U["close"] + '<'),
         ('SHARE THIS WHEEL', U["share_title"]),
         ('Anyone with this link can see your entries: they are encoded inside the link (not encrypted). Nothing is stored on our server, but the link stays in browser history and wherever you paste it, so avoid sharing private lists.', U["share_help"]),
         ('for="shareurl">Link<', 'for="shareurl">' + U["link"] + '<'), ('id="sharecopy" type="button">Copy<', 'id="sharecopy" type="button">' + U["copy"] + '<'),
         ('Embed code — paste into your website, blog or OBS browser source', U["embed_label"]), ('>Copy embed code<', '>' + U["copy_embed"] + '<'), ('Keep the credit link so others can find the wheel.', EMBED_KEEP["es"]),
         ('margin-bottom:12px">Questions<', 'margin-bottom:12px">' + U["faq"] + '<'), ('margin-bottom:20px">Related tools<', 'margin-bottom:20px">' + U["related"] + '<'),
         ('Written by <span>', 'Escrito por <span>'), ('Editor, Wheelova', 'editor de Wheelova'), ('Last updated <time', 'Actualizado el <time'), ('>October 21, 2026<', '>21 de octubre de 2026<'), ('>November 8, 2026<', '>8 de noviembre de 2026<'),
         ("Wheelova – Spin the wheel, trust the result", "Wheelova – Gira la ruleta, confía en el resultado"),
         ('content="Wheelova — spin the wheel, trust the result"', 'content="Wheelova — gira la ruleta"'),
         ]
    h = h.replace('\n<p style="margin-top:18px"><a class="more" href="/faq">More questions? Read the full FAQ →</a></p>', '')
    for a, b in R:
        h = h.replace(a, b)
    h = re.sub(r'<p class="src">Randomness:.*?(?= Sources:|</p>)', '<p class="src">' + U["rand_src"], h, count=1).replace(" Sources: ", " " + U["sources"] + " ")
    h = h.replace('<meta property="og:type"', '<meta property="og:locale" content="es_ES">\n<meta property="og:type"', 1)
    h = locdate(h, "es")
    return h



def locdate(h, lang):
    M = {"es": ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"], "fr": ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]}.get(lang)
    def f(m):
        mo, d, y = MONTHS.index(m.group(2)), int(m.group(3)), m.group(4)
        txt = f"{d} de {M[mo]} de {y}" if lang == "es" else f"{d} {M[mo]} {y}" if lang == "fr" else f"ngày {d} tháng {mo + 1} năm {y}"
        return m.group(1) + txt + "</time>"
    return re.sub(r'(<time datetime="[^"]+">)([A-Z][a-z]+) (\d+), (\d{4})</time>', f, h)

LANG_OF = {"": "en", "es": "es", "fr": "fr", "vi": "vi"}

def loc_page(p, L):
    """Single-page language homepages (fr, vi): render the English template, then localise it with the pack L."""
    q = dict(p); q["upgraded"] = True
    q["howTitle"] = L["howTitle"]
    path = "/" + p["slug"]
    h = page(q)
    h = h.replace("window.WV=" + json.dumps({k: q[k] for k in ("entries", "variants", "mode", "colorMap", "removeWinner", "resultLabel", "popLabel", "key", "prompts") if k in q}, ensure_ascii=False),
                  "window.WV=" + json.dumps(dict({k: q[k] for k in ("entries", "variants", "removeWinner", "resultLabel", "popLabel", "key", "palette") if k in q}, t=L["JS"]), ensure_ascii=False), 1)
    nav = "".join('<a href="/%s"%s%s>%s</a>' % (sl, ' aria-current="page"' if "/" + sl == path else "", "" if LANG_OF.get(sl) == L["lang"] else ' hreflang="%s" lang="%s"' % (LANG_OF.get(sl, "en"), LANG_OF.get(sl, "en")), n) for sl, n in L["NAV"])
    h = re.sub(r'<nav id="mnav" aria-label="Main">[\s\S]*?</nav>', f'<nav id="mnav" aria-label="{L["navLabel"]}">{nav}</nav>', h, count=1)
    h = re.sub(r'(<nav class="crumbs" aria-label=")Breadcrumb(">)[\s\S]*?(</nav>)', lambda m: m.group(1) + L["crumbs"] + m.group(2) + '<span aria-current="page">Wheelova</span>' + m.group(3), h, count=1)
    h = re.sub(r', \{"@type": "ListItem", "position": 2, "name": "Wheels"[^}]*\}', '', h)
    h = re.sub(r', \{"@type": "ListItem", "position": 3[^}]*\}', '', h)
    h = re.sub(r'<section><div class="wrap">\n<h2 style="margin-bottom:20px">Related tools</h2>\n<div class="grid">[\s\S]*?</div>\n', '<section><div class="wrap">\n', h, count=1)
    h = re.sub(r'<footer>[\s\S]*?</footer>', '<footer><div class="ft">' + fbrand(path, L["tagline"], L["copy"]) + L["footer"] + '</div></footer>', h, count=1)
    h = h.replace('\n<p style="margin-top:18px"><a class="more" href="/faq">More questions? Read the full FAQ →</a></p>', '')
    for a, b in L["R"]:
        h = h.replace(a, b)
    h = re.sub(r'<p class="src">Randomness:.*?(?= Sources:|</p>)', L["src"], h, count=1).replace(" Sources: ", L["sourcesSep"])
    h = h.replace('<meta property="og:type"', '<meta property="og:locale" content="%s">\n<meta property="og:type"' % L["ogLocale"], 1)
    return locdate(h, L["lang"])

_J = FR_JS
FR_L = {"lang": "fr", "JS": FR_JS, "NAV": NAV_FR, "navLabel": "Principal", "crumbs": "Fil d'Ariane", "howTitle": "Comment utiliser la roue aléatoire",
  "tagline": "Faites tourner la roue. Faites confiance au résultat.", "copy": "© 2026 Wheelova. Roue aléatoire gratuite.",
  "footer": '<div><span class="h">Langues</span><a href="/" hreflang="en" lang="en">English</a><a href="/es" hreflang="es" lang="es">Español</a><a href="/vi" hreflang="vi" lang="vi">Tiếng Việt</a></div><div><span class="h">Wheelova</span><a href="/is-the-wheel-random">Étude d\'équité (EN)</a><a href="/about">About</a><a href="/privacy">Confidentialité (EN)</a><a href="/terms">Conditions (EN)</a><a href="#cookies" data-wvcookies>Cookies</a></div>',
  "src": '<p class="src">Hasard : Wheelova utilise <a href="https://developer.mozilla.org/fr/docs/Web/API/Crypto/getRandomValues" rel="noopener">crypto.getRandomValues()</a> du navigateur (MDN Web Docs).',
  "sourcesSep": " Sources : ", "ogLocale": "fr_FR",
  "R": [('<html lang="en">', '<html lang="fr">'),
         ('aria-label="Switch to light mode"', 'aria-label="' + _J["tolight"] + '"'), ('aria-label="Open menu"', 'aria-label="Ouvrir le menu"'),
         ('aria-label="Fullscreen" title="Fullscreen (F)"', 'aria-label="Plein écran" title="Plein écran (F)"'),
         ('aria-label="Spinning wheel"', 'aria-label="Roue"'), ('aria-label="Spin the wheel">SPIN<', 'aria-label="Faire tourner la roue">TOURNER<'),
         ('Press SPIN or the Space bar', "Appuyez sur TOURNER ou sur la barre d'espace"), ('>Entries <span id="count"', '>Choix <span id="count"'),
         ('>Shuffle<', '>Mélanger<'), ('>Sort<', '>Trier<'), ('>Clear<', '>Effacer<'),
         ('aria-label="Presets"', 'aria-label="Modèles"'),
         ("You're viewing a shared wheel. Your own saved list is untouched.", "Vous regardez une roue partagée. Votre propre liste n'a pas été modifiée."), ('Back to my list', 'Revenir à ma liste'), ('>Keep this as my list<', '>Garder comme ma liste<'),
         ('<summary>My saved wheels</summary>', '<summary>Mes roues enregistrées</summary>'), ('placeholder="Name, e.g. Period 3" aria-label="Name for this wheel"', 'placeholder="Nom, ex. CM2 B" aria-label="Nom de cette roue"'),
         ('>Save list<', '>Enregistrer<'), ('Save this list under a name to switch between classes or groups. Stored only in this browser.', 'Enregistrez cette liste sous un nom pour passer d\'une classe ou d\'un groupe à l\'autre. Stockée uniquement dans ce navigateur.'),
         ('id="rcopy" type="button">Copy<', 'id="rcopy" type="button">Copier<'), ('>Undo<', '>Annuler<'),
         ('One entry per line. Saved in your browser automatically.', 'Un choix par ligne. Enregistré automatiquement dans votre navigateur.'),
         ('Remove winner after each spin', 'Retirer le gagnant après chaque tour'),
         ('<summary>Settings</summary>', '<summary>Réglages</summary>'), ('<label>Spin speed<', '<label>Vitesse<'), ('<label>Wheel colors<', '<label>Couleurs de la roue<'),
         ('id="impbtn" type="button">Import<', 'id="impbtn" type="button">Importer<'), ('<label>Column<', '<label>Colonne<'), ('> First row is a header<', '> La première ligne est un en-tête<'), ('type="button">Use column<', 'type="button">Utiliser la colonne<'), ('id="impno" type="button">Cancel<', 'id="impno" type="button">Annuler<'),
         ('>Grayscale<', '>Niveaux de gris<'), ('>Color-blind friendly<', '>Adaptée aux daltoniens<'), ('>Custom…<', '>Personnalisées…<'), ('>Ocean<', '>Océan<'), ('>Sunset<', '>Coucher de soleil<'), ('>Forest<', '>Forêt<'), ('aria-label="Color ', 'aria-label="Couleur '),
         ('> Read the result aloud<', '> Lire le résultat à voix haute<'), ('>Fast<', '>Rapide<'), ('>Normal<', '>Normale<'), ('>Slow<', '>Lente<'),
         ('Winner pop-up heading<input id="wmsg" maxlength="60" placeholder="WE HAVE A WINNER"', 'Titre de la fenêtre du gagnant<input id="wmsg" maxlength="60" placeholder="' + _J["pop"] + '"'),
         ('</span>Sound<', '</span>Son<'),
         ('Share link</button>', 'Partager le lien</button>'), ('Embed</button>', 'Intégrer</button>'),
         ('>Results <span id="rcount"', '>Résultats <span id="rcount"'),
         ('WE HAVE A WINNER', _J["pop"]), ('>Remove from wheel<', '>Retirer de la roue<'), ('>Close<', '>Fermer<'),
         ('SHARE THIS WHEEL', _J["share_title"]),
         ('Anyone with this link can see your entries: they are encoded inside the link (not encrypted). Nothing is stored on our server, but the link stays in browser history and wherever you paste it, so avoid sharing private lists.', "Toute personne qui a ce lien peut voir vos choix : ils sont encodés dans le lien (pas chiffrés). Rien n'est stocké sur notre serveur, mais le lien reste dans l'historique du navigateur et partout où vous le collez : évitez de partager des listes privées."),
         ('for="shareurl">Link<', 'for="shareurl">Lien<'), ('id="sharecopy" type="button">Copy<', 'id="sharecopy" type="button">Copier<'),
         ('Embed code — paste into your website, blog or OBS browser source', "Code d'intégration : collez-le dans votre site, votre blog ou une source navigateur OBS"), ('>Copy embed code<', '>Copier le code<'), ('Keep the credit link so others can find the wheel.', EMBED_KEEP["fr"]),
         ('margin-bottom:12px">Questions<', 'margin-bottom:12px">Questions fréquentes<'),
         ('Written by <span>', 'Écrit par <span>'), ('Editor, Wheelova', 'rédacteur de Wheelova'), ('Last updated <time', 'Mis à jour le <time'), ('>October 21, 2026<', '>21 octobre 2026<'), ('>November 8, 2026<', '>8 novembre 2026<'),
         ("Wheelova – Spin the wheel, trust the result", "Wheelova – Faites tourner la roue"),
         ('content="Wheelova — spin the wheel, trust the result"', 'content="Wheelova — faites tourner la roue"'),
]}

VI_L = {"lang": "vi", "JS": VI_JS, "NAV": NAV_VI, "navLabel": "Chính", "crumbs": "Điều hướng", "howTitle": "Cách dùng vòng quay may mắn",
  "tagline": "Quay vòng quay. Tin vào kết quả.", "copy": "© 2026 Wheelova. Vòng quay may mắn miễn phí.",
  "footer": '<div><span class="h">Ngôn ngữ</span><a href="/" hreflang="en" lang="en">English</a><a href="/es" hreflang="es" lang="es">Español</a><a href="/fr" hreflang="fr" lang="fr">Français</a></div><div><span class="h">Wheelova</span><a href="/is-the-wheel-random">Nghiên cứu tính công bằng (EN)</a><a href="/about">About</a><a href="/privacy">Quyền riêng tư (EN)</a><a href="/terms">Điều khoản (EN)</a><a href="#cookies" data-wvcookies>Cookie</a></div>',
  "src": '<p class="src">Ngẫu nhiên: Wheelova dùng hàm <a href="https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues" rel="noopener">crypto.getRandomValues()</a> của trình duyệt (MDN Web Docs).',
  "sourcesSep": " Nguồn: ", "ogLocale": "vi_VN", "R": VI_R(VI_JS)}

def fr_page(p): return loc_page(p, FR_L)
def vi_page(p): return loc_page(p, VI_L)

import shutil; shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
from static_pages import STATIC
files = {"index.html": home(), "wheels.html": hub(), "faq.html": faq_page(), study.SLUG + ".html": study_page(), "guides.html": guides_hub(), EP.SLUG + ".html": embed_page(), **{G["slug"] + ".html": guide_page(G) for G in GUIDES}}
for s in STATIC:
    files[s["slug"] + ".html"] = simple(**s)
for p in PAGES:
    files[p["slug"] + ".html"] = page(p)
for p in ES:
    files[p["slug"] + ".html"] = es_page(p)
for p in FR:
    files[p["slug"] + ".html"] = fr_page(p)
for p in VI:
    files[p["slug"] + ".html"] = vi_page(p)
os.makedirs(os.path.join(OUT, "es"), exist_ok=True)
os.makedirs(os.path.join(OUT, "guides"), exist_ok=True)
for name, body in files.items():
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(body)
for f in ["app.css", "rng.js", "consent.js", "multi.js", "app.js", "gen.js", "quiz.js", "embed.js", "embed.html", "favicon.svg", "robots.txt", "site.webmanifest"]:
    open(os.path.join(OUT, f), "w", encoding="utf-8").write(open(os.path.join(ROOT, f), encoding="utf-8").read())
shutil.copy(os.path.join(ROOT, "favicon.ico"), OUT)
shutil.copytree(os.path.join(ROOT, "icons"), os.path.join(OUT, "icons"))
shutil.copytree(os.path.join(ROOT, "fonts"), os.path.join(OUT, "fonts"))
shutil.copytree(os.path.join(ROOT, "flags"), os.path.join(OUT, "flags"))
shutil.copytree(os.path.join(ROOT, "data"), os.path.join(OUT, "data"))
for _f in [x for x in os.listdir(os.path.join(ROOT, "static", "guides")) if not x.startswith(".")]: shutil.copy(os.path.join(ROOT, "static", "guides", _f), os.path.join(OUT, "guides", _f))
import hashlib, datetime
LM_PATH = os.path.join(ROOT, "src", "lastmod.json")
try: LM = json.load(open(LM_PATH))
except Exception: LM = {}
TODAY = datetime.date.today().isoformat()
urls = ["", "wheels", "faq", study.SLUG, "guides", EP.SLUG] + [G["slug"] for G in GUIDES] + [p["slug"] for p in PAGES] + [p["slug"] for p in ES] + [p["slug"] for p in FR] + [p["slug"] for p in VI] + [s["slug"] for s in STATIC if s["slug"] != "404"]
for u in urls:
    body = files["index.html" if u == "" else u + ".html"]
    m = re.search(r"<main>[\s\S]*?</main>", body)
    hsh = hashlib.sha1((m.group(0) if m else body).encode()).hexdigest()[:12]
    if LM.get(u, {}).get("h") != hsh:
        LM[u] = {"h": hsh, "d": TODAY}
json.dump(LM, open(LM_PATH, "w"), indent=0, sort_keys=True)
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}/{u}</loc><lastmod>{LM[u]['d']}</lastmod></url>" for u in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
print("built", len(files), "pages +", len(urls), "sitemap urls")
