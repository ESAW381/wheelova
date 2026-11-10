// Embed snippets carry a plain, followed credit link to the matching tool page, outside the iframe.
// Copies the snippet from several tools, pastes each into a blank HTML file, and loads it. Run with dist on :8830. Arg: scratch dir.
const {chromium}=require('playwright');const fs=require('fs');const dir=process.argv[2]||'/tmp';
(async()=>{const b=await chromium.launch();let bad=0;const t=(c,m)=>{if(!c)bad++;console.log((c?'PASS ':'FAIL ')+m)};
const ctx=await b.newContext({reducedMotion:'reduce',timezoneId:'America/New_York'});await ctx.route(/clarity/,r=>r.fulfill({body:''}));
await ctx.route(/^https:\/\/wheelova\.com\/embed/,async r=>{const u=new URL(r.request().url());r.fulfill({status:200,contentType:'text/html',body:fs.readFileSync('dist/embed.html','utf8').replace(/(src|href)="\//g,'$1="http://localhost:8830/')})});
const cases=[['name-picker-wheel','/name-picker-wheel','Random name picker','by Wheelova'],['raffle-wheel','/raffle-wheel','Raffle wheel','by Wheelova'],['es/ruleta-si-o-no','/es/ruleta-si-o-no','Ruleta sí o no','de Wheelova'],['index','/','Spin the wheel','by Wheelova'],['vi','/vi','Vòng quay may mắn','của Wheelova']];
for(const [page,path,anchor,by] of cases){
 const p=await ctx.newPage();await p.goto('http://localhost:8830/'+page+'.html');await p.waitForTimeout(300);
 await p.click('#embedbtn');await p.waitForTimeout(200);const code=await p.inputValue('#embedcode');
 t(await p.isVisible('.ekeep'),page+': keep-the-link note shown');
 const f=dir+'/blank-'+page.replace('/','_')+'.html';fs.writeFileSync(f,'<!doctype html><html><head><meta charset="utf-8"><title>Blank</title></head><body>\n'+code+'\n</body></html>');
 const h=await ctx.newPage();await h.goto('file://'+f);await h.waitForTimeout(800);
 const a=await h.$eval('body > p > a',e=>({href:e.getAttribute('href'),text:e.textContent,rel:e.getAttribute('rel'),inIframe:!!e.closest('iframe')}));
 const ptxt=await h.$eval('body > p',e=>e.textContent);
 t(a.href==='https://wheelova.com'+path,page+': link → '+a.href);t(a.text===anchor&&ptxt.trim()===anchor+' '+by,page+': text "'+ptxt.trim()+'"');t(!a.rel,page+': no rel (followed link)');
 const fr=h.frames().find(x=>x!==h.mainFrame());const ok=fr&&await fr.waitForSelector('#spin',{timeout:5000}).then(()=>true).catch(()=>false);t(ok,page+': iframe wheel loads');
 await h.close();await p.close()}
const g=await ctx.newPage();await g.goto('http://localhost:8830/embed-a-wheel.html');await g.waitForTimeout(800);
const code=await g.inputValue('#ecode');t(/<\/iframe>\n<p style="font:12px\/1\.4 system-ui,sans-serif;margin:4px 0 0"><a href="https:\/\/wheelova\.com\/">Spin the wheel<\/a> by Wheelova<\/p>$/.test(code),'embed-a-wheel: snippet ends with the credit line');
t(await g.isVisible('.ecredit')&&(await g.textContent('.ecredit')).trim()==='Spin the wheel by Wheelova','embed-a-wheel: live preview shows the credit line');t(await g.isVisible('.ekeep'),'embed-a-wheel: keep-the-link note shown');
console.log(bad?'FAILED '+bad:'ALL PASSED');await b.close()})();
