(function(){
var cfg=window.WG||{},$=function(id){return document.getElementById(id)};
function rand(){var a=new Uint32Array(1);crypto.getRandomValues(a);return a[0]/4294967296}
function ri(n){return Math.floor(rand()*n)}
function shuffle(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=ri(i+1),t=a[i];a[i]=a[j];a[j]=t}return a}
function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
function load(k){try{return localStorage.getItem(k)}catch(e){return null}}
var out=$('gout'),err=$('gerr'),last=[];
function show(items,big){out.innerHTML='';out.className='gout'+(big?' big':'');
items.forEach(function(t){var s=document.createElement('span');s.className='gitem';s.textContent=t;out.appendChild(s)});
last=items;$('gcount').textContent=items.length+' result'+(items.length===1?'':'s');
var h=$('ghist');if(h){var li=document.createElement('li');li.textContent=items.slice(0,20).join(', ')+(items.length>20?' …':'');h.prepend(li);while(h.children.length>10)h.removeChild(h.lastChild)}}
function fail(m){err.textContent=m}
$('gcopy').onclick=function(){var txt=cfg.type==='team'?Array.prototype.map.call(out.querySelectorAll('.team'),function(t){return t.innerText}).join('\n\n'):last.join(cfg.type==='number'?', ':'\n');
try{navigator.clipboard.writeText(txt);this.textContent='Copied';var b=this;setTimeout(function(){b.textContent='Copy'},1400)}catch(e){}};

if(cfg.type==='number'){
 function run(){err.textContent='';var a=parseInt($('nmin').value,10),b=parseInt($('nmax').value,10),c=parseInt($('ncount').value,10),u=$('nuniq').checked,s=$('nsort').checked;
  if(isNaN(a)||isNaN(b)){return fail('Enter whole numbers for From and To.')}
  if(b<a){var t=a;a=b;b=t}
  if(isNaN(c)||c<1)c=1;if(c>1000)return fail('Up to 1,000 numbers at a time.');
  var span=b-a+1;if(u&&c>span)return fail('You asked for '+c+' unique numbers but the range only has '+span+'. Widen the range or allow repeats.');
  var r=[];if(u){var seen={};while(r.length<c){var x=a+ri(span);if(!seen[x]){seen[x]=1;r.push(x)}}}else{for(var i=0;i<c;i++)r.push(a+ri(span))}
  if(s)r.sort(function(p,q){return p-q});show(r.map(String),c===1);store('wg_num',JSON.stringify([a,b,c,u,s]))}
 try{var sv=JSON.parse(load('wg_num'));if(sv){$('nmin').value=sv[0];$('nmax').value=sv[1];$('ncount').value=sv[2];$('nuniq').checked=sv[3];$('nsort').checked=sv[4]}}catch(e){}
 Array.prototype.forEach.call(document.querySelectorAll('[data-range]'),function(b){b.onclick=function(){var p=b.dataset.range.split('-');$('nmin').value=p[0];$('nmax').value=p[1];$('ncount').value=1;run()}});
 $('ggo').onclick=run;
}
if(cfg.type==='team'){
 var ta=$('tnames');ta.value=load('wg_team')||cfg.sample.join('\n');
 function names(){return ta.value.split('\n').map(function(s){return s.trim()}).filter(Boolean)}
 function upd(){$('tcount').textContent='· '+names().length;store('wg_team',ta.value)}ta.addEventListener('input',upd);upd();
 function run(){err.textContent='';var n=names(),mode=$('tmode').value,k=parseInt($('tnum').value,10);
  if(n.length<2)return fail('Add at least two names.');if(isNaN(k)||k<1)return fail('Enter how many teams or people per team.');
  var teams=mode==='teams'?k:Math.ceil(n.length/k);if(teams<2)return fail('That makes only one team. Lower the number.');if(teams>n.length)return fail('More teams than people. Lower the number of teams.');
  var s=shuffle(n),g=[];for(var i=0;i<teams;i++)g.push([]);s.forEach(function(p,i){g[i%teams].push(p)});
  out.innerHTML='';out.className='gout teams';last=[];
  g.forEach(function(t,i){var d=document.createElement('div');d.className='team';var h=document.createElement('b');h.textContent='Team '+(i+1)+' ('+t.length+')';d.appendChild(h);
   var ul=document.createElement('ul');t.forEach(function(p){var li=document.createElement('li');li.textContent=p;ul.appendChild(li)});d.appendChild(ul);out.appendChild(d);last.push(t.join(', '))});
  $('gcount').textContent=teams+' teams · '+n.length+' people'}
 $('ggo').onclick=run;
}
if(cfg.type==='name'){
 var D=cfg.data;
 function run(){err.textContent='';var g=$('ngender').value,c=parseInt($('ncount').value,10),full=$('nfull').checked;if(isNaN(c)||c<1)c=1;if(c>100)return fail('Up to 100 names at a time.');
  var pool=g==='female'?D.female:g==='male'?D.male:D.female.concat(D.male),r=[],seen={},tries=0;
  while(r.length<c&&tries<5000){tries++;var nm=pool[ri(pool.length)]+(full?' '+D.last[ri(D.last.length)]:'');if(!seen[nm]){seen[nm]=1;r.push(nm)}}
  show(r,c===1)}
 $('ggo').onclick=run;
}

if(cfg.type==='coin'){
 var tot={h:0,t:0};
 function runc(){err.textContent='';var n=parseInt($('ccount').value,10)||1,r=[],best=0,cur=0,prev=null;
  for(var i=0;i<n;i++){var s=rand()<0.5?'Heads':'Tails';r.push(s);if(s===prev)cur++;else cur=1;prev=s;if(cur>best)best=cur;s==='Heads'?tot.h++:tot.t++}
  out.innerHTML='';out.className='gout'+(n===1?' big coinout':'');
  if(n===1){var c=document.createElement('div');c.className='coin '+(r[0]==='Heads'?'heads':'tails');c.innerHTML='<span></span>';c.querySelector('span').textContent=r[0]==='Heads'?'H':'T';out.appendChild(c);var l=document.createElement('div');l.className='coinlbl';l.textContent=r[0];out.appendChild(l)}
  else{r.forEach(function(s){var x=document.createElement('span');x.className='gitem '+(s==='Heads'?'ch':'ct');x.textContent=s==='Heads'?'H':'T';x.title=s;out.appendChild(x)})}
  var h=r.filter(function(s){return s==='Heads'}).length;last=r;
  $('gcount').textContent=n===1?('Session: '+tot.h+' heads · '+tot.t+' tails'):(h+' heads ('+Math.round(h/n*100)+'%) · '+(n-h)+' tails · longest streak '+best);
  var hi=$('ghist');if(hi){var li=document.createElement('li');li.textContent=n===1?r[0]:(n+' flips: '+h+' H / '+(n-h)+' T');hi.prepend(li);while(hi.children.length>10)hi.removeChild(hi.lastChild)}}
 $('ggo').onclick=runc;
}
if(cfg.type==='dice'){
 var PIPS={1:[5],2:[1,9],3:[1,5,9],4:[1,3,7,9],5:[1,3,5,7,9],6:[1,3,4,6,7,9]};
 function rund(){err.textContent='';var n=parseInt($('dcount').value,10)||1,s=parseInt($('dsides').value,10)||6,r=[];for(var i=0;i<n;i++)r.push(1+Math.floor(rand()*s));
  out.innerHTML='';out.className='gout diceout';
  r.forEach(function(v){var d=document.createElement('div');d.className='die'+(s===6?' pips':'');d.setAttribute('aria-label',v);
   if(s===6){for(var k=1;k<=9;k++){var p=document.createElement('i');if(PIPS[v].indexOf(k)>-1)p.className='on';d.appendChild(p)}}else{d.textContent=v}out.appendChild(d)});
  var sum=r.reduce(function(a,b){return a+b},0);last=r.map(String);
  $('gcount').textContent=n>1?('Total: '+sum):(n+'d'+s);
  var tl=document.createElement('div');tl.className='dicetotal';tl.textContent=n>1?('Total '+sum):('You rolled '+sum);out.appendChild(tl);
  var hi=$('ghist');if(hi){var li=document.createElement('li');li.textContent=n+'d'+s+': '+r.join(' + ')+(n>1?' = '+sum:'');hi.prepend(li);while(hi.children.length>10)hi.removeChild(hi.lastChild)}}
 $('ggo').onclick=rund;
}
document.addEventListener('keydown',function(e){if(e.key==='Enter'&&e.target.tagName==='INPUT'){e.preventDefault();$('ggo').click()}
if((cfg.type==='coin'||cfg.type==='dice')&&e.code==='Space'&&!/TEXTAREA|INPUT|SELECT|BUTTON|A/.test(document.activeElement.tagName)){e.preventDefault();$('ggo').click()}});
if(cfg.type==='coin'||cfg.type==='dice'){out.innerHTML='<div class="gwait">'+(cfg.type==='coin'?'Press Flip':'Press Roll')+'</div>'}else{$('ggo').click()}
var lg=document.querySelector('.logo');if(lg)lg.addEventListener('click',function(){try{localStorage.removeItem('wv_entries_home2')}catch(e){}});
var bg=$('burger'),nv=$('mnav');bg.onclick=function(){var o=!nv.classList.contains('open');nv.classList.toggle('open',o);bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?'Close menu':'Open menu')};
nv.addEventListener('click',function(e){if(e.target.tagName==='A'){nv.classList.remove('open');bg.setAttribute('aria-expanded',false)}});
var th=$('theme'),root=document.documentElement,mt=document.querySelector('meta[name=theme-color]');function applyT(t){root.setAttribute('data-theme',t);th.setAttribute('aria-label',t==='light'?'Switch to dark mode':'Switch to light mode');if(mt)mt.setAttribute('content',t==='light'?'#F6F6F9':'#0A0A0C')}
applyT(root.getAttribute('data-theme')||'dark');th.onclick=function(){var t=root.getAttribute('data-theme')==='light'?'dark':'light';applyT(t);store('wv_theme',t)};
})();
