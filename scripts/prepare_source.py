#!/usr/bin/env python3
"""Préparer une source avec des opérations explicites et déterministes."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

from pipeline_utils import ensure_working_output, require_lossless_output, write_metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="source immuable à lire")
    parser.add_argument("--output", type=Path, required=True, help="sortie PNG/TIFF sous working/")
    parser.add_argument("--rotate", type=float, default=0.0, help="rotation en degrés")
    parser.add_argument("--crop", type=int, nargs=4, metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"))
    parser.add_argument("--grayscale", action="store_true", help="convertir en niveaux de gris")
    parser.add_argument("--contrast", type=float, default=1.0, help="facteur de contraste (1 = inchangé)")
    parser.add_argument("--brightness", type=float, default=1.0, help="facteur de luminosité (1 = inchangé)")
    parser.add_argument("--denoise", action="store_true", help="filtre médian 3×3 très modéré")
    parser.add_argument("--dpi", type=float, help="DPI à inscrire dans l'export")
    args = parser.parse_args()
    if not args.source.is_file():
        parser.error(f"fichier source introuvable : {args.source}")
    if args.contrast <= 0 or args.brightness <= 0:
        parser.error("les facteurs de contraste et de luminosité doivent être positifs")
    try:
        output = ensure_working_output(args.output)
        require_lossless_output(output)
        with Image.open(args.source) as source:
            before, image = source.size, source.copy()
            if args.rotate:
                image = image.rotate(args.rotate, expand=True, resample=Image.Resampling.BICUBIC)
            if args.crop:
                left, top, right, bottom = args.crop
                if not (0 <= left < right <= image.width and 0 <= top < bottom <= image.height):
                    parser.error("le crop doit être entièrement inclus dans l'image courante")
                image = image.crop(tuple(args.crop))
            if args.grayscale:
                image = ImageOps.grayscale(image)
            if args.contrast != 1.0:
                image = ImageEnhance.Contrast(image).enhance(args.contrast)
            if args.brightness != 1.0:
                image = ImageEnhance.Brightness(image).enhance(args.brightness)
            if args.denoise:
                image = image.filter(ImageFilter.MedianFilter(size=3))
            after = image.size
            options: dict[str, object] = {}
            dpi = args.dpi or source.info.get("dpi")
            if dpi:
                options["dpi"] = (dpi, dpi) if isinstance(dpi, (int, float)) else dpi
            if output.suffix.lower() in {".tif", ".tiff"}:
                options["compression"] = "tiff_lzw"
            output.parent.mkdir(parents=True, exist_ok=True)
            image.save(output, **options)
    except ValueError as error:
        parser.error(str(error))
    parameters = {key: value for key, value in vars(args).items() if key not in {"source", "output"}}
    meta = write_metadata(output, source_path=args.source, script="scripts/prepare_source.py", parameters=parameters, dimensions_before=before, dimensions_after=after)
    print(f"Source préparée : {output}\nMétadonnées : {meta}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
