---
name: launch-storyboard
description: Storyboard a product launch video the way a web designer builds a site. Covers the brief and target customer, picking a hook (provocation, bold promise or story), a retention arc, the storyboard type (2D with no footage, or founder-led), and Map, Cut, Colorize, which includes finding and downloading the product's real UI library online and cutting it into bite-sized UI pieces. Ends with 4–6 poster-grade 1920×1080 frames and a creative direction for pacing and transitions. Use it for "storyboard", "launch video", "plan the frames", "board this", or before building any product film in HyperFrames.
---

# Launch storyboard (web designer's method)

A storyboard is 4–6 artsy 1920×1080 "website sections" that tell one short story about one product flow. Website skills transfer straight across: type, composition, contrast and colour. The skill people usually lack is timing, and micro-interaction work covers most of it.

Route afterwards: the owner's video rules still apply. Run `video-creative-draft` (house rules, lane), take motion ideas from `motion-library`, then build in `hyperframes`. This skill produces the board those steps build from.

## 1. Brief: know the product and who it's for
Don't start without these. Ask the client, or find them yourself.
- **Customer:** who the product is for, and what they're angry about or want.
- **Product:** one main flow. Get a walkthrough of that one feature and ask why it helps.
- **Goal and CTA:** what the viewer should do at the end, such as a URL, a download or a waitlist.

Write these in `BRIEF.md`. If any of them is a guess, mark it as a guess.

## 2. Hook: push one interest button
Pick one hook and write it in a single line. Weigh all three first.
1. **Provocation:** annoy everyone except the target customer, for example "every AI browser does X wrong".
   - Only use this when the product can prove the claim on screen.
   - Never aim it at an established company the brand needs to stay friendly with.
2. **Bold promise:** a measurable claim the video then proves, for example "as smart as the frontier models, 20× faster".
   - The claim must come from the brief. Never invent numbers.
3. **Story:** a cinematic, emotional arc. Hard to do; pick it only when the brand already lives there.

## 3. Retention arc
Hook → problem (what the alternatives make you suffer) → solution (the product, one flow) → payoff (the one surprising thing it does) → trust (security, privacy, free tier, whatever the customer worries about) → CTA.

Each beat is one frame or a short run of frames. Explaining the topic in detail is what keeps people watching, so show the real mechanics.

## 4. Pick the storyboard type
- **2D with no footage:** UI pieces, type, colour and motion. The default.
- **Founder-led explainer:** founder footage with UI overlays. Use it when the founder is the credibility. Needs footage from the client.

Anything with a film crew is out of scope.

## 5. Map, Cut, Colorize

### Map
Draw the one main flow as boxes: screen → action → result.

### Cut: get the real UI first
Never invent UI. Find the product's real UI library and download it.

**Step 1.** Ask the client for their UI library, design system or Figma file. With the right setup it's a goldmine.

**Step 2. Search online yourself**, in this order. Use WebSearch, and the built-in browser to download.

| Order | Where to look | What to grab |
|---|---|---|
| 1 | The product's own site: `/brand`, `/press`, `/media-kit`, `/design`, `/design-system` | logos, colours, fonts, product screenshots |
| 2 | A public design-system or Storybook site, e.g. `storybook.<domain>`, `design.<domain>`, "<product> design system" | components with their exact styling |
| 3 | GitHub: the company's org, searching for `ui`, `design-system`, `components`, `storybook` | component code and tokens, under its licence |
| 4 | npm: "@<company>/ui" and similar packages | the published component library |
| 5 | Figma Community: "<product> UI kit" (only official or clearly licensed files) | full screens and components |
| 6 | App store screenshots, the product's docs and changelog images | real screens of the flow |
| 7 | Live capture of the product: `npx hyperframes capture <url> --json`, or browser screenshots | pixel-true screens |

**Step 3. Save it to the project** under `ui/source/`, with one line per item in `ui/UI-SOURCES.md`: URL, what it is, licence or permission, date.
- If the licence is unclear, use it only as reference for rebuilding, and say so.
- Never use another company's UI as if it were the client's.
- If nothing official exists, rebuild the UI from live captures. Copy the real layout, don't invent features.

**Step 4. Cut the library into bite-sized UI pieces** in `ui/cuts/`: one card, one button state, one chart, one message, one row.
- Never put a whole dashboard on one screen.
- Pick the pieces that show the most interesting parts of the flow, and the payoff above all.

### Colorize
- Put the cuts onto poster-style layouts, with bold type, unusual compositions and colour contrast between sections.
- Add gradients, zooms, depth and transitions. Take inspiration from award-winning websites and from `motion-library`.
- Keep contrast between neighbouring frames (light/dark, wide/close, type/UI) so attention resets every beat.

## 6. The frames
Make 4–6 frames at 1920×1080, one per beat of the arc, built in HTML and snapshotted with HyperFrames or rendered with `canvas-design`.
- Use the brand's real type, colours, logo and UI cuts.
- Under each frame write one line: what moves, and how it connects to the next frame.
- Show the sheet to the owner and wait for the pick before animating.

## 7. Creative direction
For 2D product videos the brand caps the look, so the direction lives in three things.
- **Pacing:** where it's fast, where it holds, and which beats land on the music.
- **Transitions:** one family of moves repeated as the film's signature, such as colour waves, a UI piece that becomes the next scene, or match cuts.
- **Visual tropes:** one recurring object or device that ties the frames together.

Write all three as one short paragraph in `STORYBOARD.md`, along with the arc, the hook line, the frames list and the UI sources.

## Done when
`BRIEF.md`, `ui/UI-SOURCES.md`, `ui/cuts/`, the 4–6 frames and `STORYBOARD.md` exist, every UI piece traces back to a real source, and the owner has picked the board. Then hand off to `video-creative-draft` and `hyperframes`.
