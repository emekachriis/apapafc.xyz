#!/usr/bin/env bash
# Extract study frames and measurements from a library video.
# usage: extract.sh [--library DIR] <slug>
# Env: MOTION_LIBRARY (default: ./motion-library)
#
# Reads videos/<slug>.mp4 and writes:
#   frames/<slug>/interval/   timestamped frames (every 1s if duration <= 60s, else 2s)
#   frames/<slug>/scene/      scene-change frames (ffmpeg scene > 0.25) plus times.txt
#   frames/<slug>/review_NN.jpg  timestamped 5x4 review grids
#   sheets/<slug>.jpg         24-frame timestamped contact sheet (6x4)
#   frames/<slug>/stats.json  duration, resolution, cut count, cuts/10s, EBU R128 LUFS, mean luma

set -euo pipefail

library="${MOTION_LIBRARY:-./motion-library}"
while [[ $# -gt 0 ]]; do
  case "$1" in
    -L|--library)
      library="$2"
      shift 2
      ;;
    -h|--help)
      echo "usage: extract.sh [--library DIR] <slug>"
      exit 0
      ;;
    --)
      shift
      break
      ;;
    -*)
      echo "unknown option: $1" >&2
      exit 2
      ;;
    *)
      break
      ;;
  esac
done

slug="${1:-}"
if [[ -z "$slug" ]]; then
  echo "usage: extract.sh [--library DIR] <slug>" >&2
  exit 2
fi
if [[ "$slug" == *'/'* || "$slug" == *'..'* ]]; then
  echo "slug must be a single path segment" >&2
  exit 2
fi

if [[ ! -d "$library" ]]; then
  echo "library not found: $library" >&2
  exit 1
fi
library="$(cd "$library" && pwd)"

video="$library/videos/$slug.mp4"
if [[ ! -s "$video" ]]; then
  echo "missing video: $video" >&2
  exit 1
fi

for cmd in ffmpeg ffprobe python3; do
  if ! command -v "$cmd" >/dev/null; then
    echo "$cmd is not installed" >&2
    exit 1
  fi
done

out="$library/frames/$slug"
mkdir -p "$out/interval" "$out/scene" "$library/sheets"
rm -f "$out/interval/"* "$out/scene/"* "$out"/review_*.jpg

duration="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$video")"
interval="$(python3 -c "print(1 if float('$duration') <= 60 else 2)")"

ffmpeg -v error -y -i "$video" -vf "fps=1/${interval},scale=480:-2" -q:v 4 "$out/interval/t_%04d.jpg"
i=0
# Sort so numbering stays in order even if the glob is unsorted.
shopt -s nullglob
for f in $(ls "$out"/interval/t_*.jpg); do
  t="$(python3 -c "print(f'{$i * $interval:06.2f}')")"
  mv "$f" "$out/interval/f_${t}s.jpg"
  i=$((i + 1))
done
shopt -u nullglob

# Scene-change frames. -vsync vfr still works; -fps_mode vfr is the newer name.
ffmpeg -v info -y -i "$video" \
  -vf "select='gt(scene,0.25)',showinfo,scale=480:-2" \
  -fps_mode vfr -q:v 4 "$out/scene/s_%04d.jpg" 2>&1 \
  | grep -o 'pts_time:[0-9.]*' | cut -d: -f2 > "$out/scene/times.txt" || true

n=1
while IFS= read -r t; do
  [[ -z "$t" ]] && continue
  src="$(printf '%s/scene/s_%04d.jpg' "$out" "$n")"
  if [[ -f "$src" ]]; then
    dest="$(python3 -c "print('scene_{:06.2f}s.jpg'.format(float('$t')))")"
    mv "$src" "$out/scene/$dest"
  fi
  n=$((n + 1))
done < "$out/scene/times.txt"

# Font for burned-in timestamps: use a known file if ffmpeg's default is missing.
font_opt=()
for font in \
  /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf \
  /usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf \
  /usr/share/fonts/TTF/DejaVuSans.ttf; do
  if [[ -f "$font" ]]; then
    font_opt=(fontfile="$font")
    break
  fi
done
font_prefix=""
if [[ ${#font_opt[@]} -gt 0 ]]; then
  font_prefix="${font_opt[0]}:"
fi

ffmpeg -v error -y -i "$video" \
  -vf "fps=1/${interval},scale=384:-2,drawtext=${font_prefix}text='%{pts\:hms}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.7,tile=5x4" \
  -q:v 4 "$out/review_%02d.jpg"

ffmpeg -v error -y -i "$video" \
  -vf "fps=24/${duration},scale=320:-2,drawtext=${font_prefix}text='%{pts\:hms}':x=4:y=4:fontsize=16:fontcolor=white:box=1:boxcolor=black@0.6,tile=6x4:padding=4:color=black" \
  -frames:v 1 -q:v 3 "$library/sheets/${slug}.jpg"

lufs="$(ffmpeg -nostats -i "$video" -af ebur128 -f null - 2>&1 \
  | grep -A1 'Integrated loudness' | grep -o 'I:.*LUFS' | tr -s ' ' | cut -d' ' -f2 || true)"
luma="$(ffmpeg -v info -i "$video" \
  -vf "fps=1,scale=64:-2,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep -o 'YAVG=[0-9.]*' | cut -d= -f2 \
  | awk '{s+=$1;n++} END{if(n) printf "%.0f", s/n}')"
res="$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$video")"
cuts="$(grep -c . "$out/scene/times.txt" 2>/dev/null || echo 0)"

python3 - "$out/stats.json" << PY
import json, sys
d = float("$duration")
c = int("$cuts")
path = sys.argv[1]
json.dump(
    dict(
        slug="$slug",
        duration_s=round(d, 1),
        res="$res",
        interval_s=$interval,
        scene_cuts=c,
        cuts_per_10s=round(c / d * 10, 1) if d else None,
        lufs="${lufs:-none}",
        mean_luma="${luma}",
    ),
    open(path, "w"),
)
print(open(path).read())
PY
