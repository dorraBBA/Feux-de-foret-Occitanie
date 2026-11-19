# Fiches d'indicateurs

Objectifs de référence : `docs/analyse/objectifs.md`. Chaque fiche suit le modèle du cours : 9 champs, test d'un paramètre, RACER, garde-fous, risque résiduel.

## Sommaire

| KPI | Objectif | Rôle | Intitulé |
|---|---|---|---|
| 1.1 | 1 | Principal | Nombre moyen annuel de départs de feu par commune |
| 1.2 | 1 | Secondaire | Part de la surface forestière par commune |
| 2.1 | 2 | Principal | Taux de départs de feu par niveau de danger |
| 2.2 | 2 | Secondaire | Part des journées nécessitant une surveillance renforcée |
| 3.1 | 3 | Principal | Indice de saisonnalité des départs de feu |
| 3.2 | 3 | Secondaire | Jours d'indice supérieur ou égal à N par mois |
| 4.1 | 4 | Principal (proxy) | Part des départs de feu éloignés d'un point d'appui |

## Consigne

1. Écrire la formule de l'indicateur : numérateur, dénominateur, paramètres.
2. Choisir un paramètre, changer sa valeur : dire ce qui change dans la fiche, décision comprise, et ce qui ne change pas.
3. Ouvrir les données : écrire la source exacte et la ligne de faisabilité. Si un terme de la formule n'a pas de champ, écrire le proxy, son biais et le sens du biais (surestimation ou sous-estimation).

---

# Objectif 1 — Cartographier les zones les plus exposées aux incendies

## KPI 1.1 (principal) — Nombre moyen annuel de départs de feu par commune

| Champ | Valeur |
|---|---|
| 1. Question et objectif | Quelles sont les 10 communes de Haute-Garonne qui enregistrent le plus de départs de feu ? Objectif 1. |
| 2. Formule | Numérateur : nombre total de départs de feu dans la commune. Dénominateur : nombre d'années étudiées. KPI = nombre de départs de feu / nombre d'années. Unité : feux par commune et par an. |
| 3. Paramètres | Période : 5 ou 10 ans ; territoire : Haute-Garonne (31) ; nombre de communes : Top 10. |
| 4. Périmètre, période, granularité, fréquence | Haute-Garonne ; période proposée : 2016–2025 ; commune ; recalcul annuel. |
| 5. Source et champs | BDIFF : date, commune, département. IGN Admin Express : limites communales. IGN BD Forêt V2 : couverture forestière. Fiches : `docs/sources/fiche-BDIFF.md`, `docs/sources/fiche-BD-Foret-V2.md`. |
| 6. Lignes utilisables | Non vérifiées : export BDIFF non ouvert. À mesurer : part des lignes avec date, commune et département renseignés. |
| 7. Proxy et biais | Si les coordonnées exactes manquent, utiliser la commune déclarée. Biais : considérer toute la commune comme exposée surestime la surface réellement concernée. |
| 8. Décision éclairée | Classer les communes et proposer une surveillance prioritaire dans les 10 premières, en tenant compte de leur couverture forestière. |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** passer de 10 à 15 communes.

- Ce qui change : la carte affiche 15 communes au lieu de 10 ; la surveillance pourrait être répartie sur davantage de territoires.
- Ce qui ne change pas : la formule, les sources, la période et la méthode de calcul.
- Décision : élargir la liste des communes prioritaires si les ressources le permettent.

**RACER :**

- Relevant : permet d'identifier les communes prioritaires.
- Accepted : à confirmer avec le SDIS 31.
- Credible : oui si les données historiques sont complètes.
- Easy : simple comptage des départs de feu par commune.
- Robust : dépend de la période et de la qualité des localisations.

**Garde-fous :**

- Afficher le nombre total de feux avec la moyenne annuelle.
- Fixer la période avant de calculer le classement.
- Ne pas considérer toute la commune comme présentant le même risque.
- Vérifier les communes ayant peu de données.

**Risque résiduel :** les feux non déclarés ne sont pas comptabilisés et le passé ne garantit pas le risque futur.

---

## KPI 1.2 (secondaire) — Part de la surface forestière par commune

| Champ | Valeur |
|---|---|
| 1. Question et objectif | Quelle proportion de chaque commune est couverte par la forêt ? Complément de l'objectif 1. |
| 2. Formule | Numérateur : surface forestière de la commune. Dénominateur : surface totale de la commune. KPI = (surface forestière / surface totale) × 100. Unité : %. |
| 3. Paramètres | Territoire : Haute-Garonne ; type de végétation ; millésime BD Forêt V2. |
| 4. Périmètre, période, granularité, fréquence | Haute-Garonne ; commune ; mise à jour selon les données IGN. |
| 5. Source et champs | IGN BD Forêt V2 : polygones forestiers et géométrie. IGN Admin Express : limites communales. Fiche : `docs/sources/fiche-BD-Foret-V2.md`. |
| 6. Lignes utilisables | Non vérifiées : fichiers géographiques à ouvrir. |
| 7. Proxy et biais | Les polygones forestiers IGN estiment la couverture forestière. Biais : un millésime ancien (2007–2018) peut surestimer ou sous-estimer la surface forestière actuelle. |
| 8. Décision éclairée | Compléter le classement des communes avec leur couverture forestière. |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** modifier les types de végétation inclus.

- Ce qui change : la surface forestière calculée et la comparaison entre communes.
- Ce qui ne change pas : les départs de feu historiques et les limites administratives.
- Décision : réexaminer les priorités si l'exposition forestière estimée change.

**RACER :**

- Relevant : complète l'analyse territoriale.
- Accepted : à confirmer avec le SDIS 31.
- Credible : dépend du millésime IGN.
- Easy : nécessite une jointure spatiale.
- Robust : sensible à la définition de la forêt.

**Garde-fous :**

- Afficher le millésime des données.
- Ne pas confondre couverture forestière et probabilité d'incendie.
- Vérifier les différences entre les dates des données géographiques.

**Risque résiduel :** la couverture forestière ne dit rien sur la cause ni sur la fréquence des départs de feu.

---

# Objectif 2 — Mesurer la relation entre la Météo des forêts et les départs de feu

## KPI 2.1 (principal) — Taux de départs de feu par niveau de danger

| Champ | Valeur |
|---|---|
| 1. Question et objectif | À partir de quel niveau de danger de la Météo des forêts observe-t-on une hausse nette des départs de feu en Occitanie ? Objectif 2. |
| 2. Formule | Numérateur : nombre de départs de feu enregistrés au niveau de danger étudié. Dénominateur : nombre de journées-départements de ce niveau. KPI = nombre de départs de feu / nombre de journées-départements du niveau. Unité : feux par journée-département. |
| 3. Paramètres | Niveaux : 1 à 4 de `niveau_j1` ; période : au moins 3 années communes ; territoire : Occitanie. |
| 4. Périmètre, période, granularité, fréquence | Occitanie ; période proposée : 2024–2026 sous réserve de disponibilité ; département et jour ; recalcul après chaque saison. |
| 5. Source et champs | BDIFF : date, commune, département. Archives de la Météo des forêts : date, département, niveau de danger. Fiches : `docs/sources/fiche-BDIFF.md`, `docs/sources/fiche-Archives-meteo-des-forets.md`. |
| 6. Lignes utilisables | Non vérifiées : exports à ouvrir. À mesurer : part des enregistrements avec date, département et niveau de danger permettant le croisement. |
| 7. Proxy et biais | Le danger départemental remplace le danger local exact. Biais : le danger réel à l'endroit de l'incendie peut être surestimé ou sous-estimé selon les conditions locales. |
| 8. Décision éclairée | Identifier le premier niveau de danger associé à une hausse nette des départs de feu et proposer un seuil de surveillance renforcée. |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** passer le seuil de déclenchement de « élevé » à « modéré ».

- Ce qui change : davantage de journées peuvent nécessiter une surveillance renforcée, ce qui augmente potentiellement les coûts.
- Ce qui ne change pas : la formule, les données historiques et les taux calculés pour chaque niveau.
- Décision : comparer les deux seuils avant de choisir celui qui correspond aux risques et aux moyens disponibles.

**RACER :**

- Relevant : directement lié au déclenchement de la surveillance.
- Accepted : à confirmer avec le SDIS 31.
- Credible : oui si les données météorologiques et les incendies sont correctement croisés.
- Easy : nécessite un regroupement par date, département et niveau.
- Robust : sensible à la qualité des données et aux années étudiées.

**Garde-fous :**

- Afficher le nombre de feux et le nombre de journées-départements par niveau.
- Ne pas comparer uniquement les nombres bruts de feux.
- Fixer la période avant l'analyse.
- Vérifier les niveaux représentés par peu de journées.

**Risque résiduel :** la météo n'explique pas toutes les causes des départs de feu ; 2 à 3 saisons ne prouvent pas une causalité.

---

## KPI 2.2 (secondaire) — Part des journées nécessitant une surveillance renforcée

| Champ | Valeur |
|---|---|
| 1. Question et objectif | Combien de journées nécessiteraient une surveillance renforcée selon le seuil choisi ? Complément de l'objectif 2. |
| 2. Formule | Numérateur : nombre de journées-départements dont le danger est supérieur ou égal au seuil. Dénominateur : nombre total de journées-départements observées. KPI = (journées-départements au-dessus du seuil / journées-départements observées) × 100. Unité : %. |
| 3. Paramètres | Seuil : niveau 2, 3 ou 4 ; période ; départements d'Occitanie. |
| 4. Périmètre, période, granularité, fréquence | Occitanie ; saison de la Météo des forêts ; département et jour ; calcul mensuel et annuel. |
| 5. Source et champs | Archives de la Météo des forêts : date, département, niveau de danger. Fiche : `docs/sources/fiche-Archives-meteo-des-forets.md`. |
| 6. Lignes utilisables | Non vérifiées pour l'Occitanie : fichiers 2024 et 2026 ouverts (96 départements), fichier 2025 non ouvert. |
| 7. Proxy et biais | Les journées au-dessus du seuil estiment la charge de surveillance. Biais : surestime la mobilisation réelle si plusieurs zones sont couvertes par les mêmes équipes. |
| 8. Décision éclairée | Estimer la charge de surveillance et vérifier sa compatibilité avec les moyens du SDIS 31. |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** passer le seuil de « élevé » à « modéré ».

- Ce qui change : la part de journées nécessitant une surveillance augmente ou reste identique.
- Ce qui ne change pas : les archives, les dates et les départements étudiés.
- Décision : réévaluer les effectifs et les coûts avant de retenir le seuil.

**RACER :**

- Relevant : mesure la charge potentielle de surveillance.
- Accepted : à confirmer avec le SDIS 31.
- Credible : dépend de la complétude des archives.
- Easy : simple comptage par niveau de danger.
- Robust : dépend du seuil choisi.

**Garde-fous :**

- Afficher le nombre absolu de journées-départements avec le pourcentage.
- Distinguer les journées-départements des journées calendaires.
- Ne pas confondre journée au-dessus du seuil et intervention réelle.
- Vérifier les moyens humains et financiers disponibles.

**Risque résiduel :** un jour au-dessus du seuil sans feu n'est pas forcément une fausse alerte : le dispositif a pu fonctionner.

---

# Objectif 3 — Évolution spatio-temporelle du risque (Haute-Garonne, Occitanie, France)

## KPI 3.1 (principal) — Indice de saisonnalité des départs de feu

| Champ | Valeur |
|---|---|
| 1. Question et objectif | En quels mois renforcer les effectifs, et la Haute-Garonne diffère-t-elle de l'Occitanie et de la France ? Objectif 3. |
| 2. Formule | Numérateur : nombre de départs de feu du mois m. Dénominateur : nombre de départs de feu de l'année. Unité : % de l'année. |
| 3. Paramètres | Période (3 ou 5 ans ; 2020–2025 proposé) ; mois ou trimestre ; territoire (31, Occitanie, France). |
| 4. Périmètre, période, granularité, fréquence | Haute-Garonne, Occitanie, France métropolitaine ; mois ; recalcul annuel après validation de la campagne BDIFF. |
| 5. Source et champs | BDIFF (export CSV, `bdiff.agriculture.gouv.fr/incendies`) : `Alerte` (date), `Département`. Fiche : `docs/sources/fiche-BDIFF.md`. |
| 6. Lignes utilisables | Non vérifiées : export CSV non ouvert. À mesurer : part des lignes avec `Alerte` et `Département` renseignés. |
| 7. Proxy et biais | Un feu est rattaché au mois de son alerte, même s'il dure plusieurs jours (date d'alerte, pas de début réel) : biais faible sur le mois. Exhaustivité moindre avant 2020 hors aire méditerranéenne : sous-estimation des feux en Haute-Garonne. |
| 8. Décision éclairée | Valeur élevée sur un mois : y concentrer les effectifs. Répartition étalée : vigilance régulière. |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** passer de 3 à 5 ans.

- Ce qui change : la valeur, qui est lissée des années atypiques.
- Ce qui ne change pas : la définition du feu et la source.
- Décision : ne change que si le mois de pic change.

**RACER :**

- Relevant : lié aux effectifs par période.
- Accepted : à confirmer avec le SDIS 31 (définition de « départ de feu »).
- Credible : oui si la période et la date de référence sont fixées.
- Easy : simple comptage par mois.
- Robust : fragile avec peu de feux.

**Garde-fous :**

- Volume : nombre de feux affiché à côté de la part.
- Seuil plancher : en dessous de N feux par an (à fixer avant les résultats), la part n'est pas lue.
- Règle fixée à l'avance : période et date de référence écrites avant les résultats.
- Détournement possible : choisir la période d'une seule saison favorable pour faire apparaître un pic ; le volume et la période fixe le rendent visible.

**Risque résiduel :** le volume ne voit pas les feux non déclarés ; classer un territoire peut le stigmatiser.

---

## KPI 3.2 (secondaire) — Jours d'indice supérieur ou égal à N par mois

| Champ | Valeur |
|---|---|
| 1. Question et objectif | Le danger météo explique-t-il le pic de saisonnalité ? Prépare le KPI 3.1. Objectif 3. |
| 2. Formule | Numérateur : nombre de jours où `niveau_j1` ≥ N dans le mois. Dénominateur : nombre de jours de saison dans le mois. Unité : %. |
| 3. Paramètres | N = 2, 3 ou 4 ; territoire. |
| 4. Périmètre, période, granularité, fréquence | 31, Occitanie (13 départements), France ; juin à octobre, 2024–2026 ; mensuel. |
| 5. Source et champs | Archives de la Météo des forêts (data.gouv.fr, Météo-France) : `date`, `num_dep`, `niveau_j1`. Fiche : `docs/sources/fiche-Archives-meteo-des-forets.md`. |
| 6. Lignes utilisables | Fichiers 2024 et 2026 vérifiés : 11 520 et 12 576 lignes, 96 départements. Fichier 2025 non ouvert. Part de `niveau_j1` renseigné : à mesurer. |
| 7. Proxy et biais | `niveau_j1` est une prévision à J+1, pas le danger observé : surestimation ou sous-estimation possible du danger réel. Hors saison, pas de donnée : les mois de novembre à mai ne se comparent pas. |
| 8. Décision éclairée | Si le nombre de jours doublait, le SDIS 31 mobiliserait le dispositif plus souvent : relever N si la charge dépasse le budget (à demander). |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** passer N de 3 à 2.

- Ce qui change : le nombre de jours comptés augmente, donc la charge estimée.
- Ce qui ne change pas : les archives, les départements et les dates.
- Décision : choisir N selon le budget de mobilisation.

**RACER :**

- Relevant : explique le pic de saisonnalité.
- Accepted : à confirmer avec le SDIS 31.
- Credible : oui si N est fixé avant les résultats.
- Easy : simple comptage.
- Robust : dépend de N et de 2 à 3 saisons.

**Garde-fous :**

- Afficher le nombre de jours en valeur absolue.
- Fixer N avant de voir les résultats.
- Part des jours au-dessus de N sans feu, comme contrepoids.

**Risque résiduel :** un jour sans feu n'est pas forcément une fausse alerte.

**Rôle dans le jeu :** KPI secondaire (explique 3.1). Contexte, non piloté : la saison.

---

# Objectif 4 — Moyens de prévention et de surveillance

## KPI 4.1 (principal, proxy) — Part des départs de feu éloignés d'un point d'appui

| Champ | Valeur |
|---|---|
| 1. Question et objectif | Quels secteurs prioritaires de Haute-Garonne sont mal couverts ? Objectif 4. |
| 2. Formule | Numérateur : départs de feu à plus de X km du point d'appui le plus proche. Dénominateur : départs de feu de Haute-Garonne sur la période. Unité : %. |
| 3. Paramètres | X = 5, 10 ou 15 km ; type de point d'appui (poste de secours, point de rencontre, caméra) ; période. |
| 4. Périmètre, période, granularité, fréquence | Haute-Garonne ; 2020–2025 proposé ; commune ; annuel. |
| 5. Source et champs | BDIFF : `Commune`, `Alerte`. Admin Express : centroïdes des communes. Points d'appui : **source non retenue à ce jour** (points de rencontre des secours, carroyage DFCI ou BD TOPO du défi) : fiche et décision au journal à créer. |
| 6. Lignes utilisables | Non vérifiable : la source des points d'appui n'est pas dans l'inventaire et l'export BDIFF n'est pas ouvert. |
| 7. Proxy et biais | Terme sans champ : « couverture réelle en moyens de surveillance ». Proxy : distance à un point d'appui connu. Biais : une distance courte ne prouve pas une couverture effective (personnel, délai) ; **surestimation de la couverture**. Distance à vol d'oiseau depuis le centroïde de la commune, non depuis le lieu du feu : imprécision. |
| 8. Décision éclairée | Part élevée : installer ou déplacer des moyens vers ces secteurs. Part faible : maintenir le dispositif. |
| 9. Propriétaire | À définir avec l'équipe. |

**Test d'un paramètre :** passer X de 10 à 5 km.

- Ce qui change : la part de feux « éloignés » augmente et la liste des secteurs prioritaires s'allonge.
- Ce qui ne change pas : la source des feux et la définition d'un feu.
- Décision : choisir X selon les moyens déployables.

**RACER :**

- Relevant : indirect (proxy).
- Accepted : à valider avec le SDIS 31.
- Credible : seulement si X et le type de point d'appui sont fixés.
- Easy : dépend de la source à ajouter.
- Robust : fragile (X modifiable).

**Garde-fous :**

- Contrepoids : part du territoire situé à plus de X km d'un point d'appui. Élargir X améliore le chiffre sans changer la réalité ; le contrepoids montre le zonage.
- Volume : nombre de feux par secteur, avec seuil plancher avant de classer un secteur.
- Règle fixée à l'avance : X choisi avant les résultats.

**Risque résiduel :** la proximité ne mesure ni la rapidité d'intervention ni la compétence, et un secteur sans feu n'est pas forcément bien couvert.

---

# Jeu d'indicateurs v0

| Rôle | Indicateur |
|---|---|
| KPI principal (obj. 1) | 1.1 Nombre moyen annuel de départs de feu par commune |
| KPI secondaire (obj. 1) | 1.2 Part de la surface forestière par commune |
| KPI principal (obj. 2) | 2.1 Taux de départs de feu par niveau de danger |
| KPI secondaire (obj. 2) | 2.2 Part des journées nécessitant une surveillance renforcée |
| KPI principal (obj. 3) | 3.1 Indice de saisonnalité |
| KPI secondaire (obj. 3) | 3.2 Jours d'indice ≥ N par mois |
| KPI principal (obj. 4) | 4.1 Part des feux éloignés d'un point d'appui (proxy) |
| Garde-fous | Volume de feux ; nombre de journées-départements ; part du territoire éloigné |
| Contexte | La saison |
| Écarté | Corrélation feux / température : l'indice la contient déjà ; aucune décision ne change |

**Pré-mortem (à compléter en groupe) :** raisons plausibles d'échec : (1) BDIFF incomplète en Haute-Garonne, (2) source des points d'appui absente ou imprécise, (3) 2 à 3 saisons de météo, trop court.
