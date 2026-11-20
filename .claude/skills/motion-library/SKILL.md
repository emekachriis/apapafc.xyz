---
name: motion-library
description: House motion rules and ready-made animation patterns for the Apapa Kings FC website (Jekyll, plain CSS in assets/css/main.css, vanilla JS in assets/js/main.js). Use whenever adding or changing an animation, transition, hover effect, scroll reveal, ticker, countdown or any other movement on the site.
---

# Apapa Kings FC — motion library

The site's look is a printed street-football poster: thick ink borders, hard offset
shadows, orange kit colour. Motion should feel like that poster being *pressed and
lifted*: short, snappy, flat. No bounces, no blur, no parallax, no libraries.

## Rules (non-negotiable)

1. **Plain CSS + vanilla JS only.** No GSAP, Framer Motion, AOS, jQuery, or CDN scripts.
   The site has no build step; everything ships as-is from GitHub Pages.
2. **Respect reduced motion.** Wrap anything decorative or looping in
   `@media (prefers-reduced-motion: no-preference) { … }`. A global safety net at the
   bottom of `main.css` already zeroes durations under `reduce` — don't fight it with
   `!important`.
3. **Animate only `transform` and `opacity`** (plus `box-shadow` / `background-color`
   on small elements like buttons). Never animate `width`, `height`, `top`, `left`,
   `margin`, or `filter` on large areas — phones on Lagos data matter most.
4. **Content must work without JS.** Hidden-until-revealed states are scoped under
   `.js` (the class `main.js` sets on `<html>`), so a failed script never hides content.
5. **Put new motion CSS in the `/* ---------- motion ---------- */` section** of
   `assets/css/main.css` unless it belongs to one component's block.

## Timing tokens

| Use | Duration | Easing |
| --- | --- | --- |
| Press / hover on buttons, links, cards | `.15s` | `ease` |
| Nav underline, menu bars | `.2s` | `ease` |
| Photo zoom on hover | `.35s` | `ease` |
| Scroll reveal | `.5s` | `ease` |
| Ticker loop | `32s` | `linear` |

Stick to these. If something new needs a different value, add a comment saying why.

## Patterns already in the site — reuse them

### 1. Poster press (buttons, cards)
Lift up-left on hover and grow the hard shadow; push down-right on press.
```css
.thing { box-shadow: 4px 4px 0 var(--ink); transition: transform .15s ease, box-shadow .15s ease; }
.thing:hover  { transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--ink); }
.thing:active { transform: translate(2px, 2px);  box-shadow: 1px 1px 0 var(--ink); }
```
Cards use the same idea with an orange shadow: `translate(-3px,-3px)` + `7px 7px 0 var(--orange)`.

### 2. Arrow nudge
`.icon-arrow` slides `translateX(4px)` when its `.btn` or `.more-link` is hovered.

### 3. Underline wipe (desktop nav)
`::after` bar, `transform: scaleX(0)` → `scaleX(1)`, `transform-origin: left`, `.2s`.
Also shown for `[aria-current="page"]`.

### 4. Photo zoom
`.player:hover .player__photo { transform: scale(1.04); }` inside an `overflow: hidden` frame.
Never exceed `1.06`.

### 5. Scroll reveal
CSS (already present):
```css
@media (prefers-reduced-motion: no-preference) {
  .js .reveal { opacity: 0; transform: translateY(18px); transition: opacity .5s ease, transform .5s ease; }
  .js .reveal.is-in { opacity: 1; transform: none; }
}
```
JS: `main.js` adds `.reveal` to a selector list and uses one `IntersectionObserver`
(`rootMargin: "0px 0px -8% 0px"`, unobserve after first reveal). **To reveal a new
element type, add its selector to that existing `querySelectorAll` list** — don't
create a second observer or hard-code `class="reveal"` in templates.

Optional stagger for grids (add only if asked):
```css
.js .reveal:nth-child(2) { transition-delay: .06s; }
.js .reveal:nth-child(3) { transition-delay: .12s; }
```
Cap total stagger at ~.2s.

### 6. Ticker
`.ticker__track` holds the content **twice** and animates `translateX(-50%)` in a
`32s linear infinite` loop, only under `no-preference`. When adding items, duplicate
them in both halves or the loop will jump.

## Recipes for new work

**Stamp-in** (e.g. a "FULL TIME" or "WIN" badge appearing):
```css
@media (prefers-reduced-motion: no-preference) {
  .stamp-in { animation: stamp-in .25s ease-out both; }
}
@keyframes stamp-in {
  from { opacity: 0; transform: scale(1.25) rotate(-8deg); }
  to   { opacity: 1; transform: scale(1)    rotate(-4deg); }
}
```
End on the element's resting rotation (the site uses `-4deg` for tilted labels).

**Live/attention pulse** (e.g. countdown under an hour, "LIVE" dot) — opacity only:
```css
@media (prefers-reduced-motion: no-preference) {
  .pulse { animation: pulse 1.6s ease-in-out infinite; }
}
@keyframes pulse { 50% { opacity: .45; } }
```

**Number count-up** (season record): run from JS only when the element is revealed,
skip entirely under reduced motion, and keep the final number in the HTML so
no-JS / screen readers get the real value. Use `requestAnimationFrame`, ≤ 800ms.

## Before you finish

- Check the change with reduced motion on (DevTools → Rendering → emulate
  `prefers-reduced-motion: reduce`): nothing should move, nothing should be hidden.
- Check with JS disabled: all content visible.
- Check at 360px width: no horizontal scroll caused by transforms (add
  `overflow: hidden` to the parent if a lift or zoom pokes out).
