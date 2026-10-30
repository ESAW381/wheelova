# /is-the-wheel-random — fairness study. Every number on the page is read from fairness.json (produced by data/fairness/wheelova-spin-test.js).
import json, os, math
R = json.load(open(os.path.join(os.path.dirname(__file__), "fairness.json")))
SLUG = "is-the-wheel-random"
TITLE = "Is the Wheel Random? We Spun It 1,000,000 Times | Wheelova"
DESC = "We ran 1 million spins of Wheelova's real spin code on 2, 6 and 10-entry wheels. Results, chi-square tests, streaks and the raw data you can check yourself."
H1 = "Is the wheel random? We spun it 1,000,000 times"
SUB = "A transparent test of Wheelova's spin code: the results, the statistics, and the raw data so you can check our work."
DATE_ISO = "2026-10-22"; DATE_TXT = "October 22, 2026"

def f(n): return f"{n:,}"
def pct(x, d=2): return f"{x*100:.{d}f}%"

def dev_chart(r):
    """Deviation of each entry from the expected count, in %, with the ±2σ band."""
    n, N, c = r["n"], r["spins"], r["counts"]; exp = N / n
    sd = math.sqrt(N * (1/n) * (1 - 1/n)) / exp * 100
    devs = [(x - exp) / exp * 100 for x in c]
    W, H, L, T, B = 720, 300, 56, 24, 44; pw = W - L - 16; ph = H - T - B; lim = 1.0
    y = lambda v: T + ph / 2 - v / lim * (ph / 2)
    bw = pw / n
    g = [f'<rect x="{L}" y="{y(2*sd):.1f}" width="{pw}" height="{y(-2*sd)-y(2*sd):.1f}" fill="var(--band)"/>']
    for v in (-1, -0.5, 0, 0.5, 1):
        g.append(f'<line x1="{L}" x2="{L+pw}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="var(--grid)" stroke-width="{1.5 if v==0 else 1}"/>')
        g.append(f'<text x="{L-8}" y="{y(v)+4:.1f}" text-anchor="end" font-size="15" fill="var(--axis)">{v:+.1f}%</text>' if v else f'<text x="{L-8}" y="{y(v)+4:.1f}" text-anchor="end" font-size="15" fill="var(--axis)">0</text>')
    for i, d in enumerate(devs):
        x = L + i * bw + bw * 0.22; w = bw * 0.56; top = min(y(d), y(0)); h = abs(y(d) - y(0))
        g.append(f'<rect x="{x:.1f}" y="{top:.1f}" width="{w:.1f}" height="{max(h,1):.1f}" rx="3" fill="#6E56F0"><title>Entry {i+1}: {f(c[i])} wins ({d:+.2f}%)</title></rect>')
        g.append(f'<text x="{x+w/2:.1f}" y="{H-B+18}" text-anchor="middle" font-size="15" fill="var(--axis)">{i+1}</text>')
    g.append(f'<text x="{L+pw/2}" y="{H-6}" text-anchor="middle" font-size="15" fill="var(--axis)">Entry number</text>')
    g.append(f'<text x="{L+pw-4}" y="{y(2*sd)-6:.1f}" text-anchor="end" font-size="15" fill="var(--axis)">shaded: normal variation (±{2*sd:.2f}%)</text>')
    return f'<figure class="chart"><svg viewBox="0 0 {W} {H}" role="img" aria-label="Each of the 10 entries won within one percent of the expected 100,000 times">{"".join(g)}</svg><figcaption>10-entry wheel, 1,000,000 spins: how far each entry\'s win count is from the expected {f(int(exp))}. Hover a bar for the exact count.</figcaption></figure>'

def body():
    t, s, x = R["two"], R["six"], R["ten"]
    two_runs = t["spins"] / 2
    exp_streak = {k: two_runs * 0.5 ** (k - 1) for k in (5, 10, 15)}
    rows = "".join(f'<tr><td>{r["n"]} entries</td><td>{f(r["spins"])}</td><td>{f(int(r["expected"]))}</td><td>{min(r["counts"]):,} – {max(r["counts"]):,}</td><td>{r["chi"]} (df {r["df"]})</td><td>{r["p"]}</td><td>Pass</td></tr>' for r in (t, s, x))
    counts = "".join(f'<tr><td>Entry {i+1}</td><td>{f(c)}</td><td>{(c-x["expected"])/x["expected"]*100:+.2f}%</td></tr>' for i, c in enumerate(x["counts"]))
    over = sum(1 for c in x["counts"] if abs(c - x["expected"]) > 2 * math.sqrt(x["spins"] * 0.1 * 0.9))
    return f"""
<p class="lede"><b>Short answer: yes.</b> Across 3,000,000 simulated spins on 2, 6 and 10-entry wheels, every entry won almost exactly as often as chance predicts, no result made the next one more or less likely, and streaks appeared at the rate probability says they should. All three wheels passed the standard chi-square test. The method, the code and the raw spin data are below.</p>

<div class="statrow">
<div><b>{f(x["spins"]*3)}</b><span>spins tested</span></div>
<div><b>{x["maxdev"]}%</b><span>largest gap from expected (10-entry wheel)</span></div>
<div><b>{pct(x["repeat"])}</b><span>chance of the same result twice (10 entries; expected 10%)</span></div>
<div><b>3 / 3</b><span>wheels passed the chi-square test</span></div>
</div>

<h2>What we tested</h2>
<p>When you press Spin, Wheelova asks your browser's <code>crypto.getRandomValues()</code> for a random number. That number decides how far past six full turns the wheel travels, and the winner is whichever slice stops under the pointer. According to <a href="https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getRandomValues" rel="noopener">MDN Web Docs</a>, browsers implement this function as a cryptographically secure pseudo-random generator.</p>
<p>We copied that spin math exactly from the live site's code, including how the wheel's resting position carries over from one spin to the next, and ran it 1,000,000 times each on three wheels: 2 entries (like a yes or no wheel), 6 entries (like a die) and 10 entries (like a class name picker). The test ran in Node.js 22, which provides the same Web Crypto <code>getRandomValues()</code> function as browsers.</p>

<h2>Result 1: every entry wins equally often</h2>
<p>On the 10-entry wheel, each entry should win 100,000 times out of 1,000,000. The real counts ranged from {f(min(x["counts"]))} to {f(max(x["counts"]))}, all within {x["maxdev"]}% of the expected number.</p>
{dev_chart(x)}
<p>Perfectly equal counts would actually be suspicious: real randomness always wobbles a little. The shaded band shows the range where about 95% of entries land by chance alone. {"One entry sits just outside it" if over == 1 else f"{over} entries sit just outside it" if over else "Every entry sits inside it"}, which is expected: with 10 entries, at least one lands outside a 95% band about 40% of the time. The chi-square test below checks all entries together, which is the fair way to judge.</p>
<details class="tbl"><summary>Exact win counts for the 10-entry wheel</summary><div class="tw"><table><thead><tr><th>Entry</th><th>Wins</th><th>vs expected</th></tr></thead><tbody>{counts}</tbody></table></div></details>

<h2>Result 2: the chi-square test passes on every wheel</h2>
<p>The chi-square goodness-of-fit test measures whether a set of counts differs from equal by more than chance would explain. A p-value above 0.05 means no evidence of bias. All three wheels passed.</p>
<div class="tw"><table><thead><tr><th>Wheel</th><th>Spins</th><th>Expected per entry</th><th>Actual range</th><th>Chi-square</th><th>p-value</th><th>Result</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>A p-value is not a "randomness score": values anywhere between 0.05 and 1 are normal for a fair wheel, and running the test again gives a different value each time.</p>

<h2>Result 3: the last spin doesn't affect the next</h2>
<p>A fair wheel has no memory. We counted every pair of back-to-back results (which entry followed which) and tested whether any pairing came up more than chance allows. None did: the 10-entry wheel scored p = {x["serial_p"]}, the 6-entry wheel p = {s["serial_p"]} and the 2-entry wheel p = {t["serial_p"]}.</p>
<p>The same result came up twice in a row {pct(x["repeat"])} of the time with 10 entries (expected 10%), {pct(s["repeat"])} with 6 entries (expected 16.67%) and {pct(t["repeat"])} with 2 entries (expected 50%).</p>

<h2>Result 4: streaks happen exactly as often as they should</h2>
<p>People often think a wheel is rigged when it lands on the same answer several times in a row. On a 50/50 wheel, long streaks are a normal part of randomness. Here is what 1,000,000 spins of a 2-entry wheel produced, against what probability predicts:</p>
<div class="tw"><table><thead><tr><th>Streak of the same result</th><th>Times it happened</th><th>Expected by probability</th></tr></thead><tbody>
<tr><td>5 or more in a row</td><td>{f(t["streaks"]["5"])}</td><td>about {f(round(exp_streak[5]))}</td></tr>
<tr><td>10 or more in a row</td><td>{f(t["streaks"]["10"])}</td><td>about {f(round(exp_streak[10]))}</td></tr>
<tr><td>15 or more in a row</td><td>{f(t["streaks"]["15"])}</td><td>about {round(exp_streak[15])}</td></tr>
<tr><td>Longest streak</td><td>{t["longest"]}</td><td>typically around 19–20 in a million spins</td></tr>
</tbody></table></div>
<p>So if your yes or no wheel says "Yes" five times running, that is not a glitch. It happens about once every 16 attempts at a fresh streak.</p>

<h2>What a passing result means</h2>
<p>A chi-square pass means the data shows <b>no evidence of bias</b>: the counts are as close to equal as chance predicts. It does not prove a generator is perfect, because a very small bias could hide inside normal random variation. That is why the sample is large (1,000,000 spins per wheel) and why the raw data is published, so anyone can run their own tests. For background, see <a href="/guides/how-random-number-generators-work">how random number generators work</a>.</p>

<h2>Version history</h2>
<ul>
<li><b>October 22, 2026:</b> first published (3,000,000 spins across 2, 6 and 10-entry wheels).</li>
<li><b>October 30, 2026:</b> Wheelova's number tools (Random Number Generator, dice, coin, shuffle, quiz) moved to rejection sampling, which removes a tiny bias in how random bits become whole numbers. The wheels tested here already chose winners from a continuous random angle, so their spin code and these results are unchanged.</li>
</ul>

<h2>What this test does not show</h2>
<ul>
<li><b>It tests the spin logic, not your screen.</b> We ran the same code and random source the wheel uses, without drawing the animation. The animation only displays a result that has already been decided by the random number.</li>
<li><b>It does not stop people from rigging the list.</b> Typing an entry twice gives it two slices and twice the chance. For public draws, show the full list before you spin. See <a href="/faq#random">our FAQ on fairness</a>.</li>
<li><b>It is not a certification.</b> Wheelova is built for classrooms, games, giveaways and decisions. It is not a certified lottery or gambling system.</li>
<li><b>Results vary run to run.</b> Running the test again gives slightly different counts and p-values. That is what randomness looks like.</li>
</ul>

<h2>Check it yourself</h2>
<p>You don't have to take our word for it. Download the test script and run it with Node.js 18 or newer, or analyse our raw results in any spreadsheet or statistics tool.</p>
<ul>
<li><a href="/data/fairness/wheelova-spin-test.js">Test script (JavaScript, 1 KB)</a>: the exact spin math from Wheelova's code.</li>
<li><a href="/data/fairness/ten-entries-1m-spins.txt">Raw results, 10-entry wheel (1 MB)</a>: one digit per spin, 0 = first entry.</li>
<li><a href="/data/fairness/two-entries-1m-spins.txt">Raw results, 2-entry wheel (1 MB)</a>: one digit per spin.</li>
</ul>
<p>You may use the charts and figures on this page with a credit link to this page.</p>

<h2>Try the wheels</h2>
<p>Put the results to work: the <a href="/yes-or-no-wheel">Yes or No Wheel</a> (the 2-entry case), the <a href="/name-picker-wheel">Name Picker Wheel</a> for classrooms, or the <a href="/raffle-wheel">Raffle Wheel</a> for giveaways.</p>
"""
