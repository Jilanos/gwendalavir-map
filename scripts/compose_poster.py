#!/usr/bin/env python3
"""Recomposer une affiche sans modifier la géométrie du masque d'encre."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

from pipeline_utils import write_metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--texture", type=Path, required=True, help="texture de fond décorative")
    parser.add_argument("--ink-mask", type=Path, required=True, help="masque d'encre canonique RGBA")
    parser.add_argument("--output", type=Path, required=True, help="PNG/TIFF sous final/")
    parser.add_argument("--ink-color", default="#3b2414", help="couleur hexadécimale de l'encre")
    parser.add_argument("--dpi", type=int, default=300)
    args = parser.parse_args()
    if not args.texture.is_file() or not args.ink_mask.is_file():
        parser.error("la texture et le masque d'encre doivent exister")
    output = args.output.resolve()
    final_dir = (Path(__file__).resolve().parents[1] / "final").resolve()
    try:
        output.relative_to(final_dir)
    except ValueError:
        parser.error("la sortie doit être située sous final/")
    if output.suffix.lower() not in {".png", ".tif", ".tiff"}:
        parser.error("la sortie doit être PNG ou TIFF")
    try:
        color = tuple(int(args.ink_color[index:index + 2], 16) for index in (1, 3, 5))
        if not args.ink_color.startswith("#") or len(args.ink_color) != 7:
            raise ValueError
    except ValueError:
        parser.error("ink-color doit utiliser le format #RRGGBB")
    with Image.open(args.ink_mask) as ink_source, Image.open(args.texture) as texture_source:
        ink = ink_source.convert("RGBA")
        texture = texture_source.convert("RGB").resize(ink.size, Image.Resampling.LANCZOS).convert("RGBA")
        colored_ink = Image.new("RGBA", ink.size, (*color, 0))
        colored_ink.putalpha(ink.getchannel("A"))
        texture.alpha_composite(colored_ink)
        output.parent.mkdir(parents=True, exist_ok=True)
        options: dict[str, object] = {"dpi": (args.dpi, args.dpi)}
        if output.suffix.lower() in {".tif", ".tiff"}:
            options["compression"] = "tiff_lzw"
        texture.convert("RGB").save(output, **options)
    meta = write_metadata(output, source_path=args.ink_mask, script="scripts/compose_poster.py", parameters={"ink_color": args.ink_color, "dpi": args.dpi, "texture_resampling": "lanczos"}, dimensions_before=ink.size, dimensions_after=texture.size, additional_sources=[args.texture])
    print(f"Poster base exported: {output}\nMetadata: {meta}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
