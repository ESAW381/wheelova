(function(){
var P=['#6E56F0','#E11D48','#F59E0B','#16A34A','#2563EB','#DB2777','#0D9488','#EA580C'];
var $=function(id){return document.getElementById(id)};
var cv=$('wheel'),ctx=cv.getContext('2d'),out=$('out');
function dec(t){try{t=t.replace(/-/g,'+').replace(/_/g,'/');while(t.length%4)t+='=';var s=atob(t),u=new Uint8Array(s.length);for(var i=0;i<s.length;i++)u[i]=s.charCodeAt(i);return new TextDecoder().decode(u).split('\n').map(function(x){return x.trim()}).filter(Boolean).slice(0,1000)}catch(e){return null}}
var m=/[#&]w=([^&]+)/.exec(location.hash),mode=(/[#&]m=([a-z]+)/.exec(location.hash)||[])[1];
var entries=(m&&dec(m[1]))||['Yes','No'];if(entries.length<2)entries=['Yes','No'];
var rot=0,spinning=false;
function rand(){var a=new Uint32Array(1);crypto.getRandomValues(a);return a[0]/4294967296}
function lum(h){var r=parseInt(h.substr(1,2),16),g=parseInt(h.substr(3,2),16),b=parseInt(h.substr(5,2),16);return (0.299*r+0.587*g+0.114*b)/255}
function draw(){var W=cv.width,R=W/2,n=entries.length,seg=Math.PI*2/n;ctx.clearRect(0,0,W,W);ctx.save();ctx.translate(R,R);ctx.rotate(rot);
var base=Math.min(58,Math.max(9,(2*Math.PI*R*0.6/n)*0.46)),maxW=R-36-120;
for(var i=0;i<n;i++){var a0=-Math.PI/2+i*seg,k=(n%P.length===1&&i===n-1&&n>1)?1:i%P.length,f=P[k];
ctx.beginPath();ctx.moveTo(0,0);ctx.arc(0,0,R,a0,a0+seg);ctx.closePath();ctx.fillStyle=f;ctx.fill();
ctx.save();ctx.rotate(a0+seg/2);ctx.textAlign='right';ctx.textBaseline='middle';ctx.fillStyle=lum(f)>0.62?'#141418':'#FFFFFF';
var t=mode==='mystery'?'?':entries[i];if(t.length>24)t=t.slice(0,23)+'…';var fs=base;ctx.font='600 '+fs+'px Inter,system-ui,sans-serif';var tw=ctx.measureText(t).width;if(tw>maxW){fs=Math.max(9,fs*maxW/tw);ctx.font='600 '+fs+'px Inter,system-ui,sans-serif'}
ctx.fillText(t,R-36,0);ctx.restore()}ctx.restore()}
function idxAt(r){var n=entries.length,seg=Math.PI*2/n,a=((-r)%(Math.PI*2)+Math.PI*2)%(Math.PI*2);return Math.min(n-1,Math.floor(a/seg))}
function spin(){if(spinning)return;spinning=true;out.textContent='Spinning…';out.className='out';
var start=rot,reduce=matchMedia('(prefers-reduced-motion: reduce)').matches,target=start+Math.PI*2*(reduce?1:6)+rand()*Math.PI*2,dur=reduce?300:4600,t0=performance.now();
function ease(t){return 1-Math.pow(1-t,4)}
function f(now){var t=Math.min(1,(now-t0)/dur);rot=start+(target-start)*ease(t);draw();if(t<1)requestAnimationFrame(f);else{spinning=false;rot=rot%(Math.PI*2);out.textContent=entries[idxAt(rot)];out.className='out win'}}
requestAnimationFrame(f)}
cv.onclick=spin;$('spin').onclick=spin;
document.addEventListener('keydown',function(e){if(e.code==='Space'){e.preventDefault();spin()}});
var cr=$('credit');if(cr)cr.href='https://wheelova.com/'+(m?'#w='+m[1]:'');
draw();if(document.fonts)document.fonts.ready.then(draw);
})();
