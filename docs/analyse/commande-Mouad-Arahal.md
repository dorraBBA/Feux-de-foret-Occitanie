# Feux de foret Occitanie

## 1. Les questions:
* Quels sont les zones de Haute-Garonne où les départs de feu sont plus fréquents?
* A partir de quel niveau de danger de la méteo des forets on peut observer une hausse nette de departes de feu en occitanie? 
* et comment on peut renforcer la surveillance a partir du niveau de danger?
* Comment la frequence mensuelles des departs de feu evolue-t-elle au cours de l'année?

## 2. Les termes inconnus:
* Seuil de déclenchement : Le niveau de danger à partir duquel des mesures supplémentaires sont mises en place. 
* Météo des forêts : information sur le danger de feu de forêt
* Patrouilles : équipes qui se déplacent pour surveiller les zones à risque
* SDIS : Service Départemental d'Incendie et de Secours
* Guet : surveillance depuis un point d'observation ou à l'aide d'autres moyens pour repérer rapidement un incendie

## 3. Les besoins :

La décision à éclairer :

- Identifier les zones de Haute-Garonne où les départs de feu sont les plus fréquents.
- Définir à partir de quel niveau de danger de la Météo des forêts il faut renforcer la surveillance.

Ce qui manque :

- Historique des départs de feu.
- Localisation précise des incendies.
- Historique des niveaux de danger de la Météo des forêts.
- Seuil actuel de déclenchement de la surveillance renforcée.
- Budget et moyens humains disponibles.
- Données des autres départements d'Occitanie pour comparer les risques.



## 4. Les données:
 
* Question 1 :
- Donnée idéale : Historique des départs de feu avec leurs dates et localisations précises.
- Grain : Un départ de feu.
- Période : on peut prendre les 5 derniers été
- Fraîcheur : en se basant sur les derniers données qu'on a 
- Emprise géographique : Haute-Garonne.

* Question 2 :
- Donnée idéale : Niveaux de danger de la Météo des forêts et nombre de départs de feu observés.
- Grain : Un nombre de départ de feu par jour.
- Période : on peut prendre les 5 derniers été
- Fraîcheur : en se basant sur les derniers données qu'on a 
- Emprise géographique : Occitanie.

* Question 3 :
- Donnée idéale : Historique des départs de feu avec leurs dates et leurs localisations.
- Grain : Un départ de feu.
- Période : on peut prendre les 5 derniers été 
- Fraîcheur : en se basant sur les derniers données qu'on a 
- Emprise géographique : Occitanie.

* Question 4 :
- Donnée idéale : Nombre de départs de feu enregistrés chaque mois.
- Grain : Un département par mois.
- Période :Pendant toute l'année 2026
- Fraîcheur : en se basant sur les derniers données qu'on a 
- Emprise géographique : Occitanie.

## 5. Confrontation aux sources

### Matrice

| Question | Source | Couverture | Justification |
|---|---|---|---|
| 1. Zones les plus exposées | BDIFF | partiel | Localisation des incendies disponible, mais précision par commune et couverture de la Haute-Garonne à vérifier. |
| 2. Lien entre danger météo et départs réels | BDIFF + Météo des forêts | partiel | Les dates des incendies peuvent être croisées avec les niveaux de danger, mais l'historique météo reste à vérifier. |
| 3. Choix du seuil de déclenchement | Météo des forêts + PDPFCI + Interventions SDIS | partiel | Les niveaux de danger et les mesures de prévention sont utiles, mais les règles opérationnelles du SDIS 31 restent à confirmer. |
| 4. Fréquence mensuelle des départs de feu | BDIFF | partiel | Les dates des incendies permettent un regroupement mensuel, sous réserve de vérifier la période couverte. |


### Écarts avec la section 4

Pour chaque question, je compare la donnée idéale (section 4) à la meilleure source disponible, critère par critère. J'écris « idéal → réel » ou « = » si les deux correspondent.

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
|---|---|---|---|---|---|
| 1 | BDIFF + Admin Express (IGN) | Un départ de feu avec localisation précise → un incendie enregistré, précision géographique à vérifier | Plusieurs années récentes → historique BDIFF disponible, années exactes à vérifier | Mise à jour régulière souhaitée → fréquence réelle à vérifier | Haute-Garonne → données nationales à filtrer sur le département 31 |
| 2 | BDIFF + Archives de la Météo des forêts | Un départ de feu par jour et par zone de danger → données incendies et météo à croiser | Historique commun sur plusieurs années → période commune à vérifier | Données récentes souhaitées → disponibilité des dernières archives à vérifier | Occitanie → zones météo et localisations des incendies à rapprocher |
| 3 | PDPFCI + Interventions SDIS | Une décision de surveillance par niveau de danger → mesures de prévention et interventions, sans seuil opérationnel confirmé | Été 2027 → plans en vigueur et historiques d'intervention à vérifier | Informations opérationnelles actuelles → actualisation des plans et moyens à vérifier | Haute-Garonne → plan départemental et données du SDIS 31 à confirmer |
| 4 | BDIFF | Un départ de feu daté → un incendie avec date, à vérifier | Plusieurs années → historique BDIFF, période exacte à confirmer | Mise à jour régulière → fréquence de publication à vérifier | Haute-Garonne et Occitanie → filtrage des données par département ou région |


### Décisions

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| 1. Zones les plus exposées | Localisation précise des départs de feu par commune en Haute-Garonne. | Collecter | Vérifier les données BDIFF et demander les informations manquantes au SDIS 31. | Temps de collecte et de vérification des localisations. |
| 2. Lien entre danger météo et départs réels | Historique commun des niveaux de danger météo et des départs de feu. | Collecter | Obtenir les archives météo pour les croiser avec les dates des incendies. | Temps de collecte et de croisement des données. |
| 3. Choix du seuil de déclenchement | Seuil opérationnel actuel du SDIS 31 et moyens de surveillance engagés. | Collecter | Demander au SDIS 31 les règles de déclenchement et les moyens mobilisés. | Dépendance à la réponse du SDIS et temps d'analyse. |
| 4. Fréquence mensuelle des départs de feu | Dates complètes des incendies sur plusieurs années. | Collecter | Vérifier l'historique BDIFF pour calculer les départs de feu par mois. | Nettoyage des dates et vérification de la période couverte. |