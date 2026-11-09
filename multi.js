/* Wheelova multiple wheels (Name Picker page), modelled on the familiar "Add wheel" pattern:
   "+ Add wheel" under the entries box turns the page into 2–6 wheels side by side. One editor with a tab per wheel,
   "Spin all wheels" under the box, and each wheel can also be spun on its own (click it or its SPIN button).
   Winners come from a continuous random angle (WVRNG), same method as the single wheel.
   State is saved only in this browser (localStorage "wv_multi"). */
(function init(){
if(!window.WVRNG){if(!init.w){init.w=1;document.addEventListener('DOMContentLoaded',init)}return}
var $=function(id){return document.getElementById(id)},RNG=window.WVRNG;
var root=$('multi'),single=$('npone')||$('tool'),addBtn=$('npadd');if(!root||!single||!addBtn)return;
var CFG=window.WV||{},T=CFG.t||{},L=function(k,d){return T[k]||d};
var COLORS=['#6E56F0','#E11D48','#F59E0B','#16A34A','#2563EB','#DB2777','#0D9488','#EA580C'];
var MAX=6,KEY='wv_multi'+(CFG.key&&CFG.key!=='names'?'_'+CFG.key:''),TAU=Math.PI*2;
var grid=$('mgrid'),tabs=$('mtabs'),ta=$('mta'),ti=$('mtitle'),ck=$('mrem'),cnt=$('mcnt'),log=$('mlog'),logs=[];
var W=[],sel=0;
function mainEntries(){var m=$('entries');return m?m.value.split('\n').map(function(s){return s.trim()}).filter(Boolean):[]}
function save(on){try{localStorage.setItem(KEY,JSON.stringify({on:on!==false&&!root.hidden,sel:sel,w:W.map(function(w){return{t:w.t,e:w.e,r:w.r}})}))}catch(e){}}
function load(){try{var v=JSON.parse(localStorage.getItem(KEY));if(v&&v.w&&v.w.length>=2)return v}catch(e){}return null}
function OPTS(){var o=L('m_option','Option');return[o+' 1',o+' 2',o+' 3',o+' 4']}
function mk(t,e,r){return{t:t||'',e:(e||[]).slice(),r:!!r,rot:0,busy:false}}
function lum(h){h=h.replace('#','');var r=parseInt(h.substr(0,2),16),g=parseInt(h.substr(2,2),16),b=parseInt(h.substr(4,2),16);return(0.2126*r+0.7152*g+0.0722*b)/255}
function reduce(){return matchMedia('(prefers-reduced-motion: reduce)').matches}
function title(i){return (W[i].t||'').trim()||(L('m_wheel','Wheel')+' '+(i+1))}
function draw(w){var cv=w.cv;if(!cv)return;var c=cv.getContext('2d'),S=cv.width,R=S/2,n=w.e.length;c.clearRect(0,0,S,S);
 if(!n){c.fillStyle='#1E1E27';c.beginPath();c.arc(R,R,R,0,TAU);c.fill();c.fillStyle='#8A8A97';c.font='600 28px Inter,sans-serif';c.textAlign='center';c.fillText(L('empty','Add entries'),R,R+110);return}
 var seg=TAU/n,base=Math.min(40,Math.max(9,(TAU*R*0.6/n)*0.46)),maxW=R-24-70;c.save();c.translate(R,R);c.rotate(w.rot);
 for(var i=0;i<n;i++){var a0=-Math.PI/2+i*seg,k=(n%COLORS.length===1&&i===n-1&&n>1)?1:i%COLORS.length,f=COLORS[k];
  c.beginPath();c.moveTo(0,0);c.arc(0,0,R,a0,a0+seg);c.closePath();c.fillStyle=f;c.fill();
  c.save();c.rotate(a0+seg/2);c.textAlign='right';c.textBaseline='middle';c.fillStyle=lum(f)>0.62?'#141418':'#FFFFFF';
  var t=w.e[i];if(t.length>22)t=t.slice(0,21)+'…';var fs=base;c.font='600 '+fs+'px Inter,sans-serif';var tw=c.measureText(t).width;if(tw>maxW){fs=Math.max(9,fs*maxW/tw);c.font='600 '+fs+'px Inter,sans-serif'}
  c.fillText(t,R-24,0);c.restore()}
 c.restore()}
function idxAt(w){var n=w.e.length,seg=TAU/n,a=((-w.rot)%TAU+TAU)%TAU;return Math.min(n-1,Math.floor(a/seg))}
function spin(i,done){var w=W[i];
 if(w.busy)return done&&done(null);if(w.e.length<2){w.res.textContent=L('add2','Add at least two entries');return done&&done(null)}
 w.busy=true;w.btn.disabled=true;w.res.textContent=L('spinning','Spinning…');
 var start=w.rot,target=start+TAU*(5+RNG.rand())+RNG.rand()*TAU,dur=reduce()?0:4200+RNG.randInt(800),t0=performance.now();
 function step(now){var p=dur?Math.min(1,(now-t0)/dur):1,ease=1-Math.pow(1-p,4);w.rot=start+(target-start)*ease;draw(w);
  if(p<1){requestAnimationFrame(step);return}
  w.rot=target%TAU;var k=idxAt(w),win=w.e[k];w.res.innerHTML='';var b=document.createElement('b');b.textContent=win;w.res.appendChild(b);
  if(w.r){w.e.splice(k,1);draw(w);if(i===sel)fillEditor();updTab(i);save()}
  w.busy=false;w.btn.disabled=false;done&&done(win)}
 requestAnimationFrame(step)}
function addLog(parts){logs.unshift(parts);if(logs.length>100)logs.pop();renderLog()}
function renderLog(){log.innerHTML='';logs.forEach(function(p){var li=document.createElement('li');li.textContent=p.map(function(x){return x[0]+': '+x[1]}).join(' · ');log.appendChild(li)});$('mlogwrap').hidden=!logs.length}
function updTab(i){var b=tabs.children[i];if(b){b.firstChild.textContent=title(i);b.lastChild.textContent=W[i].e.length}var w=W[i];if(w&&w.lab)w.lab.textContent=title(i)}
function renderTabs(){tabs.innerHTML='';W.forEach(function(w,i){var b=document.createElement('button');b.type='button';b.setAttribute('role','tab');b.setAttribute('aria-selected',i===sel);b.tabIndex=i===sel?0:-1;
  b.innerHTML='<span></span><span class="mtc"></span>';b.firstChild.textContent=title(i);b.lastChild.textContent=w.e.length;b.onclick=function(){select(i)};tabs.appendChild(b)});
 $('madd').disabled=W.length>=MAX;$('madd').textContent=W.length>=MAX?L('m_max','Maximum 6 wheels'):L('m_add','+ Add wheel')}
function fillEditor(){var w=W[sel];ta.value=w.e.join('\n');ti.value=w.t;ti.placeholder=L('m_wheel','Wheel')+' '+(sel+1);ck.checked=w.r;cnt.textContent=w.e.length}
function select(i){sel=i;renderTabs();fillEditor();for(var k=0;k<W.length;k++)W[k].card.classList.toggle('on',k===sel);save()}
function card(i){var w=W[i],d=document.createElement('div');d.className='mcard';
 d.innerHTML='<button type="button" class="mlab"></button><div class="mwheel"><div class="mptr" aria-hidden="true"></div><canvas width="480" height="480" role="img"></canvas><button type="button" class="mspin">SPIN</button></div><p class="mres" aria-live="polite"></p>';
 w.card=d;w.cv=d.querySelector('canvas');w.btn=d.querySelector('.mspin');w.res=d.querySelector('.mres');w.lab=d.querySelector('.mlab');
 w.lab.textContent=title(i);w.lab.onclick=function(){select(i)};w.cv.setAttribute('aria-label',title(i));w.btn.setAttribute('aria-label',L('m_spin','Spin')+': '+title(i));w.btn.textContent=L('m_spinbtn','SPIN');
 var go=function(){select(i);spin(i,function(win){if(win!==null)addLog([[title(i),win]])})};w.btn.onclick=go;w.cv.onclick=go;
 draw(w);return d}
function renderWheels(){grid.innerHTML='';grid.className='mgrid n'+W.length;W.forEach(function(w,i){grid.appendChild(card(i))});for(var k=0;k<W.length;k++)W[k].card.classList.toggle('on',k===sel)}
function render(){renderWheels();renderTabs();fillEditor()}
function enter(state){
 if(state){W=state.w.map(function(w){return mk(w.t,w.e,w.r)});sel=Math.min(state.sel||0,W.length-1)}
 else{var rem=$('remove');W=[mk('', mainEntries(), rem&&rem.checked),mk('',OPTS(),false)];sel=1}
 single.hidden=true;root.hidden=false;render();save();ta.focus()}
function leave(){var w=W[0],m=$('entries');single.hidden=false;root.hidden=true;
 if(m){m.value=w.e.join('\n');m.dispatchEvent(new Event('input',{bubbles:true}))}
 save(false);W=[];addBtn.focus()}
addBtn.onclick=function(){enter(null)};
$('madd').onclick=function(){if(W.length>=MAX)return;W.push(mk('',OPTS(),false));sel=W.length-1;render();save();ta.focus()};
$('mdel').onclick=function(){if(W.length<=2){W.splice(sel,1);sel=0;leave();return}W.splice(sel,1);sel=Math.max(0,sel-1);render();save()};
ta.oninput=function(){var w=W[sel];w.e=ta.value.split('\n').map(function(s){return s.trim()}).filter(Boolean);cnt.textContent=w.e.length;draw(w);updTab(sel);save()};
ti.oninput=function(){W[sel].t=ti.value;updTab(sel);save()};
ck.onchange=function(){W[sel].r=ck.checked;save()};
$('mall').onclick=function(){var out=[],left=W.length,b=$('mall');b.disabled=true;
 W.forEach(function(w,i){spin(i,function(win){out[i]=win===null?null:[title(i),win];if(--left===0){b.disabled=false;var p=out.filter(Boolean);if(p.length)addLog(p)}})})};
$('mcopy').onclick=function(){var t=logs.map(function(p){return p.map(function(x){return x[0]+': '+x[1]}).join(' | ')}).join('\n');try{navigator.clipboard.writeText(t);var cb=$('mcopy'),old=cb.textContent;cb.textContent=L('copied','Copied');setTimeout(function(){cb.textContent=old},1500)}catch(e){}};
$('mclear').onclick=function(){logs=[];renderLog()};
document.addEventListener('keydown',function(e){if(root.hidden)return;var a=document.activeElement;if(a&&/INPUT|TEXTAREA|SELECT|BUTTON/.test(a.tagName))return;if(e.code==='Space'){e.preventDefault();e.stopImmediatePropagation();$('mall').click()}},true);

/* Fullscreen for the multiple-wheels view: real fullscreen where allowed, a full-window overlay otherwise (iPhone). */
var fsb=$('mfs'),bd=document.body;
function fit(){if(!bd.classList.contains('is-mfs'))return;var n=W.length,gw=window.innerWidth-(window.innerWidth<600?24:48),gh=window.innerHeight-96,best=0,bc=1;
 for(var cols=1;cols<=n;cols++){var rows=Math.ceil(n/cols),s=Math.min((gw-(cols-1)*16)/cols-12,(gh-(rows-1)*16)/rows-60);if(s>best){best=s;bc=cols}}
 root.style.setProperty('--mw',Math.max(110,Math.floor(best))+'px');grid.style.gridTemplateColumns='repeat('+bc+',auto)'}
function setMfs(on){bd.classList.toggle('is-mfs',on);fsb.setAttribute('aria-label',on?L('exitfs','Exit fullscreen'):L('fs','Fullscreen'));
 try{if(on&&document.documentElement.requestFullscreen&&!document.fullscreenElement)document.documentElement.requestFullscreen().catch(function(){});if(!on&&document.fullscreenElement)document.exitFullscreen().catch(function(){})}catch(e){}
 if(on)fit();else{root.style.removeProperty('--mw');grid.style.gridTemplateColumns=''}}
fsb.onclick=function(){setMfs(!bd.classList.contains('is-mfs'))};
$('mfsall').onclick=function(){$('mall').click()};
document.addEventListener('fullscreenchange',function(){if(!document.fullscreenElement&&bd.classList.contains('is-mfs'))setMfs(false)});
window.addEventListener('resize',fit);
document.addEventListener('keydown',function(e){if(root.hidden)return;var a=document.activeElement,typing=a&&/INPUT|TEXTAREA|SELECT/.test(a.tagName);
 if(e.key==='Escape'&&bd.classList.contains('is-mfs')){setMfs(false);return}
 if((e.key==='f'||e.key==='F')&&!typing&&!e.ctrlKey&&!e.metaKey){e.preventDefault();e.stopImmediatePropagation();setMfs(!bd.classList.contains('is-mfs'))}},true);
var _leave=leave;leave=function(){if(bd.classList.contains('is-mfs'))setMfs(false);_leave()};
var _rw=renderWheels;renderWheels=function(){_rw();fit()};
var st=load();if(st&&st.on&&!/[#&]w=/.test(location.hash))enter(st);
})();
