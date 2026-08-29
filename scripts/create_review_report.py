#!/usr/bin/env python3
"""Créer un rapport HTML autonome de revue des images intermédiaires."""

from __future__ import annotations

import argparse
import base64
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path

from PIL import Image


def embedded_preview(path: Path, maximum_width: int = 1200) -> tuple[str, tuple[int, int]]:
    """Créer un aperçu PNG embarqué sans modifier le fichier inspecté."""
    with Image.open(path) as source:
        image = source.convert("RGBA")
        canvas = Image.new("RGBA", image.size, "white")
        canvas.alpha_composite(image)
        image = canvas.convert("RGB")
        original_size = image.size
        image.thumbnail((maximum_width, maximum_width * 2), Image.Resampling.LANCZOS)
        buffer = BytesIO()
        image.save(buffer, format="PNG", optimize=True)
    return base64.b64encode(buffer.getvalue()).decode("ascii"), original_size


def figure(title: str, description: str, path: Path) -> str:
    encoded, (width, height) = embedded_preview(path)
    size_mb = path.stat().st_size / (1024 * 1024)
    return f"""
    <section class=\"artifact\">
      <h2>{title}</h2>
      <p>{description}</p>
      <p class=\"metadata\"><code>{path}</code> — {width} × {height} px — {size_mb:.2f} MiB</p>
      <img src=\"data:image/png;base64,{encoded}\" alt=\"{title}\">
    </section>"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--prepared", type=Path, required=True)
    parser.add_argument("--difference", type=Path, required=True)
    parser.add_argument("--master", type=Path, required=True)
    parser.add_argument("--ink-mask", type=Path, help="masque d'encre optionnel à intégrer au rapport")
    parser.add_argument("--output", type=Path, required=True, help="rapport HTML à écrire sous docs/")
    args = parser.parse_args()
    artifacts = tuple(path for path in (args.source, args.prepared, args.difference, args.master, args.ink_mask) if path)
    if not all(path.is_file() for path in artifacts):
        parser.error("tous les artefacts d'entrée doivent exister")
    output = args.output.resolve()
    docs_dir = (Path(__file__).resolve().parents[1] / "docs").resolve()
    try:
        output.relative_to(docs_dir)
    except ValueError:
        parser.error("la sortie du rapport doit être située sous docs/")
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    section_list = [
        figure("1. Original reference", "Official geometric reference, preserved read-only.", args.source),
        figure("2. Prepared reference", "Deterministic grayscale conversion with contrast 1.05; no crop, rotation, denoising, or generative processing.", args.prepared),
        figure("3. Pixel difference", "Difference between the original and the prepared reference. Bright areas show only the explicit grayscale/contrast change.", args.difference),
        figure("4. Master map", "8× Lanczos interpolation of the prepared map: 8,000 px wide, no synthetic details.", args.master),
    ]
    if args.ink_mask:
        section_list.append(figure("5. Canonical ink mask", "Transparent black ink derived directly from the master map at threshold 230. It preserves every detected source mark and does not classify or redraw geography.", args.ink_mask))
    sections = "\n".join(section_list)
    html = f"""<!doctype html>
<html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Map pipeline review</title><style>
body {{ max-width: 1120px; margin: 0 auto; padding: 2rem; color: #1d2524; background: #f5f1e6; font: 16px/1.5 system-ui, sans-serif; }}
h1,h2 {{ font-family: Georgia, serif; }} .lead {{ font-size: 1.15rem; }} .artifact {{ margin: 2.5rem 0; padding: 1.25rem; background: #fffdf7; border: 1px solid #d9d1c0; border-radius: 8px; }}
img {{ width: 100%; height: auto; border: 1px solid #bdb4a1; background: white; }} .metadata {{ color: #5f625a; font-size: .9rem; }} code {{ overflow-wrap: anywhere; }}
</style></head><body><h1>Faithful map pipeline — review</h1>
<p class=\"lead\">Generated {generated_at}. This report embeds previews for review; source geometry has not been altered.</p>
<h2>Review guidance</h2><ul><li>Confirm that coastlines, rivers, relief, symbols, and relative positions remain identical.</li><li>Use the difference image to decide whether the preparation settings should be reduced or adjusted.</li><li>Approve the master map before extracting layers or introducing any artistic styling.</li></ul>
{sections}</body></html>"""
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
    print(f"Review report written: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
