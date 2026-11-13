"""Make web-sized copies of club photos (originals are never touched).

Usage (from the repo root, needs Pillow: pip install pillow):
    python3 tools/optimise_photos.py player images/NEWGUY.jpg      -> images/players/newguy.jpg
    python3 tools/optimise_photos.py photo  images/match9.jpg      -> images/photos/match9.jpg
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

def player(src: Path) -> Path:
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    w, h = im.size
    # 4:5 portrait crop, keep the top of the frame (faces sit high in our shots)
    tw = min(w, int(h * 4 / 5)); th = int(tw * 5 / 4)
    left = (w - tw) // 2
    im = im.crop((left, 0, left + tw, th)).resize((640, 800), Image.LANCZOS)
    out = Path("images/players") / (src.stem.lower() + ".jpg")
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=80, optimize=True, progressive=True)
    return out

def photo(src: Path) -> Path:
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    im.thumbnail((1600, 1600), Image.LANCZOS)
    out = Path("images/photos") / (src.stem.lower() + ".jpg")
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=74, optimize=True, progressive=True)
    return out

if __name__ == "__main__":
    kind, *files = sys.argv[1:]
    fn = {"player": player, "photo": photo}[kind]
    for f in files:
        out = fn(Path(f))
        print(f"{f} -> {out} ({out.stat().st_size // 1024} KB)")
