/* Wheelova multiple wheels (Name Picker page). 2–6 independent wheels; spin one or spin all.
   Winners are chosen from a continuous random angle (WVRNG), same method as the main wheel.
   Lists are saved only in this browser (localStorage "wv_multi"). */
(function init(){
if(!window.WVRNG){if(!init.w){init.w=1;document.addEventListener('DOMContentLoaded',init)}return}
var $=function(id){return document.getElementById(id)},RNG=window.WVRNG;
var root=$('multi'),tabs=document.querySelectorAll('[data-npmode]');if(!root||!RNG)return;
var COLORS=['#6E56F0','#E11D48','#F59E0B','#16A34A','#2563EB','#DB2777','#0D9488','#EA580C'];
var MAX=6,MIN=2,KEY='wv_multi',TAU=Math.PI*2;
var DEF=[{t:'Student',e:['Emma','Liam','Olivia','Noah','Ava','Elijah','Sophia','Lucas'],r:true},{t:'Question',e:['Question 1','Question 2','Question 3','Question 4','Question 5','Question 6'],r:true}];
function load(){try{var v=JSON.parse(localStorage.getItem(KEY));if(v&&v.length>=MIN)return v.slice(0,MAX)}catch(e){}return JSON.parse(JSON.stringify(DEF))}
function save(){try{localStorage.setItem(KEY,JSON.stringify(W.map(function(w){return{t:w.t,e:w.e,r:w.r}})))}catch(e){}}
function lum(h){h=h.replace('#','');var r=parseInt(h.substr(0,2),16),g=parseInt(h.substr(2,2),16),b=parseInt(h.substr(4,2),16);return(0.2126*r+0.7152*g+0.0722*b)/255}
var W=load().map(function(w){return{t:w.t||'',e:(w.e||[]).slice(),r:!!w.r,rot:0,busy:false,last:null}});
var grid=$('mgrid'),log=$('mlog'),logs=[];
function reduce(){return matchMedia('(prefers-reduced-motion: reduce)').matches}
function draw(w){var cv=w.cv,c=cv.getContext('2d'),S=cv.width,R=S/2,n=w.e.length;c.clearRect(0,0,S,S);
 if(!n){c.fillStyle='#1E1E27';c.beginPath();c.arc(R,R,R,0,TAU);c.fill();c.fillStyle='#8A8A97';c.font='600 28px Inter,sans-serif';c.textAlign='center';c.fillText('Add entries',R,R+110);return}
 var seg=TAU/n,base=Math.min(40,Math.max(9,(TAU*R*0.6/n)*0.46)),maxW=R-24-70;c.save();c.translate(R,R);c.rotate(w.rot);
 for(var i=0;i<n;i++){var a0=-Math.PI/2+i*seg,k=(n%COLORS.length===1&&i===n-1&&n>1)?1:i%COLORS.length,f=COLORS[k];
  c.beginPath();c.moveTo(0,0);c.arc(0,0,R,a0,a0+seg);c.closePath();c.fillStyle=f;c.fill();
  c.save();c.rotate(a0+seg/2);c.textAlign='right';c.textBaseline='middle';c.fillStyle=lum(f)>0.62?'#141418':'#FFFFFF';
  var t=w.e[i];if(t.length>22)t=t.slice(0,21)+'…';var fs=base;c.font='600 '+fs+'px Inter,sans-serif';var tw=c.measureText(t).width;if(tw>maxW){fs=Math.max(9,fs*maxW/tw);c.font='600 '+fs+'px Inter,sans-serif'}
  c.fillText(t,R-24,0);c.restore()}
 c.restore()}
function idxAt(w){var n=w.e.length,seg=TAU/n,a=((-w.rot)%TAU+TAU)%TAU;return Math.min(n-1,Math.floor(a/seg))}
function spin(w,done){
 if(w.busy)return done&&done(null);if(w.e.length<2){w.res.textContent='Add at least two entries';return done&&done(null)}
 w.busy=true;w.btn.disabled=true;w.res.textContent='Spinning…';
 var start=w.rot,target=start+TAU*(5+RNG.rand())+RNG.rand()*TAU,dur=reduce()?0:4200+RNG.randInt(800),t0=performance.now();
 function step(now){var p=dur?Math.min(1,(now-t0)/dur):1,ease=1-Math.pow(1-p,4);w.rot=start+(target-start)*ease;draw(w);
  if(p<1){requestAnimationFrame(step);return}
  w.rot=target%TAU;var i=idxAt(w),win=w.e[i];w.last=win;w.res.innerHTML='';var b=document.createElement('b');b.textContent=win;w.res.appendChild(b);
  if(w.r){w.e.splice(i,1);w.ta.value=w.e.join('\n');save();draw(w);w.cnt.textContent='· '+w.e.length}
  w.busy=false;w.btn.disabled=false;done&&done(win)}
 requestAnimationFrame(step)}
function addLog(parts){logs.unshift(parts);if(logs.length>100)logs.pop();renderLog()}
function renderLog(){log.innerHTML='';logs.forEach(function(p,i){var li=document.createElement('li');li.textContent=p.map(function(x){return x[0]+': '+x[1]}).join(' · ');log.appendChild(li)});$('mlogwrap').hidden=!logs.length}
function title(w,i){return (w.t||'').trim()||('Wheel '+(i+1))}
function card(w,i){
 var d=document.createElement('div');d.className='mcard';
 d.innerHTML='<div class="mhead"><input class="mtitle" maxlength="40" aria-label="Wheel name"><span class="mcnt"></span><button type="button" class="linkbtn mdel" aria-label="Remove this wheel">Remove</button></div>'+
  '<div class="mwheel"><div class="mptr" aria-hidden="true"></div><canvas width="480" height="480" role="img"></canvas><button type="button" class="mspin">SPIN</button></div>'+
  '<p class="mres" aria-live="polite"></p>'+
  '<textarea rows="5" spellcheck="false" aria-label="Entries, one per line"></textarea>'+
  '<label class="ck"><input type="checkbox"> Remove winner after each spin</label>';
 w.cv=d.querySelector('canvas');w.btn=d.querySelector('.mspin');w.res=d.querySelector('.mres');w.ta=d.querySelector('textarea');w.cnt=d.querySelector('.mcnt');
 var ti=d.querySelector('.mtitle'),ck=d.querySelector('input[type=checkbox]');
 ti.value=w.t;ti.placeholder='Wheel '+(i+1);w.ta.value=w.e.join('\n');ck.checked=w.r;w.cnt.textContent='· '+w.e.length;
 w.cv.setAttribute('aria-label',title(w,i)+' wheel');w.btn.setAttribute('aria-label','Spin '+title(w,i));
 ti.oninput=function(){w.t=ti.value;save();w.btn.setAttribute('aria-label','Spin '+title(w,i))};
 w.ta.oninput=function(){w.e=w.ta.value.split('\n').map(function(s){return s.trim()}).filter(Boolean);w.cnt.textContent='· '+w.e.length;save();draw(w)};
 ck.onchange=function(){w.r=ck.checked;save()};
 w.btn.onclick=function(){spin(w,function(win){if(win!==null)addLog([[title(w,i),win]])})};
 d.querySelector('.mdel').onclick=function(){if(W.length<=MIN)return;W.splice(i,1);save();render()};
 d.querySelector('.mdel').hidden=W.length<=MIN;
 draw(w);return d}
function render(){grid.innerHTML='';W.forEach(function(w,i){grid.appendChild(card(w,i))});$('madd').disabled=W.length>=MAX;$('madd').textContent=W.length>=MAX?'Maximum 6 wheels':'+ Add wheel'}
$('madd').onclick=function(){if(W.length>=MAX)return;W.push({t:'',e:['Option 1','Option 2','Option 3','Option 4'],r:false,rot:0,busy:false});save();render();var c=grid.lastChild.querySelector('.mtitle');if(c)c.focus()};
$('mall').onclick=function(){var out=[],left=W.length,b=$('mall');b.disabled=true;
 W.forEach(function(w,i){spin(w,function(win){out[i]=win===null?null:[title(w,i),win];if(--left===0){b.disabled=false;var p=out.filter(Boolean);if(p.length)addLog(p)}})})};
$('mcopy').onclick=function(){var t=logs.map(function(p){return p.map(function(x){return x[0]+': '+x[1]}).join(' | ')}).join('\n');try{navigator.clipboard.writeText(t);$('mcopy').textContent='Copied';setTimeout(function(){$('mcopy').textContent='Copy'},1500)}catch(e){}};
$('mclear').onclick=function(){logs=[];renderLog()};
function setMode(m){var multi=m==='multi';root.hidden=!multi;var one=$('npone');if(one)one.hidden=multi;
 for(var i=0;i<tabs.length;i++){var on=tabs[i].getAttribute('data-npmode')===m;tabs[i].setAttribute('aria-selected',on);tabs[i].tabIndex=on?0:-1}
 try{localStorage.setItem('wv_np_mode',m)}catch(e){}if(multi&&!grid.firstChild)render()}
for(var i=0;i<tabs.length;i++)tabs[i].onclick=function(){setMode(this.getAttribute('data-npmode'))};
document.addEventListener('keydown',function(e){if(root.hidden)return;var a=document.activeElement;if(a&&/INPUT|TEXTAREA|SELECT|BUTTON/.test(a.tagName))return;if(e.code==='Space'){e.preventDefault();e.stopImmediatePropagation();$('mall').click()}},true);
var m='one';try{m=localStorage.getItem('wv_np_mode')||'one'}catch(e){}if(/[#&]w=/.test(location.hash))m='one';
setMode(m);
})();
