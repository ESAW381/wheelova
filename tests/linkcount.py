"""Count internal links pointing to each sitemap URL in dist/ (distinct source pages; nav, footer and body counted).
Usage: python3 tests/linkcount.py [--body]   --body ignores <header> and <footer> links."""
import re, os, sys, collections
D = "dist"; body_only = "--body" in sys.argv
urls = ["/" + u.replace("https://wheelova.com/", "") for u in re.findall(r"<loc>([^<]*)</loc>", open(f"{D}/sitemap.xml").read())]
urls = ["/" if u == "/" else u.rstrip("/") for u in urls]
pages = {}
for root, _, fs in os.walk(D):
    for f in fs:
        if f.endswith(".html") and f not in ("embed.html", "404.html"):
            p = os.path.join(root, f)[len(D):-5]; p = "/" if p == "/index" else p
            pages[p] = open(os.path.join(root, f), encoding="utf-8").read()
inbound = collections.defaultdict(set)
for src, h in pages.items():
    if body_only: h = re.sub(r"<header>[\s\S]*?</header>|<footer>[\s\S]*?</footer>", "", h)
    for href in re.findall(r'<a[^>]+href="(/[^"#?]*)', h):
        t = "/" if href == "/" else href.rstrip("/")
        if t != src: inbound[t].add(src)
rows = sorted((len(inbound[u]), u) for u in urls)
for n, u in rows: print(f"{n:3d}  {u}")
