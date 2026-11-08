/* Wheelova analytics consent. Microsoft Clarity loads straight away outside the EEA, UK and Switzerland.
   Inside them (detected from the browser's time zone; unknown zone = ask), it loads only after the visitor accepts.
   Clarity never loads on shared-wheel links or the embed generator. */
(function(){
var w=window,d=document,K='wv_consent';
if(/[#&]w=/.test(location.hash)||location.pathname.indexOf('/embed-a-wheel')===0)return;
function get(){try{return localStorage.getItem(K)}catch(e){return null}}
function set(v){try{localStorage.setItem(K,v)}catch(e){}}
function needs(){var z='';try{z=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}
 if(!z)return true;
 return /^Europe\//.test(z)||/^Atlantic\/(Canary|Madeira|Azores|Reykjavik|Faroe)$/.test(z)||/^Asia\/(Nicosia|Famagusta)$/.test(z)||/^Arctic\//.test(z)}
var loaded=false;
function load(){if(loaded)return;loaded=true;(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y)})(w,d,"clarity","script","z4ruz9115a")}
var es=(d.documentElement.lang||'').indexOf('es')===0;
var S=es?{t:'Usamos Microsoft Clarity para ver cómo se usa el sitio (estadísticas y grabaciones de sesión, con la ruleta y tus opciones ocultas). Puede usar cookies. ¿Lo aceptas?',a:'Aceptar',n:'Rechazar',m:'Más información',l:'Aviso de cookies'}
 :{t:'We use Microsoft Clarity to see how the site is used (usage statistics and session replays, with the wheel and your entries hidden). It may set cookies. Is that OK?',a:'Accept',n:'Decline',m:'Learn more',l:'Cookie notice'};
function banner(){if(d.getElementById('wvcons'))return;var b=d.createElement('div');b.id='wvcons';b.className='wvcons';b.setAttribute('role','region');b.setAttribute('aria-label',S.l);
 b.innerHTML='<p></p><div class="wvca"><button type="button" class="btn" data-v="no"></button><button type="button" class="btn pri" data-v="yes"></button></div>';
 b.firstChild.textContent=S.t+' ';var a=d.createElement('a');a.href='/privacy';a.textContent=S.m;b.firstChild.appendChild(a);
 var bs=b.querySelectorAll('button');bs[0].textContent=S.n;bs[1].textContent=S.a;
 b.onclick=function(e){var v=e.target&&e.target.getAttribute('data-v');if(!v)return;set(v);b.remove();if(v==='yes')load();else if(loaded){try{w.clarity('consent',false)}catch(x){}}};
 d.body.appendChild(b)}
w.wvCookieSettings=function(){try{localStorage.removeItem(K)}catch(e){}banner();var b=d.getElementById('wvcons');if(b)b.querySelector('button').focus()};
d.addEventListener('click',function(e){var t=e.target&&e.target.closest&&e.target.closest('[data-wvcookies]');if(t){e.preventDefault();w.wvCookieSettings()}});
var c=get();
if(!needs()||c==='yes')load();
else if(c!=='no'){if(d.body)banner();else d.addEventListener('DOMContentLoaded',banner)}
})();
