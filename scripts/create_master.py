#!/usr/bin/env python3
"""Créer une master map par interpolation classique, sans ajout de détail."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

from pipeline_utils import ensure_working_output, require_lossless_output, write_metadata

INTERPOLATIONS = {"nearest": Image.Resampling.NEAREST, "bilinear": Image.Resampling.BILINEAR, "bicubic": Image.Resampling.BICUBIC, "lanczos": Image.Resampling.LANCZOS}


def scaled_size(size: tuple[int, int], scale: int) -> tuple[int, int]:
    if scale <= 0:
        raise ValueError("le facteur d'agrandissement doit être strictement positif")
    return size[0] * scale, size[1] * scale


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="image préparée à lire")
    parser.add_argument("--output", type=Path, required=True, help="sortie PNG/TIFF sous working/")
    parser.add_argument("--scale", type=int, default=1, help="facteur entier d'agrandissement (défaut : 1)")
    parser.add_argument("--interpolation", choices=INTERPOLATIONS, default="lanczos")
    parser.add_argument("--dpi", type=float, help="DPI à inscrire dans l'export")
    args = parser.parse_args()
    if not args.source.is_file():
        parser.error(f"fichier source introuvable : {args.source}")
    try:
        output = ensure_working_output(args.output)
        require_lossless_output(output)
        with Image.open(args.source) as source:
            before, after = source.size, scaled_size(source.size, args.scale)
            image = source.copy() if after == before else source.resize(after, INTERPOLATIONS[args.interpolation])
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
    meta = write_metadata(output, source_path=args.source, script="scripts/create_master.py", parameters={"scale": args.scale, "interpolation": args.interpolation, "dpi": args.dpi}, dimensions_before=before, dimensions_after=after)
    print(f"Master map exportée : {output}\nMétadonnées : {meta}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
