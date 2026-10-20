(function(){
var cfg=window.WV||{};
var COLORS=['#7C6CF2','#1E1E27','#B3A8FF','#2A2A36','#5A48D8','#24242E','#D3CCFF','#33333F'];
var DARK={2:1,6:1};
var DEFAULT=cfg.entries||['Ayesha','Bilal','Chloe','Daniyal','Emma','Faisal','Grace','Hamza'];
var TEMPLATES=[
{n:'Yes or No',c:'#7C6CF2',e:['Yes','No']},
{n:'What should I eat?',c:'#E2603B',e:['Pizza','Biryani','Burger','Sushi','Tacos','Karahi','Pasta','Salad','Shawarma','Noodles','BBQ','Sandwich']},
{n:'Truth or Dare',c:'#D94F8A',e:['Truth','Dare','Truth','Dare','Truth','Dare']},
{n:'Number 1–10',c:'#2F7BF6',e:['1','2','3','4','5','6','7','8','9','10']},
{n:'Random PSL team',c:'#E0A21B',e:['Islamabad United','Karachi Kings','Lahore Qalandars','Multan Sultans','Peshawar Zalmi','Quetta Gladiators']},
{n:'Weekend activity',c:'#14A37F',e:['Movie night','Hiking','Board games','Cook something new','Visit friends','Read a book','Go to the park','Try a new café']},
{n:'Coin flip',c:'#7C6CF2',e:['Heads','Tails']},
{n:'Dice roll',c:'#2F7BF6',e:['1','2','3','4','5','6']}
];
var $=function(id){return document.getElementById(id)};
var cv=$('wheel'),ctx=cv.getContext('2d'),ta=$('entries'),res=$('result');
var KEY='wv_entries'+(cfg.key?'_'+cfg.key:'');
var entries=[],rot=0,spinning=false,removeW=!!cfg.removeWinner,sound=true,hist=[];
function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
function load(k){try{return localStorage.getItem(k)}catch(e){return null}}
function rand(){var a=new Uint32Array(1);crypto.getRandomValues(a);return a[0]/4294967296}
function parse(){entries=ta.value.split('\n').map(function(s){return s.trim()}).filter(Boolean);$('count').textContent='· '+entries.length;store(KEY,ta.value);draw()}
function setEntries(arr){ta.value=arr.join('\n');parse()}
function lum(h){h=h.replace('#','');if(h.length===3)h=h.split('').map(function(c){return c+c}).join('');var r=parseInt(h.substr(0,2),16),g=parseInt(h.substr(2,2),16),b=parseInt(h.substr(4,2),16);return (0.299*r+0.587*g+0.114*b)/255}
function fillFor(i,n,name){
if(cfg.mode==='color'&&cfg.colorMap){var c=cfg.colorMap[name.toLowerCase()];if(c)return {f:c,t:lum(c)>0.6?'#141418':'#FFFFFF'}}
var ci=(n%8===1&&i===n-1&&n>1)?3:i%8;return {f:COLORS[ci],t:DARK[ci]?'#141418':'#FFFFFF'}}
function draw(){
var W=cv.width,R=W/2,n=entries.length;ctx.clearRect(0,0,W,W);
if(!n){ctx.fillStyle='#1E1E27';ctx.beginPath();ctx.arc(R,R,R,0,Math.PI*2);ctx.fill();ctx.fillStyle='#8A8A97';ctx.font='600 36px Inter,sans-serif';ctx.textAlign='center';ctx.fillText('Add entries',R,R+150);return}
var seg=Math.PI*2/n;ctx.save();ctx.translate(R,R);ctx.rotate(rot);
var fs=n>60?14:n>40?18:n>24?22:n>14?28:n>8?34:40;
for(var i=0;i<n;i++){
var a0=-Math.PI/2+i*seg,c=fillFor(i,n,entries[i]);
ctx.beginPath();ctx.moveTo(0,0);ctx.arc(0,0,R,a0,a0+seg);ctx.closePath();
ctx.fillStyle=c.f;ctx.fill();
if(cfg.mode==='color'){ctx.strokeStyle='rgba(0,0,0,.18)';ctx.lineWidth=2;ctx.stroke()}
ctx.save();ctx.rotate(a0+seg/2);ctx.textAlign='right';ctx.textBaseline='middle';
ctx.fillStyle=c.t;ctx.font='600 '+fs+'px Inter,sans-serif';
var t=cfg.mode==='mystery'?'?':entries[i];if(t.length>22)t=t.slice(0,21)+'…';
ctx.fillText(t,R-36,0);ctx.restore()}
ctx.restore()}
var actx=null;function tick(){if(!sound)return;try{actx=actx||new (window.AudioContext||window.webkitAudioContext)();var o=actx.createOscillator(),g=actx.createGain();o.frequency.value=900;g.gain.setValueAtTime(.06,actx.currentTime);g.gain.exponentialRampToValueAtTime(.0001,actx.currentTime+.04);o.connect(g);g.connect(actx.destination);o.start();o.stop(actx.currentTime+.05)}catch(e){}}
function idxAt(r){var n=entries.length,seg=Math.PI*2/n;var a=((-r)%(Math.PI*2)+Math.PI*2)%(Math.PI*2);return Math.min(n-1,Math.floor(a/seg))}
function spin(){
if(spinning)return;if(entries.length<2){res.innerHTML='<div class="hint">Add at least two entries</div>';return}
spinning=true;res.innerHTML='<div class="hint">Spinning…</div>';
var start=rot,reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var target=start+Math.PI*2*(reduce?1:6)+rand()*Math.PI*2;
var dur=reduce?300:4600,t0=performance.now(),last=idxAt(start);
function ease(t){return 1-Math.pow(1-t,4)}
function f(now){var t=Math.min(1,(now-t0)/dur);rot=start+(target-start)*ease(t);draw();var k=idxAt(rot);if(k!==last){last=k;tick()}
if(!spinning)return;if(t<1)requestAnimationFrame(f);else done()}
requestAnimationFrame(f);clearTimeout(window._wvT);window._wvT=setTimeout(function(){if(spinning){rot=target;draw();done()}},dur+400)}
function done(){
if(!spinning)return;spinning=false;rot=rot%(Math.PI*2);var i=idxAt(rot),w=entries[i];
res.innerHTML='<div class="lbl">'+(cfg.resultLabel||'WINNER')+'</div><div class="win"></div>';res.querySelector('.win').textContent=w;
hist.unshift(w);var li=document.createElement('li');li.textContent=w;$('history').prepend(li);$('rcount').textContent='· '+hist.length;
lastIdx=i;$('popwin').textContent=w;$('poplbl').textContent=cfg.popLabel||'WE HAVE A WINNER';
var sw=$('popswatch');if(sw){var c=cfg.mode==='color'&&cfg.colorMap?cfg.colorMap[w.toLowerCase()]:null;sw.style.display=c?'block':'none';if(c)sw.style.background=c}
$('popremove').style.display=removeW?'none':'';$('pop').classList.add('on');$('popclose').focus();
if(removeW){entries.splice(i,1);ta.value=entries.join('\n');parse()}}
var lastIdx=-1;function closePop(){$('pop').classList.remove('on');$('spin').focus()}
$('popclose').onclick=closePop;$('pop').onclick=function(e){if(e.target===this)closePop()};
$('popremove').onclick=function(){if(lastIdx>-1&&lastIdx<entries.length){entries.splice(lastIdx,1);ta.value=entries.join('\n');parse()}lastIdx=-1;closePop()};
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&$('pop').classList.contains('on'))closePop()});
$('spin').onclick=spin;cv.onclick=spin;
ta.addEventListener('input',parse);
$('shuffle').onclick=function(){var a=entries.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(rand()*(i+1));var t=a[i];a[i]=a[j];a[j]=t}setEntries(a)};
$('sort').onclick=function(){setEntries(entries.slice().sort(function(a,b){return a.localeCompare(b,undefined,{numeric:true})}))};
$('clear').onclick=function(){setEntries([]);ta.focus()};
var rb=$('remove');rb.setAttribute('aria-pressed',removeW);rb.onclick=function(){removeW=!removeW;this.setAttribute('aria-pressed',removeW)};
$('sound').onclick=function(){sound=!sound;this.setAttribute('aria-pressed',sound)};
document.addEventListener('keydown',function(e){if(e.code==='Space'&&!$('pop').classList.contains('on')&&!/TEXTAREA|INPUT|BUTTON|SUMMARY|A|SELECT/.test(document.activeElement.tagName)){e.preventDefault();spin()}});
var g=$('templates');if(g){TEMPLATES.forEach(function(t){var b=document.createElement('button');b.type='button';b.className='tpl';
b.innerHTML='<span class="dot" style="background:conic-gradient('+t.c+' 0 25%,#2A2A36 0 50%,'+t.c+' 0 75%,#2A2A36 0)"></span><span><b></b><span></span></span>';
b.querySelector('b').textContent=t.n;b.querySelector('span span').textContent=t.e.length+' entries';
b.onclick=function(){setEntries(t.e);$('tool').scrollIntoView({block:'start'})};g.appendChild(b)})}
var vz=$('variants');if(vz&&cfg.variants){cfg.variants.forEach(function(v){var b=document.createElement('button');b.type='button';b.className='chip';b.textContent=v.label;b.onclick=function(){setEntries(v.entries)};vz.appendChild(b)})}
var ng=$('ngo');if(ng){ng.onclick=function(){var a=parseInt($('nmin').value,10),b=parseInt($('nmax').value,10);var err=$('nerr');
if(isNaN(a)||isNaN(b)||b<=a){err.textContent='Enter a range where "To" is bigger than "From".';return}
if(b-a+1>500){err.textContent='Up to 500 numbers per wheel.';return}err.textContent='';var arr=[];for(var x=a;x<=b;x++)arr.push(String(x));setEntries(arr)}}
var sc=$('scount');if(sc){sc.onchange=function(){var n=parseInt(sc.value,10),arr=[];for(var x=1;x<=n;x++)arr.push(String(x));setEntries(arr)}}
var saved=load(KEY);ta.value=saved!=null&&saved.trim()?saved:DEFAULT.join('\n');parse();
var bg=$('burger'),nv=$('mnav');function setNav(o){nv.classList.toggle('open',o);bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?'Close menu':'Open menu')}
bg.onclick=function(){setNav(!nv.classList.contains('open'))};nv.addEventListener('click',function(e){if(e.target.tagName==='A')setNav(false)});
var th=$('theme'),root=document.documentElement,mt=document.querySelector('meta[name=theme-color]');function applyT(t){root.setAttribute('data-theme',t);th.setAttribute('aria-label',t==='light'?'Switch to dark mode':'Switch to light mode');if(mt)mt.setAttribute('content',t==='light'?'#F6F6F9':'#0A0A0C')}
applyT(root.getAttribute('data-theme')||'dark');th.onclick=function(){var t=root.getAttribute('data-theme')==='light'?'dark':'light';applyT(t);store('wv_theme',t)};
if(document.fonts)document.fonts.ready.then(draw);
})();
