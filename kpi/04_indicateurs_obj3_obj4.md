# Indicateurs des objectifs 3 et 4

Fiches détaillées : `kpi/02_fiches_indicateurs.md`.

| KPI | Objectif | Rôle | Formule | Paramètres | Périmètre et granularité | Source et champs | Fiche source | Faisabilité | Garde-fou |
|---|---|---|---|---|---|---|---|---|---|
| 3.1 Indice de saisonnalité | 3 | Principal | Nombre de départs de feu du mois m / nombre de départs de feu de l'année (%) | Période (3 ou 5 ans) ; mois ; territoire (31, Occitanie, France) | Haute-Garonne, Occitanie, France ; mois | BDIFF : `Alerte`, `Département` | `fiche-BDIFF.md` | Export CSV non ouvert | Volume de feux affiché ; seuil plancher de feux par an |
| 3.2 Jours d'indice ≥ N par mois | 3 | Secondaire | Nombre de jours où `niveau_j1` ≥ N dans le mois / nombre de jours de saison du mois (%) | N = 2, 3 ou 4 ; territoire | 31, Occitanie, France ; juin à octobre 2024–2026 ; mois | Archives de la Météo des forêts : `date`, `num_dep`, `niveau_j1` | `fiche-Archives-meteo-des-forets.md` | Fichiers 2024 et 2026 ouverts (96 départements) ; 2025 non ouvert | N fixé avant les résultats ; nombre de jours en valeur absolue |
| 4.1 Part des feux éloignés d'un point d'appui (proxy) | 4 | Principal | Nombre de départs de feu à plus de X km du point d'appui le plus proche / nombre de départs de feu de Haute-Garonne (%) | X = 5, 10 ou 15 km ; type de point d'appui ; période | Haute-Garonne ; commune | BDIFF : `Commune`, `Alerte` ; Admin Express : centroïdes des communes ; points d'appui : source à ajouter (points de rencontre des secours, carroyage DFCI ou BD TOPO) | `fiche-BDIFF.md`, `fiche-Admin-Express.md` ; fiche à créer pour les points d'appui | Non vérifiable : source des points d'appui absente de l'inventaire | Part du territoire éloigné de plus de X km ; X fixé avant les résultats |
