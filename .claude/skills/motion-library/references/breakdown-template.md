# Breakdown template

Write one markdown file per video, named after a short slug, for example `breakdowns/brand-film-name.md`. Only claim what you saw or measured. If a claim comes from frames rather than from listening, say so.

Suggested header fields, then the required sections.

```markdown
# Brand — Film title

- **Source:** https://...
- **Brand:** ... · channel/account: ... (confirm it is the official upload, not a fan re-upload)
- **Uploaded:** YYYY-MM-DD · original title: "..."
- **Metrics:** views, likes, bookmarks, with the date you read them
- **Length:** ...s · downloaded at ... (480p or below, first 150 s if the film is longer)
- **Measured:** N scene changes (ffmpeg scene>0.25) = X.X per 10s · loudness −X.X LUFS · mean luma X/255 · tempo est. X BPM · N/M cuts within 70 ms of an audio onset (chance ≈ X%) · percussive share X.XX
- **Frames:** `frames/<slug>/` (interval/, scene/, review_NN.jpg) · contact sheet `sheets/<slug>.jpg`
- **Basis:** written from the 24-frame contact sheet plus the scene-change frames and the measurements above. Sound was measured, not listened to.

## Overall feel

A short paragraph on tone, typography, colour, and how the piece is structured. Name the hero and the payoff.

## Shot-by-shot

| Time | What happens | Techniques |
|---|---|---|
| 0–… |  |  |

## Why it works

- **Clarity / rhythm / contrast / anticipation and payoff / restraint / continuity / sound sync / …:** one or two sentences, tied to what you saw or measured.

## Sound

Layers, sync, density, silence, loudness. Say when a claim is from measurements only.

## Techniques

| Category | Use | Technique | Time | Seen |
|---|---|---|---|---|
|  |  |  |  |  |
```

**Category** is one of: framing, mask reveal, kinetic type, transition, camera, 3D, easing, colour, pacing, sound, character, UI.

**Use** is one of: hook, feature, explainer, social proof, end card.

## Filled example (abridged)

This is a shortened version of a public Adobe film, to show the shape. It is not a complete breakdown.

# Adobe — Meet Firefly Video Model

- **Source:** https://www.youtube.com/watch?v=fjk2mMFBpRo
- **Brand:** Adobe · channel/account: Adobe
- **Length:** 57s
- **Measured:** 36 scene changes (ffmpeg scene>0.25) = 6.3 per 10s · loudness −15.3 LUFS
- **Basis:** written from a 24-frame contact sheet, scene-change frames and measurements. Sound was measured, not listened to.

## Overall feel

A feature sizzle where huge bold white headlines sit directly on top of the generated imagery. Between headlines, the Firefly UI shows a prompt bar typing and a grid of results. The same jellyfish image passes from a full-frame shot into a Photoshop window, then onto a laptop on a desk, so one visual threads several shots. Ends on the Adobe wordmark on white.

## Shot-by-shot

| Time | What happens | Techniques |
|---|---|---|
| 0–4.7 | "Adobe Firefly" big over the web UI; "The ultimate in creative AI." over a grid of images. | Headline over UI |
| 7–12 | "Now with video." over a lake; "Get even more creative control" over an aurora. | Headline over the output |
| 16.6–21 | Prompt bar types, then a results grid fills. | Prompt bar → grid |
| 42.7–45 | "with the apps you love." over a jellyfish → same jellyfish inside Photoshop. | One image threads through contexts |
| 54.5 | Adobe logo on white. | End card |

## Why it works

- **Proof:** headlines sit on the product's own results, so every claim comes with evidence.
- **Continuity:** the jellyfish moves from full frame → app window → laptop, linking three ideas.

## Sound

Measured only: 36 cuts, −15.3 LUFS. No listening notes.

## Techniques

| Category | Use | Technique | Time | Seen |
|---|---|---|---|---|
| kinetic type | feature | Bold headline set directly on the product's output | 7–52s | white headline over generated images |
| transition | feature | One image threads through contexts (full frame → app → device) | 42.7–52s | jellyfish |
| UI | explainer | Prompt bar types, then a results grid fills | 16.6–21s | cleats prompt |
| pacing | end card | Wordmark on white after a dark film | 54.5s | Adobe |
