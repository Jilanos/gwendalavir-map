#!/usr/bin/env python3
"""Inspecter une image ou toutes les images d'un dossier, sans les modifier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, UnidentifiedImageError

from pipeline_utils import ensure_working_output


def image_record(path: Path) -> dict[str, object]:
    """Extraire les propriétés utiles à la comparaison d'une image."""
    with Image.open(path) as image:
        width, height = image.size
        bits = image.info.get("bits")
        if bits is None and hasattr(image, "tag_v2"):
            bits = image.tag_v2.get(258)  # TIFF BitsPerSample
        return {
            "name": path.name, "path": str(path), "format": image.format,
            "width": width, "height": height, "ratio": width / height,
            "total_pixels": width * height, "dpi": image.info.get("dpi"),
            "color_mode": image.mode, "bit_depth": bits,
            "file_size_bytes": path.stat().st_size,
            "has_alpha": "A" in image.getbands() or "transparency" in image.info,
        }


def discover_images(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if not path.is_dir():
        raise FileNotFoundError(path)
    images: list[Path] = []
    for candidate in sorted(item for item in path.rglob("*") if item.is_file()):
        try:
            with Image.open(candidate):
                pass
        except UnidentifiedImageError:
            continue
        images.append(candidate)
    return images


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="image ou dossier à inspecter")
    parser.add_argument("--inventory", type=Path, default=Path("working/source_inventory.json"), help="inventaire JSON sous working/")
    args = parser.parse_args()
    try:
        output = ensure_working_output(args.inventory)
        files = discover_images(args.input)
    except (FileNotFoundError, ValueError) as error:
        parser.error(str(error))
    records = [image_record(path) for path in files]
    records.sort(key=lambda item: int(item["total_pixels"]), reverse=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as file:
        json.dump({"input": str(args.input), "images": records}, file, ensure_ascii=False, indent=2)
        file.write("\n")
    for record in records:
        print(f"{record['name']}: {record['width']}×{record['height']} px, {record['format']}, {record['color_mode']}, {record['total_pixels']} px")
    print(f"Inventaire : {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
