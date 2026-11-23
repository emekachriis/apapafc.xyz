/* =========================================================
   EAT AND TEE — MENU AND CART
   ========================================================= */


/* ---------------------------------------------------------
   1. SETTINGS — the vendor can change these numbers
   --------------------------------------------------------- */
const PACK_FEE = 200;       // charged per meal for takeaway and delivery
const DELIVERY_FEE = 1000;  // charged once for delivery
const SHOP_NAME = "Eat and Tee";
const WHATSAPP_NUMBER = "2349043208408";  // country code + number, no "+" or leading 0


/* ---------------------------------------------------------
   2. THE MENU — edit prices, add or remove items here.

   Each item has EITHER:
     price: 1500                       (one price)
   OR:
     sizes: [ { label: "Regular", price: 1500 }, ... ]

   soldOut: true   → shows "Sold out" and hides the Add button
   pack: true      → on a category, each portion needs a takeaway pack
   --------------------------------------------------------- */
const menu = [
  {
    category: "Rice", emoji: "🍚", pack: true,
    items: [
      { id: "jollof", name: "Jollof Rice", desc: "Smoky party-style jollof.", photo: "images/jollof-rice.jpg",
        sizes: [ { label: "Regular", price: 1500 }, { label: "Large", price: 2500 } ] },
      { id: "fried-rice", name: "Fried Rice", desc: "With mixed veg and liver.", photo: "images/fried-rice.jpg",
        sizes: [ { label: "Regular", price: 1500 }, { label: "Large", price: 2500 } ] },
      { id: "white-rice", name: "White Rice & Stew", desc: "Fluffy rice, rich tomato stew.", photo: "images/white-rice-stew.jpg",
        sizes: [ { label: "Regular", price: 1300 }, { label: "Large", price: 2200 } ] },
    ],
  },
  {
    category: "Swallow", emoji: "🥣", pack: true,
    items: [
      { id: "egusi", name: "Egusi Soup with Eba", desc: "Eba is on the house 🎉 — you only pay for the soup.",
        photo: "images/eba-egusi.jpg", price: 2000 },
    ],
  },
  {
    category: "Protein", emoji: "🍗",
    items: [
      { id: "chicken", name: "Fried Chicken", desc: "One big, well-seasoned piece.", photo: "images/fried-chicken.jpg", price: 2500 },
      { id: "beef", name: "Beef", desc: "Two pieces, fried.", photo: "images/beef.jpg", price: 1000 },
      { id: "fish", name: "Fried Fish", desc: "Crispy croaker.", photo: "images/fried-fish.jpg", price: 2000 },
      { id: "asun", name: "Asun", desc: "Peppered goat meat.", photo: "images/asun.jpg", price: 3000, soldOut: true },
    ],
  },
  {
    category: "Sides", emoji: "🍌",
    items: [
      { id: "dodo", name: "Dodo", desc: "Sweet fried plantain.", photo: "images/dodo.jpg", price: 700 },
      { id: "moi-moi", name: "Moi Moi", desc: "Steamed bean pudding with egg.", photo: "images/moi-moi.jpg", price: 800 },
    ],
  },
  {
    category: "Drinks", emoji: "🥤",
    items: [
      { id: "zobo", name: "Zobo", desc: "Chilled hibiscus drink, homemade.", photo: "images/zobo.jpg",
        sizes: [ { label: "35cl", price: 500 }, { label: "50cl", price: 800 } ] },
      { id: "chapman", name: "Chapman", desc: "The classic Nigerian cocktail, no alcohol.", photo: "images/chapman.jpg", price: 1500 },
      { id: "water", name: "Bottled Water", desc: "", photo: "images/bottled-water.jpg", price: 300 },
    ],
  },
];


/* ---------------------------------------------------------
   3. THE CART — what the customer has picked so far
   --------------------------------------------------------- */
let cart = {};               // e.g. { "jollof|Large": 2, "chicken|": 1 }
let orderType = "dine-in";   // "dine-in", "takeaway" or "delivery"
const choices = {};          // details of every option, looked up by its key


/* ---------------------------------------------------------
   4. SMALL HELPERS
   --------------------------------------------------------- */

// Turns 5500 into "₦5,500"
function naira(amount) {
  return "₦" + amount.toLocaleString("en-NG");
}

// Turns "Rice" into "rice" so it can be used as an id for the #rice link
function slug(text) {
  return text.toLowerCase().replace(/[^a-z0-9]+/g, "-");
}

// The + / − buttons for one option
function stepperHTML(key) {
  const qty = cart[key] || 0;
  if (qty === 0) {
    return `<button class="add-btn" data-action="plus" data-key="${key}">+ Add</button>`;
  }
  return `
    <button class="step-btn" data-action="minus" data-key="${key}" aria-label="One less">−</button>
    <span class="qty">${qty}</span>
    <button class="step-btn" data-action="plus" data-key="${key}" aria-label="One more">+</button>`;
}


/* ---------------------------------------------------------
   5. BUILD THE PAGE FROM THE MENU LIST (runs once)
   --------------------------------------------------------- */
function drawMenu() {
  let linksHTML = "";
  let menuHTML = "";

  for (const section of menu) {
    const sectionId = slug(section.category);
    linksHTML += `<li><a href="#${sectionId}">${section.emoji} ${section.category}</a></li>`;

    menuHTML += `<section class="category" id="${sectionId}"><h2>${section.category}</h2>`;

    for (const item of section.items) {
      // Treat a single price as one option with no label, so every item works the same way
      const options = item.sizes || [ { label: "", price: item.price } ];

      let optionsHTML = "";
      for (const option of options) {
        const key = item.id + "|" + option.label;
        choices[key] = { name: item.name, label: option.label, price: option.price, pack: section.pack === true };

        optionsHTML += `
          <div class="option">
            <span class="option-label">${option.label} <strong>${naira(option.price)}</strong></span>
            <span class="stepper" data-key="${key}">${item.soldOut ? "" : stepperHTML(key)}</span>
          </div>`;
      }

      menuHTML += `
        <article class="item ${item.soldOut ? "sold-out" : ""}">
          ${item.photo ? `<img src="${item.photo}" alt="${item.name}">` : ""}
          <div class="item-text">
            <h3>${item.name} ${item.soldOut ? '<span class="badge">Sold out</span>' : ""}</h3>
            ${item.desc ? `<p class="desc">${item.desc}</p>` : ""}
            ${optionsHTML}
          </div>
        </article>`;
    }

    menuHTML += `</section>`;
  }

  document.getElementById("category-links").innerHTML = linksHTML;
  document.getElementById("menu").innerHTML = menuHTML;
  document.getElementById("notice-pack").textContent = naira(PACK_FEE);
  document.getElementById("notice-delivery").textContent = naira(DELIVERY_FEE);
}


/* ---------------------------------------------------------
   6. CHANGE A QUANTITY, THEN REFRESH EVERYTHING
   --------------------------------------------------------- */
function changeQty(key, amount) {
  cart[key] = (cart[key] || 0) + amount;
  if (cart[key] <= 0) {
    delete cart[key];
  }
  updatePage();
}

function getTotals() {
  let items = 0;
  let subtotal = 0;
  let packs = 0;

  for (const key in cart) {
    const qty = cart[key];
    const choice = choices[key];
    items += qty;
    subtotal += choice.price * qty;
    if (choice.pack) {
      packs += qty;
    }
  }

  const needsPacks = orderType === "takeaway" || orderType === "delivery";
  const packFee = needsPacks ? packs * PACK_FEE : 0;
  const deliveryFee = orderType === "delivery" ? DELIVERY_FEE : 0;

  return { items, subtotal, packs, packFee, deliveryFee, total: subtotal + packFee + deliveryFee };
}

function updatePage() {
  // 6a. Redraw every + / − button on the menu
  for (const stepper of document.querySelectorAll(".option .stepper")) {
    if (stepper.innerHTML !== "") {   // sold-out items stay empty
      stepper.innerHTML = stepperHTML(stepper.dataset.key);
    }
  }

  const t = getTotals();

  // 6b. The bar at the bottom
  document.getElementById("cart-bar").hidden = t.items === 0;
  document.getElementById("cart-count").textContent = t.items + (t.items === 1 ? " item" : " items");
  document.getElementById("cart-bar-total").textContent = naira(t.total);

  // 6c. The list inside the cart panel
  let linesHTML = "";
  for (const key in cart) {
    const choice = choices[key];
    linesHTML += `
      <li>
        <div>
          <strong>${choice.name}</strong> ${choice.label ? `<small>(${choice.label})</small>` : ""}
          <div class="line-price">${naira(choice.price * cart[key])}</div>
        </div>
        <div class="stepper">${stepperHTML(key)}</div>
      </li>`;
  }
  document.getElementById("cart-lines").innerHTML = linesHTML;

  // 6d. The sums
  document.getElementById("subtotal").textContent = naira(t.subtotal);
  document.getElementById("pack-row").hidden = t.packFee === 0;
  document.getElementById("pack-count").textContent = t.packs;
  document.getElementById("pack-fee").textContent = naira(t.packFee);
  document.getElementById("delivery-row").hidden = t.deliveryFee === 0;
  document.getElementById("delivery-fee").textContent = naira(t.deliveryFee);
  document.getElementById("grand-total").textContent = naira(t.total);

  // 6e. Show the table box for dine-in, the address box for delivery
  document.getElementById("table-field").hidden = orderType !== "dine-in";
  document.getElementById("address-field").hidden = orderType !== "delivery";

  // 6f. If the cart is now empty, close the panel
  if (t.items === 0) {
    closeCart();
  }
}


/* ---------------------------------------------------------
   7. OPEN AND CLOSE THE CART PANEL
   --------------------------------------------------------- */
function openCart() {
  document.getElementById("cart-panel").hidden = false;
  document.body.classList.add("no-scroll");
}

function closeCart() {
  document.getElementById("cart-panel").hidden = true;
  document.body.classList.remove("no-scroll");
}


/* ---------------------------------------------------------
   7b. THE WHATSAPP ORDER
   --------------------------------------------------------- */

// Reads what the customer typed (trim() removes stray spaces)
function readField(id) {
  return document.getElementById(id).value.trim();
}

// Builds the order as readable text, one line at a time
function buildMessage() {
  const t = getTotals();
  const lines = [];

  lines.push(`Hello ${SHOP_NAME}! I'd like to order:`);
  lines.push("");

  for (const key in cart) {
    const choice = choices[key];
    const size = choice.label ? ` (${choice.label})` : "";
    lines.push(`• ${cart[key]}x ${choice.name}${size} – ${naira(choice.price * cart[key])}`);
  }

  lines.push("");
  lines.push(`Food & drinks: ${naira(t.subtotal)}`);
  if (t.packFee > 0) {
    lines.push(`Packs (${t.packs}): ${naira(t.packFee)}`);
  }
  if (t.deliveryFee > 0) {
    lines.push(`Delivery: ${naira(t.deliveryFee)}`);
  }
  lines.push(`*Total: ${naira(t.total)}*`);   // *stars* make it bold in WhatsApp
  lines.push("");

  const typeNames = { "dine-in": "Dine-in", takeaway: "Takeaway", delivery: "Delivery" };
  lines.push(`Order type: ${typeNames[orderType]}`);
  lines.push(`Name: ${readField("customer-name")}`);
  if (orderType === "dine-in" && readField("table-number") !== "") {
    lines.push(`Table: ${readField("table-number")}`);
  }
  if (orderType === "delivery") {
    lines.push(`Address: ${readField("address")}`);
  }
  if (readField("note") !== "") {
    lines.push(`Note: ${readField("note")}`);
  }

  return lines.join("\n");   // glue the lines together with line breaks
}

// Checks the form, then opens WhatsApp with the message typed in
function sendOrder() {
  const error = document.getElementById("form-error");

  let problem = "";
  if (readField("customer-name") === "") {
    problem = "Please enter your name.";
  } else if (orderType === "delivery" && readField("address") === "") {
    problem = "Please enter your delivery address.";
  }

  if (problem !== "") {
    error.textContent = problem;
    error.hidden = false;
    return;   // stop here; don't open WhatsApp yet
  }
  error.hidden = true;

  const message = buildMessage();
  const url = "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(message);
  window.open(url, "_blank");
}


/* ---------------------------------------------------------
   8. EVENT LISTENERS — what happens when the customer taps
   --------------------------------------------------------- */

// Any + or − button, anywhere on the page
document.addEventListener("click", function (event) {
  const button = event.target.closest("[data-action]");
  if (!button) {
    return;
  }
  if (button.dataset.action === "plus") {
    changeQty(button.dataset.key, 1);
  } else {
    changeQty(button.dataset.key, -1);
  }
});

document.getElementById("cart-bar").addEventListener("click", openCart);
document.getElementById("close-cart").addEventListener("click", closeCart);

// Tapping the dark area outside the panel also closes it
document.getElementById("cart-panel").addEventListener("click", function (event) {
  if (event.target.id === "cart-panel") {
    closeCart();
  }
});

document.getElementById("order-btn").addEventListener("click", sendOrder);

document.getElementById("clear-cart").addEventListener("click", function () {
  cart = {};
  updatePage();
});

// Dine-in / Takeaway / Delivery
for (const radio of document.querySelectorAll('input[name="order-type"]')) {
  radio.addEventListener("change", function () {
    orderType = radio.value;
    updatePage();
  });
}


/* ---------------------------------------------------------
   9. START
   --------------------------------------------------------- */
drawMenu();
updatePage();
