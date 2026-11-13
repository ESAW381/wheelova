/* Wheelova site search: header button, Ctrl/Cmd+K or "/". Searches a small
   static index (search-index.json) in the browser; no query leaves the device. */
(function(){
var btn=document.getElementById('srch');if(!btn)return;
var L=(document.documentElement.lang||'en').slice(0,2);
var TX={en:{ph:'Search tools and guides…',none:'No matches. Try “coin”, “names” or “team”.',pop:'Popular',res:'Results',guide:'Guide',close:'Close'},
 es:{ph:'Buscar herramientas y guías…',none:'Sin resultados. Prueba “nombres”, “sí o no” o “números”.',pop:'Populares',res:'Resultados',guide:'Guía',close:'Cerrar'},
 fr:{ph:'Rechercher un outil ou un guide…',none:'Aucun résultat. Essayez « roue », « noms » ou « pièce ».',pop:'Populaires',res:'Résultats',guide:'Guide',close:'Fermer'},
 vi:{ph:'Tìm công cụ và hướng dẫn…',none:'Không có kết quả. Thử “vòng quay”, “tên” hoặc “đồng xu”.',pop:'Phổ biến',res:'Kết quả',guide:'Hướng dẫn',close:'Đóng'}}[L]||null;
TX=TX||{ph:'Search tools and guides…',none:'No matches.',pop:'Popular',res:'Results',guide:'Guide',close:'Close'};
var POP={en:['/','/name-picker-wheel','/yes-or-no-wheel','/random-number-generator','/random-team-generator','/coin-flip','/dice-roller','/raffle-wheel'],
 es:['/es','/es/ruleta-de-nombres','/es/ruleta-si-o-no','/es/ruleta-de-numeros','/es/ruleta-de-sorteo'],fr:['/fr','/'],vi:['/vi','/']}[L]||[];
var idx=null,dlg,inp,list,items=[],sel=0,lastFocus;
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/đ/g,'d')}
function load(cb){if(idx)return cb();fetch('/search-index.json?v='+(btn.getAttribute('data-v')||'')).then(function(r){return r.json()}).then(function(j){
 idx=j.map(function(p){p.nt=norm(p.t);p.nk=norm(p.k);p.nd=norm(p.d);p.nu=norm(p.u.replace(/[\/-]/g,' '));return p});cb()}).catch(function(){idx=[];cb()})}
function build(){
 dlg=document.createElement('dialog');dlg.className='sdlg';dlg.setAttribute('aria-label',TX.ph);
 dlg.innerHTML='<div class="sbox"><div class="srow"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'+
  '<input type="search" id="sq" autocomplete="off" spellcheck="false" role="combobox" aria-expanded="true" aria-controls="slist" aria-autocomplete="list"><button type="button" class="sx" aria-label="'+TX.close+'">Esc</button></div>'+
  '<div class="shead" id="shead"></div><ul class="slist" id="slist" role="listbox"></ul></div>';
 document.body.appendChild(dlg);inp=dlg.querySelector('#sq');list=dlg.querySelector('#slist');inp.placeholder=TX.ph;
 inp.addEventListener('input',function(){sel=0;render()});
 inp.addEventListener('keydown',function(e){
  if(e.key==='ArrowDown'){e.preventDefault();move(1)}else if(e.key==='ArrowUp'){e.preventDefault();move(-1)}
  else if(e.key==='Enter'){e.preventDefault();var a=items[sel];if(a)location.href=a.u}
  else if(e.key==='Escape'){e.preventDefault();close()}});
 dlg.querySelector('.sx').onclick=close;
 dlg.addEventListener('click',function(e){if(e.target===dlg)close()});
 dlg.addEventListener('close',function(){document.body.classList.remove('s-open');if(lastFocus)lastFocus.focus()});
}
function score(p,q){var ws=q.split(/\s+/).filter(Boolean),s=0;
 for(var i=0;i<ws.length;i++){var w=ws[i],hit=0;
  if(p.nt.indexOf(w)===0)hit=12;else if(p.nt.indexOf(' '+w)>-1)hit=9;else if(p.nt.indexOf(w)>-1)hit=7;
  else if(p.nk.indexOf(w)>-1)hit=5;else if(p.nu.indexOf(w)>-1)hit=4;else if(p.nd.indexOf(w)>-1)hit=2;
  if(!hit)return 0;s+=hit}
 return s+(p.l===L?3:0)-(p.g?1:0)}
function render(){
 var q=norm(inp.value.trim());
 if(!q){items=POP.map(function(u){return idx.filter(function(p){return p.u===u})[0]}).filter(Boolean);
  if(!items.length)items=idx.filter(function(p){return p.l===L}).slice(0,8);dlg.querySelector('#shead').textContent=TX.pop}
 else{items=idx.map(function(p){return [score(p,q),p]}).filter(function(x){return x[0]>0}).sort(function(a,b){return b[0]-a[0]}).slice(0,8).map(function(x){return x[1]});
  dlg.querySelector('#shead').textContent=items.length?TX.res:''}
 list.innerHTML='';
 if(!items.length){var li=document.createElement('li');li.className='snone';li.textContent=TX.none;list.appendChild(li);inp.removeAttribute('aria-activedescendant');return}
 items.forEach(function(p,i){var li=document.createElement('li');li.id='so'+i;li.setAttribute('role','option');li.setAttribute('aria-selected',String(i===sel));
  var a=document.createElement('a');a.href=p.u;a.tabIndex=-1;
  var t=document.createElement('span');t.className='st';t.textContent=p.t||p.k;
  if(p.g){var g=document.createElement('em');g.textContent=TX.guide;t.appendChild(g)}
  if(p.l!=='en'){var lg=document.createElement('em');lg.textContent=p.l.toUpperCase();t.appendChild(lg)}
  var d=document.createElement('span');d.className='sd';d.textContent=p.d;a.appendChild(t);a.appendChild(d);li.appendChild(a);
  li.onmousemove=function(){if(sel!==i){sel=i;paint()}};list.appendChild(li)});
 paint()}
function paint(){Array.prototype.forEach.call(list.children,function(li,i){li.setAttribute('aria-selected',String(i===sel))});
 if(items.length){inp.setAttribute('aria-activedescendant','so'+sel);var c=list.children[sel];c&&c.scrollIntoView&&c.scrollIntoView({block:'nearest'})}}
function move(d){if(!items.length)return;sel=(sel+d+items.length)%items.length;paint()}
function open(){lastFocus=document.activeElement;if(!dlg)build();load(function(){render()});
 if(dlg.showModal)dlg.showModal();else dlg.setAttribute('open','');document.body.classList.add('s-open');inp.value='';setTimeout(function(){inp.focus()},0)}
function close(){if(dlg.close)dlg.close();else{dlg.removeAttribute('open');document.body.classList.remove('s-open')}}
var bl={es:['Buscar','Buscar herramientas'],fr:['Rechercher','Rechercher des outils'],vi:['Tìm kiếm','Tìm công cụ']}[L];
if(bl){btn.querySelector('.srch-t').textContent=bl[0];btn.setAttribute('aria-label',bl[1])}
btn.addEventListener('click',open);
document.addEventListener('keydown',function(e){
 var tag=document.activeElement&&document.activeElement.tagName,typing=/INPUT|TEXTAREA|SELECT/.test(tag)||document.activeElement.isContentEditable;
 if((e.ctrlKey||e.metaKey)&&(e.key==='k'||e.key==='K')){e.preventDefault();dlg&&dlg.open?close():open()}
 else if(e.key==='/'&&!typing&&!(dlg&&dlg.open)){e.preventDefault();open()}},true);
if(/Mac|iPhone|iPad/.test(navigator.platform||'')){var k=btn.querySelector('.srch-k');if(k)k.textContent='⌘K';btn.title='Search (⌘K)'}
})();
