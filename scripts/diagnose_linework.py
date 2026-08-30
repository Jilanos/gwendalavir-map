#!/usr/bin/env python3
"""Créer une planche de diagnostics de lisibilité à partir d'un masque d'encre."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    if not args.source.is_file():
        parser.error("source introuvable")
    with Image.open(args.source) as source:
        alpha = source.convert("RGBA").getchannel("A")
        width, height = alpha.size
        regions = {
            "north_east_dense": (int(width * .67), 0, width, int(height * .42)),
            "south_dense": (0, int(height * .52), int(width * .48), height),
            "central_reference": (int(width * .33), int(height * .26), int(width * .67), int(height * .70)),
        }
        cells = []
        metrics = []
        for name, box in regions.items():
            crop = alpha.crop(box)
            density = sum(1 for value in crop.resize((300, 300)).getdata() if value > 30) / 90000
            preview = Image.new("RGB", crop.size, "white")
            preview.paste("black", mask=crop)
            preview.thumbnail((900, 700), Image.Resampling.LANCZOS)
            canvas = Image.new("RGB", (900, 750), "#f4f0e5")
            canvas.paste(preview, (0, 40))
            ImageDraw.Draw(canvas).text((15, 12), f"{name} — ink coverage {density:.1%}", fill="#20170f")
            cells.append(canvas)
            metrics.append({"name": name, "box_pixels": box, "ink_coverage": density})
        sheet = Image.new("RGB", (900, 750 * len(cells)), "white")
        for index, cell in enumerate(cells): sheet.paste(cell, (0, index * 750))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        sheet.save(args.output)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps({"source": str(args.source), "regions": metrics}, indent=2) + "\n", encoding="utf-8")
    print(f"Diagnostics: {args.output}\nReport: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
