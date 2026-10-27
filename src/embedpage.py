SLUG = "embed-a-wheel"
TITLE = "Embed a Spinning Wheel on Your Website – Free Code | Wheelova"
DESC = "Add a free, working spin wheel to your website, blog, Google Sites, Notion or OBS stream. Type your entries, copy the embed code, paste. No sign-up."
H1 = "Embed a spinning wheel on your website"
SUB = "Type your entries, copy the code, paste it into your site. Free, no sign-up, no ads in the wheel."

TOOL = """
<div class="embgen">
<div class="card">
<label for="eentries" style="font-weight:600;color:var(--hi)">Entries <span id="ecount" style="color:var(--mu2);font-weight:500"></span></label>
<div class="chips" id="epresets" style="margin:10px 0">
<button class="chip" type="button" data-e="Yes|No">Yes / No</button>
<button class="chip" type="button" data-e="1|2|3|4|5|6|7|8|9|10">Numbers 1–10</button>
<button class="chip" type="button" data-e="Prize A|Prize B|Prize C|Try again|Prize D|Try again">Prize wheel</button>
<button class="chip" type="button" data-e="Truth|Dare">Truth or Dare</button>
</div>
<textarea id="eentries" spellcheck="false" style="min-height:180px">Emma
Liam
Olivia
Noah
Ava
James</textarea>
<p class="small">One entry per line. The entries are stored inside the embed code itself.</p>
<div class="nrow"><label>Size<select id="esize" style="width:170px"><option value="360">Small (360px)</option><option value="560" selected>Medium (560px)</option><option value="760">Large (760px)</option></select></label></div>
<label class="ck"><input id="emyst" type="checkbox"> Mystery mode (hide entries on the wheel)</label>
<label for="ecode" style="display:block;font-weight:600;color:var(--hi);margin-top:16px">Your embed code</label>
<textarea id="ecode" readonly rows="6" style="font:13px/1.5 ui-monospace,Menlo,monospace;margin-top:8px"></textarea>
<div style="display:flex;gap:8px;margin-top:10px;flex-wrap:wrap"><button class="gbtn" id="ecopy" type="button" style="margin:0">Copy embed code</button><button class="btn" id="ecopyurl" type="button">Copy URL only (for OBS / Notion)</button></div>
<p class="err" id="eerr" role="alert"></p>
</div>
<div class="card epreview"><div style="font-weight:600;color:var(--hi);margin-bottom:10px">Live preview</div><iframe id="eframe" title="Spin the wheel – Wheelova" style="width:100%;max-width:560px;height:560px;border:0;display:block;margin:0 auto" loading="lazy"></iframe></div>
</div>
<script>(function(){var $=function(i){return document.getElementById(i)},ta=$('eentries'),SITE='https://wheelova.com',last='',n=0;
function enc(arr){var u=new TextEncoder().encode(arr.join('\\n')),s='';for(var i=0;i<u.length;i++)s+=String.fromCharCode(u[i]);return btoa(s).replace(/\\+/g,'-').replace(/\\//g,'_').replace(/=+$/,'')}
function list(){return ta.value.split('\\n').map(function(s){return s.trim()}).filter(Boolean).slice(0,1000)}
function url(){var e=list();return SITE+'/embed#w='+enc(e)+($('emyst').checked?'&m=mystery':'')}
function upd(){var e=list(),sz=$('esize').value;$('ecount').textContent='\\u00b7 '+e.length;if(e.length<2){$('eerr').textContent='Add at least two entries.';$('ecode').value='';return}$('eerr').textContent='';var u=url();
$('ecode').value='<iframe src="'+u+'" title="Spin the wheel \\u2013 Wheelova" width="100%" height="'+sz+'" style="max-width:'+sz+'px;border:0" loading="lazy"></iframe>\\n<p style="font:14px sans-serif">Spin wheel by <a href="https://wheelova.com/">Wheelova</a></p>';
var local=u.replace(SITE,'');if(local!==last){last=local;var pv=(/^(localhost|127\\.)/.test(location.hostname)?'/embed.html':'/embed')+'?p='+(++n)+local.slice(6);$('eframe').src=pv;$('eframe').style.height=Math.min(+sz,560)+'px'}}
var t;ta.addEventListener('input',function(){clearTimeout(t);t=setTimeout(upd,350)});$('esize').onchange=upd;$('emyst').onchange=upd;
Array.prototype.forEach.call(document.querySelectorAll('#epresets .chip'),function(b){b.onclick=function(){ta.value=b.dataset.e.split('|').join('\\n');upd()}});
function cp(txt,btn,lbl){var done=function(){btn.textContent='Copied';setTimeout(function(){btn.textContent=lbl},1400)};if(navigator.clipboard)navigator.clipboard.writeText(txt).then(done,done);else done()}
$('ecopy').onclick=function(){if($('ecode').value)cp($('ecode').value,this,'Copy embed code')};$('ecopyurl').onclick=function(){if(list().length>1)cp(url(),this,'Copy URL only (for OBS / Notion)')};
upd()})();</script>
"""

BODY = """## How to add the wheel to your site

1. Type or paste your entries above, one per line, or start from a preset.
2. Choose a size, and turn on mystery mode if you want the entries hidden.
3. Press **Copy embed code** and paste it where your site accepts HTML. The wheel works immediately: visitors click it or press Spin.

You can also open any Wheelova wheel and press **Embed** under the entries to get the code for that wheel.

## WordPress and most blogs

In the WordPress block editor, add a **Custom HTML** block and paste the code. Other blog platforms usually have an "HTML", "Embed" or "Code" block that works the same way. Preview the page to check the size.

## Google Sites

Choose **Insert → Embed → Embed code**, paste the code, then drag the box until the whole wheel is visible. This works well for class sites.

## Canvas, Moodle and other learning platforms

Open the page editor's **HTML** view and paste the code. Some schools restrict embedded content; if the wheel doesn't appear, ask your platform administrator to allow embeds from wheelova.com, or link to the wheel instead.

## Notion

Press **Copy URL only**, type `/embed` in a Notion page, and paste the URL.

## OBS and live streams

Press **Copy URL only**. In OBS, add a **Browser** source, paste the URL, and set the width and height to about 560 × 560. Right-click the source and choose **Interact** to spin it during the stream. The background is plain, so it sits cleanly on most overlays.

## Changing the entries later

The entries are stored inside the code, so nothing is saved on our servers. To change them, edit the list above, copy the new code, and replace the old code on your site.

## Is the embedded wheel fair?

Yes. It uses the same spin code as the main site, with your browser's cryptographically secure random number source. We tested that code with 1,000,000 spins per wheel: see the [fairness study](/is-the-wheel-random).

## Terms

The embed is free to use on any site, including commercial ones. Please keep the small credit link under the wheel. Don't use the wheel for unlawful gambling or to mislead participants; see our [terms](/terms).
"""

FAQ = [
 ("Is embedding free?", "Yes. There is no sign-up, fee or usage limit."),
 ("Does the embedded wheel show ads?", "No. The wheel itself has no ads."),
 ("How many entries can an embedded wheel have?", "Up to 1,000, though around 50 or fewer read best."),
 ("Can visitors change the entries?", "No. Visitors can spin the wheel, but the entries are fixed by your embed code."),
 ("Do you store the entries?", "No. They are encoded inside the embed code and URL, not saved on our servers."),
 ("Can I use it for a giveaway on my site?", "Yes, as long as your giveaway follows the rules that apply to you. See the [fair giveaway guide](/guides/fair-giveaway)."),
]
