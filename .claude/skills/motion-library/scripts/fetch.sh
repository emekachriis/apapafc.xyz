#!/usr/bin/env bash
# Download a source video into a motion library.
# usage: fetch.sh [--library DIR] <slug> <url>
# Env: MOTION_LIBRARY (default: ./motion-library)
# yt-dlp at 480p or below, first 150 seconds only. Writes videos/<slug>.mp4
# and info/<slug>.info.json (or similar) from yt-dlp.

set -euo pipefail

library="${MOTION_LIBRARY:-./motion-library}"
while [[ $# -gt 0 ]]; do
  case "$1" in
    -L|--library)
      library="$2"
      shift 2
      ;;
    -h|--help)
      echo "usage: fetch.sh [--library DIR] <slug> <url>"
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
url="${2:-}"
if [[ -z "$slug" || -z "$url" ]]; then
  echo "usage: fetch.sh [--library DIR] <slug> <url>" >&2
  exit 2
fi
if [[ "$slug" == *'/'* || "$slug" == *'..'* ]]; then
  echo "slug must be a single path segment" >&2
  exit 2
fi

mkdir -p "$library/videos" "$library/info"
# Resolve after mkdir so a new library path works.
library="$(cd "$library" && pwd)"
out="$library/videos/$slug.mp4"
if [[ -s "$out" ]]; then
  echo "already exists: $out"
  exit 0
fi

if ! command -v yt-dlp >/dev/null; then
  echo "yt-dlp is not installed" >&2
  exit 1
fi

yt_opts=(
  --no-warnings
  -f "bv*[height<=480][ext=mp4]+ba[ext=m4a]/bv*[height<=480]+ba/b[height<=480]/b"
  --download-sections "*0-150"
  --merge-output-format mp4
  -o "$library/videos/$slug.%(ext)s"
  --write-info-json
  --no-write-comments
  --output "infojson:$library/info/$slug"
)
if command -v node >/dev/null; then
  yt_opts+=(--js-runtimes node)
fi

err="$library/info/$slug.err"
set +e
if command -v timeout >/dev/null; then
  timeout 400 yt-dlp -q "${yt_opts[@]}" "$url" 2>"$err"
  status=$?
else
  yt-dlp -q "${yt_opts[@]}" "$url" 2>"$err"
  status=$?
fi
set -e

# yt-dlp may write .mp4 or need a rename if the merge used another ext.
if [[ ! -s "$out" ]]; then
  found="$(ls -1 "$library/videos/$slug".* 2>/dev/null | head -n 1 || true)"
  if [[ -n "${found:-}" && "$found" != "$out" ]]; then
    ffmpeg -v error -y -i "$found" -c copy "$out" && rm -f "$found"
  fi
fi

if [[ -s "$out" ]]; then
  rm -f "$err"
  echo "OK $slug -> $out"
  exit 0
fi

echo "FAIL $slug $(tail -n 1 "$err" 2>/dev/null || echo "download failed, exit $status")" >&2
exit "${status:-1}"
