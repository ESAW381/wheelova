(function(){
var cfg=window.WV||{},T=cfg.t||{};
var COLORS=['#6E56F0','#E11D48','#F59E0B','#16A34A','#2563EB','#DB2777','#0D9488','#EA580C'];
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
var sharedMode=false;function parse(){entries=ta.value.split('\n').map(function(s){return s.trim()}).filter(Boolean);$('count').textContent='· '+entries.length;if(!sharedMode)store(KEY,ta.value);draw()}
function setEntries(arr){leaveShared();ta.value=arr.join('\n');parse()}
function leaveShared(){if(!sharedMode)return;sharedMode=false;var n=$('sharenote');if(n)n.hidden=true;try{history.replaceState(null,'',location.pathname+location.search)}catch(e){}}
function lum(h){h=h.replace('#','');if(h.length===3)h=h.split('').map(function(c){return c+c}).join('');var r=parseInt(h.substr(0,2),16),g=parseInt(h.substr(2,2),16),b=parseInt(h.substr(4,2),16);return (0.299*r+0.587*g+0.114*b)/255}
function fillFor(i,n,name){
if(cfg.mode==='color'&&cfg.colorMap){var c=cfg.colorMap[name.toLowerCase()];if(c)return {f:c,t:lum(c)>0.6?'#141418':'#FFFFFF'}}
if(cfg.palette){var P=cfg.palette,k=(n%P.length===1&&i===n-1&&n>1)?1:i%P.length;return {f:P[k],t:lum(P[k])>0.62?'#141418':'#FFFFFF'}}
var ci=(n%8===1&&i===n-1&&n>1)?1:i%8;return {f:COLORS[ci],t:lum(COLORS[ci])>0.62?'#141418':'#FFFFFF'}}
var FL=cfg.flags||null,flagMode='name',FIMG={};
function flagImg(name){if(!FL)return null;var c=FL[name];if(!c)return null;if(!FIMG[c]){var im=new Image();im.onload=function(){draw()};im.src='/flags/'+c+'.svg';FIMG[c]=im}return FIMG[c]}
function draw(){
var W=cv.width,R=W/2,n=entries.length;ctx.clearRect(0,0,W,W);
if(!n){ctx.fillStyle='#1E1E27';ctx.beginPath();ctx.arc(R,R,R,0,Math.PI*2);ctx.fill();ctx.fillStyle='#8A8A97';ctx.font='600 36px Inter,sans-serif';ctx.textAlign='center';ctx.fillText((T.empty||'Add entries'),R,R+150);return}
var seg=Math.PI*2/n;ctx.save();ctx.translate(R,R);ctx.rotate(rot);
var base=Math.min(58,Math.max(9,(2*Math.PI*R*0.6/n)*0.46)),maxW=R-36-120;
for(var i=0;i<n;i++){
var a0=-Math.PI/2+i*seg,c=fillFor(i,n,entries[i]);
ctx.beginPath();ctx.moveTo(0,0);ctx.arc(0,0,R,a0,a0+seg);ctx.closePath();
ctx.fillStyle=c.f;ctx.fill();
if(cfg.mode==='color'){ctx.strokeStyle='rgba(0,0,0,.18)';ctx.lineWidth=2;ctx.stroke()}
ctx.save();ctx.rotate(a0+seg/2);ctx.textAlign='right';ctx.textBaseline='middle';
ctx.fillStyle=c.t;var t=cfg.mode==='mystery'?'?':entries[i];if(t.length>24)t=t.slice(0,23)+'…';
var xr=R-36,mw=maxW,fi=(flagMode!=='name')?flagImg(entries[i]):null;
if(fi){var fh=Math.min(64,2*Math.sin(seg/2)*(R-60)*0.62),fw=fh*4/3;if(fh>=12&&fi.complete&&fi.naturalWidth){ctx.save();ctx.translate(xr-fw/2,0);ctx.beginPath();ctx.rect(-fw/2,-fh/2,fw,fh);ctx.fillStyle='#fff';ctx.fill();ctx.drawImage(fi,-fw/2,-fh/2,fw,fh);ctx.lineWidth=2;ctx.strokeStyle='rgba(0,0,0,.25)';ctx.strokeRect(-fw/2,-fh/2,fw,fh);ctx.restore();if(flagMode==='flag'){ctx.restore();continue}xr-=fw+12;mw-=fw+12;ctx.fillStyle=c.t}}
var fs=base;ctx.font='600 '+fs+'px Inter,sans-serif';var tw=ctx.measureText(t).width;if(tw>mw){fs=Math.max(9,fs*mw/tw);ctx.font='600 '+fs+'px Inter,sans-serif'}
ctx.fillText(t,xr,0);ctx.restore()}
ctx.restore()}
var actx=null;function tick(){if(!sound)return;try{actx=actx||new (window.AudioContext||window.webkitAudioContext)();var o=actx.createOscillator(),g=actx.createGain();o.frequency.value=900;g.gain.setValueAtTime(.06,actx.currentTime);g.gain.exponentialRampToValueAtTime(.0001,actx.currentTime+.04);o.connect(g);g.connect(actx.destination);o.start();o.stop(actx.currentTime+.05)}catch(e){}}
function idxAt(r){var n=entries.length,seg=Math.PI*2/n;var a=((-r)%(Math.PI*2)+Math.PI*2)%(Math.PI*2);return Math.min(n-1,Math.floor(a/seg))}
function spin(){
if(spinning)return;if(entries.length<2){res.innerHTML='<div class="hint">'+(T.add2||'Add at least two entries')+'</div>';return}
spinning=true;idleOn=false;res.innerHTML='<div class="hint">'+(T.spinning||'Spinning…')+'</div>';
var start=rot,reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var SP={fast:[4,2600],normal:[6,4600],slow:[9,8000]}[speed]||[6,4600];
var target=start+Math.PI*2*(reduce?1:SP[0])+rand()*Math.PI*2;
var dur=reduce?300:SP[1],t0=performance.now(),last=idxAt(start);
function ease(t){return 1-Math.pow(1-t,4)}
function f(now){var t=Math.min(1,(now-t0)/dur);rot=start+(target-start)*ease(t);draw();var k=idxAt(rot);if(k!==last){last=k;tick()}
if(!spinning)return;if(t<1)requestAnimationFrame(f);else done()}
requestAnimationFrame(f);clearTimeout(window._wvT);window._wvT=setTimeout(function(){if(spinning){rot=target;draw();done()}},dur+400)}
function done(){
if(!spinning)return;spinning=false;rot=rot%(Math.PI*2);var i=idxAt(rot),w=entries[i];
res.innerHTML='<div class="lbl">'+(cfg.resultLabel||T.winner||'WINNER')+'</div><div class="win"></div>';res.querySelector('.win').textContent=w;
hist.unshift(w);var li=document.createElement('li');li.textContent=w;$('history').prepend(li);$('rcount').textContent='· '+hist.length;
lastIdx=i;$('popwin').textContent=w;var pp=$('popprompt');if(pp){var pr='';if(cfg.prompts){var dk=($('tddeck')&&$('tddeck').value)||'kids',L=cfg.prompts[dk]&&cfg.prompts[dk][w];if(L&&L.length)pr=L[Math.floor(rand()*L.length)]}pp.textContent=pr;if(pr){res.querySelector('.win').textContent=w+': '+pr}}$('poplbl').textContent=(wmsg&&wmsg.value.trim())||cfg.popLabel||T.pop||'WE HAVE A WINNER';
var pf=$('popflag');if(pf){var fc=FL&&FL[w];pf.hidden=!fc;if(fc){pf.src='/flags/'+fc+'.svg';pf.alt=''}}var sw=$('popswatch'),hx=$('pophex');var c=cfg.mode==='color'&&cfg.colorMap?cfg.colorMap[w.toLowerCase()]:null;if(sw){sw.style.display=c?'block':'none';if(c)sw.style.background=c}if(hx)hx.textContent=c?c.toUpperCase():''
if(wspk&&wspk.checked){try{speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(($('popprompt')&&$('popprompt').textContent)?w+'. '+$('popprompt').textContent:w);u.lang=document.documentElement.lang||'en';speechSynthesis.speak(u)}catch(e){}}$('popremove').style.display=removeW?'none':'';$('pop').classList.add('on');$('popclose').focus();
if(removeW){entries.splice(i,1);ta.value=entries.join('\n');parse()}}
var lastIdx=-1;function closePop(){$('pop').classList.remove('on');$('spin').focus()}
$('popclose').onclick=closePop;$('pop').onclick=function(e){if(e.target===this)closePop()};
$('popremove').onclick=function(){if(lastIdx>-1&&lastIdx<entries.length){entries.splice(lastIdx,1);ta.value=entries.join('\n');parse()}lastIdx=-1;closePop()};
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&$('pop').classList.contains('on'))closePop()});
$('spin').onclick=spin;cv.onclick=spin;
ta.addEventListener('input',function(){leaveShared();parse()});
$('shuffle').onclick=function(){var a=entries.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(rand()*(i+1));var t=a[i];a[i]=a[j];a[j]=t}setEntries(a)};
$('sort').onclick=function(){setEntries(entries.slice().sort(function(a,b){return a.localeCompare(b,undefined,{numeric:true})}))};
$('clear').onclick=function(){setEntries([]);ta.focus()};
var rb=$('remove');rb.setAttribute('aria-pressed',removeW);rb.onclick=function(){removeW=!removeW;this.setAttribute('aria-pressed',removeW)};
$('sound').onclick=function(){sound=!sound;this.setAttribute('aria-pressed',sound)};
var wf=$('wflag');if(FL){flagMode=load(KEY+'_flag')||'both';if(wf){wf.value=flagMode;wf.onchange=function(){flagMode=wf.value;store(KEY+'_flag',flagMode);draw()}}}
var speed=load('wv_speed')||'normal',wsp=$('wspeed'),wmsg=$('wmsg');if(wsp){wsp.value=speed;wsp.onchange=function(){speed=wsp.value;store('wv_speed',speed)}}
var wspk=$('wspeak');if(wspk){if(!('speechSynthesis' in window))wspk.parentNode.style.display='none';wspk.checked=load('wv_speak')==='1';wspk.onchange=function(){store('wv_speak',wspk.checked?'1':'0')}}
if(wmsg){wmsg.value=load(KEY+'_msg')||'';wmsg.addEventListener('input',function(){store(KEY+'_msg',wmsg.value)})}
document.addEventListener('keydown',function(e){if(e.code==='Space'&&!$('pop').classList.contains('on')&&!($('sharepop')&&$('sharepop').classList.contains('on'))&&!/TEXTAREA|INPUT|BUTTON|SUMMARY|A|SELECT/.test(document.activeElement.tagName)){e.preventDefault();spin()}});
var g=$('templates');if(g){TEMPLATES.forEach(function(t){var b=document.createElement('button');b.type='button';b.className='tpl';
b.innerHTML='<span class="dot" style="background:conic-gradient('+t.c+' 0 25%,#2A2A36 0 50%,'+t.c+' 0 75%,#2A2A36 0)"></span><span><b></b><span></span></span>';
b.querySelector('b').textContent=t.n;b.querySelector('span span').textContent=t.e.length+' entries';
b.onclick=function(){setEntries(t.e);$('tool').scrollIntoView({block:'start'})};g.appendChild(b)})}
var vz=$('variants');if(vz&&cfg.variants){cfg.variants.forEach(function(v){var b=document.createElement('button');b.type='button';b.className='chip';b.textContent=v.label;b.onclick=function(){setEntries(v.entries)};vz.appendChild(b)})}
var ng=$('ngo');if(ng){ng.onclick=function(){var a=parseInt($('nmin').value,10),b=parseInt($('nmax').value,10);var err=$('nerr');
if(isNaN(a)||isNaN(b)||b<=a){err.textContent='Enter a range where "To" is bigger than "From".';return}
if(b-a+1>500){err.textContent='Up to 500 numbers per wheel.';return}err.textContent='';var arr=[];for(var x=a;x<=b;x++)arr.push(String(x));setEntries(arr)}}
var sc=$('scount');if(sc){sc.onchange=function(){var n=parseInt(sc.value,10),arr=[];for(var x=1;x<=n;x++)arr.push(String(x));setEntries(arr)}}
function enc(arr){var u=new TextEncoder().encode(arr.join('\n')),s='';for(var i=0;i<u.length;i++)s+=String.fromCharCode(u[i]);return btoa(s).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'')}
function dec(t){try{t=t.replace(/-/g,'+').replace(/_/g,'/');while(t.length%4)t+='=';var s=atob(t),u=new Uint8Array(s.length);for(var i=0;i<s.length;i++)u[i]=s.charCodeAt(i);return new TextDecoder().decode(u).split('\n').map(function(x){return x.trim()}).filter(Boolean).slice(0,1000)}catch(e){return null}}
var saved=load(KEY),hm=/[#&]w=([^&]+)/.exec(location.hash),shared=hm?dec(hm[1]):null;
if(shared&&shared.length){sharedMode=true;ta.value=shared.join('\n');var sn=$('sharenote');if(sn)sn.hidden=false}else{ta.value=saved!=null&&saved.trim()?saved:DEFAULT.join('\n')}
parse();
var ml=$('mylist');if(ml)ml.onclick=function(){leaveShared();ta.value=saved!=null&&saved.trim()?saved:DEFAULT.join('\n');parse()};
var SITE='https://wheelova.com',PATH=location.pathname.replace(/index\.html$/,'').replace(/\.html$/,'');
function openShare(withEmbed){if(entries.length<2){res.innerHTML='<div class="hint">'+(T.add2share||'Add at least two entries to share')+'</div>';return}
var code=enc(entries),url=SITE+PATH+'#w='+code;$('shareurl').value=url;
var emb=SITE+'/embed#w='+code+(cfg.mode&&cfg.mode!=='color'?'&m='+cfg.mode:'');
$('embedcode').value='<iframe src="'+emb+'" title="'+(T.iframe_title||'Spin the wheel – Wheelova')+'" width="100%" height="560" style="max-width:560px;border:0" loading="lazy"></iframe>\n<p style="font:14px sans-serif">'+(T.credit_pre||'Spin wheel by')+' <a href="'+SITE+PATH+'">Wheelova</a></p>';
$('embedwrap').hidden=!withEmbed;$('sharettl').textContent=withEmbed?(T.embed_title||'EMBED THIS WHEEL'):(T.share_title||'SHARE THIS WHEEL');
var w=$('sharewarn');w.hidden=url.length<=3000;w.textContent=(T.long?T.long.replace('{n}',url.length):'This list is long, so the link is long ('+url.length+' characters). It still works, but some chat apps may cut it off.');
$('sharepop').classList.add('on');(withEmbed?$('embedcopy'):$('sharecopy')).focus()}
function copyFrom(id,btn){var el=$(id);el.select();var txt=el.value,done=function(){btn.textContent=T.copied||'Copied';setTimeout(function(){btn.textContent=id==='shareurl'?(T.copy||'Copy'):(T.copy_embed||'Copy embed code')},1500)};
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,function(){document.execCommand('copy');done()})}else{document.execCommand('copy');done()}}
if($('sharebtn')){$('sharebtn').onclick=function(){openShare(false)};$('embedbtn').onclick=function(){openShare(true)};
$('sharecopy').onclick=function(){copyFrom('shareurl',this)};$('embedcopy').onclick=function(){copyFrom('embedcode',this)};
var sp=$('sharepop');$('shareclose').onclick=function(){sp.classList.remove('on')};sp.onclick=function(e){if(e.target===sp)sp.classList.remove('on')};
document.addEventListener('keydown',function(e){if(e.key==='Escape')sp.classList.remove('on')})}
var fb=$('fsbtn'),body=document.body;function setFs(on){body.classList.toggle('is-fs',on);fb.setAttribute('aria-label',on?(T.exitfs||'Exit fullscreen'):(T.fs||'Fullscreen'));
try{if(on&&document.documentElement.requestFullscreen&&!document.fullscreenElement)document.documentElement.requestFullscreen().catch(function(){});if(!on&&document.fullscreenElement)document.exitFullscreen().catch(function(){})}catch(e){}draw()}
if(fb){fb.onclick=function(){setFs(!body.classList.contains('is-fs'))};document.addEventListener('fullscreenchange',function(){if(!document.fullscreenElement&&body.classList.contains('is-fs'))setFs(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&body.classList.contains('is-fs')&&!$('pop').classList.contains('on'))setFs(false);if((e.key==='f'||e.key==='F')&&!/TEXTAREA|INPUT|SELECT/.test(document.activeElement.tagName)&&!e.ctrlKey&&!e.metaKey)setFs(!body.classList.contains('is-fs'))})}
var bg=$('burger'),nv=$('mnav');function setNav(o){nv.classList.toggle('open',o);bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?(T.closemenu||'Close menu'):(T.openmenu||'Open menu'))}
bg.onclick=function(){setNav(!nv.classList.contains('open'))};nv.addEventListener('click',function(e){if(e.target.tagName==='A')setNav(false)});
var th=$('theme'),root=document.documentElement,mt=document.querySelector('meta[name=theme-color]');function applyT(t){root.setAttribute('data-theme',t);th.setAttribute('aria-label',t==='light'?(T.todark||'Switch to dark mode'):(T.tolight||'Switch to light mode'));if(mt)mt.setAttribute('content',t==='light'?'#F6F6F9':'#0A0A0C')}
applyT(root.getAttribute('data-theme')||'dark');th.onclick=function(){var t=root.getAttribute('data-theme')==='light'?'dark':'light';applyT(t);store('wv_theme',t)};
var idleOn=!matchMedia('(prefers-reduced-motion: reduce)').matches,idleVis=true,idleT=null;
try{new IntersectionObserver(function(es){idleVis=es[0].isIntersecting}).observe(cv)}catch(e){}
function idle(t){if(!idleOn)return;if(idleT!==null&&idleVis&&!spinning&&!document.hidden){rot+=Math.min(t-idleT,50)*0.00028;draw()}idleT=t;requestAnimationFrame(idle)}
requestAnimationFrame(idle);
var lg=document.querySelector('.logo');if(lg)lg.addEventListener('click',function(){try{localStorage.removeItem('wv_entries_home2')}catch(e){}});
if(document.fonts)document.fonts.ready.then(draw);
})();
