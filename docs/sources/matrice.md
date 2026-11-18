## Questions retenues 
<!-- Dorra -->
1. Quelles sont les zones de Haute-Garonne les plus exposées aux départs de feux ?
2. Quel est le lien entre le niveau de la Météo des forêts et les départs de feu réels ?
3. Comment se comporte la Météo des forêts en Haute-Garonne par rapport à l'Occitanie et au reste de la France ?

<!-- Ange -->
1. Comment sont calculés les seuils actuels de déclenhecment des dispositifs renforcés ?
2. Quelle superficie ou étendue de forêt est-elle perdue chaque apparition des feux de forêt ?
3. Combien de temps mettent les équipes en place pour détecter les départs des feux de forêt dans la région?


<!-- Mouad -->
1. A partir de quel niveau de danger de la méteo des forets on peut observer une hausse nette de departes de feu en occitanie?
2. Comment on peut renforcer la surveillance a partir du niveau de danger?
3. Comment la frequence mensuelles des departs de feu evolue-t-elle au cours de l'année?

<!-- Les questions de Mouad restent en attente de sa matrice (section 5 non faite). Les questions A1, D2 et M1 se recoupent (lien entre niveau de danger et départs de feu / seuil). -->

## Matrice v0 (Ange + Dorra)


| Question / sources | BDIFF | Interventions SDIS | Météo des forêts | Stats SDIS | Pyronear | PDPFCI | BD Forêt V2 | Admin Express | EFFIS | NASA FIRMS |
|---|---|---|---|---|---|---|---|---|---|---|
| A1. Calcul des seuils actuels de déclenchement | absent : aucun indice ni seuil | absent : compteurs d'interventions, aucun seuil | partiel : `niveau_j1` et `niveau_j2` (1 à 4) par département et par jour, ni méthode de calcul ni seuil du SDIS 31 | inconnu : PDF non lus | absent : images de fumée | inconnu : plan de 102 pages (Haute-Garonne), mesures de prévention possibles, non lu | absent : formations végétales | absent : limites administratives | absent : indices européens (FWI), pas le seuil du SDIS 31 | absent |
| A2. Superficie perdue par feu | inconnu : colonne `Surface` documentée (surface totale parcourue), CSV non ouvert ; définitions différentes avant/après 2023 et en aire méditerranéenne | absent : aucune colonne de surface | absent | absent : pas de surface par feu (non vérifié en détail) | absent | absent | partiel : surface forestière par zone, sert à rapporter les surfaces brûlées | absent | inconnu : base de surfaces brûlées, couverture France non vérifiée | inconnu : points de feux actifs, pas de surface |
| A3. Délai de détection des départs de feu | partiel : colonne `Alerte` (date et heure d'arrivée au CODIS), pas d'heure d'arrivée des équipes ni de délai | absent : aucune date ni heure | absent | inconnu : retours d'expérience possibles, non lus | partiel : colonnes `date`, `camera`, `partner` (date de l'image, pas l'heure d'alerte) ; SDIS 12 présent, pas le SDIS 31 | absent | absent | absent | absent | inconnu : heure de détection satellite possible, non vérifiée |
| D1. Zones de Haute-Garonne les plus exposées | inconnu : colonnes `Commune`, `Département`, `Alerte` documentées, CSV non ouvert ; data.gouv.fr dit « agrégées à la commune » | partiel : `Feux de végétations` par département et par an (Haute-Garonne : 403 en 2024), pas de commune | absent : niveaux de danger, aucun feu | absent : pas de localisation fine | absent : images d'entraînement | inconnu : cartes ou zones à risque possibles, non lu | partiel : localise les formations végétales, pas la fréquence d'incendie | partiel : limites communales pour les jointures (non téléchargé) | inconnu : surfaces brûlées, petits feux peu représentés, détail France non vérifié | inconnu : détections satellite, accès non vérifié |
| D2. Lien niveau de danger / départs de feu réels | inconnu : `Alerte` (date et heure) documentée, CSV non ouvert | partiel : feux par département et par an, pas de date : pas de comparaison quotidienne | complet : `date`, `num_dep`, `niveau_j1`, `niveau_j2` vérifiés, archives de juin 2024 seulement (2 à 3 saisons) | absent | absent | absent | absent | partiel : rattache communes et départements | absent : FWI européen, échelle différente | inconnu : détections quotidiennes possibles, non vérifiées |
| D3. Météo des forêts : Haute-Garonne vs Occitanie vs France | absent | absent | complet : `num_dep`, `nom_dep`, `niveau_j1` pour 96 départements, depuis juin 2024 | absent | absent | absent | absent | partiel : regroupe les départements par région (non téléchargé) | absent | absent |
