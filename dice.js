/* Wheelova dice roller. Every die uses WVRNG.randInt(sides): crypto.getRandomValues
   with rejection sampling, so each face is exactly equally likely. */
(function(){
var $=function(id){return document.getElementById(id)},RNG=window.WVRNG;
function load(k){try{return localStorage.getItem(k)}catch(e){return null}}
function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
var REDUCE=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var SIDES=[4,6,8,10,12,20,100],KP='wv_dice_prefs',KH='wv_dice_hist';
var PIPS={1:[5],2:[1,9],3:[1,5,9],4:[1,3,7,9],5:[1,3,5,7,9],6:[1,3,4,6,7,9]};
var pf={s:20,n:1,m:0,mode:'normal',sound:false};
try{var y=JSON.parse(load(KP)||'null');if(y)for(var k in y)pf[k]=y[k]}catch(e){}
var hist=[];try{hist=JSON.parse(load(KH)||'[]')||[]}catch(e){hist=[]}
// shared link: ?r=2d6+3 (optionally &adv=1 / &dis=1)
var q=new URLSearchParams(location.search),rq=(q.get('r')||'').replace(/\s/g,'').toLowerCase();
var mm=rq.match(/^(\d{1,2})?d(\d{1,3})([+-]\d{1,2})?$/);
if(mm&&SIDES.indexOf(+mm[2])>-1){pf.s=+mm[2];pf.n=Math.min(10,Math.max(1,+(mm[1]||1)));pf.m=Math.max(-20,Math.min(20,+(mm[3]||0)));pf.mode=q.get('adv')?'adv':q.get('dis')?'dis':'normal'}
if(SIDES.indexOf(pf.s)<0)pf.s=20;
function save(){store(KP,JSON.stringify(pf));store(KH,JSON.stringify(hist.slice(0,20)))}
function advOn(){return pf.s===20&&pf.n===1&&pf.mode!=='normal'}
function notation(){var m=pf.m;return pf.n+'d'+pf.s+(m>0?'+'+m:m<0?String(m):'')+(advOn()?(pf.mode==='adv'?' (advantage)':' (disadvantage)'):'')}

/* ---------- dice DOM ---------- */
var tray=$('dtray'),res=$('dres'),brk=$('dbrk'),tool=$('tool'),busy=false;
function face(el,v){
 el.innerHTML='';el.setAttribute('data-v',v);
 if(el.parentNode&&el.parentNode.getAttribute('data-s')==='6'){for(var k=1;k<=9;k++){var p=document.createElement('i');if(PIPS[v]&&PIPS[v].indexOf(k)>-1)p.className='on';el.appendChild(p)}}
 else{var b=document.createElement('b');b.textContent=v;el.appendChild(b)}
}
function makeDie(s,v){var d=document.createElement('button');d.type='button';d.className='dd d'+s;d.setAttribute('data-s',s);d.setAttribute('aria-label','Roll');d.onclick=roll;
 var w=document.createElement('span');w.className='dshape';d.appendChild(w);face(w,v);return d}
function build(){
 tray.innerHTML='';var cnt=advOn()?2:pf.n;tray.className='dtray n'+Math.min(cnt,10);
 for(var i=0;i<cnt;i++)tray.appendChild(makeDie(pf.s,pf.s===6?6:pf.s));
 $('dnot').textContent=notation();
 res.textContent='';res.classList.remove('show','crit','fumble');brk.textContent='Tap the dice or press Roll';
 $('dadvrow').hidden=pf.s!==20;$('dnval').textContent=pf.n;$('dmval').textContent=(pf.m>0?'+':'')+pf.m;
 Array.prototype.forEach.call($('dside').querySelectorAll('button'),function(b){b.setAttribute('aria-pressed',String(+b.getAttribute('data-v')===pf.s))});
 Array.prototype.forEach.call($('dadv').querySelectorAll('button'),function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-v')===pf.mode));b.disabled=pf.n!==1&&b.getAttribute('data-v')!=='normal'});
 $('dadvnote').hidden=pf.n===1;
 $('droll').textContent='Roll '+notation().replace(/ \(.*\)$/,'');
}

/* ---------- sound (off by default, synthesized rattle) ---------- */
var ac=null;
function clack(){if(!pf.sound)return;try{ac=ac||new (window.AudioContext||window.webkitAudioContext)();var t=ac.currentTime;
 for(var i=0;i<4;i++){var len=.03,buf=ac.createBuffer(1,ac.sampleRate*len,ac.sampleRate),d=buf.getChannelData(0);for(var j=0;j<d.length;j++)d[j]=(Math.random()*2-1)*Math.pow(1-j/d.length,3);
  var src=ac.createBufferSource(),g=ac.createGain(),f=ac.createBiquadFilter();f.type='bandpass';f.frequency.value=2200+i*400;src.buffer=buf;g.gain.value=.35;src.connect(f);f.connect(g);g.connect(ac.destination);src.start(t+i*.07)}}catch(e){}}

/* ---------- roll ---------- */
function roll(){
 if(busy)return;busy=true;
 var dice=Array.prototype.slice.call(tray.children),vals=dice.map(function(){return 1+RNG.randInt(pf.s)});
 res.classList.remove('show','crit','fumble');res.textContent='';
 var t0=Date.now(),dur=REDUCE?0:650;
 dice.forEach(function(d,i){d.classList.remove('kept','dropped');if(!REDUCE){d.classList.remove('tumble');void d.offsetWidth;d.style.animationDelay=(i*40)+'ms';d.classList.add('tumble')}});
 (function tick(){
  if(Date.now()-t0<dur){dice.forEach(function(d){face(d.firstChild,1+Math.floor(Math.random()*pf.s))});setTimeout(tick,70);return}
  dice.forEach(function(d,i){face(d.firstChild,vals[i]);d.setAttribute('aria-label','Rolled '+vals[i]+'. Roll again')});
  busy=false;clack();finish(vals,dice)})();
}
function finish(vals,dice){
 var used=vals,note='';
 if(advOn()){var keep=pf.mode==='adv'?Math.max(vals[0],vals[1]):Math.min(vals[0],vals[1]),ki=vals.indexOf(keep);
  dice.forEach(function(d,i){d.classList.add(i===ki?'kept':'dropped')});used=[keep];note=(pf.mode==='adv'?'Advantage: kept the higher of ':'Disadvantage: kept the lower of ')+vals[0]+' and '+vals[1]}
 var sum=used.reduce(function(a,b){return a+b},0),total=sum+pf.m;
 res.textContent=total;res.classList.add('show');
 var parts=(advOn()?String(used[0]):vals.join(' + '))+(pf.m?(pf.m>0?' + ':' − ')+Math.abs(pf.m):'');
 brk.textContent=(note?note+' · ':'')+notation().replace(/ \(.*\)$/,'')+': '+(used.length>1||pf.m?parts+' = '+total:'rolled '+total);
 if(pf.s===20&&used.length===1){if(used[0]===20){res.classList.add('crit');brk.textContent+=' · Natural 20!'}else if(used[0]===1){res.classList.add('fumble');brk.textContent+=' · Natural 1'}}
 hist.unshift({r:notation(),v:advOn()?vals:vals,t:total});hist=hist.slice(0,20);save();drawHist();
}
function drawHist(){var h=$('dhist');h.innerHTML='';
 if(!hist.length){h.innerHTML='<li class="hnone">Your rolls appear here</li>';return}
 hist.forEach(function(x){var li=document.createElement('li'),a=document.createElement('span'),b=document.createElement('b');a.textContent=x.r+' → '+x.v.join(', ');b.textContent=x.t;li.appendChild(a);li.appendChild(b);h.appendChild(li)})}

/* ---------- controls ---------- */
Array.prototype.forEach.call($('dside').querySelectorAll('button'),function(b){b.onclick=function(){if(busy)return;pf.s=+b.getAttribute('data-v');if(pf.s!==20)pf.mode='normal';save();build()}});
Array.prototype.forEach.call($('dadv').querySelectorAll('button'),function(b){b.onclick=function(){if(busy||b.disabled)return;pf.mode=b.getAttribute('data-v');save();build()}});
function step(id,key,d,lo,hi){$(id).onclick=function(){if(busy)return;pf[key]=Math.max(lo,Math.min(hi,pf[key]+d));if(key==='n'&&pf.n!==1)pf.mode='normal';save();build()}}
step('dnm','n',-1,1,10);step('dnp','n',1,1,10);step('dmm','m',-1,-20,20);step('dmp','m',1,-20,20);
$('droll').onclick=roll;
$('dclear').onclick=function(){hist=[];save();drawHist()};
$('dshare').onclick=function(){var b=this,u=location.origin+location.pathname+'?r='+encodeURIComponent(pf.n+'d'+pf.s+(pf.m>0?'+'+pf.m:pf.m<0?pf.m:''))+(advOn()?(pf.mode==='adv'?'&adv=1':'&dis=1'):'');
 try{navigator.clipboard.writeText(u);b.textContent='Link copied';setTimeout(function(){b.textContent='Share link'},1600)}catch(e){prompt('Copy this link',u)}};
var sb=$('dsound');function sUI(){sb.setAttribute('aria-pressed',String(pf.sound));sb.setAttribute('aria-label',pf.sound?'Sound on':'Sound off');sb.classList.toggle('on',pf.sound)}
sb.onclick=function(){pf.sound=!pf.sound;save();sUI();if(pf.sound)clack()};
var fb=$('dfs');
function isFs(){return document.fullscreenElement===tool||tool.classList.contains('is-cfs')}
function fsUI(){var on=isFs();fb.setAttribute('aria-label',on?'Exit fullscreen':'Fullscreen');document.body.classList.toggle('cfs-on',on)}
fb.onclick=function(){if(isFs()){if(document.fullscreenElement)document.exitFullscreen();tool.classList.remove('is-cfs')}
 else if(tool.requestFullscreen){tool.requestFullscreen().catch(function(){tool.classList.add('is-cfs');fsUI()})}else tool.classList.add('is-cfs');fsUI()};
document.addEventListener('fullscreenchange',fsUI);
document.addEventListener('keydown',function(e){
 var tag=document.activeElement&&document.activeElement.tagName;
 if(/INPUT|TEXTAREA|SELECT/.test(tag)||document.querySelector('.sdlg[open]'))return;
 if(e.code==='Space'&&!/BUTTON|A/.test(tag)){e.preventDefault();roll()}
 else if((e.key==='f'||e.key==='F')&&!e.ctrlKey&&!e.metaKey){fb.click()}
 else if(e.key==='Escape'&&tool.classList.contains('is-cfs')){tool.classList.remove('is-cfs');fsUI()}});
sUI();build();drawHist();
})();
