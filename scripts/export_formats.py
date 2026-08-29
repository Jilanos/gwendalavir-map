#!/usr/bin/env python3
"""Exporter une image vers JPEG, TIFF et HEIC sans modifier la source."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def flattened_rgb(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    background = Image.new("RGBA", rgba.size, "white")
    background.alpha_composite(rgba)
    return background.convert("RGB")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--jpeg-quality", type=int, default=95)
    parser.add_argument("--heic-quality", type=int, default=90)
    args = parser.parse_args()
    if not args.source.is_file():
        parser.error(f"fichier source introuvable : {args.source}")
    if not 1 <= args.jpeg_quality <= 100 or not 1 <= args.heic_quality <= 100:
        parser.error("les qualités doivent être comprises entre 1 et 100")
    try:
        import pillow_heif
    except ImportError:
        parser.error("pillow-heif est requis pour HEIC ; installez requirements.txt")
    pillow_heif.register_heif_opener()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = args.source.stem
    with Image.open(args.source) as source:
        rgb = flattened_rgb(source)
        dpi = source.info.get("dpi")
        options = {"dpi": dpi} if dpi else {}
        jpg = args.output_dir / f"{stem}.jpg"
        tif = args.output_dir / f"{stem}.tiff"
        heic = args.output_dir / f"{stem}.heic"
        rgb.save(jpg, quality=args.jpeg_quality, subsampling=0, **options)
        rgb.save(tif, compression="tiff_lzw", **options)
        rgb.save(heic, quality=args.heic_quality, **options)
    print(f"JPEG: {jpg}\nTIFF: {tif}\nHEIC: {heic}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
