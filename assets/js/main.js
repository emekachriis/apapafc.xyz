/* Apapa Kings FC — small enhancements. The site works without this file. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  /* ---------- mobile menu ---------- */
  var toggle = document.querySelector("[data-menu-toggle]");
  var menu = document.querySelector("[data-menu]");
  if (toggle && menu) {
    var setOpen = function (open) {
      toggle.setAttribute("aria-expanded", String(open));
      menu.hidden = !open;
      document.body.classList.toggle("menu-open", open);
      toggle.querySelector(".menu-toggle__label").textContent = open ? "Close" : "Menu";
      if (open) { var first = menu.querySelector("a"); if (first) first.focus(); }
    };
    toggle.addEventListener("click", function () { setOpen(menu.hidden); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !menu.hidden) { setOpen(false); toggle.focus(); }
    });
    menu.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
    window.matchMedia("(min-width: 960px)").addEventListener("change", function (mq) { if (mq.matches) setOpen(false); });
  }

  /* ---------- next match countdown ---------- */
  document.querySelectorAll("[data-next-match]").forEach(function (box) {
    var start = new Date(box.getAttribute("data-start")).getTime();
    var cd = box.querySelector("[data-countdown]");
    var done = box.querySelector("[data-match-done]");
    if (!cd || isNaN(start)) return;
    var out = {};
    cd.querySelectorAll("[data-cd]").forEach(function (el) { out[el.getAttribute("data-cd")] = el; });
    var pad = function (n) { return n < 10 ? "0" + n : String(n); };
    var timer;
    var tick = function () {
      var diff = start - Date.now();
      if (diff <= 0) {
        clearInterval(timer);
        cd.hidden = true;
        // match is on or finished: two hours after kick-off, say the result is coming
        if (done && Date.now() - start > 2 * 3600 * 1000) done.hidden = false;
        return;
      }
      out.d.textContent = pad(Math.floor(diff / 864e5));
      out.h.textContent = pad(Math.floor(diff % 864e5 / 36e5));
      out.m.textContent = pad(Math.floor(diff % 36e5 / 6e4));
      out.s.textContent = pad(Math.floor(diff % 6e4 / 1e3));
    };
    tick();
    timer = setInterval(tick, 1000);
  });

  /* ---------- news filter ---------- */
  var filter = document.querySelector("[data-filter]");
  var list = document.querySelector("[data-filter-list]");
  if (filter && list) {
    filter.addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-kind]");
      if (!btn) return;
      var kind = btn.getAttribute("data-kind");
      filter.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      list.querySelectorAll("[data-kind]").forEach(function (card) {
        card.hidden = kind !== "all" && card.getAttribute("data-kind") !== kind;
      });
    });
  }

  /* ---------- forms that open WhatsApp with a ready message ---------- */
  var waNumber = (document.querySelector('a[href^="https://wa.me/"]') || {}).href;
  waNumber = waNumber ? waNumber.replace(/^https:\/\/wa\.me\/(\d+).*$/, "$1") : "";
  document.querySelectorAll("[data-wa-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var lines = [form.getAttribute("data-intro"), ""];
      new FormData(form).forEach(function (value, key) {
        value = String(value).trim();
        if (value) lines.push(key + ": " + value);
      });
      window.location.href = "https://wa.me/" + waNumber + "?text=" + encodeURIComponent(lines.join("\n"));
    });
  });

  /* ---------- copy link ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var label = btn.querySelector("span");
      var url = btn.getAttribute("data-copy");
      var ok = function () { label.textContent = "Copied!"; setTimeout(function () { label.textContent = "Copy link"; }, 2000); };
      if (navigator.clipboard) navigator.clipboard.writeText(url).then(ok, function () { window.prompt("Copy this link:", url); });
      else window.prompt("Copy this link:", url);
    });
  });

  /* ---------- reveal on scroll ---------- */
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll(".news-card, .player-grid .player, .result, .values li, .join-card").forEach(function (el) {
      el.classList.add("reveal"); io.observe(el);
    });
  }
})();
