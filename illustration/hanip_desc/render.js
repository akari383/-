const { chromium } = require('playwright');
(async () => {
  const ids = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport:{width:600,height:900}, deviceScaleFactor:2 });
  for (const id of ids){
    await p.goto('file://'+process.cwd()+'/shot'+id+'.html',{waitUntil:'networkidle'});
    await p.waitForTimeout(400);
    await (await p.$('.sc')).screenshot({path:'raw'+id+'.png'});
  }
  await b.close();
})();
