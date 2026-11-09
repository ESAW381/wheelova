// Fullscreen for multiple wheels. Run with dist on :8830. Arg: screenshot dir.
const {chromium}=require('playwright');const dir=process.argv[2]||'/tmp';
(async()=>{const b=await chromium.launch();let bad=0;const t=(c,m)=>{if(!c)bad++;console.log((c?'PASS ':'FAIL ')+m)};
for(const [vw,vh,n] of [[1440,900,'desk'],[390,844,'phone']]){
const ctx=await b.newContext({viewport:{width:vw,height:vh},reducedMotion:'reduce'});await ctx.route(/clarity/,r=>r.fulfill({body:''}));
const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8830/name-picker-wheel.html');await p.waitForTimeout(300);await p.click('#npadd');await p.click('#madd');await p.waitForTimeout(150);
t(await p.isVisible('#mfs')&&!(await p.isVisible('#mfsall')),n+': fullscreen button shown, fullscreen spin hidden');
await p.click('#mfs');await p.waitForTimeout(300);
t(await p.evaluate(()=>document.body.classList.contains('is-mfs')),n+': fullscreen on');
t(!(await p.isVisible('.mpanel'))&&await p.isVisible('#mfsall'),n+': editor hidden, Spin all shown');
const fits=await p.evaluate(()=>{const r=[...document.querySelectorAll('.mwheel')].map(e=>e.getBoundingClientRect());return r.every(x=>x.right<=innerWidth+1&&x.left>=-1)&&Math.max(...r.map(x=>x.bottom))<=innerHeight+80});
t(fits,n+': 3 wheels fit the screen');
await p.click('#mfsall');await p.waitForTimeout(400);t((await p.$$eval('.mres',e=>e.filter(x=>x.textContent.trim()).length))===3,n+': Spin all works in fullscreen');
await p.screenshot({path:dir+'/mfs-'+n+'.png'});
await p.keyboard.press('Escape');await p.waitForTimeout(200);t(!(await p.evaluate(()=>document.body.classList.contains('is-mfs')))&&await p.isVisible('.mpanel'),n+': Escape exits');
await p.click('h1');await p.keyboard.press('f');await p.waitForTimeout(200);t(await p.evaluate(()=>document.body.classList.contains('is-mfs')&&!document.body.classList.contains('is-fs')),n+': F toggles multi fullscreen only');
await p.keyboard.press('f');await p.waitForTimeout(200);t(!(await p.evaluate(()=>document.body.classList.contains('is-mfs'))),n+': F again exits');
t(errs.length===0,n+': no page errors '+errs.join(';'));await ctx.close()}
console.log(bad?'FAILED '+bad:'ALL PASSED');await b.close()})();
