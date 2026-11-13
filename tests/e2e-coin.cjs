// Coin flip redesign: behaviour + layout checks. Run with dist served on :8830.
const {chromium}=require('playwright');const OUT=process.argv[2]||'.';
let fails=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)fails++};
(async()=>{const b=await chromium.launch();
for(const [name,vp] of [['desk',{width:1440,height:900}],['mob',{width:390,height:844}]]){
 const ctx=await b.newContext({viewport:vp});await ctx.route(/clarity/,r=>r.fulfill({body:''}));const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://localhost:8830/coin-flip.html');await p.waitForTimeout(400);
 ok(await p.locator('.c3d').count()===1,name+': one coin visible on load');
 ok(await p.locator('.c3d').first().isVisible(),name+': coin is on screen');
 if(name==='desk')await p.screenshot({path:OUT+'/coin-load-'+name+'.png'});
 await p.click('#cflip');await p.waitForTimeout(1400);
 const r=(await p.textContent('#cres')).trim();ok(r==='Heads'||r==='Tails',name+': Flip button gives '+r);
 ok(await p.textContent('#stot')==='1',name+': total = 1');
 await p.locator('.c3d').first().click();await p.waitForTimeout(1300);ok(await p.textContent('#stot')==='2',name+': tap coin flips');
 await p.locator('h1').click();await p.keyboard.press('Space');await p.waitForTimeout(1300);ok(await p.textContent('#stot')==='3',name+': Space flips');
 await p.click('#cn button[data-v="3"]');ok(await p.locator('.c3d').count()===3,name+': 3 coins');
 await p.click('#cflip');await p.waitForTimeout(1500);ok(/\d+ Heads · \d+ Tails/.test(await p.textContent('#cres')),name+': multi result line');
 ok(await p.textContent('#stot')==='6',name+': stats count every coin');
 await p.screenshot({path:OUT+'/coin-3-'+name+'.png'});
 await p.click('#cfaces button[data-v="yn"]');await p.click('#cflip');await p.waitForTimeout(1500);ok(/Yes|No/.test(await p.textContent('#cres')),name+': Yes/No faces');
 await p.click('#cfaces button[data-v="custom"]');await p.fill('#cfh','Pizza');await p.fill('#cft','Tacos');
 ok((await p.locator('.cf.ch').first().textContent())==='Pizza',name+': custom face text');
 await p.click('#cn button[data-v="10"]');ok(await p.locator('.c3d').count()===10,name+': 10 coins');
 await p.click('#cs button[data-v="silver"]');ok(await p.getAttribute('#tool','data-style')==='silver',name+': silver style');
 await p.click('#cflip');await p.waitForTimeout(1900);
 await p.screenshot({path:OUT+'/coin-10-'+name+'.png'});
 await p.click('#cbatchgo');ok(/longest streak/.test(await p.textContent('#cbatch')),name+': batch of 100');
 ok(await p.locator('.bstrip i').count()===100,name+': batch strip 100');
 await p.reload();await p.waitForTimeout(400);ok(await p.locator('.c3d').count()===10&&(await p.locator('.cf.ch').first().textContent())==='Pizza',name+': settings persist');
 ok(Number(await p.textContent('#stot'))>=16,name+': stats persist');
 await p.click('#creset');ok(await p.textContent('#stot')==='0',name+': reset');
 await p.goto('http://localhost:8830/coin-flip.html?h=Left&t=Right');await p.waitForTimeout(300);ok((await p.locator('.cf.ch').first().textContent())==='Left',name+': share link faces');
 const ov=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);ok(!ov,name+': no horizontal overflow');
 await p.evaluate(()=>{localStorage.clear()});await p.goto('http://localhost:8830/coin-flip.html');await p.waitForTimeout(300);
 await p.keyboard.press('f');await p.waitForTimeout(400);ok(await p.evaluate(()=>document.body.classList.contains('cfs-on')),name+': fullscreen on F');
 await p.screenshot({path:OUT+'/coin-fs-'+name+'.png'});
 ok(errs.length===0,name+': no page errors '+errs.join(';'));await ctx.close()}
// fairness smoke test: 20,000 single flips through the UI code path is slow; check RNG split directly
const p=await b.newPage();await p.goto('http://localhost:8830/coin-flip.html');
const h=await p.evaluate(()=>{let h=0;for(let i=0;i<200000;i++)if(WVRNG.randInt(2)===0)h++;return h});
ok(Math.abs(h-100000)<1500,'RNG 200k flips: '+h+' heads');
await b.close();console.log(fails?fails+' FAILED':'ALL PASSED');process.exit(fails?1:0)})();
