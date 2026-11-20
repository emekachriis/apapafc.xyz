# Technique families

These 45 families were grouped from 82 big-brand motion breakdowns, plus an earlier catalog. Counts are how many of those 82 had at least one technique in the family. The goal is to invent with these, not to remake the references.

How to use a family: name the beat's use (hook, feature, explainer, social proof, end card), pick one or two families, read why they work, then run the invention prompts and the remix operators in `principles.md` until the move is original. Recipes below cover After Effects, Blender and code.

## Use: hook

Hooks in this set work by a question (anticipation), a contrast, or an unexpected actor in the first 1–3 s.

<a id="one-word"></a>
### One word (or phrase) per beat

- **Seen in:** 14 videos (Anthropic, Apple, Discord, Headspace, Microsoft, Mozilla Firefox, Polestar, Slack, Spotify, The Browser Company (Arc)) · uses: hook 7, feature 4, end card 4, explainer 2
- **Principle:** rhythm. A word per beat turns copy into rhythm; it reads on mute and locks to the music.
- **After Effects:** One text layer per word, cut on the beat (hard cuts, no fades), set big; alternate grounds or weights.
- **Blender:** Not needed.
- **Code:** One scene or text layer per word. Cut times come from a beat grid (at 120 BPM and 30 fps, that is 15 frames per beat).
- **References:**
  - [Anthropic — Highlight-and-swap one word in the tagline](https://x.com/claudeai/status/2120206365759094857) @ 48–52.9s
  - [Microsoft — Big section word on a colour field](https://www.youtube.com/watch?v=Uh9643c2P6k&t=125s) @ 125–143s
  - [Polestar — Tiny question placed in negative space, one per shot](https://www.youtube.com/watch?v=hJDnGlUOTeQ&t=10s) @ 10–52.5s
- **Invention prompts:**
  - Change the ground colour, not just the word, on each beat.
  - Let each word be performed by a different agent/character.
  - Drop one beat (silence + empty frame) before the last word.
  - Combine with **One UI element isolated as the hero** (also strong for hook): what happens if both land on the same beat?

<a id="dark-light"></a>
### Dark → light release (glow, light-only reveal, silhouette)

- **Seen in:** 8 videos (Apple, Duolingo, GitHub, Google, Nothing, OpenAI, Polestar) · uses: hook 5, feature 2, explainer 1, end card 1
- **Principle:** contrast. A long dark hold makes the light (or the white end card) feel like a release.
- **After Effects:** Hold near-black for 1–3 s, then a glow (Deep Glow/Glow) or cut to white; use exposure keyframes not opacity.
- **Blender:** Emission-only product (lights on, body black) then key world strength up; rim light from behind for silhouettes.
- **Code:** Drive the release with exposure or a blend to white, not opacity alone. A blurred, bright copy added on top makes a glow.
- **References:**
  - [Google — Glow burst after a long dark hold](https://www.youtube.com/watch?v=OMVpP-Zam1A&t=18s) @ 18–22s
  - [Duolingo — Delayed character reveal (silhouette → feet → face)](https://www.youtube.com/watch?v=o3ftECYtkf0&t=7s) @ 7–23.5s
  - [Apple — Silhouette on white](https://www.youtube.com/watch?v=EMmKs8vMKhU&t=2s) @ 2s, 6s, 32s
- **Invention prompts:**
  - The character "switches on" the frame (eyes light first, then the world).
  - Silhouette the product, then let its UI light it from inside.
  - Go light → dark for an "after hours, the character keeps working" beat.
  - Combine with **One word (or phrase) per beat** (also strong for hook): what happens if both land on the same beat?

<a id="character-acting"></a>
### Character acting (eyes, takes, delayed reveal)

- **Seen in:** 8 videos (Coca-Cola, Duolingo, GitHub, Headspace, Spotify) · uses: hook 5, feature 2, social proof 1, explainer 1
- **Principle:** character. Faces get attention; small eye acting sells emotion more than body moves.
- **After Effects:** Rig with Duik/Joysticks; key blinks every 0.6–0.8 s, brow and pupil offsets; 2–3 fr anticipation before a take.
- **Blender:** Shape keys for eyelids/brows; drivers from a control bone; Grease Pencil for 2D faces.
- **Code:** Give the face expression specs (eyes, blinks, brows). Support yaw and roll so the head can take and spin. Blink about every 0.6–0.8 s.
- **References:**
  - [Headspace — Simple round characters with dot eyes](https://www.youtube.com/watch?v=wyj8l9miy4w) @ whole
  - [Duolingo — Plush 3D mascot with eye acting](https://www.youtube.com/watch?v=IEHiY8scAKI) @ whole
  - [Coca-Cola — Witness reaction shots (characters watch the hero)](https://www.youtube.com/watch?v=Yy6fByUmPuE&t=12s) @ 12.5–50s
- **Invention prompts:**
  - A head spin as the hero move, then reuse the spin as a dial or selector.
  - The mascot reacts to the product's result (a take when the email sends).
  - Eyes become UI (caret, loading ring).
  - Combine with **One word (or phrase) per beat** (also strong for hook): what happens if both land on the same beat?

<a id="pullback"></a>
### Pull back to reveal the frame (world → screen, macro → device)

- **Seen in:** 10 videos (Coca-Cola, Duolingo, Figma, Framer, Google, Microsoft, Raycast, Shopify) · uses: hook 4, end card 3, feature 3
- **Principle:** anticipation → payoff. The viewer reads the content first and the context second, so the reveal reframes what they just saw.
- **After Effects:** Precompose the "inside" content at full resolution; in the main composition, scale it down into a device screen corner-pinned (or CC Power Pin) while a 3D camera dollies out; 1–1.5 s, ease out strongly.
- **Blender:** Put the content on an emissive screen plane; the camera starts touching the screen and dollies back on a log-scale distance curve.
- **Code:** Composite UI into a screen quad on a device, then animate camera Z with a strong ease-out over 1–1.5 s. For a real device, render RGBA 3D frames and composite them.
- **References:**
  - [Framer — Pull back to reveal the tool around the result](https://www.youtube.com/watch?v=6xJWQRVl9nw&t=10s) @ 10.8s
  - [Google — Pull-back reveal: the screen was the frame](https://www.youtube.com/watch?v=OMVpP-Zam1A&t=17s) @ 17.5–20s
  - [Microsoft — Pull back: an epic world turns out to be on the screen](https://www.youtube.com/watch?v=fm6VQgCkj20&t=0s) @ 0–6.8s
- **Invention prompts:**
  - Pull back through more than one layer (a chat → a laptop → a desk → the character sitting at the desk).
  - Reverse the joke: what looks like a tiny UI chip is actually a building-sized object.
  - Pull back on a beat drop, not on a cut, so sound tells you the world got bigger.
  - Combine with **One word (or phrase) per beat** (also strong for hook): what happens if both land on the same beat?

<a id="typed"></a>
### Typed text (prompt, title or caption types itself)

- **Seen in:** 9 videos (Adobe, Framer, Google, Microsoft, Notion, OpenAI, Vercel) · uses: hook 4, feature 3, explainer 2, end card 1
- **Principle:** anticipation. You read along at reading speed; the cursor promises something is coming.
- **After Effects:** Text animator: Range Selector by character with Opacity 0 and Smoothness 0, keyed over N frames (2–3 fr/char), plus a blinking cursor layer parented to the last character via sourceRectAtTime.
- **Blender:** Usually 2D; for 3D type use a Text object with Build modifier or drive the body string with a driver on frame.
- **Code:** A type-on function that adds letters or words on a step interval, plus a blinking caret.
- **References:**
  - [Framer — Button label types itself](https://www.youtube.com/watch?v=6xJWQRVl9nw&t=0s) @ 0s
  - [Google — Type-on prompt as the whole story](https://www.youtube.com/watch?v=OMVpP-Zam1A&t=2s) @ 2.5–17.5s
  - [Microsoft — Monospace caption decodes letter by letter with a block cursor](https://www.youtube.com/watch?v=fm6VQgCkj20&t=0s) @ 0–58s
- **Invention prompts:**
  - Type something funny that is also the pitch (Pixel 9 Pro Fold's breakup letter).
  - Let the mascot's eyes become the caret.
  - Type in the wrong thing and correct it: the correction is the feature.
  - Combine with **One word (or phrase) per beat** (also strong for hook): what happens if both land on the same beat?

<a id="texture"></a>
### Living background texture (grid, halftone, particles, shader)

- **Seen in:** 11 videos (Anthropic, Figma, Framer, GitHub, Google, LottieFiles, Nothing, OpenAI, Perplexity, Vercel) · uses: hook 4, explainer 4, feature 3, social proof 1
- **Principle:** restraint. A slow-moving ground keeps a still frame alive without competing with the content.
- **After Effects:** Fractal Noise/Cell Pattern at low contrast, evolution keyed slowly; or a dot grid with a lit area following the action.
- **Blender:** Procedural noise shader on a background plane; slow W animation.
- **Code:** A shader, particle system, or tiled pattern on a full-frame layer, with slow drift or a seed that changes per beat.
- **References:**
  - [Anthropic — Faint dot grid on warm paper](https://x.com/claudeai/status/2120206365759094857) @ whole
  - [Framer — Proof wall grid of real outputs](https://www.youtube.com/watch?v=6xJWQRVl9nw&t=15s) @ 15s
  - [OpenAI — Dashes as abstract lines of text](https://www.youtube.com/watch?v=--khbXchTeE&t=0s) @ 0s, 56s
- **Invention prompts:**
  - The texture reacts to the character (dots light where the character walks).
  - The background grid becomes the calendar.
  - Texture made of the product's own content (tiny email lines).
  - Combine with **One word (or phrase) per beat** (also strong for hook): what happens if both land on the same beat?

<a id="macro"></a>
### Macro / impossible close-up of the object

- **Seen in:** 7 videos (Apple, Figma, Google, Microsoft, Samsung) · uses: hook 3, feature 3, explainer 1
- **Principle:** contrast (scale). Too close to recognise makes you lean in; the object becomes a landscape before it becomes a product.
- **After Effects:** 3D layer of a hi-res render or UI scaled 800–1500%, 3D camera with shallow depth of field, slow track (2–4 px/frame).
- **Blender:** Camera focal length 100mm+, f/1.4 DOF on a very small focus distance; skim along the edge with a Follow Path constraint; bevel the model so speculars catch.
- **Code:** Render or crop in at a very close focal length and add shallow depth of field. A slight dolly or rack focus sells the scale.
- **References:**
  - [Samsung — Impossible-magnification macro of tech](https://www.youtube.com/watch?v=2gYqEi8-am4&t=68s) @ 68s
  - [Microsoft — Macro CG of internals](https://www.youtube.com/watch?v=fm6VQgCkj20&t=34s) @ 34–68s
  - [Apple — Edge-on sliver reveal](https://www.youtube.com/watch?v=4Y9ITR44W5s&t=2s) @ 2.4s, 43.5s
- **Invention prompts:**
  - Macro on something the character does (a cursor caret, a stamp's rubber texture) instead of hardware.
  - Make the macro a puzzle: the viewer guesses what it is before the pull-back.
  - Use the macro texture as the background of the next scene (continuity).
  - Combine with **One word (or phrase) per beat** (also strong for hook): what happens if both land on the same beat?

<a id="word-swap"></a>
### Fixed line, one swapping word

- **Seen in:** 7 videos (Apple, Duolingo, Google, Microsoft, Perplexity, Slack) · uses: hook 3, explainer 2, social proof 1, feature 1
- **Principle:** rhythm (pattern + variation). The fixed part teaches the pattern, the swapping word is the news; the eye only reads the change.
- **After Effects:** Two text layers; the swap word in a precomp with a vertical slide mask (drum) or a highlight box that wipes then swaps; track the width with sourceRectAtTime so the line re-centres.
- **Blender:** Not needed.
- **Code:** Keep the sentence as one locked layout. Swap only the changing word (cut or morph) on the beat.
- **References:**
  - [Google — Fixed caption template with one swapping word](https://www.youtube.com/watch?v=3KtWfp0UopM&t=9s) @ 9.5–220s
  - [Slack — Pill sentence with a swapping object](https://www.youtube.com/watch?v=zYotA_PNwbw&t=18s) @ 18.7–21.2s
  - [Apple — Glyph swap (icon replaces a letter)](https://www.youtube.com/watch?v=ISYIEmQxs2M&t=0s) @ 0s
- **Invention prompts:**
  - Swap the object, not the word: the word stays, the icon beside it changes.
  - End the swap list on a word that breaks the pattern (the joke or the brand).
  - Let the swapping happen on the character's screen as it works.
  - Combine with **One word (or phrase) per beat** (also strong for hook): what happens if both land on the same beat?

<a id="zero-cut"></a>
### Zero-cut single take

- **Seen in:** 5 videos (Google, Microsoft, Monzo, Netflix, Pitch) · uses: hook 3, explainer 2
- **Principle:** restraint + continuity. One take feels honest and calm; it forces every change to be a move, not an edit.
- **After Effects:** Build the whole film as one comp with a single camera; change content by moves, masks and morphs.
- **Blender:** One camera, one long shot; scenes are areas of one world.
- **Code:** One continuous camera path, no hard cuts. Animate the camera and objects; do scene changes with moves and morphs.
- **References:**
  - [Google — Zero-cut single take](https://www.youtube.com/watch?v=OMVpP-Zam1A) @ whole
  - [Netflix — One continuous shot for a teaser](https://x.com/netflix/status/2121318431139967161) @ whole
  - [Microsoft — Single continuous ground, zero cuts](https://www.youtube.com/watch?v=NbpVLqtML2M) @ whole
- **Invention prompts:**
  - Make the whole spot one desktop the camera never leaves.
  - Single take where the mascot carries each piece to the next app.
  - Use cuts only for the end card; everything before is one move.
  - Combine with **One word (or phrase) per beat** (also strong for hook): what happens if both land on the same beat?

<a id="sentence-split"></a>
### Progressive reveal (sentence completes, list unblurs)

- **Seen in:** 5 videos (GitHub, LottieFiles, Microsoft, Monzo) · uses: hook 2, end card 2, explainer 1
- **Principle:** anticipation → payoff. Half a sentence is a question; the second half is the answer.
- **After Effects:** Line 1 holds, cut or slide to the second shot, line 2 lands on a beat; keep baseline and size identical across shots.
- **Blender:** Not needed.
- **Code:** Hold the unfinished line, then complete it (or unblur the next item) on the payoff frame.
- **References:**
  - [Microsoft — Sentence split across shots](https://www.youtube.com/watch?v=hsles7xMMFA&t=17s) @ 17.5–19.8s
  - [LottieFiles — Sentence completed across two shots](https://www.youtube.com/watch?v=jUEUaCFINro&t=9s) @ 9.2–12.3s
  - [GitHub — Blurred agenda list that unblurs item by item](https://x.com/github/status/2121689749043785812) @ 4–31s
- **Invention prompts:**
  - Complete the sentence with an object instead of a word.
  - Let the second half be spoken by sound (a stamp hit) instead of text.
  - Split across three shots with growing scale.
  - Combine with **One word (or phrase) per beat** (also strong for hook): what happens if both land on the same beat?

<a id="framing"></a>
### Framing devices (grids, splits, symmetry, borders, masks)

- **Seen in:** 6 videos (Duolingo, Figma, Google, LottieFiles) · uses: hook 2, explainer 2, feature 2, end card 1, social proof 1
- **Principle:** clarity. A strong frame structure organises many items at once.
- **After Effects:** Guides + shape-layer masks; split screens via track mattes; symmetrical rows by duplicating with offsets.
- **Blender:** Multiple cameras composited, or a grid of planes.
- **Code:** Masks, grids, splits or borders as a reusable frame. Animate the mask path rather than cutting.
- **References:**
  - [Duolingo — Symmetrical rows](https://www.youtube.com/watch?v=o3ftECYtkf0&t=0s) @ 0–6s
  - [Figma — Translucent mask fill, then erase](https://x.com/figma/status/2118751599312937096) @ 9–14s
  - [LottieFiles — Gallery of real app screens using it](https://www.youtube.com/watch?v=A_sjNPSA4kg&t=85s) @ 85–90s
- **Invention prompts:**
  - Split screen of user vs bot doing the same task.
  - Grid of all the apps that collapses to the one in use.
  - A frame-within-frame that the mascot climbs out of.
  - Combine with **One word (or phrase) per beat** (also strong for hook): what happens if both land on the same beat?

**Also used for hook:** [One UI element isolated as the hero](#ui-hero) (6) · [Logo built from a motif (dot, ribbon, shapes, lines)](#logo-build) (5) · [Expressive type motion (tilt, scale jump, slice, ribbon, burst)](#expressive-type) (5) · [Transition made from a scene element (shape, wave, tiles, dots)](#element-wipe) (4) · [Concrete metaphor (abstract idea as a physical thing)](#metaphor) (4) · [Match cut / one object carried through contexts](#match-relay) (3) · [Assembly / exploded view (parts fly in and lock)](#assembly) (3) · [Type physically on or through the object](#type-object) (2) · [One accent colour on one element](#accent-one) (2) · [Bookend / callback / seamless loop](#bookend) (2) · [Mascot / product as a character that does things](#mascot-cameo) (2) · [Confirmation pop (toast, badge, check, shimmer, ring)](#confirm) (2) · [Continuous camera flight / glide over a world or UI](#flight) (1) · [Fast montage / sizzle (8–15 cuts per 10s)](#fast-montage) (1) · [Sound shaped to picture (cut on onset, quiet mix, SFX on actions)](#sound) (1) · [Objects orbit or float around a hero](#orbit) (1) · [UI on tilted planes / over footage or soft backgrounds](#ui-planes) (1) · [Visual gag / pun as payoff](#gag) (1) · [Small type in negative space (captions, lower thirds, quotes)](#small-type) (1)

## Use: feature

Feature callouts isolate one control or one result and give it a reward (pop, badge, glow).

<a id="expressive-type"></a>
### Expressive type motion (tilt, scale jump, slice, ribbon, burst)

- **Seen in:** 14 videos (Anthropic, Figma, Google, Headspace, McDonald's, Microsoft, Netflix, Slack, Spotify, The Browser Company (Arc), Vercel) · uses: feature 9, hook 5, end card 3, explainer 1
- **Principle:** character (type with a voice). The type performs the meaning (stretches, tilts, bursts), so tone comes through on mute.
- **After Effects:** Per-character text animators (position, rotation, scale) with a Wiggly or Expression Selector; 3D per-character for ribbons; offset by 1–2 fr.
- **Blender:** Text to mesh, Geometry Nodes per-glyph instances; curve-deform for ribbons.
- **Code:** Animate type with scale pops, tilt, slices or a ribbon path. Overshoot the scale and settle. Keep to one motion idea per word.
- **References:**
  - [Anthropic — Tilted words drift in and settle level](https://x.com/claudeai/status/2120206365759094857) @ 4.8–7.2s
  - [Netflix — Title forms from embers/light streaks](https://x.com/netflix/status/2121318431139967161) @ 13.8–14.7s
  - [Slack — Magnifier over a word](https://www.youtube.com/watch?v=zYotA_PNwbw&t=16s) @ 16s
- **Invention prompts:**
  - Make the verb do the verb (SENT slams, WAIT stretches).
  - Use the mascot's eye shapes as the letterforms' accents.
  - Words tilt in and settle on the beat — combine with a stamp hit.
  - Combine with **Product lineup and spec-as-hero** (also strong for feature): what happens if both land on the same beat?

<a id="lineup-spec"></a>
### Product lineup and spec-as-hero

- **Seen in:** 9 videos (Apple, Google, Notion, Samsung) · uses: feature 8, explainer 1
- **Principle:** clarity. A clean row or one spec at hero size reads instantly.
- **After Effects:** Render variants and slide them into a row with 2-fr stagger; spec number in big type next to the product.
- **Blender:** Duplicate collection with material variants; orthographic-ish long lens for the row.
- **Code:** Lay out products or specs on a grid or path; isolate one as the hero with scale, light or a callout.
- **References:**
  - [Apple — Lineup row of variants](https://www.youtube.com/watch?v=EMmKs8vMKhU&t=20s) @ 20s
  - [Google — Lineup row of variants](https://www.youtube.com/watch?v=otomCbnwsv0&t=67s) @ 67s
  - [Notion — Device lineup](https://x.com/NotionHQ/status/2118407963723567512) @ 10–12s
- **Invention prompts:**
  - Lineup of agents instead of devices.
  - Spec as a character line ("handles 200 emails before 9am").
  - Lineup that the mascot walks along.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="ui-hero"></a>
### One UI element isolated as the hero

- **Seen in:** 14 videos (Anthropic, Figma, Google, Linear, LottieFiles, Notion, Raycast, The Browser Company (Arc)) · uses: feature 8, hook 6, explainer 1, end card 1
- **Principle:** clarity + restraint. Strip the app away and one control becomes the story.
- **After Effects:** Rebuild the element as shape layers at 300–600%; soft shadow; empty or blurred ground.
- **Blender:** Extrude the UI element slightly, glossy material, soft area light.
- **Code:** Draw one control alone on a quiet ground, large in the frame. Other chrome stays off or heavily faded.
- **References:**
  - [Google — Iconic UI element clicked as the opening](https://www.youtube.com/watch?v=3KtWfp0UopM&t=0s) @ 0s
  - [Anthropic — UI drawn as a simple pill in the illustration style](https://www.youtube.com/watch?v=VHsp6Hp7Stw&t=25s) @ 25s, 50s
  - [Notion — App icon tap as the opening](https://x.com/NotionHQ/status/2118407963723567512) @ 0–1.3s
- **Invention prompts:**
  - The isolated element gets a personality (a toggle that hesitates).
  - Grow one chip into the whole context (Notion Calendar).
  - Isolate the result, not the control (the sent email).
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="orbit"></a>
### Objects orbit or float around a hero

- **Seen in:** 12 videos (Anthropic, Discord, Duolingo, Figma, Loom, Microsoft, Notion, Runway, Shopify, Spotify, Stripe) · uses: feature 7, social proof 3, hook 1, explainer 1
- **Principle:** hierarchy. Satellites make the hero bigger and show breadth (integrations, features) without a list.
- **After Effects:** Parent items to a rotating null; 3D layers so they pass in front/behind; vary speed per ring.
- **Blender:** Empty with rotation, children at offsets; or particle instancing on a circle.
- **Code:** Place objects on a circular path around a still hero; ease the angular velocity. A slow 3D turntable also works.
- **References:**
  - [Anthropic — Partner icons scatter outward](https://x.com/claudeai/status/2120206365759094857) @ 45.8s
  - [Duolingo — Icons/flags pop in around the character](https://www.youtube.com/watch?v=P3ZTxke4AOU&t=2s) @ 2.5–6.3s
  - [Figma — Cards fan into a 3D carousel](https://x.com/figma/status/2120926665790681354) @ 5.8s
- **Invention prompts:**
  - The orbit itself is the selector, and it lands on a choice on the downbeat.
  - Satellites are fuel the hero eats.
  - Orbit collapses into the logo for the end card.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="confirm"></a>
### Confirmation pop (toast, badge, check, shimmer, ring)

- **Seen in:** 10 videos (Airbnb, Duolingo, Figma, GitHub, Linear, Shopify, Slack, The Browser Company (Arc)) · uses: feature 7, hook 2, social proof 1
- **Principle:** payoff. A small reward on completion closes the loop.
- **After Effects:** Scale 0→108→100% over 4–5 fr (back-out), plus a ring or shimmer sweep (gradient matte moving across).
- **Blender:** Not needed.
- **Code:** A short pop (scale 0→1.1→1) of a toast, badge or ring on the downbeat, with a matching sound.
- **References:**
  - [Duolingo — Incoming-call ring pulse](https://www.youtube.com/watch?v=vBjfn2Pb6DI&t=2s) @ 2.8s
  - [Shopify — Success badge pop as the payoff](https://x.com/Shopify/status/2120220849789882374) @ 12.5–14s
  - [GitHub — Checklist fills itself (agent plan)](https://www.youtube.com/watch?v=EPyyyB23NUU&t=29s) @ 29–31s
- **Invention prompts:**
  - Replace the checkmark with a character action (a stamp or a physical mark). Show the user's approval tap first.
  - Shimmer as a call to act on the CTA.
  - Ring pulse that becomes the next scene's circle.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="push-in"></a>
### Push in / dive into one item until it fills the frame

- **Seen in:** 5 videos (Figma, LottieFiles, Notion, Raycast) · uses: feature 5
- **Principle:** clarity. The camera chooses for you: one item grows until it is the only thing to look at.
- **After Effects:** Scale/position the precomp on a null with an expo ease, 0.6–1 s; motion blur on; fade surrounding items as it passes 150%.
- **Blender:** Camera dolly with an F-curve on distance (log scale); for "dive into the logo" put the camera through a gap in the mesh.
- **Code:** Scale or dolly the composited layer until one item fills the frame. A scene-changing push should run at least 20 frames with a gentle ease-in.
- **References:**
  - [Notion — Slow push-in on the input as each task starts](https://www.youtube.com/watch?v=FElBbgnNtVA&t=7s) @ 7–14s, 57–67s
  - [Figma — Push in on the result](https://x.com/figma/status/2118751599312937096) @ 20–23s
  - [Raycast — Grid zooms to one item with a focus ring](https://www.youtube.com/watch?v=Mi173xGb0ZA&t=11s) @ 11–14.5s
- **Invention prompts:**
  - Push in on the exact pixel that changes next (the unread badge) so the move is also a pointer.
  - Push into a word of the headline and come out inside the product.
  - Slow it down: a push that changes scenes should run at least 20 frames.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="type-object"></a>
### Type physically on or through the object

- **Seen in:** 9 videos (Adobe, Apple, Google, McDonald's, Microsoft, Monzo, Runway, Samsung, Spotify) · uses: feature 5, end card 2, hook 2, explainer 1
- **Principle:** integration. When type lives in the scene (printed, engraved, behind) it feels made, not added.
- **After Effects:** Track or 3D-place the text layer on the surface (Camera Tracker or 3D layers matched to the render); use the object as a track matte to put type behind it.
- **Blender:** Text object boolean/displace into the surface for engraving; or render a separate object-ID mask to composite type behind.
- **Code:** Composite order: background, then type, then the object (or the reverse if type sits on the object). For printed type, scroll a sprite out of a masked slot.
- **References:**
  - [Samsung — Word engraved along the product edge](https://www.youtube.com/watch?v=2gYqEi8-am4&t=18s) @ 18.7s
  - [Apple — Word passes through the object (input → output)](https://www.youtube.com/watch?v=EMmKs8vMKhU&t=28s) @ 28–30s
  - [Microsoft — Word framed by a real object in the shot](https://www.youtube.com/watch?v=l4B1UflAty8&t=15s) @ 15s
- **Invention prompts:**
  - Let a prop deliver the message (McDonald's receipt printer → an email that prints itself).
  - Type that the mascot hides behind or leans on.
  - Engrave the claim into the product's screen bezel.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="match-relay"></a>
### Match cut / one object carried through contexts

- **Seen in:** 12 videos (Adobe, Apple, Coca-Cola, Duolingo, Google, Headspace, LottieFiles, Microsoft, Runway, The Browser Company (Arc)) · uses: feature 5, explainer 5, hook 3, end card 1
- **Principle:** continuity. One thing stays constant while everything else changes, so the change is what you notice.
- **After Effects:** Align the object's position/scale across cuts (guide layers), cut on motion; or keep the object layer above two backgrounds.
- **Blender:** Same object and camera framing across scenes; swap materials/environment by collection visibility keyed on the cut frame.
- **Code:** Keep one object's identity (shape, colour or image) constant while the world around it changes at each cut or morph.
- **References:**
  - [Coca-Cola — Object handed across art styles (style-switch relay)](https://www.youtube.com/watch?v=VGa1imApfdg&t=14s) @ 14–93s
  - [Duolingo — Full-frame world ↔ the same world inside the device](https://www.youtube.com/watch?v=Ew4kM1FmM8o&t=1s) @ 1.4–21.9s
  - [Apple — Same line, changing container](https://www.youtube.com/watch?v=ISYIEmQxs2M&t=11s) @ 11.7–14.6s
- **Invention prompts:**
  - The mascot is the constant; the apps around it swap each beat.
  - Hand one email across five apps like a relay baton.
  - Match the logo shape to a real-world object (a clock face → the week flip).
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="ui-planes"></a>
### UI on tilted planes / over footage or soft backgrounds

- **Seen in:** 7 videos (Apple, Cursor, Duolingo, Google, Microsoft, Monzo, Raycast) · uses: feature 5, explainer 1, hook 1
- **Principle:** depth. Tilting or floating UI over a soft ground adds depth without needing full 3D.
- **After Effects:** 3D layer with Y rotation 15–30°, camera DOF on the background; CC Glass/blur behind for frosted panels.
- **Blender:** UI texture on planes, tilt 20°, DOF background plate.
- **Code:** Place UI on a 3D plane with a slight tilt; the background can be footage or a soft gradient. Keep type readable (limit the tilt).
- **References:**
  - [Cursor — UI over a soft painted landscape wallpaper](https://www.youtube.com/watch?v=An8IM-kPyms&t=34s) @ 34.7–40s
  - [Duolingo — Lesson UI overlaid on the story scene](https://www.youtube.com/watch?v=P3ZTxke4AOU&t=15s) @ 15–21s
  - [Apple — Small lower-third caption over footage](https://www.youtube.com/watch?v=oT5iDm9XRl8&t=0s) @ 0s, 14.6s, 29s
- **Invention prompts:**
  - Tilt the UI toward the mascot as if it is reading.
  - UI planes that fall into place like cards dealt.
  - Frosted prompt bar over the user's real desk.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="prompt-ui"></a>
### Prompt bar, chips and bubbles (AI UI)

- **Seen in:** 7 videos (Airtable, Anthropic, GitHub, Google, Loom, OpenAI, Perplexity) · uses: feature 5, explainer 3
- **Principle:** clarity. Prompts, chips and bubbles are the AI era's universal shorthand: viewers know what happens next.
- **After Effects:** Rounded rect + text animator; chips pop in staggered; results grid fills with 2-fr stagger.
- **Blender:** Not needed.
- **Code:** Animate a prompt bar, chips or bubbles as real objects: type-on, chip-in, bubble-spawn with easing. Don't treat them as a static screenshot.
- **References:**
  - [Anthropic — Messy items auto-sort into labelled columns](https://x.com/claudeai/status/2120973994191094179) @ 31–36s
  - [Google — Screen demo with caption chips under the window](https://www.youtube.com/watch?v=Fs0t6SdODd8&t=93s) @ 93–106s
  - [OpenAI — Prompt chip floating above the UI](https://www.youtube.com/watch?v=Ej6hnsQgV_c&t=53s) @ 53s
- **Invention prompts:**
  - The prompt chip travels into the app it controls.
  - Bubbles stack into a physical pile.
  - The loading ring is the mascot's eye.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="accent-one"></a>
### One accent colour on one element

- **Seen in:** 9 videos (Anthropic, Apple, Cursor, Google, LottieFiles, Microsoft, Netflix, Nothing, OpenAI) · uses: feature 4, explainer 2, hook 2, social proof 1
- **Principle:** contrast + restraint. If only one thing is coloured, the eye knows where to go.
- **After Effects:** Keep the comp in greys; Fill effect on the single layer in the brand accent; animate the fill on at the key beat.
- **Blender:** Neutral materials on everything; one emissive or saturated material; colour management Filmic/AgX so the accent does not clip.
- **Code:** Keep the theme in greys or neutrals. Draw only the focus element in the one accent colour.
- **References:**
  - [Cursor — Minimal bar chart with one highlighted bar](https://www.youtube.com/watch?v=An8IM-kPyms&t=5s) @ 5.3s
  - [Netflix — One warm light as the only colour in a cold frame](https://x.com/netflix/status/2121318431139967161) @ 5.2–11s
  - [OpenAI — List with one item highlighted in the accent](https://www.youtube.com/watch?v=--khbXchTeE&t=75s) @ 75s
- **Invention prompts:**
  - Let the accent travel from object to object as the story moves (cursor → card → stamp).
  - Make the accent the only warm thing in a cold frame (Planeswalker flame).
  - Remove the accent for one beat to make its return land.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="assembly"></a>
### Assembly / exploded view (parts fly in and lock)

- **Seen in:** 6 videos (Airtable, Framer, Microsoft, Samsung) · uses: feature 4, hook 3, explainer 2
- **Principle:** payoff (the build is the reveal). Watching something get built shows how it works and gives a satisfying lock.
- **After Effects:** 3D layers or Element 3D parts offset on Z, staggered 2–3 fr, ease into place with a small overshoot.
- **Blender:** Key each part from an exploded offset to 0 with staggered keyframes; or Geometry Nodes offset by index × factor.
- **Code:** Animate parts from an exploded position onto their final seats, staggered, with a lock or settle on the last piece.
- **References:**
  - [Samsung — Labelled exploded chip with % callouts](https://www.youtube.com/watch?v=2gYqEi8-am4&t=37s) @ 37.5–43.7s
  - [Framer — Layout assembles piece by piece (wireframe → content)](https://www.youtube.com/watch?v=6xJWQRVl9nw&t=1s) @ 1.5–9.2s
  - [Microsoft — Icons tumble and assemble into the new layout](https://www.youtube.com/watch?v=Uh9643c2P6k&t=18s) @ 18.7–31s
- **Invention prompts:**
  - Assemble the character's workday from app tiles.
  - Explode the UI into its layers, then snap back when the character acts.
  - Build from a single line (Samsung fold) using the caret as the line.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="inline-object"></a>
### Object sits in the line of type (inline glyph, object as a word)

- **Seen in:** 6 videos (Apple, Google, Mozilla Firefox, Slack) · uses: feature 3, end card 3
- **Principle:** clarity + surprise. Text and image read as one unit; the object is the noun.
- **After Effects:** Measure the gap with sourceRectAtTime, place the object layer in it at cap height, then scale it out of the line on the next beat.
- **Blender:** Solve the camera so the object's bounding box fits the text slot, and render with a render border.
- **Code:** Typeset the sentence and leave a gap the width of the object. Place the object baseline-aligned in that gap, then (if needed) scale it up to a three-quarter view.
- **References:**
  - [Google — Product sits between brand and product name](https://www.youtube.com/watch?v=OMVpP-Zam1A&t=23s) @ 23.8s
  - [Slack — Inline emoji/icon inside a sentence](https://www.youtube.com/watch?v=zYotA_PNwbw&t=5s) @ 5–17.5s
  - [Apple — Inline object as a word](https://www.youtube.com/watch?v=ISYIEmQxs2M&t=10s) @ 10.2s
- **Invention prompts:**
  - The inline object reacts to the words around it (waves, hides behind a letter).
  - Start inline, then grow to near full screen at an angle — keep it sharp at both sizes.
  - Replace the brand name in a sentence with the mascot's face.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="cursor"></a>
### Cursor or named agent pointer driving the UI

- **Seen in:** 4 videos (Anthropic, Figma, Linear) · uses: feature 3, social proof 1, explainer 1
- **Principle:** clarity (agency). A cursor shows who is acting; a named cursor makes the AI a collaborator.
- **After Effects:** Cursor layer on a bezier path with ease; click = 2-fr scale down; name tag parented.
- **Blender:** Not needed.
- **Code:** Animate a pointer or named agent as a real character: it moves, hovers, and clicks. The UI state change happens on the click frame.
- **References:**
  - [Anthropic — Agent's named cursor tag builds the canvas](https://x.com/claudeai/status/2120206365759094857) @ 14.4–19.3s
  - [Figma — Oversized cursor driving UI](https://www.youtube.com/watch?v=0wCIP2Ox-EQ&t=10s) @ 10–47s
  - [Linear — Big soft circle cursor](https://www.youtube.com/watch?v=jZvZfBl3VOw&t=19s) @ 19–99s
- **Invention prompts:**
  - The selector follows the character.
  - Make the cursor the mascot's hand.
  - Two cursors (user and bot) race or collaborate.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="whip"></a>
### Whip / motion-blur fly-through

- **Seen in:** 2 videos (Discord, Duolingo) · uses: feature 2
- **Principle:** energy. Speed hides the cut and adds energy at a key moment.
- **After Effects:** Fast position/scale move over 4–6 fr with CC Force Motion Blur or RSMB, cut at the blurriest frame.
- **Blender:** Fast camera move with motion blur shutter 0.5–1.0; cut mid-blur.
- **Code:** A few frames of heavy directional motion blur, then a sharp landing. Keep the whip short (4–8 frames) and cut or ease out hard.
- **References:**
  - [Duolingo — Motion-blur whip through a tunnel](https://www.youtube.com/watch?v=IEHiY8scAKI&t=56s) @ 56–63s
  - [Discord — Headline flies through the lens (motion blur)](https://www.youtube.com/watch?v=1ubOtOeM6ok&t=18s) @ 18s
- **Invention prompts:**
  - Whip along the path a message travels (sender → recipient).
  - Use one whip per film only, at the energy peak.
  - Whip into a hard stop with a squash on the landing.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="rings"></a>
### Pulse rings / radar rings as a motif

- **Seen in:** 3 videos (Apple, Google, LottieFiles) · uses: feature 2, end card 1
- **Principle:** rhythm. Expanding rings mark a beat and a centre at once; they can become the logo or the next shape.
- **After Effects:** Ellipse shape layers with Scale 0→300% and Opacity 100→0, staggered by 4–6 fr; Repeater for many.
- **Blender:** Torus or circle curves with keyed scale and an emission material fading out.
- **Code:** Emit circular pulse rings from a point (product, logo, cursor). Stagger two or three rings; they fade as they grow.
- **References:**
  - [Apple — Concentric pulse rings as a feature motif](https://www.youtube.com/watch?v=EMmKs8vMKhU&t=2s) @ 2–12s, 22s
  - [Google — Radar rings around a pin](https://www.youtube.com/watch?v=1ndT_uyeK64&t=34s) @ 34s
  - [LottieFiles — Concentric rings expand](https://www.youtube.com/watch?v=A_sjNPSA4kg&t=95s) @ 95s
- **Invention prompts:**
  - Rings come from where the character "listens" (its ear or eye).
  - Each ring carries one integration logo outward.
  - Rings that freeze into the calendar grid.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="colour-system"></a>
### One colour system across the whole film

- **Seen in:** 4 videos (Headspace, Microsoft, Stripe) · uses: feature 2, explainer 1, social proof 1
- **Principle:** continuity. One palette or grade across very different shots makes a film feel like one brand.
- **After Effects:** Adjustment layer with Lumetri/curves over everything; limit to 3–4 swatches in the comp.
- **Blender:** AgX look + one LUT on the compositor output.
- **Code:** One palette for the whole film, applied through a theme or a colour grade. Change value and layout, not the palette.
- **References:**
  - [Headspace — Muted 3–4 colour palette on cream](https://www.youtube.com/watch?v=wyj8l9miy4w) @ whole
  - [Microsoft — One sculpted hero wallpaper recurring as the ground](https://www.youtube.com/watch?v=Uh9643c2P6k&t=37s) @ 37.5s, 100s
  - [Stripe — One brand grade across all footage](https://www.youtube.com/watch?v=KH0_HM6e66w) @ whole
- **Invention prompts:**
  - Palette taken from the user's own apps (Material You did this from wallpaper).
  - Product colour = set colour = mascot colour.
  - A single recurring background image that changes mood each scene.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

<a id="gag"></a>
### Visual gag / pun as payoff

- **Seen in:** 2 videos (Google, McDonald's) · uses: feature 1, hook 1
- **Principle:** surprise. A joke gives the viewer a reward and a reason to share.
- **After Effects:** Set up the expectation for 1–2 s, break it in one frame; hold the break.
- **Blender:** Not needed.
- **Code:** Script the punchline to land on a downbeat, with a real sound effect. The setup and the gag should be the same visual idea.
- **References:**
  - [Google — Word pun revealed by the product's own motion (unfold)](https://www.youtube.com/watch?v=NC_A3EHFKF4&t=20s) @ 20–22.5s
  - [McDonald's — Endless-repeat gag (letter keeps printing)](https://x.com/McDonalds/status/2122359723668222462) @ 1.5–6s
- **Invention prompts:**
  - The character sends one email too many (endless print gag).
  - A word pun revealed by the product's own motion (unfold → "Oh hi").
  - The end card gets a reaction from the mascot.
  - Combine with **Expressive type motion (tilt, scale jump, slice, ribbon, burst)** (also strong for feature): what happens if both land on the same beat?

**Also used for feature:** [One word (or phrase) per beat](#one-word) (4) · [Transition made from a scene element (shape, wave, tiles, dots)](#element-wipe) (4) · [Concrete metaphor (abstract idea as a physical thing)](#metaphor) (4) · [Pull back to reveal the frame (world → screen, macro → device)](#pullback) (3) · [Macro / impossible close-up of the object](#macro) (3) · [Typed text (prompt, title or caption types itself)](#typed) (3) · [Data beats (count-up, bars, counters, flow diagrams, logo rows)](#data) (3) · [Living background texture (grid, halftone, particles, shader)](#texture) (3) · [Dark → light release (glow, light-only reveal, silhouette)](#dark-light) (2) · [Character acting (eyes, takes, delayed reveal)](#character-acting) (2) · [Framing devices (grids, splits, symmetry, borders, masks)](#framing) (2) · [Fixed line, one swapping word](#word-swap) (1) · [Colour field per section / per idea](#palette-section) (1) · [Alternation rhythm (text card ↔ demo, abstract ↔ proof)](#alternation) (1) · [Mascot / product as a character that does things](#mascot-cameo) (1) · [Small type in negative space (captions, lower thirds, quotes)](#small-type) (1)

## Use: explainer

Explainers use one constant (character, shape, layout) and alternate claim and proof.

<a id="palette-section"></a>
### Colour field per section / per idea

- **Seen in:** 9 videos (Airtable, Figma, Framer, Google, Headspace, Mozilla Firefox, Slack, Spotify) · uses: explainer 8, social proof 1, feature 1
- **Principle:** clarity (chaptering). A ground change tells you a new idea started without a title card.
- **After Effects:** Solid layers per section, cut or wipe on the beat; keep the type colour constant for continuity.
- **Blender:** World colour per scene; or flat-shaded backdrop plane with keyed emission colour.
- **Code:** Give each section a colour field (full-frame or a large shape). Switch the field when the idea switches.
- **References:**
  - [Slack — Customer quote as a colour-block poster with a name chip](https://www.youtube.com/watch?v=zYotA_PNwbw&t=6s) @ 6–17.5s
  - [Headspace — Palette shifts from tension to calm with the story](https://www.youtube.com/watch?v=Mb19Ee8Dino&t=43s) @ 43–54s
  - [Airtable — Colour-block ground per use case](https://www.youtube.com/watch?v=UcZfSIegPNw&t=29s) @ 29–44s
- **Invention prompts:**
  - Tie each colour to an agent or app so colour = who is working.
  - Let the colour change happen via a character action (the mascot paints the wall).
  - Shift colour temperature with emotion (tension teal → calm pink).
  - Combine with **Continuous camera flight / glide over a world or UI** (also strong for explainer): what happens if both land on the same beat?

<a id="flight"></a>
### Continuous camera flight / glide over a world or UI

- **Seen in:** 7 videos (Duolingo, Google, Headspace, Linear, Loom, Microsoft, Netflix) · uses: explainer 5, hook 1, end card 1
- **Principle:** continuity. No cuts means no re-orienting: the viewer is carried, which feels calm and premium.
- **After Effects:** One long 3D-camera move over a large precomp/world; ease in/out only at the ends; add parallax layers at different Z.
- **Blender:** Bezier path + Follow Path camera; constant speed in the middle; separate foreground objects for parallax.
- **Code:** A continuous camera path over a world or a long UI. No cuts; ease through interest points.
- **References:**
  - [Netflix — Drift up into empty sky to make room for the title](https://x.com/netflix/status/2121318431139967161) @ 12–13s
  - [Google — Perspective grid floor fly-over](https://www.youtube.com/watch?v=Fs0t6SdODd8&t=112s) @ 112–118s
  - [Duolingo — Continuous camera flight through an illustrated world](https://www.youtube.com/watch?v=RavRouFiUio&t=2s) @ 2.7–8s
- **Invention prompts:**
  - Let the camera follow a moving actor (the mascot, a message) rather than a path.
  - Fly through the product's data (a week of calendar days) like a landscape.
  - Combine with a pull-back at the end so the flight was inside the device.
  - Combine with **Colour field per section / per idea** (also strong for explainer): what happens if both land on the same beat?

<a id="element-wipe"></a>
### Transition made from a scene element (shape, wave, tiles, dots)

- **Seen in:** 14 videos (Anthropic, Duolingo, Framer, Headspace, McDonald's, Microsoft, Mozilla Firefox, Netflix, Nothing, Pitch, The Browser Company (Arc)) · uses: explainer 5, hook 4, feature 4, social proof 1
- **Principle:** continuity. The transition belongs to the world, so it feels like an event, not an edit.
- **After Effects:** Animate the element to cover 100% of frame for 2–4 frames; use it as a track matte for the incoming comp.
- **Blender:** Foreground object passes the lens (near clip), cut on the frame it fills; render an alpha mask from it.
- **Code:** The transition is an object already in the shot (a shape, wave, tile grid or dots) growing to cover the frame, then revealing the next scene.
- **References:**
  - [Anthropic — AI as a participant tile in a video-call grid](https://x.com/claudeai/status/2120973994191094179) @ 0–7.8s
  - [Netflix — Spectrum stripe burst then collapse to one line](https://www.youtube.com/watch?v=GV3HUDMQ-F8&t=2s) @ 2.3–3.9s
  - [Microsoft — Frosted-glass icon tile floating alone](https://www.youtube.com/watch?v=Uh9643c2P6k&t=50s) @ 50–56s
- **Invention prompts:**
  - Wipe with the character's body (a head spin fills the frame).
  - Turn a split-flap card into the transition (the week flip becomes the cut).
  - A stamp hit cracks the frame into the next scene.
  - Combine with **Colour field per section / per idea** (also strong for explainer): what happens if both land on the same beat?

<a id="alternation"></a>
### Alternation rhythm (text card ↔ demo, abstract ↔ proof)

- **Seen in:** 8 videos (Apple, Cursor, GitHub, Google, Notion, OpenAI, Samsung) · uses: explainer 5, social proof 2, feature 1
- **Principle:** rhythm + clarity. Claim then proof, claim then proof: a steady beat of tell/show.
- **After Effects:** Two comp templates (text card, demo) alternated on a fixed beat (~1 s cards, 2–4 s demos).
- **Blender:** Not needed.
- **Code:** Alternate two templates (text card ↔ demo, abstract ↔ proof) on a fixed rhythm. Break the pattern for the payoff.
- **References:**
  - [Samsung — Cold CG = tech, warm live action = life](https://www.youtube.com/watch?v=2gYqEi8-am4) @ whole
  - [Cursor — Sentence card → UI demo alternation on paper](https://www.youtube.com/watch?v=An8IM-kPyms) @ whole
  - [OpenAI — Interviews intercut with minimal cards](https://www.youtube.com/watch?v=--khbXchTeE) @ whole
- **Invention prompts:**
  - Let the card and the demo be the same frame (the text becomes the UI).
  - Alternate the mascot's face with the result it produced.
  - Break the alternation once for emphasis.
  - Combine with **Colour field per section / per idea** (also strong for explainer): what happens if both land on the same beat?

<a id="metaphor"></a>
### Concrete metaphor (abstract idea as a physical thing)

- **Seen in:** 12 videos (Anthropic, Coca-Cola, Duolingo, Google, Headspace, LottieFiles, McDonald's, Microsoft, Perplexity, Vercel) · uses: explainer 5, feature 4, hook 4
- **Principle:** metaphor. An abstract benefit becomes a thing you can see happen (fuel, a stamp, a wave).
- **After Effects:** Design the metaphor object, then animate the one action that shows the benefit.
- **Blender:** Model the prop simply; physics (rigid body) for things that fill, fall or pour.
- **Code:** Replace an abstract UI state (progress, integration, done) with a physical action or prop, animated as a real object.
- **References:**
  - [Headspace — Abstract idea as a physical prop the character fights](https://www.youtube.com/watch?v=wyj8l9miy4w&t=11s) @ 11.6–65.7s
  - [Duolingo — Abstract feature shown as a physical object being built](https://www.youtube.com/watch?v=IEHiY8scAKI&t=7s) @ 7.5s, 22–26s, 48s
  - [Coca-Cola — Static artworks come alive and act](https://www.youtube.com/watch?v=VGa1imApfdg&t=14s) @ 14–84s
- **Invention prompts:**
  - Replace every progress bar with an object filling up.
  - A split-flap board for time passing.
  - Turn a security claim into a shield, a speed claim into a whip, a "done" into a stamp.
  - Combine with **Colour field per section / per idea** (also strong for explainer): what happens if both land on the same beat?

<a id="sound"></a>
### Sound shaped to picture (cut on onset, quiet mix, SFX on actions)

- **Seen in:** 4 videos (Coca-Cola, Cursor, Google, Nothing) · uses: explainer 3, hook 1
- **Principle:** sound sync. Sound tells you what matters: a hit on the key action, silence for calm.
- **After Effects:** Place markers from the music in AE (Convert Audio to Keyframes) and snap key actions to them; mix in Audition.
- **Blender:** VSE: add the music strip, mark beats, key actions to markers.
- **Code:** Drive cuts and pops from a cue list of picture events. Place real sound effects on those frames; measure onset alignment after the mix.
- **References:**
  - [Cursor — Near-silent mix (−29 LUFS) for a calm launch](https://www.youtube.com/watch?v=An8IM-kPyms) @ whole
  - [Coca-Cola — Cuts placed off the beat for a gentle feel](https://www.youtube.com/watch?v=Yy6fByUmPuE) @ whole
  - [Nothing — Fast cutting over dense percussive music (alignment at chance)](https://www.youtube.com/watch?v=w1h5ukOqOKs) @ whole
- **Invention prompts:**
  - Give every character action its own real sound.
  - Use a quiet mix for a calm brand, with one loud hit.
  - Sync only the 3–4 key actions, not every cut (brand average: cuts barely beat chance).
  - Combine with **Colour field per section / per idea** (also strong for explainer): what happens if both land on the same beat?

<a id="mascot-cameo"></a>
### Mascot / product as a character that does things

- **Seen in:** 9 videos (Airtable, Anthropic, Duolingo, Headspace, Mozilla Firefox, Runway) · uses: explainer 3, hook 2, end card 2, social proof 2, feature 1
- **Principle:** character + playfulness. A character doing the task is easier to love than a UI doing it.
- **After Effects:** Puppet tool or Duik rig; keep the character in every scene as a running presence.
- **Blender:** Simple rigged mesh; or Grease Pencil character over 3D.
- **Code:** Give the mascot hops, squash and stretch, and task-specific actions (typing, carrying, stamping). It performs the product action; the UI doesn't do it alone.
- **References:**
  - [Anthropic — Status circle acts out the current task](https://x.com/claudeai/status/2120973994191094179) @ 15.6s, 28.7s
  - [Duolingo — Mascot photobombs the final scene](https://www.youtube.com/watch?v=Ew4kM1FmM8o&t=27s) @ 27s
  - [Headspace — Proverb acted out literally by a mascot](https://www.youtube.com/watch?v=Mb19Ee8Dino&t=5s) @ 5.4–54s
- **Invention prompts:**
  - Give the mascot a physical job (typing, stamping, carrying logos as fuel).
  - Let it interact with the type (hide behind a letter, push the headline).
  - The status ring IS the character (Claude meetings, Airtable).
  - Combine with **Colour field per section / per idea** (also strong for explainer): what happens if both land on the same beat?

<a id="hold"></a>
### Hold / breath beat before the payoff

- **Seen in:** 3 videos (Airbnb, Netflix, OpenAI) · uses: explainer 2, end card 1
- **Principle:** restraint + anticipation. Silence and stillness make the next thing land harder.
- **After Effects:** Leave 12–30 fr of near-empty frame before the key reveal; lower the music bed there.
- **Blender:** Not needed.
- **Code:** Hold the settled pose for a beat (or a bar) before the payoff. Duck the music slightly into the hold.
- **References:**
  - [Netflix — Hold before the payoff](https://www.youtube.com/watch?v=GV3HUDMQ-F8&t=0s) @ 0.5–1.8s
  - [OpenAI — Long holds on real tasks (0.8 cuts/10s)](https://www.youtube.com/watch?v=Ej6hnsQgV_c) @ whole
  - [Airbnb — Minimal title card between worlds](https://www.youtube.com/watch?v=Rz2FWiJq4Mw&t=27s) @ 27s, 38.7s, 65.8s
- **Invention prompts:**
  - Hold on the character's blink before it acts.
  - Empty white beat before the stamp hit.
  - If a beat cannot be read, lengthen the film rather than squeeze the holds.
  - Combine with **Colour field per section / per idea** (also strong for explainer): what happens if both land on the same beat?

<a id="small-type"></a>
### Small type in negative space (captions, lower thirds, quotes)

- **Seen in:** 5 videos (Duolingo, Google, Perplexity, Samsung, Stripe) · uses: explainer 2, hook 1, feature 1, social proof 1
- **Principle:** restraint. Small type in lots of space reads as confident; it never fights the image.
- **After Effects:** Type at 2–3% of frame height, tracked +50–100 for caps; 6-fr fade or no animation.
- **Blender:** Not needed.
- **Code:** Place captions or quotes small, in real negative space, not as a lower-third bar that covers the action.
- **References:**
  - [Samsung — Superlative headline over a CG world](https://www.youtube.com/watch?v=2gYqEi8-am4&t=12s) @ 12.5s, 56s, 118s
  - [Duolingo — One short caption above the device](https://www.youtube.com/watch?v=Ew4kM1FmM8o&t=5s) @ 5.5–21.9s
  - [Google — Small process captions at the bottom](https://x.com/Google/status/2121274901898170752) @ 4.6–20.6s
- **Invention prompts:**
  - One small caption that the character reads aloud.
  - Small type that grows to a headline on the payoff.
  - Caption chips for mute viewing in vertical cuts.
  - Combine with **Colour field per section / per idea** (also strong for explainer): what happens if both land on the same beat?

<a id="easing"></a>
### Visible easing: springs, overshoot and settle

- **Seen in:** 1 videos (Figma) · uses: explainer 1
- **Principle:** anticipation → payoff (physics). Motion that overshoots and settles reads as physical; showing the curve teaches it.
- **After Effects:** Graph Editor: speed graph with 80–90% influence ease-out; pops 0→108→100% over 3–5 fr; or a spring expression (amp*sin(freq*t*2PI)/exp(decay*t)).
- **Blender:** F-curve Back/Elastic easing modes in the keyframe Interpolation menu; or the Cycles modifier for loops.
- **Code:** Use springs or overshoot (pass the rest value, then settle). Avoid linear moves on anything the eye tracks.
- **References:**
  - [Figma — Spring curve with overshoot shown beside the motion it drives](https://x.com/figma/status/2120200083992105008) @ 20–31s
- **Invention prompts:**
  - Give each character a signature ease (the character snaps, the user drifts).
  - Show the spring as a physical thing (a stamp handle that wobbles).
  - Overshoot only on the payoff; everything else eases plainly.
  - Combine with **Colour field per section / per idea** (also strong for explainer): what happens if both land on the same beat?

<a id="scale-play"></a>
### Scale play (tiny figure, giant object, miniature)

- **Seen in:** 1 videos (Duolingo) · uses: explainer 1
- **Principle:** contrast (scale). Size contrast makes the hero feel big without saying so.
- **After Effects:** Tiny character layer next to a giant product layer; slow move to emphasise scale.
- **Blender:** Real scale scene; long lens to compress.
- **Code:** Jump the scale of a figure or object by a large factor (a tiny figure in a giant world, or a giant object in a normal room). Keep one continuous camera if you can.
- **References:**
  - [Duolingo — Scale cut: tiny in a big world → face-filling close-up](https://www.youtube.com/watch?v=IEHiY8scAKI&t=15s) @ 15–19s
- **Invention prompts:**
  - The character is tiny in a giant inbox, then the inbox shrinks to fit its hand.
  - Inline at text height, then near full screen.
  - Miniature world that turns out to be on a desk.
  - Combine with **Colour field per section / per idea** (also strong for explainer): what happens if both land on the same beat?

**Also used for explainer:** [Match cut / one object carried through contexts](#match-relay) (5) · [Living background texture (grid, halftone, particles, shader)](#texture) (4) · [Prompt bar, chips and bubbles (AI UI)](#prompt-ui) (3) · [Typed text (prompt, title or caption types itself)](#typed) (2) · [One word (or phrase) per beat](#one-word) (2) · [Fixed line, one swapping word](#word-swap) (2) · [One accent colour on one element](#accent-one) (2) · [Bookend / callback / seamless loop](#bookend) (2) · [Zero-cut single take](#zero-cut) (2) · [Assembly / exploded view (parts fly in and lock)](#assembly) (2) · [Data beats (count-up, bars, counters, flow diagrams, logo rows)](#data) (2) · [Framing devices (grids, splits, symmetry, borders, masks)](#framing) (2) · [Macro / impossible close-up of the object](#macro) (1) · [Progressive reveal (sentence completes, list unblurs)](#sentence-split) (1) · [Type physically on or through the object](#type-object) (1) · [Expressive type motion (tilt, scale jump, slice, ribbon, burst)](#expressive-type) (1) · [Dark → light release (glow, light-only reveal, silhouette)](#dark-light) (1) · [Character acting (eyes, takes, delayed reveal)](#character-acting) (1) · [Objects orbit or float around a hero](#orbit) (1) · [Product lineup and spec-as-hero](#lineup-spec) (1) · [One UI element isolated as the hero](#ui-hero) (1) · [UI on tilted planes / over footage or soft backgrounds](#ui-planes) (1) · [Cursor or named agent pointer driving the UI](#cursor) (1) · [One colour system across the whole film](#colour-system) (1)

## Use: social proof

Social proof shows volume (montage, walls, counters) or a real person, not a claim.

<a id="fast-montage"></a>
### Fast montage / sizzle (8–15 cuts per 10s)

- **Seen in:** 5 videos (Adobe, Airbnb, Google, Microsoft, Stripe) · uses: social proof 5, hook 1
- **Principle:** energy + social proof. Volume says "a lot is happening"; works only with a strong music grid.
- **After Effects:** Edit to markers placed on the beat; 4–8 fr shots; same type system over all of them.
- **Blender:** Not needed.
- **Code:** 8–15 hard cuts per 10 s, one type system on top. Keep a constant (type voice, grade, or graphic frame) so the cuts read as one sentence.
- **References:**
  - [Google — Montage cut to the music](https://www.youtube.com/watch?v=3KtWfp0UopM) @ whole
  - [Microsoft — Ultra-fast montage (≈15 cuts/10s)](https://www.youtube.com/watch?v=l4B1UflAty8) @ whole
  - [Airbnb — Recognisable IP montage before the product](https://www.youtube.com/watch?v=Rz2FWiJq4Mw&t=3s) @ 3.9–77s
- **Invention prompts:**
  - Montage of the character's actual outputs (sent emails, booked slots) as proof.
  - Accelerate: shots get shorter toward the drop.
  - Freeze the montage on one frame for the payoff.
  - Combine with **Data beats (count-up, bars, counters, flow diagrams, logo rows)** (also strong for social proof): what happens if both land on the same beat?

<a id="data"></a>
### Data beats (count-up, bars, counters, flow diagrams, logo rows)

- **Seen in:** 7 videos (GitHub, Google, LottieFiles, Microsoft, OpenAI, Pitch) · uses: social proof 4, feature 3, explainer 2
- **Principle:** proof. One number that moves is proof; keep it to one highlighted bar or number.
- **After Effects:** Slider Control → text expression Math.round(); bars scale Y from 0 with ease-out and 2-fr stagger.
- **Blender:** Geometry Nodes bars with scale driven by a value; Text with driver.
- **Code:** Animate a number, bar, flow or logo row as the beat. Count-ups should be readable and land on a round, true figure.
- **References:**
  - [Microsoft — Partner logo row](https://www.youtube.com/watch?v=Uh9643c2P6k&t=143s) @ 143s
  - [OpenAI — Minimal two-bar comparison](https://www.youtube.com/watch?v=--khbXchTeE&t=25s) @ 25s
  - [Google — Stacked numbers settling](https://www.youtube.com/watch?v=1ndT_uyeK64&t=28s) @ 28s
- **Invention prompts:**
  - Count something human (hours saved) and land on a round number.
  - The counter is a split-flap board.
  - Bars that the mascot climbs.
  - Combine with **Fast montage / sizzle (8–15 cuts per 10s)** (also strong for social proof): what happens if both land on the same beat?

**Also used for social proof:** [Objects orbit or float around a hero](#orbit) (3) · [Alternation rhythm (text card ↔ demo, abstract ↔ proof)](#alternation) (2) · [Mascot / product as a character that does things](#mascot-cameo) (2) · [End-card sequence (beats after the logo)](#endcard) (1) · [Fixed line, one swapping word](#word-swap) (1) · [One accent colour on one element](#accent-one) (1) · [Colour field per section / per idea](#palette-section) (1) · [Transition made from a scene element (shape, wave, tiles, dots)](#element-wipe) (1) · [Character acting (eyes, takes, delayed reveal)](#character-acting) (1) · [Cursor or named agent pointer driving the UI](#cursor) (1) · [Confirmation pop (toast, badge, check, shimmer, ring)](#confirm) (1) · [Living background texture (grid, halftone, particles, shader)](#texture) (1) · [One colour system across the whole film](#colour-system) (1) · [Small type in negative space (captions, lower thirds, quotes)](#small-type) (1) · [Framing devices (grids, splits, symmetry, borders, masks)](#framing) (1)

## Use: end card

End cards are quiet, in steps, and often resolve a motif into the logo or add one joke beat.

<a id="endcard"></a>
### End-card sequence (beats after the logo)

- **Seen in:** 20 videos (Adobe, Airbnb, Apple, Discord, Duolingo, Figma, GitHub, Google, Linear, McDonald's, Notion, Perplexity, Samsung, Shopify, Slack, Stripe, The Browser Company (Arc)) · uses: end card 21, social proof 1
- **Principle:** restraint. Big brands end quiet and in steps (status → URL → logo, or logo → joke) so each item gets its own read.
- **After Effects:** Separate comps per beat, 0.8–1.5 s each, hard cut or 6-fr fade; type at small size centred; leave the logo on screen for ≥1.5 s.
- **Blender:** Not needed: do it in the compositor or the 2D renderer. If 3D, render the hero product still and overlay type in the VSE.
- **Code:** One short scene per beat after the logo (wordmark, URL, line of type). Time the beats to the bar grid.
- **References:**
  - [Duolingo — Co-brand "×" card](https://www.youtube.com/watch?v=o3ftECYtkf0&t=26s) @ 26s
  - [Slack — "And [logo] Brand" partner line over footage](https://www.youtube.com/watch?v=zYotA_PNwbw&t=3s) @ 3.7s, 8.7s, 13.7s
  - [Apple — Logo on black after a hold](https://www.youtube.com/watch?v=oT5iDm9XRl8&t=61s) @ 61–67s
- **Invention prompts:**
  - Add one beat after the CTA that pays off a running gag (the mascot winks, the stamp lands on the logo).
  - Make the co-brand divider do something only these two brands can do (one logo feeds the other).
  - Let the end card be a frame from the product itself (a sent email, a calendar slot) instead of a white card.
  - Combine with **Logo built from a motif (dot, ribbon, shapes, lines)** (also strong for end card): what happens if both land on the same beat?

<a id="logo-build"></a>
### Logo built from a motif (dot, ribbon, shapes, lines)

- **Seen in:** 15 videos (Adobe, Anthropic, Apple, Discord, Figma, Google, Headspace, Linear, Microsoft, Netflix, Notion, Perplexity, Vercel) · uses: end card 11, hook 5
- **Principle:** payoff. The end mark is the last beat of the film, not a sticker: the shape the viewer has been following becomes the logo.
- **After Effects:** Animate the motif as shape layers; on the last beat parent them to a null and keyframe Path/Position into the logo shape (or use the logo as a track matte that grows from the motif). Ease: 80% ease-in into the lock, 3–5 fr overshoot.
- **Blender:** Model the logo as curves/mesh; drive the motif objects with shape keys or a Geometry Nodes "Sample Nearest Surface" morph from scattered points to the logo surface; key the factor 0→1.
- **Code:** Interpolate a motif (dots, ribbons, lines) into the logo outline, then pop the filled mark on a downbeat. Use motion blur on the fast frames.
- **References:**
  - [Google — Number worked into the logo](https://www.youtube.com/watch?v=3KtWfp0UopM&t=226s) @ 226s
  - [Netflix — Logo build from ribbons with fold shading](https://www.youtube.com/watch?v=GV3HUDMQ-F8&t=0s) @ 0–0.5s
  - [Microsoft — Fly through the logo as architecture](https://www.youtube.com/watch?v=Uh9643c2P6k&t=6s) @ 6–12s
- **Invention prompts:**
  - Let the product's own action draw the mark (a cursor drags it, a stamp prints it, a laptop lid closes onto it).
  - Build the logo from the thing the film was about (data points, chat bubbles, agents) so the end card restates the story.
  - Reverse it: start on the logo and let it break into the motif as the hook.
  - Combine with **End-card sequence (beats after the logo)** (also strong for end card): what happens if both land on the same beat?

<a id="bookend"></a>
### Bookend / callback / seamless loop

- **Seen in:** 8 videos (Anthropic, Apple, Framer, Headspace, Linear, Notion) · uses: end card 4, explainer 2, hook 2
- **Principle:** continuity. Ending where you started makes the film feel complete and makes social loops seamless.
- **After Effects:** Duplicate the opening comp for the end; for loops match the last frame to frame 0 and cut there.
- **Blender:** Key the last frame equal to the first (cyclic F-curves).
- **Code:** Repeat the opening frame or sound at the end, with or without a change. For a loop, the last frame should cut cleanly to the first.
- **References:**
  - [Headspace — Callback to the opening image](https://www.youtube.com/watch?v=wyj8l9miy4w&t=81s) @ 81–85s
  - [Anthropic — Headline → prompt → canvas loop per product](https://x.com/claudeai/status/2120206365759094857) @ whole
  - [Framer — Bookend on a single button](https://www.youtube.com/watch?v=6xJWQRVl9nw&t=0s) @ 0s / 32.3s
- **Invention prompts:**
  - Callback with a change: the same opening shot, but now the character has done the work.
  - Loop the mascot's head spin so the end hands straight back to the start.
  - Bookend with sound only (same click at start and end).
  - Combine with **End-card sequence (beats after the logo)** (also strong for end card): what happens if both land on the same beat?

**Also used for end card:** [One word (or phrase) per beat](#one-word) (4) · [Pull back to reveal the frame (world → screen, macro → device)](#pullback) (3) · [Object sits in the line of type (inline glyph, object as a word)](#inline-object) (3) · [Expressive type motion (tilt, scale jump, slice, ribbon, burst)](#expressive-type) (3) · [Progressive reveal (sentence completes, list unblurs)](#sentence-split) (2) · [Type physically on or through the object](#type-object) (2) · [Mascot / product as a character that does things](#mascot-cameo) (2) · [Continuous camera flight / glide over a world or UI](#flight) (1) · [Typed text (prompt, title or caption types itself)](#typed) (1) · [Dark → light release (glow, light-only reveal, silhouette)](#dark-light) (1) · [Match cut / one object carried through contexts](#match-relay) (1) · [Hold / breath beat before the payoff](#hold) (1) · [One UI element isolated as the hero](#ui-hero) (1) · [Pulse rings / radar rings as a motif](#rings) (1) · [Framing devices (grids, splits, symmetry, borders, masks)](#framing) (1)

## Method and limits

- Breakdowns were written from 24-frame contact sheets, scene-change frames and measurements. Techniques were tagged by hand, then grouped into families.
- Videos longer than 150 s were analysed on their first 150 s only. Many social videos are downloaded at 480p or below, so fine detail and exact easing curves are not measurable from them.
- Scene detection (threshold 0.25) misses fades, morphs and moves. "0 cuts" means no hard cut, not no change.
- Sound: loudness, onsets and tempo were measured. Music and sound effects were not listened to, so nothing here describes how a track sounds.
