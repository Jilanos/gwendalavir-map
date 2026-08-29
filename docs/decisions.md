# Journal des décisions

Consigner ici les choix techniques et artistiques ayant un impact sur le
pipeline, avec leur justification et la date.

| Date | Décision | Justification | Impact |
| --- | --- | --- | --- |
| 2026-08-29 | Les sources originales sont immuables et font foi. | Préserver strictement la géographie officielle. | Toute stylisation est contrainte par les couches et masques. |
| 2026-08-29 | Pillow est la seule dépendance initiale. | Les scripts de base ne requièrent pas encore OpenCV ou NumPy. | Installation minimale et reproductible. |
| 2026-08-29 | Les sorties d'ingestion sont limitées à `working/`. | Empêcher tout écrasement ou changement involontaire des originaux. | Les scripts refusent une sortie hors de cet arbre. |
| 2026-08-29 | La master map est agrandie par facteur entier et interpolation classique. | Conserver exactement le ratio sans inventer de détail. | PNG/TIFF sans perte, aucun modèle génératif. |
| 2026-08-29 | Chaque image générée reçoit un manifeste SHA256. | Assurer une traçabilité reproductible des transformations. | Fichier associé `*.meta.json`. |
