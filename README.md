# Gwendalavir Map

Pipeline reproductible pour créer une affiche HD colorisée de la carte de
Gwendalavir à partir de cartes officielles. Les sources originales constituent
la vérité géographique : leurs côtes, reliefs, cours d'eau, positions relatives
et toponymes ne doivent jamais être librement réinterprétés par un outil
génératif.

## Workflow

1. Placer les scans et images de référence dans `source/` et `references/`.
2. Nettoyer, redresser et aligner les références dans `working/`.
3. Produire une master map haute définition sans perte.
4. Extraire ou reconstruire les couches (`layers/`) et leurs masques.
5. Employer la génération d'image uniquement pour le rendu artistique des
   couches, sans déplacement des éléments structurants.
6. Recomposer l'image, ajouter les textes depuis `data/labels.json`, puis
   préparer les exports d'impression dans `final/`.

Le pipeline détaillé est décrit dans [docs/workflow.md](docs/workflow.md) et
la spécification de référence dans [docs/map-spec.md](docs/map-spec.md).

## Structure

- `source/` : originaux immuables et scans.
- `references/` : cartes et références artistiques externes.
- `working/` : dérivés de travail nettoyés, alignés et upscalés.
- `layers/` : couches géographiques et masques.
- `data/` : données structurées des noms et repères.
- `prompts/` : direction artistique et modèles de prompts.
- `generated/` : essais et rendus retenus.
- `final/` : livrables raster, impression et vectoriels.
- `scripts/` : outils exécutables depuis la racine du dépôt.
- `docs/` : spécification, workflow et journal des décisions.

## Dépendances

Python 3.10+ et Pillow sont nécessaires à cette première étape.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Commandes principales

```bash
python3 scripts/inspect_image.py source/
python3 scripts/prepare_source.py source/original/carte.png \
  --output working/cleaned/carte_cleaned.tiff
python3 scripts/create_master.py working/cleaned/carte_cleaned.tiff \
  --scale 4 --interpolation lanczos --output working/upscaled/master.tiff
```

Les scripts n'appliquent que des opérations déterministes. La préparation peut
effectuer rotation, crop et corrections explicitement demandées ; la master map
utilise uniquement une interpolation classique, sans transformation générative.
