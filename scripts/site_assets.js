// Builds site images from the workbook exports. Run from the repo root:
//   node scripts/site_assets.js
// Needs: Playwright (Chromium) and ImageMagick `convert`.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const site = path.join(root, 'site');
const exp = path.join(root, 'workbook', 'exports');

(async () => {
  // 1. Screenshots resized to 1400px wide for the page, sample PDF copied.
  for (const n of ['shot-summary.png', 'shot-ledger.png', 'shot-tieout.png']) {
    execFileSync('convert', [path.join(exp, n), '-resize', '1400x', '-strip', '+dither', '-colors', '48',
      'PNG8:' + path.join(site, 'img', n)]);  // ~70 KB each, text stays crisp
  }
  fs.copyFileSync(path.join(exp, 'sample-summary-schedule-e.pdf'), path.join(site, 'sample-rental-books-2026.pdf'));

  const browser = await chromium.launch();
  const page = await browser.newPage();
  const svg = fs.readFileSync(path.join(site, 'favicon.svg'), 'utf8');

  // 2. Favicon PNGs from the SVG.
  for (const [size, name] of [[32, 'favicon-32.png'], [180, 'apple-touch-icon.png']]) {
    await page.setViewportSize({ width: size, height: size });
    await page.setContent(`<style>html,body{margin:0}svg{width:${size}px;height:${size}px;display:block}</style>${svg}`);
    await page.screenshot({ path: path.join(site, name), omitBackground: true });
  }

  // 3. OG image 1200x630 from the Summary screenshot.
  const shot = fs.readFileSync(path.join(exp, 'shot-summary.png')).toString('base64');
  await page.setViewportSize({ width: 1200, height: 630 });
  await page.setContent(`<!doctype html><style>
    body{margin:0;width:1200px;height:630px;background:#fbfaf7;font-family:Georgia,serif;overflow:hidden;position:relative}
    .band{position:absolute;left:0;top:0;bottom:0;width:470px;background:#1f3a5f;color:#fff;padding:56px 44px;box-sizing:border-box}
    h1{font-weight:normal;font-size:44px;line-height:1.18;margin:0 0 22px}
    p{font:22px/1.4 Arial,sans-serif;margin:0 0 14px;color:#dbe4ee}
    .d{position:absolute;bottom:44px;left:44px;right:30px;font:16px/1.35 Arial,sans-serif;color:#b9c7d6}
    img{position:absolute;left:500px;top:60px;width:1000px;border:1px solid #d8dee6;box-shadow:0 6px 24px rgba(0,0,0,.12)}
    .tag{position:absolute;left:500px;bottom:40px;font:16px Arial,sans-serif;color:#55606e}
  </style><div class="band"><h1>A year of PM statements, reconciled for your CPA</h1>
  <p>One per-property workbook from your property manager statements and bank export.</p>
  <div class="d">Bookkeeping prepared for your CPA. Not tax advice, tax preparation or tax filing.</div></div>
  <img src="data:image/png;base64,${shot}"><div class="tag">Sample Summary sheet. Fictional data.</div>`);
  await page.screenshot({ path: path.join(site, 'img', 'og-image.png') });
  await browser.close();
  console.log('site assets written');
})();
