// Consent gating for Microsoft Clarity. Run with dist served on :8830.
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();let bad=0;const t=(c,m)=>{if(!c)bad++;console.log((c?'PASS ':'FAIL ')+m)};
async function page(tz){const ctx=await b.newContext({timezoneId:tz});const reqs=[];await ctx.route(/clarity\.ms/,r=>{reqs.push(r.request().url());r.fulfill({status:200,contentType:'text/javascript',body:''})});const p=await ctx.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));p.reqs=reqs;return p}
let p=await page('America/New_York');await p.goto('http://localhost:8830/');await p.waitForTimeout(500);
t(p.reqs.length>0,'US: Clarity loads');t(!(await p.$('#wvcons')),'US: no banner');
p=await page('Asia/Karachi');await p.goto('http://localhost:8830/name-picker-wheel.html');await p.waitForTimeout(500);t(p.reqs.length>0&&!(await p.$('#wvcons')),'PK: loads, no banner');
p=await page('Europe/Berlin');await p.goto('http://localhost:8830/');await p.waitForTimeout(500);
t(p.reqs.length===0,'DE: Clarity not loaded before consent');t(await p.isVisible('#wvcons'),'DE: banner shown');
await p.click('#wvcons [data-v="no"]');await p.waitForTimeout(300);t(p.reqs.length===0&&!(await p.$('#wvcons')),'DE: decline keeps it off');
await p.reload();await p.waitForTimeout(400);t(p.reqs.length===0&&!(await p.$('#wvcons')),'DE: decline remembered');
await p.click('footer [data-wvcookies]');await p.waitForTimeout(200);t(await p.isVisible('#wvcons'),'Cookie settings reopens banner');
await p.click('#wvcons [data-v="yes"]');await p.waitForTimeout(500);t(p.reqs.length>0,'DE: accept loads Clarity');
await p.reload();await p.waitForTimeout(500);t(!(await p.$('#wvcons')),'DE: accept remembered');
p=await page('Europe/London');await p.goto('http://localhost:8830/es.html');await p.waitForTimeout(400);t(/Aceptar/.test(await p.textContent('#wvcons')),'Spanish banner');
p=await page('Europe/Madrid');await p.goto('http://localhost:8830/name-picker-wheel.html#w=QQpC');await p.waitForTimeout(400);t(p.reqs.length===0&&!(await p.$('#wvcons')),'shared link: no Clarity, no banner');
p=await page('Europe/Paris');await p.setViewportSize({width:360,height:740});await p.goto('http://localhost:8830/');await p.waitForTimeout(400);
t(await p.evaluate(()=>document.documentElement.scrollWidth<=360),'banner fits 360px');
await p.screenshot({path:process.argv[2]||'/tmp/consent.png'});
t(p.errs.length===0,'no page errors');console.log(bad?'FAILED '+bad:'ALL PASSED');await b.close()})();
