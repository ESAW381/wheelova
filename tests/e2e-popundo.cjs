// "Remove from wheel" in the winner pop-up can be undone. Run with dist on :8830.
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();let bad=0;const t=(c,m)=>{if(!c)bad++;console.log((c?'PASS ':'FAIL ')+m)};
const c=await b.newContext({reducedMotion:'reduce',timezoneId:'America/New_York'});await c.route(/clarity/,r=>r.fulfill({body:''}));
for(const [u,re] of [['decision-wheel','Removed'],['es/ruleta-de-decisiones','Se quitó'],['vi','Đã loại']]){
 const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('http://localhost:8830/'+u+'.html');await p.waitForTimeout(300);
 if(await p.$('#remove[aria-pressed="true"]'))await p.click('#remove');
 const before=await p.inputValue('#entries');await p.click('#spin');await p.waitForSelector('#pop.on');const w=(await p.textContent('#popwin')).trim();
 t(await p.isVisible('#popremove'),u+': Remove from wheel shown');await p.click('#popremove');await p.waitForTimeout(200);
 t(!(await p.inputValue('#entries')).split('\n').includes(w),u+': winner removed ('+w+')');
 t(await p.isVisible('#wtundo')&&new RegExp(re).test(await p.textContent('#wtmsg')),u+': toast with Undo: '+(await p.textContent('#wtmsg')));
 await p.click('#wtundo');await p.waitForTimeout(200);t(await p.inputValue('#entries')===before,u+': Undo restores the list');
 t(errs.length===0,u+': no errors '+errs.join(';'));await p.close()}
console.log(bad?'FAILED '+bad:'ALL PASSED');await b.close()})();
