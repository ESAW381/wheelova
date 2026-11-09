// New pages (Nov 8 2026): spin works, presets load, localized UI, no errors. Run with dist on :8830. Arg: screenshot dir.
const {chromium}=require('playwright');const dir=process.argv[2]||'/tmp';
(async()=>{const b=await chromium.launch();let bad=0;const t=(c,m)=>{if(!c)bad++;console.log((c?'PASS ':'FAIL ')+m)};
const ctx=await b.newContext({timezoneId:'America/New_York',viewport:{width:390,height:844},deviceScaleFactor:1,reducedMotion:'reduce'});await ctx.route(/clarity\.ms/,r=>r.fulfill({status:200,body:''}));
for(const [u,chip,expect] of [['random-word-wheel','Verbs','jump'],['drawing-prompt-wheel','Scenes','a market at sunrise'],['food-wheel','Cuisines','Italian'],['es/ruleta-de-colores','Primarios (3)','Rojo'],['es/ruleta-de-numeros','1–20','20'],['fr','Oui / Non','Oui'],['vi','Hôm nay ăn gì?','Phở']]){
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://localhost:8830/'+u+'.html');await p.waitForTimeout(300);
 await p.click(`#variants button:has-text("${chip}")`);await p.waitForTimeout(150);
 t((await p.inputValue('#entries')).split('\n').includes(expect),u+': preset "'+chip+'" loads');
 await p.click('#spin');await p.waitForSelector('#pop.on',{timeout:15000});
 const w=(await p.textContent('#popwin')).trim();t((await p.inputValue('#entries')).split('\n').includes(w),u+': spin picks an entry ('+w+')');
 if(u==='es/ruleta-de-colores'){const bg=await p.$eval('#popswatch',e=>getComputedStyle(e).display);t(bg==='block','colores: swatch shown');t(/#[0-9A-F]{6}/i.test(await p.textContent('#pophex')),'colores: hex shown')}
 await p.keyboard.press('Escape');await p.click('#popclose',{timeout:1000}).catch(()=>{});
 if(u==='es/ruleta-de-numeros'){await p.fill('#nmin','5');await p.fill('#nmax','3');await p.click('#ngo');t(/Hasta/.test(await p.textContent('#nerr')),'numeros: Spanish range error');await p.fill('#nmax','15');await p.click('#ngo');t((await p.inputValue('#entries')).split('\n').length===11,'numeros: range 5–15 builds 11 slices')}
 t(await p.evaluate(()=>document.documentElement.scrollWidth<=390),u+': no horizontal overflow');
 await p.evaluate(()=>window.scrollTo(0,0));await p.screenshot({path:dir+'/np-'+u.replace('/','_')+'.png'});
 t(errs.length===0,u+': no page errors '+errs.join(';'));await p.close()}
const p=await (await b.newContext({timezoneId:'Europe/Paris'})).newPage();await p.goto('http://localhost:8830/fr.html');await p.waitForTimeout(400);t(/Accepter/.test(await p.textContent('#wvcons')),'fr: French cookie banner');
const pv=await (await b.newContext({timezoneId:'Europe/Berlin'})).newPage();await pv.goto('http://localhost:8830/vi.html');await pv.waitForTimeout(400);t(/Đồng ý/.test(await pv.textContent('#wvcons')),'vi: Vietnamese cookie banner');
console.log(bad?'FAILED '+bad:'ALL PASSED');await b.close()})();
