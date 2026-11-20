---
name: motion-library
description: >
  Use this when building or growing a library of motion-design techniques from
  real brand videos, when breaking down a motion reference shot by shot, or when
  turning that library into an original storyboard or concept for a brief. Do
  not use it to copy a reference.
---

# Motion library: learn why great motion works, then invent

The goal is not to copy reference videos. Learn why great motion works, then invent original moves that still clear that bar.

Load these files when you need them (paths are relative to this skill folder):

- `references/principles.md` — ten evidence-backed principles and the remix operators
- `references/technique-families.md` — families grouped by use (hook, feature, explainer, social proof, end card), with After Effects, Blender and code recipes
- `references/premium-sound.md` — what brand mixes measure like, and how to build premium sound
- `references/preflight-checklist.md` — rules and the checklist to run before every storyboard or render
- `references/breakdown-template.md` — the breakdown file format
- `scripts/fetch.sh`, `scripts/extract.sh`, `scripts/analyze_sound.py` — download, frame, and measure a source video

The owner's working library (videos, frames, breakdowns, lessons) is a separate folder. Pass it to the scripts with `--library` or the `MOTION_LIBRARY` environment variable. The default is `./motion-library`.

## A. Grow the library

1. **Pick sources.** Prefer official brand uploads (check the channel name; fan re-uploads are common) and the most-saved motion posts on X. Skip live action, talking heads, screen recordings and near-duplicates, and log each exclusion with a reason.
2. **Fetch and measure.** Use `scripts/fetch.sh` (yt-dlp, 480p or below, first 150 s of long videos). Then `scripts/extract.sh` for interval frames, scene-change frames, a timestamped 24-frame contact sheet, a cut count and EBU R128 loudness. Optionally run `scripts/analyze_sound.py` for tempo, onsets, and how often cuts land on sound hits compared with chance. Note the limits: cut detection misses fades and morphs, and silent clips report no loudness.
3. **Break down each video.** Follow `references/breakdown-template.md`: overall feel, a shot-by-shot table, why it works, sound, and a techniques table tagged by category and by use. Only claim what you saw or measured, and say when a claim is from frames rather than from listening.
4. **Rebuild the indexes.** Update the catalog and a machine-readable `techniques.tsv` (category, name, how, good_for, slug, timestamp, use, principle).
5. **Clean up disk.** Delete the raw videos once the frames and sheets exist. Keep each source URL in the breakdown so it can be re-fetched.

## B. The possibilities guide

Work from `references/principles.md` and `references/technique-families.md`. Start with the principles, then the remix operators, then technique cards grouped by use. Each card has recipes, public reference links, and invention prompts that push past the reference. Design sound with `references/premium-sound.md`: generic sound effects are the clearest tell of cheap or AI-made motion.

## C. Use it on a brief

For a product launch film, board it first with the companion skill `launch-storyboard`: brief and target customer, hook, retention arc, the product's real UI library found and downloaded online, then 4–6 frames. Then run the steps below on that board.

1. Name the use for each beat (hook, feature, explainer, social proof, end card).
2. Pick one or two technique families per beat, read why they work, then run the invention prompts and remix operators until you have a move none of the references made.
3. Storyboard each beat with timing, the visual, the motion move, on-screen text, and the sound cue. One idea per beat, one accent colour, a clear hero, a setup that pays off, and the 3–5 key actions that must land on a real sound.
4. Run the pre-flight checklist in `references/preflight-checklist.md` before every storyboard or render.
5. Keep a lessons file of the owner's revision notes, written as rules. Add each new round of feedback. A template is at the end of the checklist file.

Never post or publish anything. Hand concepts and renders to the owner for review. Only claim what was seen or measured.
