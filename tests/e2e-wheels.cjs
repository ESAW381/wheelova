// jsdom smoke test for every wheel/generator page. Run from dist/: cd dist && NODE_PATH=$(npm root -g) node ../tests/e2e-wheels.cjs
const {JSDOM,VirtualConsole}=require('jsdom');const fs=require('fs');
const pages=fs.readdirSync('.').filter(f=>f.endsWith('.html')&&!['about.html','privacy.html','terms.html','wheels.html','404.html','embed.html','faq.html','es.html','is-the-wheel-random.html','guides.html','embed-a-wheel.html','flag-quiz.html','random-pair-generator.html'].includes(f));
function mk(f){let html=fs.readFileSync(f,'utf8').replace(/<script src="\/(app|gen|rng)\.js\?v=\d+"><\/script>/g,(m,n)=>'<script>'+fs.readFileSync(n+'.js','utf8')+'</script>').replace(/<script defer src="\/_vercel[^>]*><\/script>/,'');
let errs=[];const vc=new VirtualConsole();vc.on('jsdomError',e=>errs.push(e.message));
const d=new JSDOM(html,{url:'https://wheelova.com/'+f,runScripts:'dangerously',pretendToBeVisual:true,virtualConsole:vc,beforeParse(w){w.HTMLCanvasElement.prototype.getContext=()=>new Proxy({},{get:(t,k)=>k in t?t[k]:(k==='measureText'?()=>({width:100}):()=>{}),set:(t,k,v)=>(t[k]=v,true)});w.matchMedia=()=>({matches:false});w.crypto=require('crypto').webcrypto;w.navigator.clipboard={writeText:()=>{}}}});return [d,errs]}
(async()=>{for(const f of pages){const [d,errs]=mk(f);const D=d.window.document,$=id=>D.getElementById(id);let r='';
if($('ccount')||$('dcount')){$('ggo').click();r='names: '+$('gcount').textContent+' | '+D.querySelectorAll('#gout .gitem,#gout .coin,#gout .die').length}
else if($('ggo')){
 if($('nuniq')&&$('nmin')){$('nmin').value='1';$('nmax').value='10';$('ncount').value='10';$('nuniq').checked=true;$('ggo').click();const v=[...D.querySelectorAll('.gitem')].map(x=>x.textContent);r='10 unique of 1-10: '+(new Set(v).size===10)+' ';$('ncount').value='11';$('ggo').click();r+='| over-range msg: '+!!$('gerr').textContent}
 else if($('tnames')){$('tmode').value='teams';$('tnum').value='3';$('ggo').click();r='teams: '+[...D.querySelectorAll('.team b')].map(x=>x.textContent).join(', ');$('tmode').value='size';$('tnum').value='2';$('ggo').click();r+=' | pairs→'+D.querySelectorAll('.team').length}
 else{$('ncount').value='5';$('ggo').click();r='names: '+[...D.querySelectorAll('.gitem')].map(x=>x.textContent).join(', ')}
}else{const ch=D.querySelectorAll('#variants .chip');if(ch.length>1){ch[1].click();r='preset2→'+$('count').textContent+' '}$('spin').click();await new Promise(x=>setTimeout(x,5100));r+='popup '+$('pop').classList.contains('on')+' : '+$('popwin').textContent+($('pophex').textContent?' '+$('pophex').textContent:'')}
console.log(f.padEnd(32),r,errs.length?'ERR '+errs:'')}process.exit()})();
