
# Feux de foret Occitanie

## 1.Les questions:
1) Comment sont calculés les seuils actuels de déclenhecment des dispositifs renforcés ?
2) A quelle fréquence a - ton les feux de forêt dans la région ?
3) Quelle superficie/ étendue de forêt est-elle perdue chaque apparition des feux de forêt ?
4) combien de temps mettent les équipes en place pour détecter les départs des feux de forêt dans la région?


## 2. Les termes inconnus:
Météo de forêt : un service d'information lancé par Météo-France pour sensibiliser le public et prévenir le risque d'incendies de forêt et de végétation
grain : le niveau de détail des données
emprise : l'étendue de la donnée, sa couverture
guet : surveillance

## 3. Les besoins:
La décision à éclairer, en une phrase : où concentrer les moyens humains et financiers du SDIS 31 pour la saison feux 2027, et à partir de quel niveau de la Météo des forêts déclencher le dispositif renforcé.

Ce qui manque dans la commande pour y répondre :
- Le seuil actuel : à quel niveau de la Météo des forêts le dispositif renforcé se déclenche-t-il aujourd'hui, et comment a-t-il été fixé ?
- La définition de « feu de forêt » et de « départ de feu » : les interventions pour feu de végétation, de broussailles ou de culture sont-elles incluses ? Sous quel seuil de surface ?
- Le périmètre de « notre département » : le territoire administratif de la Haute-Garonne ou la zone d'intervention du SDIS 31 ?
- Le périmètre de « la région » : l'Occitanie (13 départements) et les départements limitrophes sont-ils tous concernés ?
- Les moyens disponibles et leur coût : effectifs, patrouilles, guet, budget, et ce que coûte un jour de dispositif renforcé.
- Le critère de réussite : à partir de quand le seuil est-il jugé bon (moins de fausses alertes, moins de feux sans alerte, ou les deux) ?
- L'horizon et la période d'étude : combien d'années d'historique, quelle saison (été seul ou toute l'année) ?
- Hypothèse à confirmer : un été 2027 comparable à 2026 voire pire, donc l'historique des étés précédents reste représentatif.
- Les données internes du SDIS 31 (heures d'alerte et d'arrivée des équipes, mode de détection) : sont-elles accessibles, et sous quelle forme ?
- Le niveau de détail attendu de la réponse : par commune, par massif ou par département.

## 4. Les données:

| Question | Donnée idéale | Grain (une ligne = ?) | Période | Fraîcheur | Emprise géographique |
|---|---|---|---|---|---|
| 1 | Niveau de l'indice Météo des forêts (et ses composantes) par jour et par zone, mis en regard des départs de feu réellement déclarés, pour comparer le seuil actuel de déclenchement aux jours avec/sans feu | Une ligne = un jour × une zone (département ou massif) | Au moins 10 ans, avec les saisons estivales complètes | Mise à jour quotidienne, historique à jour jusqu'à la saison précédente | Haute-Garonne, autres départements d'Occitanie, France entière pour comparer |
| 2 | Liste des départs de feu de forêt avec leur date et leur commune | Une ligne = un départ de feu | Au moins 10 ans (2015 à 2026) | Annuelle au plus tard, idéalement mise à jour en continu | Occitanie, par département et par commune |
| 3 | Surface brûlée de chaque feu de forêt, avec le type de végétation touchée | Une ligne = un feu | Au moins 10 ans | Annuelle | Occitanie, par commune |
| 4 | Heures d'alerte (détection) et d'arrivée des équipes de chaque intervention pour feu de forêt, et mode de détection (guet, patrouille, appel) | Une ligne = une intervention | Au moins 5 ans | Annuelle, idéalement quasi temps réel | SDIS d'Occitanie, au minimum le SDIS 31 |


## 5. Confrontation aux sources

### Matrice

Sources de l'inventaire : BDIFF, Interventions SDIS, Météo des forêts (API et archives), Statistiques nationales des SDIS, Pyronear, PDPFCI, BD Forêt V2, Admin Express, EFFIS, NASA FIRMS. Les fiches sont dans `docs/sources/`. Les sources non retenues du défi (BD TOPO, Corine Land Cover, AROME, etc.) n'ont pas de rapport direct avec mes quatre questions.

| Question / Source | BDIFF | Interventions SDIS | Météo des forêts | Stats SDIS | Pyronear | PDPFCI | BD Forêt V2 | Admin Express | EFFIS | NASA FIRMS |
|---|---|---|---|---|---|---|---|---|---|---|
| 1. Seuils de déclenchement | absent : rubrique « Grain », aucun indice ni seuil | absent : colonnes de compteurs d'interventions par type, aucun seuil | partiel : colonnes `niveau_j1` et `niveau_j2` par département et par jour, mais ni méthode de calcul ni seuil du SDIS 31 (PDF de présentation non lu) | inconnu : documents PDF non lus, rubrique « Clés » : aucune clé commune | absent : images de fumée | inconnu : plan en PDF de 102 pages pour la Haute-Garonne, mesures de prévention possibles, non lu | absent : polygones de formations végétales | absent : limites administratives | absent : indices européens (FWI), pas le seuil du SDIS 31 | absent |
| 2. Fréquence des feux | inconnu : fiche annonce un incendie par ligne depuis 2006, mais colonnes date et commune non vérifiées, et la fiche data.gouv.fr dit « agrégées à la commune » | partiel : colonne `Feux de végétations` par département et par an (Haute-Garonne : 403 en 2024), mais pas de date et mélange avec feux d'herbe | absent : niveaux de danger, aucun feu | partiel : rubrique « Grain » : un document par statistique, niveau de détail variable | absent : images d'entraînement pour la détection, pas de statistique de feux | absent : mesures de prévention | absent : rubrique « Grain » (zone forestière) | absent : sert aux jointures | inconnu : totaux par pays, détail France non vérifié | inconnu : détections satellite, accès non vérifié |
| 3. Surface perdue | inconnu : fiche annonce la surface de chaque incendie, colonne non vérifiée | absent : aucune colonne de surface | absent | absent : rubrique « Grain », documents sans surface par feu (non vérifié en détail) | absent | absent | partiel : surface forestière par zone, pour rapporter les surfaces brûlées, pas la surface perdue | absent | inconnu : base de surfaces brûlées, couverture France non vérifiée | inconnu : points de feux actifs, pas de surface |
| 4. Délai de détection | inconnu : colonnes d'horaires non vérifiées (fiche : localisation, surface, nature) | absent : 71 colonnes de compteurs, aucune date ni heure | absent | inconnu : retours d'expérience (RETEX) possibles, non lus | partiel : colonnes `date`, `camera`, `partner` : date de l'image seulement, pas l'heure d'alerte ; partenaires dont SDIS 12 (Aveyron), pas le SDIS 31 | absent | absent | absent | absent | inconnu : heure de détection satellite possible, non vérifiée |
### Écarts avec la section 4

Pour chaque question, comparez la donnée idéale (section 4) à la meilleure source disponible, critère par critère : écrivez « idéal → réel », ou « = » si les deux correspondent.

| Question | Meilleure source | Grain | Période | Fraîcheur | Emprise |
| -------- | ---------------- | ----- | ------- | --------- | ------- |
| 1        | Archives de la Météo des forêts | jour × département = | 10 ans → 2024 à 2026 (2 à 3 saisons) | quotidienne = | département (96 en métropole) = |
| 2        | BDIFF (à vérifier) ; sinon Interventions SDIS | un départ de feu → un département × un an pour Interventions SDIS (BDIFF : un incendie, non vérifié) | 10 ans → 2008 à 2024 pour Interventions SDIS ; BDIFF : 2006 à 2022 ou 2025 selon les fiches | annuelle = | commune → département pour Interventions SDIS ; BDIFF : commune ou localisation exacte, non vérifié |
| 3        | BDIFF (à vérifier) | un feu = (non vérifié) | 10 ans → 2006 à 2022 ou 2025 (non vérifié) | annuelle = | Occitanie = (non vérifié) |
| 4        | Pyronear (indirect) | une intervention → une image | 5 ans → 2023 à 2025 | annuelle ou quasi temps réel → non renseignée | SDIS 31 → SDIS 07, 12, 77 et Force 06 : pas de SDIS 31 |

### Décisions

| Question | Ce qui manque | Décision | Pourquoi | Ce que la décision coûte |
|---|---|---|---|---|
| 1. Seuils de déclenchement | Le seuil actuel du SDIS 31 et la méthode de calcul de l'indice ; aucune source ne les donne | collecter | Seul le SDIS 31 connaît son seuil. Lire en plus le PDF de présentation de la Météo des forêts (jeu « Archives ») et le PDPFCI de la Haute-Garonne | Dépend d'une réponse du SDIS 31 ; sans réponse, tester plusieurs seuils (niveaux 2, 3 et 4) sans connaître le seuil actuel |
| 2. Fréquence des feux | Vérifier d'abord les colonnes de la BDIFF (date de chaque feu, commune) ; sinon seulement un compteur annuel par département | approximer | Les `Feux de végétations` par département et par an (Interventions SDIS) donnent un ordre de grandeur en attendant la BDIFF | Mélange feux de forêt et feux d'herbe ; impossible de croiser avec l'indice journalier |
| 3. Surface perdue | Surface par feu : colonne de la BDIFF non vérifiée | collecter | Télécharger l'export BDIFF d'Occitanie et vérifier la colonne de surface. Si absente, EFFIS (gros feux seulement) en proxy | Temps de téléchargement et de nettoyage ; petits feux absents si repli sur EFFIS |
| 4. Délai de détection | Heures d'alerte et d'arrivée des équipes : aucune source ouverte ne les contient | renoncer | Donnée interne aux SDIS, non publiée. Reformuler : « où et quand les feux démarrent-ils ? » (BDIFF), sauf si le SDIS 31 transmet ses horodatages | Plus de mesure du délai ; on ne peut pas juger l'efficacité de la détection |
