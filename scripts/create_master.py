#!/usr/bin/env python3
"""Créer une master map sans transformation générative."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_crop(value: str) -> tuple[int, int, int, int]:
    try:
        coordinates = tuple(int(part.strip()) for part in value.split(","))
    except ValueError as error:
        raise argparse.ArgumentTypeError("crop attendu : left,top,right,bottom") from error
    if len(coordinates) != 4:
        raise argparse.ArgumentTypeError("crop attendu : left,top,right,bottom")
    left, top, right, bottom = coordinates
    if right <= left or bottom <= top:
        raise argparse.ArgumentTypeError("le crop doit avoir une surface positive")
    return coordinates


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="image source immuable à lire")
    parser.add_argument("output", type=Path, help="master map à exporter (.png ou .tif/.tiff)")
    parser.add_argument("--rotate", type=float, default=0.0, help="rotation déterministe en degrés")
    parser.add_argument("--crop", type=parse_crop, metavar="L,T,R,B", help="recadrage en pixels")
    parser.add_argument("--dpi", type=float, help="DPI à inscrire dans le fichier exporté")
    args = parser.parse_args()

    if not args.source.is_file():
        parser.error(f"fichier source introuvable : {args.source}")
    if args.output.suffix.lower() not in {".png", ".tif", ".tiff"}:
        parser.error("la sortie doit être au format PNG, TIFF ou TIF")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(args.source) as source:
        image = source.copy()
        if args.rotate:
            image = image.rotate(args.rotate, expand=True, resample=Image.Resampling.BICUBIC)
        if args.crop:
            image = image.crop(args.crop)

        save_options: dict[str, object] = {}
        dpi = args.dpi or source.info.get("dpi")
        if dpi:
            save_options["dpi"] = (dpi, dpi) if isinstance(dpi, (int, float)) else dpi
        if args.output.suffix.lower() in {".tif", ".tiff"}:
            save_options["compression"] = "tiff_lzw"
        image.save(args.output, **save_options)

    print(f"Master map exportée : {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
