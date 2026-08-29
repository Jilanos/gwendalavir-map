# Spécification de la carte

Ce document devient la source de référence des décisions cartographiques. Toute
mesure est exprimée dans le repère de la master map une fois celle-ci définie.

## Source utilisée

- Fichier source : à renseigner.
- Édition / provenance : à renseigner.
- Date d'acquisition et droits : à renseigner.

## Cadre

- Orientation : à renseigner.
- Ratio de la carte : à renseigner.
- Dimensions de la master map : à renseigner.

## Master map requirements

- Aucune modification de la géographie originale n'est autorisée.
- Aucune déformation non maîtrisée ne doit être introduite ; toute rotation,
  découpe ou transformation d'alignement est explicite, reproductible et
  contrôlable visuellement.
- Aucune génération de détail, super-résolution générative ou interprétation
  artistique n'est admise dans la master map.
- Le ratio est conservé lors de l'agrandissement et seules des interpolations
  classiques peuvent être utilisées.
- La master map devient le système de coordonnées spatial de référence pour la
  suite du projet.

### Coordonnées normalisées

Toutes les positions futures sont stockées sous forme normalisée : `x ∈ [0,1]`
et `y ∈ [0,1]`. L'origine est située en haut à gauche, `x` croît vers la droite
et `y` vers le bas. Les coordonnées pixels sont converties à partir des
dimensions de la master map au moment du rendu, ce qui permet de changer sa
résolution sans déplacer labels et repères.

## Géographie

- Contours géographiques : à inventorier depuis la source.
- Hydrographie : rivières, lacs et littoral à relever.
- Relief : chaînes, sommets, plaines et autres formes à relever.
- Végétation : forêts et zones végétales à relever.
- Villes et lieux : à référencer depuis `data/landmarks.json`.

## Habillage

- Typographie : noms exacts gérés séparément dans `data/labels.json`.
- Éléments décoratifs : cadre, cartouche, rose des vents, textures — à définir.

## Positions à préserver strictement

Les contours, côtes, rivières, lacs, reliefs, forêts, villes, frontières,
symboles structurants et positions relatives issus de la source ne peuvent pas
être déplacés par la stylisation ou une génération d'image.

## Interprétation artistique autorisée

Palette, textures, ombrage, niveau de détail pictural, traitement des reliefs,
motifs de forêt, atmosphère, encadrements et décorations peuvent être adaptés,
à condition de respecter les géométries et masques de référence.
