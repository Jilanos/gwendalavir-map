# Workflow cible

```text
source originale
→ nettoyage
→ redressement / alignement
→ master haute définition
→ extraction ou création des différentes couches
→ création des masques
→ stylisation / colorisation
→ recomposition
→ ajout des textes
→ upscale final
→ préparation impression
```

## Ingestion déterministe et master map

Les commandes suivantes sont exécutées depuis la racine. Elles lisent les
sources sans les modifier et écrivent uniquement dans `working/`.

```bash
python3 scripts/inspect_image.py source/ --inventory working/source_inventory.json
python3 scripts/prepare_source.py source/original/map.jpg \
  --rotate 0.8 --crop 120 80 2450 3350 --grayscale \
  --output working/cleaned/map_cleaned.tif
python3 scripts/align_sources.py working/cleaned/reference.tif working/cleaned/scan.tif \
  --output working/aligned/scan_aligned.tif \
  --comparison working/aligned/scan_overlay.png --comparison-mode overlay
python3 scripts/create_master.py working/cleaned/map_cleaned.tif --scale 4 \
  --interpolation lanczos --output working/upscaled/master_map.tif
python3 scripts/extract_ink_mask.py working/upscaled/master_map.tif \
  --threshold 230 --output layers/masks/canonical_ink_mask.png
python3 scripts/compose_poster.py --texture generated/selected/parchment_texture_v1.png \
  --ink-mask layers/masks/canonical_ink_mask.png \
  --output final/raster/poster_base.png --dpi 300
# Révision print discrète : parchemin moins saturé et encre légèrement renforcée.
python3 scripts/compose_poster.py --texture generated/selected/parchment_texture_v1.png \
  --ink-mask layers/masks/canonical_ink_mask_12000.png \
  --output final/raster/poster_refined_12000.png --dpi 300 \
  --ink-color '#20170f' --texture-saturation 0.55 --texture-strength 0.58 \
  --ink-opacity 1.12
python3 scripts/compare_images.py working/cleaned/map_cleaned.tif working/aligned/scan_aligned.tif \
  --mode difference --output working/aligned/check_difference.png
python3 scripts/create_review_report.py \
  --source source/original/map.jpg --prepared working/cleaned/map_cleaned.tif \
  --difference working/cleaned/check_difference.png \
  --master working/upscaled/master_map.tif \
  --output docs/reports/pipeline-review.html
```

Chaque image produite est accompagnée d'un fichier `.meta.json` contenant sa
source, les paramètres, les dimensions, la date et les SHA256 concernés.
Le rapport HTML autonome embarque des aperçus des étapes intermédiaires afin de
permettre une validation visuelle avant toute extraction de couche ou
stylisation.

1. Préserver l'original dans `source/` sans modification.
2. Créer des dérivés nettoyés dans `working/cleaned/`, puis alignés dans
   `working/aligned/`.
3. Exporter une master map sans perte (TIFF ou PNG) dans `working/`.
4. Extraire ou dessiner les couches géographiques dans `layers/` et définir des
   masques explicites dans `layers/masks/`.
5. Appliquer la stylisation à des couches ou zones masquées. La génération ne
   doit pas déterminer la géographie.
6. Recomposer les couches dans un rendu intermédiaire.
7. Ajouter les textes finaux à partir des données structurées ; ne pas les
   générer dans une image.
8. Effectuer l'upscale final et exporter les fichiers destinés à l'impression.

Chaque transformation significative doit être scriptée, versionnée ou notée
dans `docs/decisions.md`.
