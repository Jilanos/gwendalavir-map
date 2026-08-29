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
