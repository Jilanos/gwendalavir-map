# Journal des décisions

Consigner ici les choix techniques et artistiques ayant un impact sur le
pipeline, avec leur justification et la date.

| Date | Décision | Justification | Impact |
| --- | --- | --- | --- |
| 2026-08-29 | Les sources originales sont immuables et font foi. | Préserver strictement la géographie officielle. | Toute stylisation est contrainte par les couches et masques. |
| 2026-08-29 | Pillow est la seule dépendance initiale. | Les scripts de base ne requièrent pas encore OpenCV ou NumPy. | Installation minimale et reproductible. |
