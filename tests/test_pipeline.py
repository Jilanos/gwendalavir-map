import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from create_master import scaled_size
from pipeline_utils import (
    PROJECT_ROOT,
    ensure_working_output,
    normalized_from_pixels,
    pixels_from_normalized,
    sha256_file,
    write_metadata,
)


def test_scale_preserves_ratio_for_integer_factor() -> None:
    assert scaled_size((1000, 765), 4) == (4000, 3060)


def test_normalized_coordinate_round_trip() -> None:
    normalized = normalized_from_pixels(500, 382.5, 1000, 765)
    assert normalized == (0.5, 0.5)
    assert pixels_from_normalized(*normalized, 1000, 765) == (500, 382.5)


def test_source_cannot_be_an_output() -> None:
    with pytest.raises(ValueError):
        ensure_working_output(PROJECT_ROOT / "source" / "original" / "forbidden.png")


def test_metadata_contains_hashes_and_dimensions(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    output = tmp_path / "output.png"
    source.write_bytes(b"source-bytes")
    output.write_bytes(b"generated-bytes")
    meta_path = write_metadata(
        output,
        source_path=source,
        script="scripts/example.py",
        parameters={"scale": 2},
        dimensions_before=(10, 5),
        dimensions_after=(20, 10),
    )
    metadata = json.loads(meta_path.read_text(encoding="utf-8"))
    assert metadata["source_sha256"] == sha256_file(source)
    assert metadata["generated_sha256"] == sha256_file(output)
    assert metadata["dimensions_after"] == {"width": 20, "height": 10}
