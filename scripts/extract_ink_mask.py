#!/usr/bin/env python3
"""Extraire un masque d'encre transparent sans modifier la géométrie raster."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

from pipeline_utils import write_metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="master map ou référence en niveaux de gris")
    parser.add_argument("--output", type=Path, required=True, help="masque PNG sous layers/")
    parser.add_argument("--threshold", type=int, default=230, help="blanc à rendre transparent, entre 1 et 255")
    args = parser.parse_args()
    if not args.source.is_file():
        parser.error(f"fichier source introuvable : {args.source}")
    if not 1 <= args.threshold <= 255:
        parser.error("le seuil doit être compris entre 1 et 255")
    output = args.output.resolve()
    layers_dir = (Path(__file__).resolve().parents[1] / "layers").resolve()
    try:
        output.relative_to(layers_dir)
    except ValueError:
        parser.error("la sortie doit être située sous layers/")
    if output.suffix.lower() != ".png":
        parser.error("le masque doit être exporté au format PNG")

    with Image.open(args.source) as source:
        before = source.size
        grayscale = source.convert("L")
        alpha = grayscale.point(lambda value: 0 if value >= args.threshold else round((args.threshold - value) * 255 / args.threshold))
        ink = Image.new("RGBA", grayscale.size, (0, 0, 0, 0))
        ink.putalpha(alpha)
        output.parent.mkdir(parents=True, exist_ok=True)
        ink.save(output)
    meta = write_metadata(
        output,
        source_path=args.source,
        script="scripts/extract_ink_mask.py",
        parameters={"threshold": args.threshold, "method": "grayscale_to_transparent_black_alpha"},
        dimensions_before=before,
        dimensions_after=ink.size,
    )
    print(f"Ink mask exported: {output}\nMetadata: {meta}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
