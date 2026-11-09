// "+ Add wheel" on every homepage (en/es/fr/vi). Run with dist on :8830. Arg: screenshot dir.
const {chromium}=require('playwright');const dir=process.argv[2]||'/tmp';
(async()=>{const b=await chromium.launch();let bad=0;const t=(c,m)=>{if(!c)bad++;console.log((c?'PASS ':'FAIL ')+m)};
const ctx=await b.newContext({viewport:{width:1280,height:900},reducedMotion:'reduce',timezoneId:'America/New_York'});await ctx.route(/clarity/,r=>r.fulfill({body:''}));
for(const [u,all,wheel] of [['index','Spin all wheels','Wheel 2'],['es','Girar todas las ruletas','Ruleta 2'],['fr','Faire tourner toutes les roues','Roue 2'],['vi','Quay tất cả','Vòng 2']]){
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('http://localhost:8830/'+u+'.html');await p.waitForTimeout(300);
 const main=(await p.inputValue('#entries')).split('\n').filter(Boolean);
 t(await p.isVisible('#npadd'),u+': Add wheel button under entries');await p.click('#npadd');await p.waitForTimeout(200);
 t(await p.isVisible('#multi')&&!(await p.isVisible('#tool')),u+': switches to two wheels');
 t((await p.textContent('#mtabs button:nth-child(2)')).startsWith(wheel)&&(await p.textContent('#mall'))===all,u+': translated labels ('+wheel+', '+all+')');
 await p.click('#mtabs button:nth-child(1)');t((await p.inputValue('#mta')).split('\n').filter(Boolean).join('|')===main.join('|'),u+': wheel 1 keeps the homepage list');
 await p.click('#mall');await p.waitForTimeout(400);t((await p.$$eval('.mres',e=>e.filter(x=>x.textContent.trim()).length))===2,u+': spin all works');
 await p.screenshot({path:dir+'/mh-'+u+'.png'});
 await p.click('#mdel');await p.waitForTimeout(150);t(await p.isVisible('#tool')&&!(await p.isVisible('#multi')),u+': back to single wheel');
 t(errs.length===0,u+': no page errors '+errs.join(';'));await p.close()}
const a=await ctx.newPage();await a.goto('http://localhost:8830/es.html');await a.click('#npadd');await a.goto('http://localhost:8830/index.html');await a.waitForTimeout(300);
t(await a.isVisible('#tool'),'each homepage keeps its own multi-wheel state (EN not affected by ES)');
console.log(bad?'FAILED '+bad:'ALL PASSED');await b.close()})();
