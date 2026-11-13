// Header search: open/close, keyboard, results, navigation, mobile, other languages.
const {chromium}=require('playwright');const OUT=process.argv[2]||'.';let fails=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)fails++};
(async()=>{const b=await chromium.launch();
for(const [name,vp] of [['desk',{width:1440,height:900}],['mob',{width:390,height:844}]]){
 const c=await b.newContext({viewport:vp});await c.route(/clarity/,r=>r.fulfill({body:''}));const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://localhost:8830/coin-flip.html');await p.waitForTimeout(300);
 ok(await p.isVisible('#srch'),name+': search button visible');
 await p.click('#srch');await p.waitForSelector('.sdlg[open]');ok(await p.evaluate(()=>document.activeElement.id==='sq'),name+': input focused');
 ok(await p.locator('.slist li').count()>=5,name+': popular list shown');
 if(name==='desk')await p.screenshot({path:OUT+'/search-pop-'+name+'.png'});
 await p.keyboard.type('coin');await p.waitForTimeout(100);ok((await p.locator('.slist li .st').first().textContent()).startsWith('Flip a Coin'),name+': "coin" → Flip a Coin');
 await p.keyboard.type('f');ok(!(await p.evaluate(()=>document.body.classList.contains('cfs-on'))),name+': typing f does not trigger fullscreen');
 await p.fill('#sq','team');ok((await p.locator('.slist li .st').first().textContent()).includes('Team'),name+': "team" result');
 await p.fill('#sq','raffle giveaway');ok(await p.locator('.slist li').count()>=1,name+': multi-word query');
 await p.fill('#sq','zzzqqq');ok(await p.locator('.snone').count()===1,name+': empty state');
 await p.fill('#sq','ruleta');ok((await p.locator('.slist li .st').first().textContent()).toLowerCase().includes('ruleta'),name+': Spanish pages found');
 await p.fill('#sq','dice');await p.screenshot({path:OUT+'/search-dice-'+name+'.png'});
 await p.keyboard.press('Escape');await p.waitForTimeout(150);ok(!(await p.isVisible('.sdlg[open]')),name+': Esc closes');
 await p.keyboard.press('Control+k');await p.waitForSelector('.sdlg[open]');ok(true,name+': Ctrl+K opens');
 await p.fill('#sq','dice');await p.keyboard.press('ArrowDown');await p.keyboard.press('ArrowUp');await p.keyboard.press('Enter');await p.waitForURL(/dice-roller/);await p.goto('http://localhost:8830/dice-roller.html');await p.waitForTimeout(300);ok(true,name+': Enter navigates');
 await p.locator('h1').click();await p.keyboard.press('/');await p.waitForSelector('.sdlg[open]');ok(true,name+': "/" opens');await p.keyboard.press('Escape');
 const ov=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);ok(!ov,name+': no overflow');
 await p.goto('http://localhost:8830/index.html');await p.waitForTimeout(300);await p.screenshot({path:OUT+'/search-hdr-'+name+'.png',clip:{x:0,y:0,width:vp.width,height:90}});
 await p.goto('http://localhost:8830/es.html');ok((await p.getAttribute('#srch','aria-label'))==='Buscar herramientas',name+': Spanish label');
 ok(errs.length===0,name+': no page errors '+errs.join(';'));await c.close()}
await b.close();console.log(fails?fails+' FAILED':'ALL PASSED');process.exit(fails?1:0)})();
