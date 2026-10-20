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
document.addEventListener('keydown',function(e){if(e.key==='Enter'&&e.target.tagName==='INPUT'){e.preventDefault();$('ggo').click()}});
$('ggo').click();
var bg=$('burger'),nv=$('mnav');bg.onclick=function(){var o=!nv.classList.contains('open');nv.classList.toggle('open',o);bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?'Close menu':'Open menu')};
nv.addEventListener('click',function(e){if(e.target.tagName==='A'){nv.classList.remove('open');bg.setAttribute('aria-expanded',false)}});
var th=$('theme'),root=document.documentElement,mt=document.querySelector('meta[name=theme-color]');function applyT(t){root.setAttribute('data-theme',t);th.setAttribute('aria-label',t==='light'?'Switch to dark mode':'Switch to light mode');if(mt)mt.setAttribute('content',t==='light'?'#F6F6F9':'#0A0A0C')}
applyT(root.getAttribute('data-theme')||'dark');th.onclick=function(){var t=root.getAttribute('data-theme')==='light'?'dark':'light';applyT(t);store('wv_theme',t)};
})();
