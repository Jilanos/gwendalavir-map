#!/usr/bin/env python3
"""Renforcer prudemment l'opacité d'un masque d'encre canonique."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

from pipeline_utils import write_metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--alpha-gamma", type=float, default=0.82, help="< 1 renforce les traits partiellement opaques")
    parser.add_argument("--opacity", type=float, default=1.06)
    args = parser.parse_args()
    if not args.source.is_file():
        parser.error("source introuvable")
    if args.alpha_gamma <= 0 or args.opacity <= 0:
        parser.error("les facteurs doivent être positifs")
    output = args.output.resolve()
    layers_dir = (Path(__file__).resolve().parents[1] / "layers").resolve()
    try:
        output.relative_to(layers_dir)
    except ValueError:
        parser.error("la sortie doit être sous layers/")
    with Image.open(args.source) as source:
        image = source.convert("RGBA")
        alpha = image.getchannel("A").point(lambda value: min(255, round(((value / 255) ** args.alpha_gamma) * 255 * args.opacity)))
        refined = Image.new("RGBA", image.size, (0, 0, 0, 0))
        refined.putalpha(alpha)
        output.parent.mkdir(parents=True, exist_ok=True)
        refined.save(output)
    meta = write_metadata(output, source_path=args.source, script="scripts/refine_linework.py", parameters={"alpha_gamma": args.alpha_gamma, "opacity": args.opacity, "geometry": "unchanged_alpha_only"}, dimensions_before=image.size, dimensions_after=refined.size)
    print(f"Refined linework: {output}\nMetadata: {meta}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
