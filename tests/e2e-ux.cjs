// Phase 2 UX checks. Serve dist on 8830 first (see e2e-trust.cjs), then: NODE_PATH=$(npm root -g) node tests/e2e-ux.cjs
const {chromium}=require('playwright');const B='http://localhost:8830/';let fails=0;const fs=require('fs');
const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)fails++};
const enc=s=>Buffer.from(s).toString('base64').replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({acceptDownloads:true});await ctx.route(/clarity\.ms/,r=>r.abort());
 const errs=[];const page=async u=>{const p=await ctx.newPage();p.on('pageerror',e=>errs.push(u+': '+e.message));await p.goto(B+u);await p.waitForTimeout(250);return p};
 let p=await page('name-picker-wheel.html');const val=()=>p.inputValue('#entries');
 await p.fill('#entries','Ana\nBo\nCy');await p.click('#clear');ok((await val())===''&&!(await p.$eval('#wtoast',e=>e.hidden)),'Clear shows Undo toast');
 await p.click('#wtundo');ok((await val())==='Ana\nBo\nCy','Undo restores cleared list');
 await p.click('#variants .chip >> nth=0');ok((await val())!=='Ana\nBo\nCy'&&!(await p.$eval('#wtundo',e=>e.hidden)),'Preset offers Undo');await p.click('#wtundo');ok((await val())==='Ana\nBo\nCy','Undo restores after preset');
 // saved wheels
 await p.click('#wsaves summary');await p.click('#wssave');ok(/name/i.test(await p.textContent('#wtmsg')),'Save without name asks for a name');
 await p.fill('#wsname','Period 3');await p.press('#wsname','Enter');ok((await p.$$('#wslist li')).length===1,'Saved wheel listed');
 await p.fill('#entries','Xi\nYu');await p.fill('#wsname','Team B');await p.click('#wssave');ok((await p.$$('#wslist li')).length===2,'Second wheel saved');
 await p.reload();await p.waitForTimeout(200);await p.click('#wsaves summary');ok((await p.$$('#wslist li')).length===2,'Saved wheels persist after reload');
 const names=await p.$$eval('#wslist .wsn',l=>l.map(x=>x.textContent));ok(names[0].startsWith('Team B')&&names[1].startsWith('Period 3'),'Newest first');
 await p.click('#wslist li:nth-child(2) .btn');ok((await val())==='Ana\nBo\nCy','Load restores entries');
 await p.click('#wslist li:nth-child(1) .linkbtn');ok((await p.$$('#wslist li')).length===1,'Delete removes');await p.click('#wtundo');ok((await p.$$('#wslist li')).length===2,'Undo delete');
 await p.fill('#entries','Zed\nWu');await p.fill('#wsname','period 3');await p.click('#wssave');ok((await p.$$('#wslist li')).length===2&&/Updated/.test(await p.textContent('#wtmsg')),'Same name updates (case-insensitive)');
 // XSS in saved names
 await p.fill('#wsname','<img src=x onerror=alert(9)>');await p.click('#wssave');ok(errs.length===0&&(await p.$$('#wslist img')).length===0,'Saved names rendered as text');
 // results export
 await p.fill('#entries','=SUM(1,2)\nBob, Jr.\n"Q"\nDee\nEve');for(let i=0;i<3;i++){await p.click('#spin');await p.waitForSelector('#pop.on',{timeout:10000});await p.click('#popclose');await p.waitForTimeout(100)}
 ok(!(await p.$eval('#resacts',e=>e.hidden)),'Export buttons appear after a spin');
 const [dl]=await Promise.all([p.waitForEvent('download'),p.click('#rcsv')]);const csv=fs.readFileSync(await dl.path(),'utf8');
 ok(/^﻿Spin,Winner,Time\r\n1,/.test(csv)&&csv.split('\r\n').length===4,'CSV has header and 3 rows');ok(!/\n\d+,=SUM/.test(csv),'CSV neutralises formula cells');
 ok(/wheelova-results-\d{4}-\d\d-\d\d\.csv/.test(dl.suggestedFilename()),'CSV filename');
 // shared wheel banner
 await p.fill('#entries','Mine1\nMine2');await p.waitForTimeout(100);
 p=await page('name-picker-wheel.html#w='+enc('Sh1\nSh2\nSh3'));ok(!(await p.$eval('#sharenote',e=>e.hidden)),'Shared banner visible');
 await p.fill('#entries','Sh1\nSh2\nEdited');await p.waitForTimeout(100);ok(await p.evaluate(()=>localStorage.getItem('wv_entries_names'))==='Mine1\nMine2','Editing a shared wheel does not overwrite own list');
 await p.click('#mylist');ok((await val())==='Mine1\nMine2','Back to my list restores own list');
 p=await page('name-picker-wheel.html#w='+enc('Sh1\nSh2\nSh3'));await p.click('#savesh');ok(await p.evaluate(()=>localStorage.getItem('wv_entries_names'))==='Sh1\nSh2\nSh3'&&await p.$eval('#sharenote',e=>e.hidden),'Keep as my list saves shared wheel');
 ok(!(await p.$eval('#wtundo',e=>e.hidden)),'Keep offers Undo');await p.click('#wtundo');ok(await p.evaluate(()=>localStorage.getItem('wv_entries_names'))==='Mine1\nMine2','Undo restores previous own list');
 p=await page('#w='+enc('H1\nH2'));ok(!(await p.$eval('#sharenote',e=>e.hidden)),'Homepage shows shared banner');
 // Spanish + other wheels load without errors
 for(const u of ['es/ruleta-de-nombres.html','es.html','yes-or-no-wheel.html','random-country-generator.html','raffle-wheel.html']){await page(u)}
 const m=await b.newPage({viewport:{width:360,height:740}});await m.goto(B+'name-picker-wheel.html');await m.click('#wsaves summary');ok(await m.evaluate(()=>document.documentElement.scrollWidth)<=360,'No overflow at 360px with saved-wheels panel open');
 ok(errs.length===0,'No page errors '+errs.join(' | '));
 await b.close();console.log(fails?fails+' FAILED':'ALL PASSED');process.exit(fails?1:0)})();
