// Playwright checks for Phase 1 (privacy, dialogs, number input). Run from repo root after building:
//   (cd dist && python3 -m http.server 8830 &) ; NODE_PATH=$(npm root -g) node tests/e2e-trust.cjs
const {chromium}=require('playwright');const B='http://localhost:8830/';let fails=0;
const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)fails++};
const enc=s=>Buffer.from(s).toString('base64').replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext();const clarity=[];
 await ctx.route(/clarity\.ms/,r=>{clarity.push(r.request().url());r.abort()});
 const page=async u=>{const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('dialog',d=>{errs.push('dialog:'+d.message());d.dismiss()});await p.goto(B+u);await p.waitForTimeout(300);return [p,errs]};
 let [p,errs]=await page('name-picker-wheel.html');ok(clarity.length>=1,'Clarity requested on a normal page');
 clarity.length=0;[p]=await page('name-picker-wheel.html#w='+enc('Secret A\nSecret B'));ok(clarity.length===0,'Clarity NOT requested on a shared-wheel link');
 ok((await p.inputValue('#entries')).startsWith('Secret A'),'shared entries loaded');
 clarity.length=0;await page('embed-a-wheel.html');ok(clarity.length===0,'Clarity NOT requested on the embed generator');
 [p,errs]=await page('name-picker-wheel.html');ok(!(await p.content()).includes('_vercel/insights'),'no Vercel insights tag');
 ok((await p.textContent('#sharehelp')).includes('not encrypted'),'share dialog explains encoding');
 // XSS strings render as text
 [p,errs]=await page('name-picker-wheel.html#w='+enc('<img src=x onerror=alert(1)>\n"><script>alert(2)</script>\nThird\nFourth'));await p.click('#spin');await p.waitForSelector('#pop.on',{timeout:10000});
 ok(errs.length===0,'no script execution from entries');
 // focus trap in winner dialog
 for(let i=0;i<6;i++)await p.keyboard.press('Tab');ok(await p.evaluate(()=>document.getElementById('pop').contains(document.activeElement)),'Tab stays inside winner dialog');
 await p.keyboard.press('Shift+Tab');ok(await p.evaluate(()=>document.getElementById('pop').contains(document.activeElement)),'Shift+Tab stays inside winner dialog');
 await p.keyboard.press('Escape');ok(await p.evaluate(()=>document.activeElement.id==='spin'),'focus returns to Spin after close');
 // share dialog trap + return
 await p.click('#sharebtn');for(let i=0;i<5;i++)await p.keyboard.press('Tab');ok(await p.evaluate(()=>document.getElementById('sharepop').contains(document.activeElement)),'Tab stays inside share dialog');
 await p.keyboard.press('Escape');ok(await p.evaluate(()=>document.activeElement.id==='sharebtn'),'focus returns to Share after close');
 // number generator validation and big ranges
 [p,errs]=await page('random-number-generator.html');const gen=async(a,c,n)=>{await p.fill('#nmin',a);await p.fill('#nmax',c);await p.fill('#ncount',n);await p.click('#ggo');return [await p.textContent('#gerr'),await p.evaluate(()=>[...document.querySelectorAll('#gout .gitem')].map(x=>x.textContent))]};
 let [e1]=await gen('1','1e15','1');ok(/whole numbers/.test(e1),'exponent input rejected');
 [e1]=await gen('1.5','10','1');ok(/whole numbers/.test(e1),'decimal input rejected');
 [e1]=await gen('1','99999999999999999999','1');ok(/between/.test(e1),'over-safe-integer rejected');
 let [e2,vals]=await gen('1','1000000000000','50');ok(!e2&&vals.length===50&&vals.every(v=>+v>=1&&+v<=1e12),'1..1e12 generates in range');
 [e2,vals]=await gen('10','1','10');ok(!e2&&new Set(vals).size===10&&vals.every(v=>+v>=1&&+v<=10),'inverted range swapped, 10 unique');
 [p,errs]=await page('coin-flip.html');await p.selectOption('#ccount','100');await p.click('#ggo');ok(/heads/.test(await p.textContent('#gcount'))&&errs.length===0,'coin flip works');
 [p,errs]=await page('dice-roller.html');await p.click('#ggo');ok(/Total/.test(await p.textContent('#gcount'))&&errs.length===0,'dice roller works');
 [p,errs]=await page('flag-quiz.html');await p.click('#qstart');ok((await p.$$('.qopt')).length===4&&errs.length===0,'flag quiz works');
 [p,errs]=await page('random-pair-generator.html');await p.click('#ggo');ok(/pairs/.test(await p.textContent('#gcount'))&&errs.length===0,'pair generator works');
 // homepage card
 [p]=await page('');const html=await p.content();ok(!html.includes('Fair-Spin receipts')&&html.includes('Tested fairness'),'homepage card replaced');
 // mobile overflow
 const m=await b.newPage({viewport:{width:360,height:740}});let over=[];for(const u of ['','name-picker-wheel.html','random-number-generator.html','flag-quiz.html','random-pair-generator.html','embed-a-wheel.html','is-the-wheel-random.html','es.html','privacy.html','guides/fair-giveaway.html']){await m.goto(B+u);const w=await m.evaluate(()=>document.documentElement.scrollWidth);if(w>360)over.push(u)}
 ok(over.length===0,'no horizontal overflow at 360px '+over.join(','));
 await b.close();console.log(fails?fails+' FAILED':'ALL PASSED');process.exit(fails?1:0)})();
