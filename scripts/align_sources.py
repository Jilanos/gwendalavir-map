#!/usr/bin/env python3
"""Aligner une image sur une référence avec OpenCV, sans fusion automatique."""

from __future__ import annotations

import argparse
from pathlib import Path

from pipeline_utils import ensure_working_output, require_lossless_output, write_metadata


def comparison(cv2: object, reference: object, aligned: object, mode: str, opacity: float) -> object:
    if mode == "overlay":
        return cv2.addWeighted(reference, 1 - opacity, aligned, opacity, 0)
    return cv2.absdiff(reference, aligned)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path, help="image qui définit le repère cible")
    parser.add_argument("moving", type=Path, help="image à aligner")
    parser.add_argument("--output", type=Path, required=True, help="sortie PNG/TIFF sous working/")
    parser.add_argument("--model", choices=("affine", "homography"), default="homography")
    parser.add_argument("--comparison", type=Path, help="overlay/diff inspectable sous working/")
    parser.add_argument("--comparison-mode", choices=("overlay", "difference"), default="overlay")
    parser.add_argument("--opacity", type=float, default=0.5)
    parser.add_argument("--max-features", type=int, default=5000)
    args = parser.parse_args()
    try:
        import cv2
        import numpy as np
    except ImportError:
        parser.error("OpenCV et NumPy sont requis ; installez requirements.txt")
    if not args.reference.is_file() or not args.moving.is_file():
        parser.error("la référence et l'image mobile doivent exister")
    if not 0 <= args.opacity <= 1 or args.max_features < 4:
        parser.error("opacité invalide ou nombre de points insuffisant")
    try:
        output = ensure_working_output(args.output)
        require_lossless_output(output)
        comparison_output = ensure_working_output(args.comparison) if args.comparison else None
        if comparison_output:
            require_lossless_output(comparison_output)
    except ValueError as error:
        parser.error(str(error))
    reference = cv2.imread(str(args.reference), cv2.IMREAD_COLOR)
    moving = cv2.imread(str(args.moving), cv2.IMREAD_COLOR)
    if reference is None or moving is None:
        parser.error("OpenCV ne peut pas lire une des images")
    detector = cv2.ORB_create(nfeatures=args.max_features)
    ref_points, ref_desc = detector.detectAndCompute(cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY), None)
    mov_points, mov_desc = detector.detectAndCompute(cv2.cvtColor(moving, cv2.COLOR_BGR2GRAY), None)
    if ref_desc is None or mov_desc is None:
        parser.error("points caractéristiques insuffisants")
    matches = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(mov_desc, ref_desc), key=lambda match: match.distance)
    if len(matches) < 4:
        parser.error("moins de quatre correspondances fiables")
    selected = matches[: min(100, len(matches))]
    source_points = np.float32([mov_points[m.queryIdx].pt for m in selected]).reshape(-1, 1, 2)
    target_points = np.float32([ref_points[m.trainIdx].pt for m in selected]).reshape(-1, 1, 2)
    if args.model == "affine":
        matrix, _ = cv2.estimateAffinePartial2D(source_points, target_points, method=cv2.RANSAC)
        if matrix is None:
            parser.error("estimation affine impossible")
        aligned = cv2.warpAffine(moving, matrix, (reference.shape[1], reference.shape[0]))
        transform = matrix.tolist()
    else:
        matrix, _ = cv2.findHomography(source_points, target_points, cv2.RANSAC)
        if matrix is None:
            parser.error("estimation homographique impossible")
        aligned = cv2.warpPerspective(moving, matrix, (reference.shape[1], reference.shape[0]))
        transform = matrix.tolist()
    output.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(output), aligned):
        parser.error("échec d'écriture de l'image alignée")
    parameters = {"model": args.model, "matches_used": len(selected), "max_features": args.max_features, "transform": transform}
    meta = write_metadata(output, source_path=args.moving, script="scripts/align_sources.py", parameters=parameters, dimensions_before=(moving.shape[1], moving.shape[0]), dimensions_after=(aligned.shape[1], aligned.shape[0]), additional_sources=[args.reference])
    if comparison_output:
        comparison_output.parent.mkdir(parents=True, exist_ok=True)
        cv2.imwrite(str(comparison_output), comparison(cv2, reference, aligned, args.comparison_mode, args.opacity))
        write_metadata(comparison_output, source_path=args.reference, script="scripts/align_sources.py", parameters={**parameters, "comparison_mode": args.comparison_mode, "opacity": args.opacity}, dimensions_before=(reference.shape[1], reference.shape[0]), dimensions_after=(reference.shape[1], reference.shape[0]), additional_sources=[args.moving, output])
    print(f"Image alignée : {output}\nMétadonnées : {meta}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
