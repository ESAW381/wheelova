/* Wheelova coin flip. Every coin uses WVRNG.randInt(2): crypto.getRandomValues
   with rejection sampling, so heads and tails are exactly 50/50. */
(function(){
var $=function(id){return document.getElementById(id)},RNG=window.WVRNG;
function load(k){try{return localStorage.getItem(k)}catch(e){return null}}
function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
var REDUCE=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var PRESETS={ht:['Heads','Tails'],yn:['Yes','No'],n12:['1','2'],ab:['Team A','Team B']};
var KS='wv_coin_stats',KP='wv_coin_prefs',MAXL=14;

/* ---------- state ---------- */
var st={h:0,t:0,cur:0,curS:'',best:0,hist:[]};
try{var x=JSON.parse(load(KS)||'null');if(x&&typeof x.h==='number')st=x}catch(e){}
var pf={n:1,style:'gold',sound:false,faces:'ht',hl:'Heads',tl:'Tails'};
try{var y=JSON.parse(load(KP)||'null');if(y)for(var k in y)pf[k]=y[k]}catch(e){}
// shared link: ?h=Yes&t=No overrides faces for this visit
var q=new URLSearchParams(location.search);
if(q.get('h')&&q.get('t')){pf.faces='custom';pf.hl=q.get('h').slice(0,MAXL);pf.tl=q.get('t').slice(0,MAXL)}
if([1,2,3,5,10].indexOf(pf.n)<0)pf.n=1;
function save(){store(KS,JSON.stringify(st));store(KP,JSON.stringify(pf))}
function faces(){return pf.faces==='custom'?[pf.hl||'Heads',pf.tl||'Tails']:(PRESETS[pf.faces]||PRESETS.ht)}

/* ---------- coins ---------- */
var grid=$('cgrid'),res=$('cres'),tool=$('tool'),busy=false,coins=[];
function fsize(t){var n=t.length;return n<=2?'cf-xl':n<=5?'cf-l':n<=8?'cf-m':'cf-s'}
function build(){
 grid.innerHTML='';coins=[];grid.className='cgrid n'+pf.n;
 var F=faces();
 for(var i=0;i<pf.n;i++){
  var b=document.createElement('button');b.type='button';b.className='c3d';b.setAttribute('aria-label','Flip the coin');
  b.innerHTML='<span class="ctoss"><span class="cin"><span class="cf ch"></span><span class="cf ct"></span></span></span>';
  var h=b.querySelector('.ch'),t=b.querySelector('.ct');h.textContent=F[0];t.textContent=F[1];h.classList.add(fsize(F[0]));t.classList.add(fsize(F[1]));
  b.onclick=flip;grid.appendChild(b);coins.push({el:b,rot:0});
 }
 tool.setAttribute('data-style',pf.style);
 res.textContent=pf.n===1?'Tap the coin or press Flip':'Tap a coin or press Flip';
}

/* ---------- sound (off by default, synthesized) ---------- */
var ac=null;
function ping(){if(!pf.sound)return;try{ac=ac||new (window.AudioContext||window.webkitAudioContext)();
 var o=ac.createOscillator(),g=ac.createGain(),t=ac.currentTime;o.type='triangle';o.frequency.setValueAtTime(2100,t);o.frequency.exponentialRampToValueAtTime(1400,t+.25);
 g.gain.setValueAtTime(.0001,t);g.gain.exponentialRampToValueAtTime(.18,t+.01);g.gain.exponentialRampToValueAtTime(.0001,t+.45);o.connect(g);g.connect(ac.destination);o.start(t);o.stop(t+.5)}catch(e){}}

/* ---------- flip ---------- */
function flip(){
 if(busy)return;busy=true;var F=faces(),out=[];
 coins.forEach(function(c,i){
  var heads=RNG.randInt(2)===0;out.push(heads);
  var base=Math.ceil((c.rot+1)/360)*360,turns=REDUCE?0:360*(4+RNG.randInt(2));
  c.rot=base+turns+(heads?0:180);
  var inner=c.el.querySelector('.cin'),toss=c.el.querySelector('.ctoss');
  inner.style.transitionDelay=toss.style.animationDelay=(REDUCE?0:i*60)+'ms';
  inner.style.transform='rotateY('+c.rot+'deg)';
  c.el.setAttribute('aria-label',(heads?F[0]:F[1])+'. Flip again');
  if(!REDUCE){toss.classList.remove('up');void toss.offsetWidth;toss.classList.add('up')}
 });
 res.textContent='';res.classList.remove('show');
 var wait=REDUCE?0:1050+coins.length*60;
 setTimeout(function(){busy=false;ping();record(out,F)},wait);
}
function record(out,F){
 out.forEach(function(h){var s=h?'H':'T';h?st.h++:st.t++;if(s===st.curS)st.cur++;else{st.curS=s;st.cur=1}if(st.cur>st.best)st.best=st.cur;st.hist.unshift(s)});
 st.hist=st.hist.slice(0,24);save();
 var nh=out.filter(Boolean).length,n=out.length;
 res.textContent=n===1?(out[0]?F[0]:F[1]):(nh+' '+F[0]+' · '+(n-nh)+' '+F[1]);
 res.classList.add('show');stats();
}
function pct(a,b){return a+b?Math.round(a/(a+b)*100)+'%':''}
function stats(){
 var F=faces();
 $('sh').textContent=st.h;$('st').textContent=st.t;$('shl').textContent=(F[0]+' '+pct(st.h,st.t)).trim();$('stl').textContent=(F[1]+' '+pct(st.t,st.h)).trim();
 $('stot').textContent=st.h+st.t;$('scur').textContent=st.cur?st.cur+' '+(st.curS==='H'?F[0]:F[1]):'0';$('sbest').textContent=st.best;
 var hb=$('chist');hb.innerHTML='';
 st.hist.forEach(function(s){var i=document.createElement('span');i.className='hc '+(s==='H'?'hh':'ht');i.textContent=(s==='H'?F[0]:F[1]).charAt(0).toUpperCase();i.title=s==='H'?F[0]:F[1];hb.appendChild(i)});
 if(!st.hist.length)hb.innerHTML='<span class="hnone">Your last flips appear here</span>';
}

/* ---------- controls ---------- */
function seg(id,key,val,after){var bs=Array.prototype.slice.call($(id).querySelectorAll('button'));
 function val_(b){var v=b.getAttribute('data-v');return key==='n'?parseInt(v,10):v}
 function paint(){bs.forEach(function(b){b.setAttribute('aria-pressed',String(val_(b)===pf[key]))})}
 bs.forEach(function(b){b.onclick=function(){if(busy)return;pf[key]=val_(b);save();paint();after&&after()}});paint()}
function facesUI(){var c=pf.faces==='custom';$('cfcustom').hidden=!c;$('cfh').value=faces()[0];$('cft').value=faces()[1]}
seg('cn','n',null,build);seg('cs','style',null,function(){tool.setAttribute('data-style',pf.style)});
seg('cfaces','faces',null,function(){facesUI();build();stats()});
function onFace(){pf.hl=$('cfh').value.slice(0,MAXL);pf.tl=$('cft').value.slice(0,MAXL);save();build();stats()}
$('cfh').oninput=onFace;$('cft').oninput=onFace;
var sb=$('csound');function sUI(){sb.setAttribute('aria-pressed',String(pf.sound));sb.setAttribute('aria-label',pf.sound?'Sound on':'Sound off');sb.classList.toggle('on',pf.sound)}
sb.onclick=function(){pf.sound=!pf.sound;save();sUI();if(pf.sound)ping()};
$('cflip').onclick=flip;
$('creset').onclick=function(){st={h:0,t:0,cur:0,curS:'',best:0,hist:[]};save();stats()};
$('cshare').onclick=function(){var F=faces(),u=location.origin+location.pathname+(pf.faces==='ht'?'':'?h='+encodeURIComponent(F[0])+'&t='+encodeURIComponent(F[1])),b=this;
 try{navigator.clipboard.writeText(u);b.textContent='Link copied';setTimeout(function(){b.textContent='Share link'},1600)}catch(e){prompt('Copy this link',u)}};
$('cbatchgo').onclick=function(){
 var F=faces(),n=100,h=0,best=0,cur=0,prev=-1,seq=[];
 for(var i=0;i<n;i++){var r=RNG.randInt(2);seq.push(r);if(r===0)h++;if(r===prev)cur++;else cur=1;prev=r;if(cur>best)best=cur}
 var o=$('cbatch');o.hidden=false;
 o.innerHTML='<b></b><div class="bstrip"></div><p class="small"></p>';
 o.querySelector('b').textContent=h+' '+F[0]+' ('+h+'%) · '+(n-h)+' '+F[1]+' · longest streak '+best;
 var bs=o.querySelector('.bstrip');seq.forEach(function(r){var i=document.createElement('i');i.className=r===0?'hh':'ht';bs.appendChild(i)});
 o.querySelector('p').textContent='A separate batch of 100 flips. It is not added to your stats above.';
};
/* fullscreen */
var fb=$('cfs');
function isFs(){return document.fullscreenElement===tool||tool.classList.contains('is-cfs')}
function fsUI(){var on=isFs();fb.setAttribute('aria-label',on?'Exit fullscreen':'Fullscreen');document.body.classList.toggle('cfs-on',on)}
fb.onclick=function(){if(isFs()){if(document.fullscreenElement)document.exitFullscreen();tool.classList.remove('is-cfs')}
 else if(tool.requestFullscreen){tool.requestFullscreen().catch(function(){tool.classList.add('is-cfs');fsUI()})}else tool.classList.add('is-cfs');fsUI()};
document.addEventListener('fullscreenchange',fsUI);
document.addEventListener('keydown',function(e){
 var tag=document.activeElement&&document.activeElement.tagName;
 if(/INPUT|TEXTAREA|SELECT/.test(tag))return;
 if(e.code==='Space'&&!/BUTTON|A/.test(tag)){e.preventDefault();flip()}
 else if((e.key==='f'||e.key==='F')&&!e.ctrlKey&&!e.metaKey){fb.click()}
 else if(e.key==='Escape'&&tool.classList.contains('is-cfs')){tool.classList.remove('is-cfs');fsUI()}});
sUI();facesUI();build();stats();
})();
