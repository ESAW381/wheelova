(function(){
var cfg=window.WQ||{},$=function(id){return document.getElementById(id)};
var RNG=window.WVRNG,ri=RNG.randInt,shuffle=RNG.shuffle;
function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
function load(k){try{return localStorage.getItem(k)}catch(e){return null}}
var R=cfg.regions,ISO=cfg.iso,regionOf={};Object.keys(R).forEach(function(r){R[r].forEach(function(c){regionOf[c]=r})});
var all=Object.keys(regionOf);
var qs=[],qi=0,score=0,streak=0,bestStreak=0,missed=[],locked=false,region='all',total=10;
var flag=$('qflag'),opts=$('qopts'),fb=$('qfeedback'),prog=$('qprog'),sc=$('qscore'),stk=$('qstreak'),nextb=$('qnext'),play=$('qplay'),res=$('qresult');
function pool(){return region==='all'?all:R[region]}
function bestKey(){return 'wq_best_'+region+'_'+total}
function start(){var qn=$('qintro');if(qn)qn.hidden=true;region=$('qregion').value;total=$('qcount').value==='all'?pool().length:Math.min(+$('qcount').value,pool().length);
 qs=shuffle(pool()).slice(0,total);qi=0;score=0;streak=0;bestStreak=0;missed=[];res.hidden=true;play.hidden=false;ask();if(window.innerWidth<900)play.scrollIntoView({block:'start',behavior:'smooth'})}
function ask(){locked=false;nextb.hidden=true;fb.textContent='';fb.className='qfb';var c=qs[qi];
 flag.src='/flags/'+ISO[c]+'.svg';flag.alt='Flag to identify';
 var same=R[regionOf[c]].filter(function(x){return x!==c}),other=all.filter(function(x){return x!==c&&regionOf[x]!==regionOf[c]});
 var d=shuffle(same).slice(0,3);if(d.length<3)d=d.concat(shuffle(other).slice(0,3-d.length));
 var ch=shuffle(d.concat([c]));opts.innerHTML='';
 ch.forEach(function(n,i){var b=document.createElement('button');b.type='button';b.className='qopt';b.innerHTML='<span class="k">'+(i+1)+'</span><span></span>';b.lastChild.textContent=n;b.onclick=function(){answer(b,n)};opts.appendChild(b)});
 prog.textContent='Question '+(qi+1)+' of '+total;sc.textContent=score;stk.textContent=streak;
 var nx=qs[qi+1];if(nx){var im=new Image();im.src='/flags/'+ISO[nx]+'.svg'}}
function answer(btn,n){if(locked)return;locked=true;var c=qs[qi],ok=n===c;
 Array.prototype.forEach.call(opts.children,function(b){b.disabled=true;var t=b.lastChild.textContent;if(t===c)b.classList.add('ok');else if(b===btn)b.classList.add('bad')});
 if(ok){score++;streak++;if(streak>bestStreak)bestStreak=streak;fb.textContent='Correct!';fb.className='qfb ok'}
 else{streak=0;missed.push(c);fb.textContent='It was '+c+'.';fb.className='qfb bad'}
 sc.textContent=score;stk.textContent=streak;nextb.hidden=false;nextb.textContent=qi+1<total?'Next flag':'See results';nextb.focus()}
function next(){if(qi+1<total){qi++;ask()}else finish()}
function finish(){play.hidden=true;res.hidden=false;var pct=Math.round(score/total*100),bk=bestKey(),best=+(load(bk)||0);var nb=score>best;if(nb)store(bk,score);
 $('rscore').textContent=score+' / '+total;$('rpct').textContent=pct+'%';$('rstreak').textContent=bestStreak;$('rbest').textContent=nb?'New personal best!':'Your best: '+best+' / '+total;
 var ml=$('rmissed');ml.innerHTML='';$('rmissedwrap').hidden=!missed.length;
 missed.forEach(function(c){var li=document.createElement('li');li.innerHTML='<img alt="" width="40" height="30" loading="lazy"><span></span>';li.firstChild.src='/flags/'+ISO[c]+'.svg';li.lastChild.textContent=c;ml.appendChild(li)});
 $('qagain').focus()}
$('qstart').onclick=start;$('qagain').onclick=start;nextb.onclick=next;
$('qretry').onclick=function(){if(!missed.length)return;qs=shuffle(missed);total=qs.length;qi=0;score=0;streak=0;bestStreak=0;missed=[];res.hidden=true;play.hidden=false;ask()};
document.addEventListener('keydown',function(e){if(play.hidden||/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName))return;
 if(!locked&&/^[1-4]$/.test(e.key)){var b=opts.children[+e.key-1];if(b)b.click()}else if(locked&&(e.key==='Enter'||e.key===' ')&&document.activeElement!==nextb){e.preventDefault();next()}});
var lg=document.querySelector('.logo');if(lg)lg.addEventListener('click',function(){try{localStorage.removeItem('wv_entries_home2')}catch(e){}});
var bg=$('burger'),nv=$('mnav');bg.onclick=function(){var o=!nv.classList.contains('open');nv.classList.toggle('open',o);bg.setAttribute('aria-expanded',o)};
nv.addEventListener('click',function(e){if(e.target.tagName==='A'){nv.classList.remove('open');bg.setAttribute('aria-expanded',false)}});
var th=$('theme'),root=document.documentElement;th.onclick=function(){var t=root.getAttribute('data-theme')==='light'?'dark':'light';root.setAttribute('data-theme',t);store('wv_theme',t)};
})();
