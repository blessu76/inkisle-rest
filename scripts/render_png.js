// Render PNGs from the generated SVG art with headless Chromium (Playwright).
//   NODE_PATH=<dir containing playwright> node scripts/render_png.js
// -> assets/og-image.png (1200x630), assets/icon-180.png, assets/icon-512.png
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const A = path.join(__dirname, '..', 'assets');
(async () => {
  const b = await chromium.launch();
  const jobs = [['og-source.svg', 'og-image.png', 1200, 630, false], ['favicon.svg', 'icon-180.png', 180, 180, true], ['favicon.svg', 'icon-512.png', 512, 512, true]];
  for (const [src, out, w, h] of jobs) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    const svg = fs.readFileSync(path.join(A, src), 'utf8');
    await p.setContent(`<body style="margin:0"><div style="width:${w}px;height:${h}px">${svg.replace(/width="\d+" height="\d+"/, `width="${w}" height="${h}"`)}</div></body>`);
    await p.screenshot({ path: path.join(A, out) });
    await p.close();
  }
  await b.close();
  console.log('render_png: ok');
})();
