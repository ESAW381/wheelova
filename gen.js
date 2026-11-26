(function(){
var cfg=window.WG||{},$=function(id){return document.getElementById(id)};
var RNG=window.WVRNG,rand=RNG.rand,ri=RNG.randInt,shuffle=RNG.shuffle;
function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
function load(k){try{return localStorage.getItem(k)}catch(e){return null}}
var out=$('gout')||document.createElement('div'),err=$('gerr')||document.createElement('p'),last=[];
function show(items,big){out.innerHTML='';out.className='gout'+(big?' big':'');
items.forEach(function(t){var s=document.createElement('span');s.className='gitem';s.textContent=t;out.appendChild(s)});
last=items;$('gcount').textContent=items.length+' result'+(items.length===1?'':'s');
var h=$('ghist');if(h){var li=document.createElement('li');li.textContent=items.slice(0,20).join(', ')+(items.length>20?' …':'');h.prepend(li);while(h.children.length>10)h.removeChild(h.lastChild)}}
function fail(m){err.textContent=m}
if($('gcopy'))$('gcopy').onclick=function(){var txt=cfg.type==='list'?(window.WGLIST?window.WGLIST():''):cfg.type==='pair'?last.join('\n'):cfg.type==='team'?Array.prototype.map.call(out.querySelectorAll('.team'),function(t){return t.innerText}).join('\n\n'):last.join(cfg.type==='number'?', ':'\n');
try{navigator.clipboard.writeText(txt);this.textContent='Copied';var b=this;setTimeout(function(){b.textContent='Copy'},1400)}catch(e){}};

if(cfg.type==='number'){
 function int(v){v=String(v).trim();return /^-?\d+$/.test(v)?Number(v):NaN}
 function run(){err.textContent='';var a=int($('nmin').value),b=int($('nmax').value),c=int($('ncount').value),u=$('nuniq').checked,s=$('nsort').checked,M=Number.MAX_SAFE_INTEGER;
  if(isNaN(a)||isNaN(b)){return fail('Enter whole numbers for From and To (digits only, e.g. 1 and 100).')}
  if(Math.abs(a)>M||Math.abs(b)>M){return fail('Numbers must be between -9,007,199,254,740,991 and 9,007,199,254,740,991.')}
  if(b<a){var t=a;a=b;b=t}
  if(isNaN(c)||c<1)c=1;if(c>1000)return fail('Up to 1,000 numbers at a time.');
  var span=b-a+1;if(span>9007199254740992)return fail('That range is too large. Use a range of at most 9,007,199,254,740,992 numbers.');if(u&&c>span)return fail('You asked for '+c+' unique numbers but the range only has '+span+'. Widen the range or allow repeats.');
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
if(cfg.type==='pair'){
 var pa=$('pnames');pa.value=load('wg_pair')||cfg.sample.join('\n');
 function pn(){return pa.value.split('\n').map(function(s){return s.trim()}).filter(Boolean)}
 function pu(){$('pcount').textContent='· '+pn().length;store('wg_pair',pa.value)}pa.addEventListener('input',pu);pu();
 var pb=$('pnames2'),pw=$('pbwrap'),pml=document.querySelector('label[for="pnames"]'),pmd=$('pmode');if(pb){pb.value=load('wg_pair2')||'';
 function pn2(){return pb.value.split('\n').map(function(s){return s.trim()}).filter(Boolean)}
 function pu2(){$('pcount2').textContent='· '+pn2().length;store('wg_pair2',pb.value)}pb.addEventListener('input',pu2);pu2();
 function pmv(){var two=pmd.value==='two';pw.hidden=!two;$('poddl').style.display=two?'none':'';pml.firstChild.nodeValue=two?'List A ':'Names ';store('wg_pmode',pmd.value)}
 var sm=load('wg_pmode');if(sm&&/^(pairs|rr|two)$/.test(sm))pmd.value=sm;pmd.addEventListener('change',pmv);pmv()}
 function box(title,items){var d=document.createElement('div');d.className='team';var h=document.createElement('b');h.textContent=title;d.appendChild(h);var ul=document.createElement('ul');items.forEach(function(t){var li=document.createElement('li');li.textContent=t;ul.appendChild(li)});d.appendChild(ul);out.appendChild(d)}
 function runp(){err.textContent='';var n=shuffle(pn()),mode=$('pmode').value,odd=$('podd').value;out.innerHTML='';out.className='gout teams';last=[];
  if(n.length<(mode==='two'?1:2))return fail(mode==='two'?'Add at least one name to List A.':'Add at least two names.');if(n.length>500)return fail('Up to 500 names at a time.');
  if(mode==='two'){var B=shuffle(pn2());if(!B.length)return fail('Add at least one item to List B.');if(B.length>500)return fail('Up to 500 items in List B.');
   var A=n,uses={},rows=[];if(B.length>=A.length){A.forEach(function(a,i){rows.push([a,B[i]])})}else{var pool=[];while(pool.length<A.length)pool=pool.concat(shuffle(B));A.forEach(function(a,i){rows.push([a,pool[i]])})}
   rows.forEach(function(r,i){box('Match '+(i+1),r);last.push(r[0]+' → '+r[1])});
   var left=B.length>A.length?B.slice(A.length):[];if(left.length){box('Not matched',left);last.push('Not matched: '+left.join(', '))}
   $('gcount').textContent=rows.length+' matches · '+A.length+' + '+B.length+' items'}
  else if(mode==='pairs'){var pairs=[];for(var i=0;i+1<n.length;i+=2)pairs.push([n[i],n[i+1]]);var extra=n.length%2?n[n.length-1]:null;
   if(extra){if(odd==='trio'&&pairs.length)pairs[pairs.length-1].push(extra);}
   pairs.forEach(function(p,i){box('Pair '+(i+1)+(p.length===3?' (trio)':''),p);last.push('Pair '+(i+1)+': '+p.join(' & '))});
   if(extra&&odd==='bye'){box('Sits out',[extra]);last.push('Sits out: '+extra)}
   $('gcount').textContent=pairs.length+' pairs · '+n.length+' people'}
  else{if(n.length>40)return fail('Round-robin schedules work for up to 40 names.');var L=n.slice();if(L.length%2)L.push(null);var m=L.length,rounds=m-1,tot=0;
   for(var r=0;r<rounds;r++){var g=[],bye=null;for(var k=0;k<m/2;k++){var a=L[k],b=L[m-1-k];if(a===null||b===null)bye=a===null?b:a;else{g.push(a+' vs '+b);tot++}}
    if(bye)g.push(bye+' — bye');box('Round '+(r+1),g);last.push('Round '+(r+1)+': '+g.join('; '));L.splice(1,0,L.pop())}
   $('gcount').textContent=rounds+' rounds · '+tot+' matches'}
  var h=$('ghist');if(h){var li=document.createElement('li');li.textContent=(mode==='pairs'?'Pairs':mode==='two'?'Two-list match':'Round robin')+' for '+n.length+' people';h.prepend(li);while(h.children.length>10)h.removeChild(h.lastChild)}}
 $('ggo').onclick=runp;
}
if(cfg.type==='list'){
 var la=$('lnames');la.value=load('wg_list')||cfg.sample.join('\n');
 function items(){var v=la.value,raw=v.indexOf('\n')<0&&v.indexOf(',')>=0?v.split(','):v.split('\n');return raw.map(function(s){return s.trim()}).filter(Boolean)}
 function lu(){var n=items().length;$('lcount').textContent='· '+n+(la.value.indexOf('\n')<0&&la.value.indexOf(',')>=0?' (split on commas)':'');store('wg_list',la.value)}la.addEventListener('input',lu);lu();
 var shown=[];
 window.WGLIST=function(){var f=$('lfmt').value;return f==='num'?shown.map(function(t,i){return (i+1)+'. '+t}).join('\n'):f==='comma'?shown.join(', '):shown.join('\n')};
 function render(){out.innerHTML='';out.className='gout lout';var f=$('lfmt').value;
  if(f==='comma'){var p=document.createElement('p');p.className='lcomma';p.textContent=shown.join(', ');out.appendChild(p);return}
  var ol=document.createElement(f==='num'?'ol':'ul');ol.className='llist'+(f==='num'?'':' plain');shown.forEach(function(t){var li=document.createElement('li');li.textContent=t;ol.appendChild(li)});out.appendChild(ol)}
 function runl(){err.textContent='';var n=items();if($('ldedupe').checked){var seen={};n=n.filter(function(t){var k=t.toLowerCase();if(seen[k])return false;seen[k]=1;return true})}
  if(n.length<2)return fail('Add at least two items, one per line.');if(n.length>10000)return fail('Up to 10,000 items at a time.');
  var k=parseInt($('lkeep').value,10),all=n.length;var s=shuffle(n);if(!isNaN(k)&&k>=1&&k<s.length)s=s.slice(0,k);shown=s;render();last=s;
  $('gcount').textContent=(s.length<all?s.length+' of '+all+' items':all+' items')+' in random order';
  var h=$('ghist');if(h){var li=document.createElement('li');li.textContent=s.slice(0,8).join(', ')+(s.length>8?' …':'');h.prepend(li);while(h.children.length>10)h.removeChild(h.lastChild)}}
 $('lfmt').addEventListener('change',function(){if(shown.length)render()});
 $('ggo').onclick=runl;
}
if(cfg.type==='name'){
 var D=cfg.data;
 function run(){err.textContent='';var g=$('ngender').value,c=parseInt($('ncount').value,10),full=$('nfull').checked;if(isNaN(c)||c<1)c=1;if(c>100)return fail('Up to 100 names at a time.');
  var pool=g==='female'?D.female:g==='male'?D.male:D.female.concat(D.male),r=[],seen={},tries=0;
  while(r.length<c&&tries<5000){tries++;var nm=pool[ri(pool.length)]+(full?' '+D.last[ri(D.last.length)]:'');if(!seen[nm]){seen[nm]=1;r.push(nm)}}
  show(r,c===1)}
 $('ggo').onclick=run;
}

document.addEventListener('keydown',function(e){if(e.key==='Enter'&&e.target.tagName==='INPUT'&&$('ggo')){e.preventDefault();$('ggo').click()}});
if(cfg.type!=='coin'&&cfg.type!=='dice'){$('ggo').click()}
var lg=document.querySelector('.logo');if(lg)lg.addEventListener('click',function(){try{localStorage.removeItem('wv_entries_home2')}catch(e){}});
var bg=$('burger'),nv=$('mnav');bg.onclick=function(){var o=!nv.classList.contains('open');nv.classList.toggle('open',o);bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?'Close menu':'Open menu')};
nv.addEventListener('click',function(e){if(e.target.tagName==='A'){nv.classList.remove('open');bg.setAttribute('aria-expanded',false)}});
var th=$('theme'),root=document.documentElement,mt=document.querySelector('meta[name=theme-color]');function applyT(t){root.setAttribute('data-theme',t);th.setAttribute('aria-label',t==='light'?'Switch to dark mode':'Switch to light mode');if(mt)mt.setAttribute('content',t==='light'?'#F6F6F9':'#0A0A0C')}
applyT(root.getAttribute('data-theme')||'dark');th.onclick=function(){var t=root.getAttribute('data-theme')==='light'?'dark':'light';applyT(t);store('wv_theme',t)};
})();
