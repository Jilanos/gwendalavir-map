#!/usr/bin/env python3
"""Afficher les propriétés principales d'une image."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def format_dpi(dpi: object) -> str:
    if not dpi:
        return "non disponible"
    if isinstance(dpi, tuple):
        return " × ".join(f"{value:g}" for value in dpi)
    return str(dpi)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="chemin vers l'image à inspecter")
    args = parser.parse_args()

    if not args.image.is_file():
        parser.error(f"fichier introuvable : {args.image}")

    with Image.open(args.image) as image:
        width, height = image.size
        print(f"Chemin : {args.image}")
        print(f"Dimensions : {width} × {height} px")
        print(f"Ratio : {width / height:.6f} ({width}:{height})")
        print(f"Mode colorimétrique : {image.mode}")
        print(f"DPI : {format_dpi(image.info.get('dpi'))}")
        print(f"Format : {image.format or 'inconnu'}")
    print(f"Taille du fichier : {args.image.stat().st_size} octets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
