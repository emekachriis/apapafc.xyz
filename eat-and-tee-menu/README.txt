EAT AND TEE — DIGITAL MENU
==========================

WHAT'S IN THIS FOLDER
  index.html        The menu page customers see
  style.css         How the menu looks
  script.js         The menu list, cart and WhatsApp order
  logo.svg          The Eat and Tee logo
  images/           One picture per dish
  table-card.html   Makes the printable A5 table card with the QR code
  qrcode.min.js     Draws the QR code (used by table-card.html)

CHANGE A PRICE OR MARK SOMETHING SOLD OUT
  Open script.js, find the item in section 2 (THE MENU),
  change the number, or add  soldOut: true

CHANGE THE PACK FEE, DELIVERY FEE OR WHATSAPP NUMBER
  Open script.js, section 1 (SETTINGS)

PUT IT ONLINE (Netlify)
  Drag this whole folder onto your site's "Deploys" page on Netlify.
  Your link stays the same every time.

MAKE THE TABLE CARD
  1. Open  your-netlify-link/table-card.html  in Chrome
     (it fills in your link automatically)
  2. Scan the QR code with your phone to check it
  3. Click "Save as PDF": Paper A5, Margins None, Background graphics ON
  4. Print at 100% / actual size on thick card, matte laminated
