// Dice roller redesign: behaviour + layout checks. Run with dist served on :8830.
const {chromium}=require('playwright');const OUT=process.argv[2]||'.';let fails=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)fails++};
(async()=>{const b=await chromium.launch();
for(const [name,vp] of [['desk',{width:1440,height:900}],['mob',{width:390,height:844}]]){
 const c=await b.newContext({viewport:vp});await c.route(/clarity/,r=>r.fulfill({body:''}));const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://localhost:8830/dice-roller.html');await p.waitForTimeout(300);
 ok(await p.locator('.dd').count()===1&&await p.locator('.dd').first().isVisible(),name+': a die is visible on load');
 await p.click('#droll');await p.waitForTimeout(900);let t=+(await p.textContent('#dres'));ok(t>=1&&t<=20,name+': d20 roll in 1–20 ('+t+')');
 await p.locator('.dd').first().click();await p.waitForTimeout(900);ok((await p.locator('#dhist li').count())===2,name+': tapping the die rolls; history 2');
 await p.locator('h1').click();await p.keyboard.press('Space');await p.waitForTimeout(900);ok((await p.locator('#dhist li').count())===3,name+': Space rolls');
 await p.click('#dside button[data-v="6"]');await p.click('#dnp');await p.click('#dmp');await p.click('#dmp');await p.click('#dmp');
 ok((await p.textContent('#dnot'))==='2d6+3',name+': notation 2d6+3');ok(await p.locator('.d6 .dshape i').count()===18,name+': two d6 with pips');
 await p.click('#droll');await p.waitForTimeout(900);t=+(await p.textContent('#dres'));ok(t>=5&&t<=15,name+': 2d6+3 total in 5–15 ('+t+')');
 ok(/2d6\+3: \d \+ \d \+ 3 = \d+/.test(await p.textContent('#dbrk')),name+': breakdown shown');
 await p.screenshot({path:OUT+'/dice-2d6-'+name+'.png'});
 await p.click('#dside button[data-v="20"]');await p.click('#dnm');await p.click('#dadv button[data-v="adv"]');ok(await p.locator('.dd').count()===2,name+': advantage shows two d20');
 await p.click('#droll');await p.waitForTimeout(900);
 const v=await p.$$eval('.dd .dshape b',e=>e.map(x=>+x.textContent));const base=+(await p.textContent('#dres'))-3;ok(base===Math.max(...v),name+': advantage keeps higher '+v+' → '+base);
 ok(await p.locator('.dd.dropped').count()===1,name+': other die dimmed');
 await p.click('#dadv button[data-v="dis"]');await p.click('#droll');await p.waitForTimeout(900);
 const v2=await p.$$eval('.dd .dshape b',e=>e.map(x=>+x.textContent));ok(+(await p.textContent('#dres'))-3===Math.min(...v2),name+': disadvantage keeps lower');
 await p.screenshot({path:OUT+'/dice-adv-'+name+'.png'});
 await p.click('#dnp');ok(await p.isDisabled('#dadv button[data-v="adv"]'),name+': advantage disabled with 2 dice');
 await p.click('#dside button[data-v="100"]');for(let i=0;i<8;i++)await p.click('#dnp');ok(await p.locator('.dd').count()===10,name+': 10 d100');
 await p.click('#droll');await p.waitForTimeout(1000);await p.screenshot({path:OUT+'/dice-10-'+name+'.png'});
 const ov=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);ok(!ov,name+': no horizontal overflow');
 await p.reload();await p.waitForTimeout(300);ok(await p.locator('.dd').count()===10&&(await p.locator('#dhist li').count())>=6,name+': settings + history persist');
 await p.click('#dclear');ok((await p.locator('#dhist li.hnone').count())===1,name+': clear history');
 await p.goto('http://localhost:8830/dice-roller.html?r=3d8-2');await p.waitForTimeout(300);ok((await p.textContent('#dnot'))==='3d8-2',name+': share link loads 3d8-2');
 await p.keyboard.press('f');await p.waitForTimeout(300);ok(await p.evaluate(()=>document.body.classList.contains('cfs-on')),name+': F fullscreen');await p.keyboard.press('Escape');
 await p.keyboard.press('Control+k');await p.waitForSelector('.sdlg[open]');await p.keyboard.type(' f');ok(!(await p.evaluate(()=>document.querySelector('.sdlg[open] #sq').value==='')),name+': typing in search does not roll');
 ok(errs.length===0,name+': no page errors '+errs.join(';'));await c.close()}
const p=await b.newPage();await p.goto('http://localhost:8830/dice-roller.html');
const r=await p.evaluate(()=>{const c=Array(20).fill(0);for(let i=0;i<200000;i++)c[WVRNG.randInt(20)]++;return [Math.min(...c),Math.max(...c)]});
ok(r[0]>9400&&r[1]<10600,'RNG 200k d20 rolls: every face '+r.join('–'));
await b.close();console.log(fails?fails+' FAILED':'ALL PASSED');process.exit(fails?1:0)})();
