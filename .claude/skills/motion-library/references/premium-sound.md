# Premium sound design

Cheap, generic sound effects are the clearest tell of AI-made motion. This note is about what a set of brand mixes actually measures like, and how to build sound that holds up next to them.

**Method.** The audio of 39 brand videos with sound (the first 90 s of each) was measured with ffmpeg (EBU R128) and librosa. **Limits:**

- These are whole mixes, so music, sound effects and voice-over cannot be separated. A "hit" is any strong transient in the mix: a level jump of at least 10 dB over the previous 150 ms, measured on a 10 ms window.
- Nothing was judged by ear.
- The reference audio is YouTube or X AAC or Opus, so values above 16 kHz are less reliable.
- Two sister spots in the set share one soundtrack, so only one of them is counted.

## What the reference set measures like (39 mixes)

| Measure | Median | Middle half (IQR) | Range | Examples |
|---|---|---|---|---|
| Integrated loudness | −15.8 LUFS | −20.4 to −13.2 | −29.2 (Cursor 2.0) to −9.9 (Figma 3D transforms) | Premium is not the same as loud. Anthropic (−26.4), Microsoft 365 Copilot (−25.2) and Netflix Planeswalker (−22.7) mix quiet. |
| Peak-to-loudness ratio (headroom for hits) | 14.6 dB | 12.4–16.1 | 10.3–21.5 | Microsoft 365 Copilot 21.5, Lottie 20.2, Netflix Planeswalker 19.1. |
| Loudness range (LRA) | 5.1 LU | 3.4–7.1 | 1.4–17.7 | Duolingo Duo work day 17.7, iPad Air 17.1, Duolingo × Squid Game 13.3 and Windows 11 13.0 use big quiet/loud swings. |
| Strong hits per 10 s | 8.6 | 4.5–14.2 | 0.9–34.1 | Sparse: Slack AI 0.9, Samsung Z Fold6 design film 1.3, Planeswalker 1.9, Windows 11 3.3, Linear 3.3. Dense: Cursor 2.0 34.1, Figma Config 20.6, Figma 3D transforms 20.2, Nothing Phone (2) 19.1. |
| Hit prominence over the bed | 12.9 dB | 11.9–14.8 | 11.0–16.8 (Netflix logo sting excluded: 68 dB from silence) | Highest: Samsung Z Fold6 16.8, Headspace Letting go 16.8, Headspace Elephant 16.5, Nothing 16.4, Duolingo video call 16.1. |
| Hit decay (time to fall 10 dB) | 128 ms | 90–150 | 50–1,145 | Long tails: Z Fold6 1,145 ms, Planeswalker 435, Slack AI 435, McDonald's WcDonald's 202, Airbnb Icons 188. |
| Time a hit stays above the bed (+3 dB) | 145 ms | 100–210 | 65–1,500 | |
| Low end (<80 Hz share of energy) | 31% | 7–49% | 0.3–73% | Product films are bass-heavy: Planeswalker 73%, Pixel 9 Pro 63%, AirPods Pro 3 61%, Squid Game 56%, MacBook Air 49%. Character or voice-over films are light: Headspace 0.3–0.9%, Duolingo video call 0.9%. |
| "Air" (>10 kHz share) | 0.26% | 0.17–0.58% | 0.0–2.41% | Brighter mixes have less sub (Spearman ρ −0.36, p 0.03). |
| Stereo side/mid | −12.0 dB | −14.8 to −6.8 | | |
| Mid-film silence (≥0.3 s, ≥20 dB under the median level) | 0 drops | 0–1 | 14 of 39 have at least one | Airbnb Icons (3 drops, 2 followed by a hit within 0.6 s), Windows 11 (2), iPad Air (2), Duolingo Duo work day (2), Z Fold6 (2). Headspace drops are mostly voice-over pauses. |

## What the evidence says premium sound does

1. **Sparse edits let hits ring; dense edits keep them short.** Across the set, more hits per 10 s goes with shorter decay (ρ −0.30, p 0.06; a weak trend). The calm product films (Z Fold6, Planeswalker, Slack AI) have about 1–2 hits per 10 s with 400–1,100 ms tails. The dense ones (Nothing, Arc, Cursor) cut hits short (50–70 ms) but sit on a steady music grid.
2. **Hits stand about 12–15 dB above what came just before.** That needs headroom, and the median peak-to-loudness ratio is 14.6 dB. Over-limiting flattens the hits.
3. **Weight comes from the low end, not from brightness.** The big product films put half or more of their energy under 80 Hz. Bright, thin mixes are the exception.
4. **Silence is used, but sparingly.** About a third of the films drop out mid-piece at least once. In Airbnb Icons, a drop followed by a hit is the reveal.
5. **Cuts don't have to land on the music.** From the 82-video cut analysis, 52.4% of 1,710 cuts land on an onset against 50.8% by chance. Sync the hero actions, not every edit.

## How to build premium sound effects

- **Layering:** build each hero hit from three parts, aligned to the same frame:
  - a **transient** (a click or snap, 0–10 ms)
  - a **body** with pitch and weight (a thump or tonal hit, 30–200 ms)
  - a **tail or sweetener** (room, shimmer, debris, 0.3–1.5 s)
  - Add a sub layer under 80 Hz only for the 3–5 biggest moments.
  - After Effects: lay the layers out in Audition or Premiere on separate tracks and nudge them by frames. In code, place the three files on the same frame with different low-pass and high-pass filters.
- **Transient design:**
  - Shape the attack: a short fade-in of 1–3 ms, no clipped starts.
  - Keep transients distinct from the music's kick (high-pass the click, low-pass the body).
  - Never fire the same transient twice in a row without variation.
- **Tails and room:**
  - Give every sound a shared space: one room or plate reverb send for the whole sound-effects bus, so sounds feel recorded in the same place.
  - Never truncate a tail with a 40 ms fade unless the next sound masks it. Hero tails should run 300 ms or longer, as the long-tail references do.
  - In code, convolve the sound-effects bus with an impulse response at about −18 to −24 dB wet.
- **Variation (round robin):**
  - Use 3–6 different recordings for any repeated action (key clicks, flaps, pops).
  - Add ±3–8% pitch, ±1.5 dB level and ±5–10 ms timing scatter.
  - Cap reuse of one file at about 4 times per 30 s.
- **Foley, not stock:**
  - Record physical actions for real: a rubber stamp on card, real keyboard keys, a laptop lid, paper. A phone recorder in a quiet room at 48 kHz/24-bit beats a game-UI pack.
  - Use stock only for sweeteners. Use lossless WAV sources only, never preview MP3s or low-bitrate OGGs.
- **The mix leaves space:**
  - Decide per scene whether music or sound effects lead.
  - Carve EQ: duck the music 3–6 dB around hero hits and notch the music where the hit's body sits.
  - Leave at least one real silence (0.3–1 s) before the biggest reveal.
  - Print the mix for about 14–16 dB peak-to-loudness rather than pushing to −14 LUFS through a limiter.
- **Blender:** the VSE can place and mix sound strips, but do the design in a DAW (Reaper, Audition, Logic) and import the stems.

## Invention prompts

- Make one sound signature the character's "voice": a tonal blip family (three pitches) that every character action is built from, the sonic equivalent of a logo motif.
- Score silence as an event: the character freezes, the room tone drops out, then the hit lands into nothing.
- Use the music's own instruments as sound effects: pull a tom or a pluck from the stem so hits feel composed, not added.
- Diegetic to score: a mechanical action speeds up into the beat of the next section.
- Foley the metaphor: if logos are fuel, they should sound like real liquid or a real engine, not UI pops.

## Better sound-effect sources

Licences last checked 16 November 2026. Always read the licence on the page you download from.

| Source | Cost | Licence (summary) | Good for |
|---|---|---|---|
| [Sonniss #GameAudioGDC bundles](https://sonniss.com/gameaudiogdc/) ([licence](https://sonniss.com/gdc-bundle-license/)) | Free | Royalty-free and commercial, no attribution, unlimited projects. No redistributing the sounds as sounds, no AI training. | Pro-grade WAV libraries (impacts, foley, UI, whooshes) from professional vendors. |
| [Freesound](https://freesound.org/) | Free | A licence per sound: CC0, CC BY 4.0 (credit required) or CC BY-NC 4.0 (non-commercial only, so not for client ads). Check each sound. | Specific foley and room tones; filter to CC0 for commercial work. |
| [Pixabay sound effects](https://pixabay.com/sound-effects/) ([licence](https://pixabay.com/service/license-summary/)) | Free | Pixabay Content License: commercial use, no attribution, no selling the sounds standalone. | Quick sweeteners. Quality varies, so audition each one. |
| [ZapSplat](https://www.zapsplat.com/) ([licence](https://www.zapsplat.com/license-type/standard-license/)) | Free with attribution; **paid** Premium removes attribution and adds WAV | Free tier: MP3 only, credit "ZapSplat", download limits. Premium: WAV, no attribution, and sounds stay attribution-free for life. | Broad foley library. Use Premium for WAVs. |
| [BBC Sound Effects](https://sound-effects.bbcrewind.co.uk/) ([licence](https://sound-effects.bbcrewind.co.uk/licensing)) | Free for **non-commercial** use only; commercial use is **paid** via Pro Sound Effects | RemArc licence: personal, research and education only. Commercial licences come from Pro Sound Effects (single sounds from $5). | Real-world foley and ambiences, licensed if it's for an ad. |
| [Soundly](https://getsoundly.com/) | Free tier; Pro is **paid** (subscription) | Commercial sync licence. Productions completed while subscribed stay licensed for good. | Big curated cloud library plus a search tool for your own files. |
| [Pro Sound Effects](https://www.prosoundeffects.com/licensing) | **Paid** | Lifetime 1-user royalty-free licence (or a subscription). No resale and no AI training. | Industry-standard libraries, including BBC commercial. |
| [BOOM Library](https://www.boomlibrary.com/shop/) | **Paid** | Perpetual royalty-free single-user buyout. | Cinematic impacts, whooshes, UI and designed hits. |
| [A Sound Effect](https://www.asoundeffect.com/license-agreement/) | **Paid** (marketplace; also a free cloud section) | Perpetual, royalty-free, non-exclusive. Sync use only, no standalone resale, no AI training. | Indie pro libraries; a good place to find foley packs. |
| [Soundsnap](https://www.soundsnap.com/license) | **Paid** (subscription) | Royalty-free and perpetual for projects made while subscribed. Pro+ adds broadcast/OTT. | Large general library. |
| [Epidemic Sound](https://www.epidemicsound.com/pricing/) | **Paid** (subscription) | Royalty-free sound effects and music within the plan's terms. | Music and sound effects from one place. |
| [Artlist](https://help-center.artlist.io/media/ttipdwa1/artlist-license.pdf) | **Paid** (subscription) | Commercial use. Projects made while subscribed stay covered; no standalone use. | Music and sound effects. |
| [Splice Sounds](https://support.splice.com/en/articles/8652642-splice-sounds-licensing-faq) | **Paid** (subscription) | Royalty-free and commercial, including video. Downloads stay licensed; no redistribution as samples. | Musical one-shots and tonal hits for a sonic "voice". |
| [Kenney](https://kenney.nl/assets) and [Mixkit](https://mixkit.co/free-sound-effects/) | Free | Kenney: CC0. Mixkit: Mixkit Sound Effects Free License. | Fine for scratch and placeholders. Game-UI style and lossy files, so keep them away from hero moments. |
