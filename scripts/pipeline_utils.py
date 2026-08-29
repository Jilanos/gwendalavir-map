"""Utilitaires déterministes partagés par le pipeline d'ingestion."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
WORKING_DIR = (PROJECT_ROOT / "working").resolve()
SOURCE_DIR = (PROJECT_ROOT / "source").resolve()
LOSSLESS_SUFFIXES = {".png", ".tif", ".tiff"}


def sha256_file(path: Path) -> str:
    """Retourner le SHA256 d'un fichier sans le modifier."""
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
    except ValueError:
        return False
    return True


def ensure_working_output(path: Path) -> Path:
    """Valider qu'une sortie est strictement située sous ``working/``."""
    resolved = path.resolve()
    if not is_within(resolved, WORKING_DIR):
        raise ValueError(f"la sortie doit être située dans {WORKING_DIR}")
    if is_within(resolved, SOURCE_DIR):
        raise ValueError("une source ne peut jamais être écrasée")
    return resolved


def require_lossless_output(path: Path) -> None:
    if path.suffix.lower() not in LOSSLESS_SUFFIXES:
        raise ValueError("la sortie doit être au format PNG, TIFF ou TIF")


def normalized_from_pixels(x: float, y: float, width: int, height: int) -> tuple[float, float]:
    """Convertir des pixels en coordonnées normalisées, origine en haut à gauche."""
    if width <= 0 or height <= 0:
        raise ValueError("les dimensions doivent être strictement positives")
    return x / width, y / height


def pixels_from_normalized(x: float, y: float, width: int, height: int) -> tuple[float, float]:
    """Convertir des coordonnées normalisées en pixels."""
    if width <= 0 or height <= 0:
        raise ValueError("les dimensions doivent être strictement positives")
    if not 0 <= x <= 1 or not 0 <= y <= 1:
        raise ValueError("les coordonnées normalisées doivent appartenir à [0, 1]")
    return x * width, y * height


def metadata_path(image_path: Path) -> Path:
    return image_path.with_name(f"{image_path.name}.meta.json")


def write_metadata(output_path: Path, *, source_path: Path, script: str, parameters: dict[str, Any], dimensions_before: tuple[int, int], dimensions_after: tuple[int, int], additional_sources: list[Path] | None = None) -> Path:
    """Écrire les métadonnées associées à une image générée."""
    meta_path = metadata_path(output_path)
    data: dict[str, Any] = {
        "source_file": str(source_path), "script": script, "parameters": parameters,
        "dimensions_before": {"width": dimensions_before[0], "height": dimensions_before[1]},
        "dimensions_after": {"width": dimensions_after[0], "height": dimensions_after[1]},
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_sha256": sha256_file(source_path), "generated_sha256": sha256_file(output_path),
    }
    if additional_sources:
        data["additional_sources"] = [{"file": str(path), "sha256": sha256_file(path)} for path in additional_sources]
    with meta_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")
    return meta_path
