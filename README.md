# Wheelova

Free spin-the-wheel random picker — https://wheelova.com

## How it works
- `src/pages.py` — every tool page as data (entries, presets, copy, FAQ, related wheels).
- `src/build.py` — renders all pages into `dist/` with the shared header, footer and wheel.
- `app.js` / `app.css` — the wheel engine and styles shared by every page.
- `index.html` — homepage content (its `<main>` is wrapped by the build).

## Add or edit a page
1. Add or edit a dict in `src/pages.py`.
2. Run `python3 src/build.py` and open `dist/` to check.
3. Commit and push — Vercel builds and deploys automatically.
