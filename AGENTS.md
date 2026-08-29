# Règles permanentes

- Ne jamais modifier, déplacer ou écraser un fichier situé dans `source/` : ces
  originaux sont immuables.
- Les scripts d'ingestion ne lisent `source/` qu'en lecture seule et écrivent
  toutes leurs sorties sous `working/`.
- Travailler dans `working/`, `layers/`, `generated/` ou `final/`.
- Préférer des scripts reproductibles aux modifications manuelles.
- Conserver les étapes intermédiaires importantes.
- Documenter les transformations significatives dans `docs/decisions.md`.
- Ne jamais laisser un générateur d'image produire les textes définitifs.
- Considérer les fichiers de `source/` comme références géographiques absolues.
- Éviter toute transformation générative susceptible de déplacer les éléments de
  la carte.
- Privilégier Python, OpenCV, Pillow, NumPy et les formats PNG, TIFF et SVG
  selon les usages.
- Produire des scripts exécutables depuis la racine du repository.
