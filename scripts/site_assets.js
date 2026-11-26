// Builds site images. Run from the repo root AFTER `python3 scripts/build_site.py`:
//   node scripts/site_assets.js
// Writes site/favicon-32.png, site/apple-touch-icon.png, site/img/og-image.png (from the real page),
// and copies the sample PDF. Needs Playwright (Chromium); fonts load from Google Fonts.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const http = require('http');

const root = path.resolve(__dirname, '..');
const site = path.join(root, 'site');
const types = { '.html': 'text/html', '.svg': 'image/svg+xml', '.png': 'image/png', '.pdf': 'application/pdf' };

(async () => {
  fs.copyFileSync(path.join(root, 'workbook', 'exports', 'sample-summary-schedule-e.pdf'),
    path.join(site, 'sample-rental-books-2026.pdf'));
  const server = http.createServer((q, s) => {
    const p = path.join(site, decodeURIComponent(q.url.split('?')[0]).replace(/\/$/, '/index.html'));
    fs.readFile(p, (e, d) => { if (e) { s.writeHead(404); s.end(); return; }
      s.writeHead(200, { 'Content-Type': types[path.extname(p)] || 'application/octet-stream' }); s.end(d); });
  }).listen(0);
  const base = `http://localhost:${server.address().port}/`;
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const svg = fs.readFileSync(path.join(site, 'favicon.svg'), 'utf8');
  for (const [size, name] of [[32, 'favicon-32.png'], [180, 'apple-touch-icon.png']]) {
    await page.setViewportSize({ width: size, height: size });
    await page.setContent(`<style>html,body{margin:0}svg{width:${size}px;height:${size}px;display:block}</style>${svg}`);
    await page.screenshot({ path: path.join(site, name), omitBackground: true });
  }

  // OG image: the real page at 1200px wide, cropped to the H1, offer bar and first row of tiles.
  await page.setViewportSize({ width: 1200, height: 900 });
  await page.goto(base, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const top = await page.evaluate(() => document.querySelector('.intro').getBoundingClientRect().top - 28);
  await page.screenshot({ path: path.join(site, 'img', 'og-image.png'), clip: { x: 0, y: top, width: 1200, height: 630 } });
  await browser.close();
  server.close();
  console.log('site assets written');
})();
