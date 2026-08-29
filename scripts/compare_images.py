#!/usr/bin/env python3
"""Créer une comparaison côte à côte, overlay ou différence de deux images."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops

from pipeline_utils import ensure_working_output, require_lossless_output, write_metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("first", type=Path)
    parser.add_argument("second", type=Path)
    parser.add_argument("--output", type=Path, required=True, help="sortie PNG/TIFF sous working/")
    parser.add_argument("--mode", choices=("side-by-side", "overlay", "difference"), default="side-by-side")
    parser.add_argument("--opacity", type=float, default=0.5, help="opacité de la seconde image pour overlay")
    args = parser.parse_args()
    if not args.first.is_file() or not args.second.is_file():
        parser.error("les deux images doivent exister")
    if not 0 <= args.opacity <= 1:
        parser.error("l'opacité doit être comprise entre 0 et 1")
    try:
        output = ensure_working_output(args.output)
        require_lossless_output(output)
        with Image.open(args.first) as first_source, Image.open(args.second) as second_source:
            first, second = first_source.convert("RGBA"), second_source.convert("RGBA")
            before = first.size
            if args.mode == "side-by-side":
                image = Image.new("RGBA", (first.width + second.width, max(first.height, second.height)))
                image.alpha_composite(first, (0, 0))
                image.alpha_composite(second, (first.width, 0))
            else:
                if first.size != second.size:
                    parser.error("overlay et difference exigent des dimensions identiques")
                image = Image.blend(first, second, args.opacity) if args.mode == "overlay" else ImageChops.difference(first, second)
            output.parent.mkdir(parents=True, exist_ok=True)
            options = {"compression": "tiff_lzw"} if output.suffix.lower() in {".tif", ".tiff"} else {}
            image.save(output, **options)
    except ValueError as error:
        parser.error(str(error))
    meta = write_metadata(output, source_path=args.first, script="scripts/compare_images.py", parameters={"mode": args.mode, "opacity": args.opacity}, dimensions_before=before, dimensions_after=image.size, additional_sources=[args.second])
    print(f"Comparaison exportée : {output}\nMétadonnées : {meta}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
