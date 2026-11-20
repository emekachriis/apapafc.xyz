#!/usr/bin/env python3
"""Measure tempo, onsets, and cut-to-onset alignment for a library video.

usage: analyze_sound.py [--library DIR] <slug>

Reads videos/<slug>.mp4 and frames/<slug>/scene/times.txt (from extract.sh).
Writes frames/<slug>/sound.json.

Requires ffmpeg, numpy and librosa. Sound is measured, not listened to.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-L", "--library", default=os.environ.get("MOTION_LIBRARY", "./motion-library"))
    parser.add_argument("slug")
    args = parser.parse_args()

    if "/" in args.slug or ".." in args.slug:
        print("slug must be a single path segment", file=sys.stderr)
        return 2

    library = Path(args.library).resolve()
    video = library / "videos" / f"{args.slug}.mp4"
    out_dir = library / "frames" / args.slug
    times_path = out_dir / "scene" / "times.txt"
    if not video.is_file():
        print(f"missing video: {video}", file=sys.stderr)
        return 1

    try:
        import numpy as np
        import librosa
    except ImportError:
        print("analyze_sound.py needs numpy and librosa (pip install -r requirements.txt)", file=sys.stderr)
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    result = {"slug": args.slug}

    with tempfile.TemporaryDirectory(prefix="motion-library-sound-") as tmp:
        wav = Path(tmp) / f"{args.slug}.wav"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vn", "-ac", "1", "-ar", "22050", str(wav)],
            check=False,
        )
        if not wav.is_file() or wav.stat().st_size < 10000:
            result["audio"] = "none"
        else:
            y, sr = librosa.load(str(wav), sr=22050)
            oenv = librosa.onset.onset_strength(y=y, sr=sr)
            tempo = float(np.atleast_1d(librosa.feature.tempo(onset_envelope=oenv, sr=sr, aggregate=np.median))[0])
            onsets = librosa.onset.onset_detect(onset_envelope=oenv, sr=sr, units="time")
            cuts = []
            if times_path.is_file():
                cuts = [float(x) for x in times_path.read_text().split() if x.strip()]
            dur = len(y) / sr
            hit = 0
            if len(onsets) and cuts:
                hit = sum(1 for c in cuts if np.min(np.abs(onsets - c)) <= 0.07)
            chance = 0.0
            if len(onsets):
                grid = np.arange(0, dur, 0.01)
                chance = float(np.mean([np.min(np.abs(onsets - g)) <= 0.07 for g in grid]))
            _h, p = librosa.effects.hpss(y)
            perc = float(np.sum(p**2) / (np.sum(_h**2) + np.sum(p**2) + 1e-9))
            rms = librosa.feature.rms(y=y)[0]
            rdb = 20 * np.log10(rms + 1e-9)
            ref = np.percentile(rdb, 90)
            quiet = float(np.mean(rdb < ref - 20))
            result.update(
                audio="yes",
                tempo_bpm=round(tempo, 1),
                onsets_per_s=round(len(onsets) / dur, 2) if dur else None,
                cuts=len(cuts),
                cuts_on_onset=hit,
                cut_onset_share=round(hit / len(cuts), 2) if cuts else None,
                chance_share=round(chance, 2),
                percussive_share=round(perc, 2),
                quiet_share=round(quiet, 2),
            )

    dest = out_dir / "sound.json"
    dest.write_text(json.dumps(result))
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
