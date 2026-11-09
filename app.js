(function(){
var cfg=window.WV||{},T=cfg.t||{};
var PALS={pastel:['#A5B4FC','#FDA4AF','#FCD34D','#86EFAC','#93C5FD','#F9A8D4','#5EEAD4','#FDBA74'],ocean:['#0C4A6E','#0284C7','#38BDF8','#0E7490','#22D3EE','#1E3A8A','#7DD3FC','#155E75'],sunset:['#7C2D12','#EA580C','#FB923C','#F59E0B','#DC2626','#BE185D','#FDE047','#9A3412'],forest:['#14532D','#16A34A','#4ADE80','#65A30D','#A3E635','#3F6212','#86EFAC','#166534'],mono:['#18181B','#52525B','#A1A1AA','#3F3F46','#D4D4D8','#71717A'],safe:['#E69F00','#56B4E9','#009E73','#F0E442','#0072B2','#D55E00','#CC79A7','#000000']};
function parsePal(v){if(!v||v==='default')return null;if(PALS[v])return PALS[v];var m=/^custom:((?:[0-9a-fA-F]{6}\.?){2,8})$/.exec(v);if(!m)return null;return m[1].split('.').filter(Boolean).map(function(h){return '#'+h.toUpperCase()})}
var palSel=(function(){var h=/[#&]c=([a-z0-9:.]+)/i.exec(location.hash);if(h&&/[#&]w=/.test(location.hash))return h[1];try{return localStorage.getItem('wv_colors')||'default'}catch(e){return 'default'}})();
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
var RNG=window.WVRNG;function rand(){return RNG.rand()}
var sharedMode=false;function parse(){entries=ta.value.split('\n').map(function(s){return s.trim()}).filter(Boolean);$('count').textContent='· '+entries.length;if(!sharedMode)store(KEY,ta.value);draw()}
function setEntries(arr,msg){var prev=ta.value;ta.value=arr.join('\n');parse();if(msg&&prev.trim()&&prev!==ta.value)offerUndo(msg,prev)}
function leaveShared(){if(!sharedMode)return;sharedMode=false;var n=$('sharenote');if(n)n.hidden=true;try{history.replaceState(null,'',location.pathname+location.search)}catch(e){}}
function lum(h){h=h.replace('#','');if(h.length===3)h=h.split('').map(function(c){return c+c}).join('');var r=parseInt(h.substr(0,2),16),g=parseInt(h.substr(2,2),16),b=parseInt(h.substr(4,2),16);return (0.299*r+0.587*g+0.114*b)/255}
function fillFor(i,n,name){
if(cfg.mode==='color'&&cfg.colorMap){var c=cfg.colorMap[name.toLowerCase()];if(c)return {f:c,t:lum(c)>0.6?'#141418':'#FFFFFF'}}
var UP=parsePal(palSel);if(UP){var k2=(n%UP.length===1&&i===n-1&&n>1)?1:i%UP.length;return {f:UP[k2],t:lum(UP[k2])>0.62?'#141418':'#FFFFFF'}}
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
var now=new Date();hist.unshift({w:w,t:now});var li=document.createElement('li');li.textContent=w;var tm=document.createElement('span');tm.className='rtime';tm.textContent=' '+now.toLocaleTimeString([],{hour:'2-digit',minute:'2-digit',second:'2-digit'});li.appendChild(tm);$('history').prepend(li);$('rcount').textContent='· '+hist.length;var ra=$('resacts');if(ra)ra.hidden=false;
lastIdx=i;$('popwin').textContent=w;var pp=$('popprompt');if(pp){var pr='';if(cfg.prompts){var dk=($('tddeck')&&$('tddeck').value)||'kids',L=cfg.prompts[dk]&&cfg.prompts[dk][w];if(L&&L.length)pr=L[RNG.randInt(L.length)]}pp.textContent=pr;if(pr){res.querySelector('.win').textContent=w+': '+pr}}$('poplbl').textContent=(wmsg&&wmsg.value.trim())||cfg.popLabel||T.pop||'WE HAVE A WINNER';
var pf=$('popflag');if(pf){var fc=FL&&FL[w];pf.hidden=!fc;if(fc){pf.src='/flags/'+fc+'.svg';pf.alt=''}}var sw=$('popswatch'),hx=$('pophex');var c=cfg.mode==='color'&&cfg.colorMap?cfg.colorMap[w.toLowerCase()]:null;if(sw){sw.style.display=c?'block':'none';if(c)sw.style.background=c}if(hx)hx.textContent=c?c.toUpperCase():''
if(wspk&&wspk.checked){try{speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(($('popprompt')&&$('popprompt').textContent)?w+'. '+$('popprompt').textContent:w);u.lang=document.documentElement.lang||'en';speechSynthesis.speak(u)}catch(e){}}$('popremove').style.display=removeW?'none':'';$('pop').classList.add('on');$('popclose').focus();
if(removeW){entries.splice(i,1);ta.value=entries.join('\n');parse()}}
var lastIdx=-1;function closePop(){$('pop').classList.remove('on');$('spin').focus()}
function trap(e){if(e.key!=='Tab')return;var d=$('pop').classList.contains('on')?$('pop'):($('sharepop')&&$('sharepop').classList.contains('on')?$('sharepop'):null);if(!d)return;
var f=Array.prototype.filter.call(d.querySelectorAll('button,input,textarea,a[href],select'),function(x){return !x.disabled&&x.offsetParent!==null});if(!f.length)return;
var first=f[0],lastEl=f[f.length-1];if(!d.contains(document.activeElement)){e.preventDefault();first.focus()}else if(e.shiftKey&&document.activeElement===first){e.preventDefault();lastEl.focus()}else if(!e.shiftKey&&document.activeElement===lastEl){e.preventDefault();first.focus()}}
document.addEventListener('keydown',trap);
$('popclose').onclick=closePop;$('pop').onclick=function(e){if(e.target===this)closePop()};
$('popremove').onclick=function(){var i=lastIdx;lastIdx=-1;closePop();if(i>-1&&i<entries.length){var arr=entries.slice(),nm=arr.splice(i,1)[0];setEntries(arr,(T.removedw||'Removed "{w}" from the wheel.').replace('{w}',nm))}};
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&$('pop').classList.contains('on'))closePop()});
$('spin').onclick=spin;cv.onclick=spin;
ta.addEventListener('input',parse);
$('shuffle').onclick=function(){setEntries(RNG.shuffle(entries))};
$('sort').onclick=function(){setEntries(entries.slice().sort(function(a,b){return a.localeCompare(b,undefined,{numeric:true})}))};
(function(){var b=$('impbtn'),f=$('impfile'),pan=$('impcol');if(!b||!f)return;var rows=null,MAX=2000;
function csv(t){t=t.replace(/^﻿/,'');var first=(t.split(/\r?\n/)[0]||''),d=first.indexOf('\t')>-1?'\t':(first.split(';').length>first.split(',').length?';':',');
 var out=[],row=[],cur='',q=false;for(var i=0;i<t.length;i++){var c=t[i];
  if(q){if(c==='"'){if(t[i+1]==='"'){cur+='"';i++}else q=false}else cur+=c}
  else if(c==='"'&&cur==='')q=true;else if(c===d){row.push(cur);cur=''}else if(c==='\n'||c==='\r'){if(c==='\r'&&t[i+1]==='\n')i++;row.push(cur);out.push(row);row=[];cur=''}else cur+=c}
 if(cur!==''||row.length){row.push(cur);out.push(row)}return out.filter(function(r){return r.some(function(x){return x.trim()})})}
function use(list,note){list=list.map(function(x){return x.trim()}).filter(Boolean);if(!list.length){showToast(T.impempty||'No entries found in that file.');return}
 var cut=list.length>MAX;if(cut)list=list.slice(0,MAX);var msg=(T.imported||'Imported {n} entries.').replace('{n}',list.length)+(cut?' '+(T.impcut||'Only the first 2,000 were kept.'):'');
 var prev=ta.value;leaveShared();setEntries(list,msg);if(!(prev.trim()&&prev!==ta.value))showToast(msg)}
b.onclick=function(){f.value='';f.click()};
f.onchange=function(){var file=f.files&&f.files[0];if(!file)return;if(file.size>5e6){showToast(T.impbig||'That file is too large (5 MB max).');return}
 if(/\.xlsx?$/i.test(file.name)){showToast(T.impxls||'Save the sheet as CSV first, or copy the column and paste it.');return}
 var r=new FileReader();r.onload=function(){rows=csv(String(r.result));if(!rows.length){showToast(T.impempty||'No entries found in that file.');return}
  var w=Math.max.apply(null,rows.map(function(x){return x.length}));if(w<2){use(rows.map(function(x){return x[0]||''}));return}
  var sel=$('impsel');sel.innerHTML='';for(var i=0;i<w;i++){var o=document.createElement('option');o.value=i;o.textContent=(rows[0][i]||'').trim()||((T.col||'Column')+' '+(i+1));sel.appendChild(o)}
  pan.hidden=false;sel.focus()};r.readAsText(file)};
$('impok').onclick=function(){var i=+$('impsel').value,h=$('imphdr').checked;pan.hidden=true;use(rows.slice(h?1:0).map(function(x){return x[i]||''}))};
$('impno').onclick=function(){pan.hidden=true;rows=null;b.focus()};
})();
$('clear').onclick=function(){setEntries([],T.cleared||'List cleared.');ta.focus()};
var rb=$('remove');rb.setAttribute('aria-pressed',removeW);rb.onclick=function(){removeW=!removeW;this.setAttribute('aria-pressed',removeW)};
$('sound').onclick=function(){sound=!sound;this.setAttribute('aria-pressed',sound)};
var wf=$('wflag');if(FL){flagMode=load(KEY+'_flag')||'both';if(wf){wf.value=flagMode;wf.onchange=function(){flagMode=wf.value;store(KEY+'_flag',flagMode);draw()}}}
(function(){var sel=$('wcolors'),cu=$('wcust');if(!sel)return;if(cfg.mode==='color'){sel.parentNode.hidden=true;return}
var ins=cu?cu.querySelectorAll('input'):[],base=parsePal(palSel)||cfg.palette||COLORS;
function setIns(p){for(var i=0;i<ins.length;i++)ins[i].value=(p[i%p.length]||'#6E56F0').toLowerCase()}
var cur=/^custom:/.test(palSel)?'custom':(PALS[palSel]?palSel:'default');sel.value=cur;setIns(base);if(cu)cu.hidden=cur!=='custom';
function custom(){var a=[];for(var i=0;i<ins.length;i++)a.push(ins[i].value.replace('#','').toUpperCase());return 'custom:'+a.join('.')}
function apply(v){palSel=v;if(!sharedMode)store('wv_colors',v);draw()}
sel.onchange=function(){if(cu)cu.hidden=sel.value!=='custom';apply(sel.value==='custom'?custom():sel.value)};
for(var i=0;i<ins.length;i++)ins[i].oninput=function(){if(sel.value==='custom')apply(custom())}})();
var speed=load('wv_speed')||'normal',wsp=$('wspeed'),wmsg=$('wmsg');if(wsp){wsp.value=speed;wsp.onchange=function(){speed=wsp.value;store('wv_speed',speed)}}
var wspk=$('wspeak');if(wspk){if(!('speechSynthesis' in window))wspk.parentNode.style.display='none';wspk.checked=load('wv_speak')==='1';wspk.onchange=function(){store('wv_speak',wspk.checked?'1':'0')}}
if(wmsg){wmsg.value=load(KEY+'_msg')||'';wmsg.addEventListener('input',function(){store(KEY+'_msg',wmsg.value)})}
document.addEventListener('keydown',function(e){if(e.code==='Space'&&!$('pop').classList.contains('on')&&!($('sharepop')&&$('sharepop').classList.contains('on'))&&!/TEXTAREA|INPUT|BUTTON|SUMMARY|A|SELECT/.test(document.activeElement.tagName)){e.preventDefault();spin()}});
var g=$('templates');if(g){TEMPLATES.forEach(function(t){var b=document.createElement('button');b.type='button';b.className='tpl';
b.innerHTML='<span class="dot" style="background:conic-gradient('+t.c+' 0 25%,#2A2A36 0 50%,'+t.c+' 0 75%,#2A2A36 0)"></span><span><b></b><span></span></span>';
b.querySelector('b').textContent=t.n;b.querySelector('span span').textContent=t.e.length+' entries';
b.onclick=function(){setEntries(t.e,T.replaced||'List replaced.');$('tool').scrollIntoView({block:'start'})};g.appendChild(b)})}
var vz=$('variants');if(vz&&cfg.variants){cfg.variants.forEach(function(v){var b=document.createElement('button');b.type='button';b.className='chip';b.textContent=v.label;b.onclick=function(){setEntries(v.entries,T.replaced||'List replaced.')};vz.appendChild(b)})}
var ng=$('ngo');if(ng){ng.onclick=function(){var a=parseInt($('nmin').value,10),b=parseInt($('nmax').value,10);var err=$('nerr');
if(isNaN(a)||isNaN(b)||b<=a){err.textContent=T.nrange||'Enter a range where "To" is bigger than "From".';return}
if(b-a+1>500){err.textContent=T.nmax||'Up to 500 numbers per wheel.';return}err.textContent='';var arr=[];for(var x=a;x<=b;x++)arr.push(String(x));setEntries(arr,T.replaced||'List replaced.')}}
var sc=$('scount');if(sc){sc.onchange=function(){var n=parseInt(sc.value,10),arr=[];for(var x=1;x<=n;x++)arr.push(String(x));setEntries(arr,T.replaced||'List replaced.')}}
function enc(arr){var u=new TextEncoder().encode(arr.join('\n')),s='';for(var i=0;i<u.length;i++)s+=String.fromCharCode(u[i]);return btoa(s).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'')}
function dec(t){try{t=t.replace(/-/g,'+').replace(/_/g,'/');while(t.length%4)t+='=';var s=atob(t),u=new Uint8Array(s.length);for(var i=0;i<s.length;i++)u[i]=s.charCodeAt(i);return new TextDecoder().decode(u).split('\n').map(function(x){return x.trim()}).filter(Boolean).slice(0,1000)}catch(e){return null}}
var saved=load(KEY),hm=/[#&]w=([^&]+)/.exec(location.hash),shared=hm?dec(hm[1]):null;
if(shared&&shared.length){sharedMode=true;ta.value=shared.join('\n');var sn=$('sharenote');if(sn)sn.hidden=false}else{ta.value=saved!=null&&saved.trim()?saved:DEFAULT.join('\n')}
parse();
var ml=$('mylist');if(ml)ml.onclick=function(){leaveShared();palSel=load('wv_colors')||'default';var wc=$('wcolors');if(wc){wc.value=/^custom:/.test(palSel)?'custom':(PALS[palSel]?palSel:'default');var wq=$('wcust');if(wq)wq.hidden=wc.value!=='custom'}ta.value=saved!=null&&saved.trim()?saved:DEFAULT.join('\n');parse()};
var ks=$('savesh');if(ks)ks.onclick=function(){var old=saved;leaveShared();store('wv_colors',palSel);parse();saved=ta.value;if(old&&old.trim()&&old!==ta.value)offerUndo(T.kept||'Shared wheel saved as your list.',old);else showToast(T.kept||'Shared wheel saved as your list.')};
var SITE='https://wheelova.com',PATH=location.pathname.replace(/index\.html$/,'').replace(/\.html$/,'');
function openShare(withEmbed){if(entries.length<2){res.innerHTML='<div class="hint">'+(T.add2share||'Add at least two entries to share')+'</div>';return}
var code=enc(entries),cp=parsePal(palSel)?'&c='+palSel:'',url=SITE+PATH+'#w='+code+cp;$('shareurl').value=url;
var emb=SITE+'/embed#w='+code+(cfg.mode&&cfg.mode!=='color'?'&m='+cfg.mode:'')+cp;
$('embedcode').value='<iframe src="'+emb+'" title="'+(T.iframe_title||'Spin the wheel – Wheelova')+'" width="100%" height="560" style="max-width:560px;border:0" loading="lazy"></iframe>\n<p style="font:14px sans-serif">'+(T.credit_pre||'Spin wheel by')+' <a href="'+SITE+PATH+'">Wheelova</a></p>';
$('embedwrap').hidden=!withEmbed;$('sharettl').textContent=withEmbed?(T.embed_title||'EMBED THIS WHEEL'):(T.share_title||'SHARE THIS WHEEL');
var w=$('sharewarn');w.hidden=url.length<=3000;w.textContent=(T.long?T.long.replace('{n}',url.length):'This list is long, so the link is long ('+url.length+' characters). It still works, but some chat apps may cut it off.');
$('sharepop').classList.add('on');(withEmbed?$('embedcopy'):$('sharecopy')).focus()}
function copyFrom(id,btn){var el=$(id);el.select();var txt=el.value,done=function(){btn.textContent=T.copied||'Copied';setTimeout(function(){btn.textContent=id==='shareurl'?(T.copy||'Copy'):(T.copy_embed||'Copy embed code')},1500)};
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,function(){document.execCommand('copy');done()})}else{document.execCommand('copy');done()}}
if($('sharebtn')){$('sharebtn').onclick=function(){shareRet=this;openShare(false)};$('embedbtn').onclick=function(){shareRet=this;openShare(true)};
$('sharecopy').onclick=function(){copyFrom('shareurl',this)};$('embedcopy').onclick=function(){copyFrom('embedcode',this)};
var sp=$('sharepop'),shareRet=null;function closeShare(){if(!sp.classList.contains('on'))return;sp.classList.remove('on');if(shareRet)shareRet.focus()}$('shareclose').onclick=closeShare;sp.onclick=function(e){if(e.target===sp)closeShare()};
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeShare()})}
var fb=$('fsbtn'),body=document.body;function setFs(on){body.classList.toggle('is-fs',on);fb.setAttribute('aria-label',on?(T.exitfs||'Exit fullscreen'):(T.fs||'Fullscreen'));
try{if(on&&document.documentElement.requestFullscreen&&!document.fullscreenElement)document.documentElement.requestFullscreen().catch(function(){});if(!on&&document.fullscreenElement)document.exitFullscreen().catch(function(){})}catch(e){}draw()}
if(fb){fb.onclick=function(){setFs(!body.classList.contains('is-fs'))};document.addEventListener('fullscreenchange',function(){if(!document.fullscreenElement&&body.classList.contains('is-fs'))setFs(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&body.classList.contains('is-fs')&&!$('pop').classList.contains('on'))setFs(false);if((e.key==='f'||e.key==='F')&&!/TEXTAREA|INPUT|SELECT/.test(document.activeElement.tagName)&&!e.ctrlKey&&!e.metaKey)setFs(!body.classList.contains('is-fs'))})}
var bg=$('burger'),nv=$('mnav');function setNav(o){nv.classList.toggle('open',o);bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?(T.closemenu||'Close menu'):(T.openmenu||'Open menu'))}
bg.onclick=function(){setNav(!nv.classList.contains('open'))};nv.addEventListener('click',function(e){if(e.target.tagName==='A')setNav(false)});
var th=$('theme'),root=document.documentElement,mt=document.querySelector('meta[name=theme-color]');function applyT(t){root.setAttribute('data-theme',t);th.setAttribute('aria-label',t==='light'?(T.todark||'Switch to dark mode'):(T.tolight||'Switch to light mode'));if(mt)mt.setAttribute('content',t==='light'?'#F6F6F9':'#0A0A0C')}
applyT(root.getAttribute('data-theme')||'dark');th.onclick=function(){var t=root.getAttribute('data-theme')==='light'?'dark':'light';applyT(t);store('wv_theme',t)};
var undoPrev=null,toastT=null;
function showToast(msg,canUndo){var t=$('wtoast');if(!t)return;$('wtmsg').textContent=msg;$('wtundo').hidden=!canUndo;t.hidden=false;clearTimeout(toastT);toastT=setTimeout(function(){t.hidden=true;undoPrev=null},10000)}
function offerUndo(msg,prev){undoPrev=prev;showToast(msg,true)}
if($('wtundo'))$('wtundo').onclick=function(){if(undoPrev==null)return;var p=undoPrev;undoPrev=null;if(typeof p==='function')p();else{ta.value=p;parse();if(!sharedMode)saved=p}$('wtoast').hidden=true;ta.focus()};
function stamp(d){function z(n){return(n<10?'0':'')+n}return d.getFullYear()+'-'+z(d.getMonth()+1)+'-'+z(d.getDate())+' '+z(d.getHours())+':'+z(d.getMinutes())+':'+z(d.getSeconds())}
function csvCell(v){v=String(v);if(/^[=+\-@\t\r]/.test(v))v="'"+v;return /[",\n\r]/.test(v)?'"'+v.replace(/"/g,'""')+'"':v}
function ordered(){return hist.slice().reverse()}
if($('rcopy'))$('rcopy').onclick=function(){var b=this,txt=ordered().map(function(h,i){return (i+1)+'. '+h.w+' ('+stamp(h.t)+')'}).join('\n');var fin=function(){b.textContent=T.copied||'Copied';setTimeout(function(){b.textContent=T.copy||'Copy'},1400)};if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(txt).then(fin,fin);else fin()};
if($('rcsv'))$('rcsv').onclick=function(){var rows=[[T.csv_spin||'Spin',T.csv_winner||'Winner',T.csv_time||'Time']].concat(ordered().map(function(h,i){return [i+1,h.w,stamp(h.t)]}));
 var csv='﻿'+rows.map(function(r){return r.map(csvCell).join(',')}).join('\r\n');var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));a.download='wheelova-results-'+stamp(new Date()).slice(0,10)+'.csv';document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove()},500)};
var SK='wv_saved';function sv(){try{var v=JSON.parse(load(SK)||'[]');return Array.isArray(v)?v.filter(function(x){return x&&typeof x.n==='string'&&Array.isArray(x.e)}):[]}catch(e){return []}}
function svPut(v){store(SK,JSON.stringify(v));renderSaved()}
function renderSaved(){var ul=$('wslist');if(!ul)return;var v=sv();ul.innerHTML='';$('wsempty').hidden=v.length>0;
 v.forEach(function(it){var li=document.createElement('li');var nm=document.createElement('span');nm.className='wsn';nm.textContent=it.n+' ';var c=document.createElement('span');c.className='wsc';c.textContent='('+it.e.length+')';nm.appendChild(c);
  var ld=document.createElement('button');ld.type='button';ld.className='btn';ld.textContent=T.load||'Load';ld.onclick=function(){setEntries(it.e,(T.loaded||'Loaded')+' "'+it.n+'".')};
  var del=document.createElement('button');del.type='button';del.className='linkbtn';del.textContent=T.del||'Delete';del.setAttribute('aria-label',(T.del||'Delete')+' '+it.n);del.onclick=function(){var cur=sv(),ix=-1;cur.forEach(function(x,j){if(x.n===it.n)ix=j});if(ix<0)return;var removed=cur.splice(ix,1)[0];svPut(cur);undoPrev=function(){var c2=sv();c2.splice(Math.min(ix,c2.length),0,removed);svPut(c2)};showToast((T.deleted||'Deleted')+' "'+it.n+'".',true)};
  li.appendChild(nm);li.appendChild(ld);li.appendChild(del);ul.appendChild(li)})}
if($('wssave'))$('wssave').onclick=function(){var nm=$('wsname').value.trim();if(!nm){$('wsname').focus();showToast(T.needname||'Type a name for this wheel first.');return}if(entries.length<1){showToast(T.empty||'Add entries');return}
 var v=sv(),ix=-1;v.forEach(function(x,j){if(x.n.toLowerCase()===nm.toLowerCase())ix=j});var item={n:nm,e:entries.slice(0,1000),t:Date.now()};
 if(ix>-1){v[ix]=item;showToast((T.updated||'Updated')+' "'+nm+'".')}else{if(v.length>=50){showToast(T.full||'You can save up to 50 wheels. Delete one first.');return}v.unshift(item);showToast((T.saved||'Saved')+' "'+nm+'".')}
 svPut(v);$('wsname').value=''};
if($('wsname'))$('wsname').addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();$('wssave').click()}});
renderSaved();
var idleOn=!matchMedia('(prefers-reduced-motion: reduce)').matches,idleVis=true,idleT=null;
try{new IntersectionObserver(function(es){idleVis=es[0].isIntersecting}).observe(cv)}catch(e){}
function idle(t){if(!idleOn)return;if(idleT!==null&&idleVis&&!spinning&&!document.hidden){rot+=Math.min(t-idleT,50)*0.00028;draw()}idleT=t;requestAnimationFrame(idle)}
requestAnimationFrame(idle);
var lg=document.querySelector('.logo');if(lg)lg.addEventListener('click',function(){try{localStorage.removeItem('wv_entries_home2')}catch(e){}});
if(document.fonts)document.fonts.ready.then(draw);
})();
