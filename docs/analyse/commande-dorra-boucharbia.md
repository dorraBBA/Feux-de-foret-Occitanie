# Feux de foret Occitanie

## 1.Les questions:

1. Quelles sont les zones de Haute-Garonne les plus exposées aux départs de feux ?
2. Quel est le lien entre le niveau de la Météo des forêts et les départs de feu réels ?
3. Quel niveau de danger faut-il choisir pour déclencher le dispositif renforcé ?
4. Comment se comporte la Météo des forêts en Haute-Garonne par rapport à l'Occitanie et au reste de la France ?

## 2. Les termes inconnus:

- Météo des forêts : indicateur du niveau de danger d'incendie -> À vérifier : ses niveaux et ses critères de calcul.
- Fausse alerte : situation où un niveau de danger élevé est annoncé sans départ de feu -> À vérifier : comment elle est définie et mesurée.
- Départ de feu : début d'un incendie -> À vérifier : les types de feux concernés.
- Dispositif renforcé : patrouilles et surveillance supplémentaires -> À vérifier : les moyens et les coûts.
- Seuil de déclenchement : niveau de danger à partir duquel le dispositif est renforcé -> À vérifier : le seuil actuel.
- Emprise géographique : territoire couvert par l'étude -> À vérifier : les limites géographiques et les échelles disponibles dans les données.

## 3. Les besoins:

La décision à éclairer :
- Identifier les zones prioritaires.
- Définir le meilleur seuil de déclenchement du dispositif renforcé.

Ce qui manque :
- Historique des départs de feu.
- Historique des niveaux de la Météo des forêts.
- Localisation et gravité des incendies.
- Budget et moyens disponibles.
- Données des autres départements pour comparaison.

## 4. Les données: 

Question 1 : Localisation des zones à risque
- Donnée idéale : localisation et nombre de départs de feu.
- Grain : un incendie.
- Période : 5 à 10 dernières années.
- Fraîcheur : mise à jour annuelle.
- Emprise géographique : Haute-Garonne.

Question 2 : Fiabilité de la Météo des forêts
- Donnée idéale : niveau de danger et nombre de départs de feu.
- Grain : un jour par zone.
- Période : 5 à 10 dernières années.
- Fraîcheur : quotidienne.
- Emprise géographique : Haute-Garonne.

Question 3 : Choix du seuil de déclenchement
- Donnée idéale : niveau de danger, nombre d'incendies, gravité et coûts des moyens engagés.
- Grain : un jour par zone.
- Période : plusieurs saisons estivales.
- Fraîcheur : quotidienne.
- Emprise géographique : Haute-Garonne.

Question 4 : Comparaison avec les autres territoires
- Donnée idéale : historique des niveaux météo et des départs de feu.
- Grain : un jour par département.
- Période : 5 à 10 dernières années.
- Fraîcheur : quotidienne.
- Emprise géographique : Occitanie et France entière.


## 5. Confrontation aux sources

### Matrice

Sources de l'inventaire : BDIFF, Interventions SDIS, Archives de la Météo des forêts, API Météo des forêts, Admin Express (IGN), BD Forêt V2 et EFFIS. Les fiches sont dans `docs/sources/`. Les autres sources du défi ne sont pas retenues car elles apportent peu d'informations directement exploitables pour les quatre questions.

| Question / Source | BDIFF | Interventions SDIS | Météo des forêts (API et archives) | Admin Express | BD Forêt V2 | EFFIS |
|---|---|---|---|---|---|---|
| 1. Zones les plus exposées | Oui : localisation des incendies par commune, date d'alerte et surfaces parcourues. Permet d'identifier les communes les plus touchées en Haute-Garonne | Partiel : nombre annuel d'interventions pour feux de végétation par département, sans localisation communale ni date précise | Absent : indique le niveau de danger par département, mais pas les départs de feu réels | Oui : limites communales et départementales pour cartographier les incendies | Partiel : localisation des formations végétales et des espaces forestiers. Permet d'identifier les zones forestières, mais pas leur fréquence réelle d'incendie | Partiel : surfaces brûlées et localisation des grands incendies, mais les petits feux sont peu représentés |
| 2. Lien entre danger météo et départs réels | Oui : date, heure, commune et surface de chaque incendie. Permet de comparer les départs de feu aux niveaux de danger | Partiel : nombre annuel de feux de végétation par département, sans date permettant une comparaison quotidienne | Oui, indispensable : niveaux de danger par département et par jour (J+1 et J+2). Archives disponibles depuis juin 2024. Permet de croiser les niveaux avec les incendies réels | Partiel : permet de rattacher les communes aux départements pour les jointures géographiques | Absent : décrit les formations végétales, pas les conditions météorologiques ni les incendies | Partiel : indices de danger et surfaces brûlées, mais échelle et seuils différents de la Météo des forêts |
| 3. Choix du seuil de déclenchement | Partiel : historique des départs de feu et surfaces brûlées. Ne contient pas les coûts ni les moyens de surveillance engagés | Partiel : nombre d'interventions par département et par an. Ne donne pas les moyens mobilisés ni leurs coûts | Oui, indispensable : niveaux de danger 1 à 4 par département et par jour. Permet de comparer les départs de feu selon chaque niveau, mais ne fournit pas le seuil opérationnel du SDIS 31 | Absent : limites administratives uniquement | Absent : formations végétales, sans information sur les moyens opérationnels | Partiel : indices de danger et surfaces brûlées, utiles pour compléter l'analyse, mais pas pour déterminer directement le seuil du SDIS 31 |
| 4. Comparaison Haute-Garonne / Occitanie / France | Oui : données disponibles à l'échelle communale et nationale. Permet de comparer les départs de feu entre territoires | Partiel : statistiques annuelles par département, utiles pour comparer les volumes d'interventions | Oui, indispensable : niveaux de danger quotidiens par département. Permet de comparer la Haute-Garonne, les départements d'Occitanie et la France métropolitaine | Oui : permet de regrouper les départements par région et de réaliser les comparaisons territoriales | Partiel : permet de comparer la couverture forestière des territoires, mais pas les niveaux de danger | Partiel : statistiques européennes et nationales sur les incendies et les surfaces brûlées. Le détail départemental n'est pas garanti |

### Écarts avec la section 4

Pour chaque question, comparer la donnée idéale (section 4) à la meilleure source disponible, critère par critère : écrire « idéal → réel », ou « = » si les deux correspondent.

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
|---|---|---|---|---|---|
| 1 | BDIFF + Admin Express + BD Forêt V2 | un incendie → une commune = ; BD Forêt : une zone de formation végétale | 5 à 10 ans → BDIFF : 2006 à 2022 dans les métadonnées du jeu ; données consultables plus récentes dans l'application | annuelle = | Haute-Garonne = |
| 2 | Archives de la Météo des forêts + BDIFF | un jour × département + un incendie → croisement possible, mais périodes et grains différents | 5 à 10 ans → archives disponibles depuis juin 2024 (2024 à 2026) | quotidienne = | Haute-Garonne = |
| 3 | Archives de la Météo des forêts + BDIFF + Interventions SDIS | un jour × département + un incendie ; coûts et moyens engagés absents | plusieurs saisons estivales → archives depuis 2024 ; BDIFF depuis 2006 | quotidienne pour la météo ; annuelle pour les interventions SDIS | Haute-Garonne = |
| 4 | Archives de la Météo des forêts + Admin Express | un jour × département = ; agrégation possible à l'échelle régionale et nationale | 5 à 10 ans → 2024 à 2026 seulement pour les archives | quotidienne = | Occitanie et France entière = |

### Décisions

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| 1. Zones les plus exposées | Vérifier les données de localisation et les colonnes de surface de la BDIFF. Il manque également une analyse croisée avec les zones forestières | collecter | Télécharger les données BDIFF pour la Haute-Garonne, les joindre à Admin Express et BD Forêt V2, puis calculer le nombre de départs de feu par commune | Temps de téléchargement, nettoyage et jointure des données ; risque de sous-estimation des feux non renseignés |
| 2. Lien entre danger météo et départs réels | Historique commun limité à partir de 2024. Les archives météo ne couvrent pas les 5 à 10 dernières années | approximer | Croiser les niveaux de danger quotidiens de Météo-France avec les dates d'alerte de la BDIFF. Calculer le nombre de départs de feu pour chaque niveau de danger | Analyse limitée à quelques saisons estivales ; données BDIFF potentiellement incomplètes ; une association ne prouve pas une causalité |
| 3. Choix du seuil de déclenchement | Seuil opérationnel actuel du SDIS 31, coûts des patrouilles, moyens humains et matériels mobilisés | collecter | Comparer le nombre de départs de feu et leur gravité selon les niveaux 1, 2, 3 et 4. Demander au SDIS 31 ses critères opérationnels et ses coûts pour proposer un seuil adapté | Dépend de la disponibilité des données du SDIS 31 ; sans les coûts, impossible de mesurer précisément le rapport entre prévention et moyens engagés |
| 4. Comparaison Haute-Garonne / Occitanie / France | Historique météo limité à 2024-2026. Nécessité de disposer des mêmes niveaux de danger pour tous les départements | approximer | Utiliser les archives départementales de Météo-France et Admin Express pour comparer la fréquence des niveaux de danger en Haute-Garonne, en Occitanie et en France métropolitaine | Période d'observation courte ; différences climatiques et forestières entre départements à prendre en compte |