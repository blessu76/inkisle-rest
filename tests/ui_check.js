// UI gate: no horizontal overflow at 375 / 320 / 768 / 1280 px, no console errors, screenshots.
//   NODE_PATH=<dir containing playwright> node tests/ui_check.js [outDir]
// Serves the repo root on a random local port (static, like GitHub Pages: /dir/ -> /dir/index.html).
const http = require('http'), fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const ROOT = path.join(__dirname, '..');
const OUT = process.argv[2] || path.join(require('os').tmpdir(), 'inkisle-ui');
const WIDTHS = [[375, 812], [320, 568], [768, 1024], [1280, 800]];
const TYPES = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.xml': 'application/xml', '.txt': 'text/plain' };
const server = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  let f = path.join(ROOT, p);
  if (!f.startsWith(ROOT)) { res.writeHead(403); return res.end(); }
  if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html');
  if (!fs.existsSync(f)) { res.writeHead(404); return res.end('404'); }
  res.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});
function pagesToCheck() {
  const out = ['/', '/about/', '/privacy/', '/journal/'];
  const langs = fs.readdirSync(ROOT).filter(d => /^[a-z]{2}$/.test(d) && fs.existsSync(path.join(ROOT, d, 'index.html')));
  const J = path.join(ROOT, 'content', 'journal');
  const slugs = fs.existsSync(J) ? fs.readdirSync(J).filter(d => fs.statSync(path.join(J, d)).isDirectory()) : [];
  if (slugs.length) out.push('/journal/' + slugs[0] + '/');
  for (const l of langs) { out.push('/' + l + '/'); if (slugs.length) out.push('/' + l + '/journal/' + slugs[0] + '/'); }
  return out;
}
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const base = 'http://127.0.0.1:' + server.address().port;
  const b = await chromium.launch();
  const bad = [];
  let n = 0;
  for (const [w, h] of WIDTHS) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    for (const pth of pagesToCheck()) {
      const page = await ctx.newPage();
      const errs = [];
      page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
      page.on('pageerror', e => errs.push(String(e)));
      page.on('requestfailed', r => errs.push('request failed: ' + r.url()));
      const resp = await page.goto(base + pth, { waitUntil: 'load' });
      if (resp.status() !== 200) bad.push(`${w}px ${pth}: HTTP ${resp.status()}`);
      const m = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, iw: window.innerWidth,
        wide: [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > window.innerWidth + 1 && !e.closest('.table-wrap') && !e.closest('.lang ul') && getComputedStyle(e).position !== 'fixed')
          .slice(0, 3).map(e => e.tagName + '.' + e.className) }));
      if (m.sw > m.iw) bad.push(`${w}px ${pth}: horizontal overflow scrollWidth ${m.sw} > ${m.iw} (${m.wide.join(', ')})`);
      for (const e of errs) bad.push(`${w}px ${pth}: console: ${e}`);
      n++;
      if (pth === '/' || pth === '/ko/' || pth === '/ar/' || /journal\/[^/]+\/$/.test(pth) && !pth.startsWith('/') === false && (pth.startsWith('/journal') || pth.startsWith('/ko/') || pth.startsWith('/ar/')))
        await page.screenshot({ path: path.join(OUT, `${w}-${pth.replace(/\//g, '_') || '_'}.png`), fullPage: true });
      await page.close();
    }
    await ctx.close();
  }
  // dark theme + open language menu once at 375
  const ctx = await b.newContext({ viewport: { width: 375, height: 812 }, colorScheme: 'dark' });
  const page = await ctx.newPage();
  await page.goto(base + '/', { waitUntil: 'load' });
  await page.click('.lang summary');
  await page.screenshot({ path: path.join(OUT, '375-dark-langmenu.png') });
  const sw = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
  if (sw > 0) bad.push('375px dark + language menu: overflow ' + sw);
  await b.close(); server.close();
  console.log(`ui_check: ${n} page views, screenshots in ${OUT}`);
  if (bad.length) { console.error('ui_check FAILED:\n  ' + bad.join('\n  ')); process.exit(1); }
  console.log('ui_check: OK — no horizontal overflow at 375/320/768/1280, no console errors');
})();
