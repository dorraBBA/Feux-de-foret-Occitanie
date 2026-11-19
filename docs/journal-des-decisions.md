# Journal des décisions


## Décision 001 — [Questions analytiques à retenir]

- **Date :** 18-11-2026
- **Auteurs :** Ange , Dorra
- **Question :** Quelles questions analytique retenir ? 
- **Manque :** xx
- **Décision :** Retenir 9 questions 
- **Raison :** Certaines questions répondaient au même problème donc ont été laissées
- **Ce que la décision coûte :**  abandonner des questions
- **Termes du glossaire touchés :**  aucun


## Décision 002 — [A1 : seuils de déclenchement actuels]

- **Date :** 18-11-2026
- **Auteurs :** Ange, Dorra
- **Question :** A1 — Comment sont calculés les seuils actuels de déclenchement des dispositifs renforcés ?
- **Manque :** Aucune source ne donne la méthode ni le seuil du SDIS 31 ; la Météo des forêts fournit seulement `niveau_j1` et `niveau_j2`.
- **Décision :** Collecter
- **Raison :** Demander au SDIS 31 la méthode et le seuil ; la Météo des forêts seule ne suffit pas.
- **Ce que la décision coûte :** Dépend de la réponse du SDIS 31.
- **Termes du glossaire touchés :** aucun


## Décision 003 — [A2 : superficie perdue par feu]

- **Date :** 18-11-2026
- **Auteurs :** Ange, Dorra
- **Question :** A2 — Quelle superficie est perdue à chaque feu ?
- **Manque :** Colonne `Surface` de la BDIFF documentée mais non vérifiée dans le CSV ; définitions différentes avant/après 2023.
- **Décision :** Collecter
- **Raison :** Ouvrir l'export CSV de la BDIFF et vérifier `Surface`.
- **Ce que la décision coûte :** Temps de téléchargement et de nettoyage ; surfaces non comparables entre périodes.
- **Termes du glossaire touchés :** à vérifier (surface, feu de forêt)


## Décision 004 — [A3 : délai de détection]

- **Date :** 18-11-2026
- **Auteurs :** Ange, Dorra
- **Question :** A3 — Combien de temps faut-il pour détecter les départs de feu ?
- **Manque :** Aucune source ne donne l'heure d'arrivée des équipes ; seule l'heure d'alerte (`Alerte`) existe.
- **Décision :** Renoncer au délai réel, approximer avec `Alerte`
- **Raison :** Aucune source ne donne l'arrivée des équipes.
- **Ce que la décision coûte :** On ne mesure pas le délai de détection, seulement le moment de l'alerte.
- **Termes du glossaire touchés :** à vérifier (date d'alerte)


## Décision 005 — [D1 : zones les plus exposées]

- **Date :** 18-11-2026
- **Auteurs :** Ange, Dorra
- **Question :** D1 — Quelles zones de Haute-Garonne sont les plus exposées aux départs de feu ?
- **Manque :** Colonne `Commune` de la BDIFF non vérifiée dans le CSV.
- **Décision :** Collecter
- **Raison :** BDIFF par commune + Admin Express + BD Forêt V2.
- **Ce que la décision coûte :** Temps de téléchargement, nettoyage et jointures ; feux non renseignés sous-estimés.
- **Termes du glossaire touchés :** aucun


## Décision 006 — [D2 : lien niveau de danger / départs de feu]

- **Date :** 18-11-2026
- **Auteurs :** Ange, Dorra
- **Question :** D2 — Quel est le lien entre le niveau de la Météo des forêts et les départs de feu réels ?
- **Manque :** Archives de la Météo des forêts disponibles seulement depuis juin 2024.
- **Décision :** Approximer
- **Raison :** Historique commun limité à 2024-2026.
- **Ce que la décision coûte :** Analyse sur 2 à 3 saisons ; une association ne prouve pas une causalité.
- **Termes du glossaire touchés :** aucun


## Décision 007 — [D3 : Haute-Garonne vs Occitanie vs France]

- **Date :** 18-11-2026
- **Auteurs :** Ange, Dorra
- **Question :** D3 — Comment se comporte la Météo des forêts en Haute-Garonne par rapport à l'Occitanie et au reste de la France ?
- **Manque :** Aucun manque bloquant.
- **Décision :** Collecter
- **Raison :** Météo des forêts suffit (96 départements).
- **Ce que la décision coûte :** Période courte (2024-2026) ; différences climatiques entre départements.
- **Termes du glossaire touchés :** aucun

## Décision 007 — [Proposition d'architecture]

- **Date :** 18-11-2026
- **Auteurs :** Ange
- **Question :** Aucune
- **Manque :** 
- **Décision :** A valider 
- **Raison :** 
- **Ce que la décision coûte :** Premier jet d'une architecture
- **Termes du glossaire touchés :** aucun