# Pre-flight checklist and general rules

Run this checklist before every storyboard or render. Cheap, generic sound effects are the main tell of AI-made motion, so the sound section is not optional.

Keep a lessons file of the owner's revision notes (a template is at the end of this file). Add each new round of feedback as a rule, and update the checklist when a new rule shows up.

## General rules

These started as revision notes on product films. They travel.

1. **Open on a hero move, not a fade-in.** The first second needs one signature move by the hero character: anticipation → fast action → overshoot → settle. A logo or mascot that just fades in is not a hook.
2. **The character drives the UI.** When the character is on screen, selections, sends and confirmations come from the character (head, eyes, hands) or from a visible user action. Land the choice on a downbeat.
3. **Real 3D for anything that moves in depth.** Objects that turn, open, or are flown into should be real 3D renders with real lighting and motion blur. A photo or flat plate with a keystone is only acceptable for distant, static props.
4. **Readable pacing.** If a beat cannot be read at normal speed, lengthen the film by whole bars rather than squeezing holds. Readability beats a tight runtime. The big-brand median in the reference set is 1.85 scene cuts per 10 s.
5. **Introduce a new hero object inline.** Place it small, at text height or at the centre of attention, with negative space around it, so the sentence explains it. Then grow it to near full screen at an angle, never flat-on. Do not introduce it as a tiny corner speck.
6. **Playful character actions, not static UI.** Every product action is performed by the character as a physical action (typing, stamping, carrying), not shown only as a UI state change.
7. **Concrete metaphors, not progress bars.** Never use a plain progress bar, spinner or checkmark as the story beat. Turn the abstract (integration, time passing, done) into an object doing something.
8. **Real sound, treated as craft, not just sync.** Every visible action that matters gets a real sound on the exact frame. Music is a real licensed or CC track cut on its bar grid. No synthesized placeholders in anything shown to the owner. Each hero action gets a layered, designed sound in a shared room, made from lossless sources and real foley where the action is physical. Repeated actions use varied takes, and the mix leaves room. Free UI packs are for scratch tracks only. See `premium-sound.md`.

## Pre-flight checklist

- [ ] **Hook:** the first second has one signature move by the hero (anticipation → action → overshoot → settle). Not a fade-in.
- [ ] **Character drives UI:** every selection, send or confirmation is triggered by the character or the user, and the selector follows the character.
- [ ] **Approval shown:** any action that sends, books or buys shows the user's approval tap before the character acts.
- [ ] **No generic progress UI:** no plain progress bars, spinners or checkmarks as story beats; each is a concrete metaphor or a character action.
- [ ] **3D is real:** objects that move in depth are real 3D renders (lighting, motion blur), sharp at every size they appear (check the smallest size at 100%).
- [ ] **Intro composition:** new hero objects enter inline with the type or at the centre of attention, with negative space; never as a corner speck. They grow to near full screen at an angle, not flat-on.
- [ ] **Pacing readable:** every text line holds ≥0.8 s after it lands; every beat can be read at 1x on a first view; pushes or dollies that change scenes are ≥20 frames. If not, lengthen by whole bars.
- [ ] **Safe zones:** no moving element crosses live text (check every scene's title bounding box).
- [ ] **Sound is real:** every key action has a real sound effect on the exact frame; music is real and on its bar grid; mix about −14 LUFS integrated, ≤ −1 dBTP. No synthesized temp audio.
- [ ] **Sound quality, not just sync.** For each hero sound, check:
  - **Layering:** transient + body + tail/sweetener, plus sub only on the 3–5 biggest hits.
  - **Transient design:** shaped attack, no clipped starts, and the click doesn't fight the music's kick.
  - **Tails and room:** a shared room or plate send on the sound-effects bus; no tail cut short unless the next sound masks it; hero tails ≥300 ms.
  - **Variation:** 3–6 takes for any repeated action, ±3–8% pitch and ±1.5 dB scatter, and no single file used more than about 4 times per 30 s.
  - **Foley rather than stock:** physical actions (stamp, keys, lid, paper) recorded or sourced as real foley in lossless WAV; no preview MP3s or game-UI packs on hero moments.
  - **The mix leaves space:** decide per scene whether music or sound effects lead; duck the music around hero hits; leave at least one real silence before the biggest reveal; print the mix for about 14–16 dB peak-to-loudness instead of limiting hard to −14 LUFS.
  - **A/B before sign-off:** measure the mix (loudness, peak-to-loudness, hit decay, energy above 10 kHz) and compare it with the brand middle half in `premium-sound.md`.
- [ ] **Principles check** (`principles.md`): name the constant (continuity), the one idea per beat (clarity), what was removed (restraint), the hero's contrast, the setup → payoff, and the 3–5 hits that must land on sound.
- [ ] **Originality:** each borrowed move has been changed by at least one remix operator (swap the actor, swap the scale, make it literal, reverse, constrain, combine, move the medium, give it a cost). Learn from references; do not copy them.
- [ ] **QA:** contact sheet and review grids viewed; no stacked motion-blur copies, no hard jumps at cuts, no blur across cuts.
- [ ] **Don't publish.** Hand concepts and renders to the owner. Never post or send them yourself.

## Lessons file template

Keep this next to the library, for example at `lessons/revisions.md`. Write the owner's note, what you built, and the reusable rule. Add new rounds at the bottom; do not rewrite old ones.

```markdown
# Revision lessons

Source: the owner's notes on [project], [date]. Read this before storyboarding or rendering. Each lesson gives the note, what was built, and the general rule to reuse.

## Lesson 0 (most important): cheap sound effects are the main tell of AI-made motion

- **Note:**
- **What we found:**
- **Rule:** treat sound design as craft, not sync. See `premium-sound.md`.

## 1. Title of the rule

- **Note:** (quote or summarise the owner)
- **Built:** (what changed in the film)
- **Rule:** (the reusable version)

## Open issues

1.

## Checklist additions

- [ ]
```
