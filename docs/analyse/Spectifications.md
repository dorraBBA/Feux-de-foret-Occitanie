
# Spécification — [Occitanie]

Groupe : Occitanie classe 2 · V0.0.1 18-11-2026


## 1. La décision

Le commanditaire est le SDIS 31 (Haute-Garonne), pour la saison feux 2027.

Décision à éclairer : 
1)  où concentrer les moyens de surveillance et de prévention,
2) à partir de quel niveau de la Météo des forêts déclencher le dispositif renforcé. 

Echéance : être prêt pour la saison 2027 
## 2. Les questions retenues

| N° | Question | Décision qu'elle éclaire | Proposée par |
|---|---|---|---|
| A1 | Comment sont calculés les seuils actuels de déclenchement des dispositifs renforcés ? | Conserver ou ajuster le seuil actuel | Ange |
| A2 | Quelle superficie de forêt est perdue à chaque feu ? | Gravité des feux : renforcer la lutte ou la prévention | Ange |
| A3 | Combien de temps faut-il pour détecter les départs de feu dans la région ? | Renforcer ou maintenir la détection | Ange |
| D1 | Quelles zones de Haute-Garonne sont les plus exposées aux départs de feu ? | Où concentrer les moyens | Dorra |
| D2 | Quel est le lien entre le niveau de la Météo des forêts et les départs de feu réels ? | Utiliser l'indice pour anticiper ou le compléter | Dorra |
| D3 | Comment se comporte la Météo des forêts en Haute-Garonne par rapport à l'Occitanie et à la France ? | Organisation spécifique ou stratégie régionale | Dorra |
| M1 | À partir de quel niveau de danger observe-t-on une hausse nette des départs de feu en Occitanie ? | Niveau de déclenchement du dispositif renforcé | Mouad |
| M2 | Comment renforcer la surveillance à partir du niveau de danger ? | Organisation des patrouilles et de la détection | Mouad |
| M3 | Comment la fréquence mensuelle des départs de feu évolue-t-elle au cours de l'année ? | Effectifs et matériel par période | Mouad |

Les questions M1 à M3 sont retenues mais pas encore confrontées aux sources (matrice de Mouad en attente). M1 recoupe A1 et D2.

Questions écartées, avec la raison et le renvoi au journal :

- Q « fréquence des feux » (Ange, question d'origine) et Q « niveau de danger pour déclencher » (Dorra) : non retenues, car elles recoupent M3 et M1/A1. Voir décision 001 du journal.
- Autres questions d'origine non retenues : voir décision 001 (9 questions retenues sur 12).

## 3. Les sources retenues

| Source | Fiche | Localisation (URL, API, fichier) | Mode de récupération | Champs utiles | Questions servies |
|---|---|---|---|---|---|
| BDIFF | `fiche-BDIFF.md` | `bdiff.agriculture.gouv.fr/incendies` (export CSV en zip) ; jeu sur data.gouv.fr | Téléchargement manuel de l'export, puis dépôt en Bronze | `Alerte` (date et heure), `Département`, `Commune`, `Surface`, `Nature` (non vérifiés dans le CSV) | A2, A3 (partiel), D1, D2, M3 |
| Météo des forêts, archives | `fiche-Archives-meteo-des-forets.md` | data.gouv.fr : `mdf_2024.csv.gz`, `mdf_2025.csv.gz`, `mdf_2026.csv.gz` | Téléchargement (script Python) | `date`, `num_dep`, `nom_dep`, `niveau_j1`, `niveau_j2` | A1 (partiel), D2, D3, M1 |
| Météo des forêts, API | `fiche-météo_des_forêts.md` | API Météo des forêts (voir fiche) | Appel API quotidien, stockage des réponses (à confirmer) | niveaux de danger par département | D2, D3, M1 |
| Interventions SDIS | `fiche-Interventions-SDIS.md` | data.gouv.fr : `interventionsAAAA.csv` (2008 à 2024) | Téléchargement (script Python) | `Numéro`, `Département`, `Année`, `Feux de végétations`, `Fausses alertes` | D1 (approximation), D2 (approximation), M3 (approximation) |
| Admin Express | `fiche-Admin-Express.md` | IGN, data.gouv.fr (mise à jour mensuelle) | Téléchargement unique, versionné par édition | Codes et limites des communes, départements, régions | D1, D3 (jointures) |
| BD Forêt V2 | `fiche-BD-Foret-V2.md` | IGN (Shapefile, millésimes 2007 à 2018) | Téléchargement unique | Formations végétales, surface forestière | A2 (rapporter les surfaces), D1 |
| PDPFCI Haute-Garonne | `fiche-PDPFCI.md` | PDF de 102 pages (Haute-Garonne 2019–2029) | Lecture manuelle, extraction des critères | Mesures de prévention, zones à risque | A1, M2 (sous réserve de lecture) |
| Pyronear | `fiche-Images_de_départs_de_feux-SDIS-2024.md` | Jeu d'images sur data.gouv.fr | Téléchargement des métadonnées | `date`, `camera`, `partner` | A3 (partiel) |

Sources écartées, avec la raison :

- Statistiques nationales des SDIS : PDF sans clé commune, non lus ; à réintégrer si la lecture montre des retours d'expérience utiles pour A3.
- EFFIS : indices européens (FWI) et surfaces brûlées, mais couverture France et licence non vérifiées ; second avis possible sur A2.
- NASA FIRMS : accès non vérifié, pas de surface ; ne répond à aucune question de façon vérifiée.
- Corine Land Cover : occupation des sols qui double BD Forêt V2 pour D1 ; fiche présente mais non retenue en V0.
- Sources du défi sans rapport direct avec les questions (BD TOPO, AROME / ARPEGE, etc.) : non retenues, car non nécessaires pour la V0. Les hypothèses les citent comme compléments possibles.

## 4. Les sources de référence

| Donnée | Sources concernées | Source de référence | Pourquoi |
|---|---|---|---|
| Départs de feu (date, commune) | BDIFF, Interventions SDIS, Pyronear, EFFIS | BDIFF | Un incendie par ligne avec date, heure et commune ; les autres sources sont agrégées ou partielles |
| Surface brûlée | BDIFF, EFFIS, BD Forêt V2 | BDIFF | Surface par incendie ; BD Forêt V2 sert seulement à rapporter à la surface forestière |
| Niveau de danger | Météo des forêts (archives et API), EFFIS | Météo des forêts | C'est l'indice utilisé par le SDIS ; EFFIS a une autre échelle |
| Limites départementales et communales | Admin Express, Interventions SDIS, BDIFF | Admin Express | Référentiel officiel IGN, sert aux jointures |
| Volume annuel de feux de végétation | Interventions SDIS, BDIFF | BDIFF (pour les feux de forêt), Interventions SDIS (pour les feux de végétation au sens large) | Définitions différentes : à ne pas additionner |

## 5. Les manques

Matrice complète : `docs/sources/matrice.md`

| Question | Ce qui manque | Décision | Ce que la décision coûte | Journal |
|---|---|---|---|---|
| A1 | Méthode et seuil du SDIS 31 | Collecter | Dépend de la réponse du SDIS 31 | Décision 002 |
| A2 | Colonne `Surface` de la BDIFF non vérifiée ; définitions différentes avant et après 2023 | Collecter | Temps de nettoyage ; surfaces non comparables entre périodes | Décision 003 |
| A3 | Heure d'arrivée des équipes : aucun délai réel de détection | Renoncer au délai réel, approximer avec `Alerte` | On mesure le moment de l'alerte, pas le délai | Décision 004 |
| D1 | Colonne `Commune` de la BDIFF non vérifiée dans le CSV | Collecter | Jointures et nettoyage ; feux non renseignés sous-estimés | Décision 005 |
| D2 | Archives météo seulement depuis juin 2024 | Approximer | 2 à 3 saisons ; association, pas causalité | Décision 006 |
| D3 | Aucun manque bloquant | Collecter | Période courte (2024–2026) | Décision 007 |
| M1 à M3 | Non confrontées aux sources | En attente de la matrice de Mouad | À définir | À saisir |

## 6. Les incohérences repérées et les transformations nécessaires

| Sources | Nature (format de date, unité, recouvrement, clé) | Exemple tiré du fichier | Transformation nécessaire |
|---|---|---|---|
| Météo des forêts 2024 / 2026 | Séparateur | `,` en 2024, `;` en 2026 | Lire chaque fichier avec son séparateur, puis unifier |
| Météo des forêts 2024 / 2026 | Clé département | `num_dep` = « 1 » en 2024, « 01 » en 2026 | Compléter sur 2 caractères |
| Météo des forêts | Format de date | Horodatage UTC avec heure | Convertir en date locale (Europe/Paris), garder la date du jour |
| Interventions SDIS | Encodage et nombres | Latin-1 ; milliers avec espace | Lire en Latin-1, retirer les espaces des nombres |
| Interventions SDIS | Clé / nom de région | Noms de région différents avant 2016 | Joindre sur `Numéro`, pas sur le nom |
| Interventions SDIS / BDIFF | Définition | `Feux de végétations` mélange feux d'herbe et de forêt, BDIFF = feux de forêt | Ne pas additionner ; documenter dans le glossaire |
| BDIFF | Unité / définition de surface | Définition différente avant 2023 et en aire méditerranéenne (11, 30, 34, 48, 66) | Colonne « période de définition » et indicateur d'aire |
| BDIFF / data.gouv.fr | Recouvrement de période | Fiche : 2006 à 2025 ; data.gouv.fr : 2006 à 2022 | Confirmer sur l'export ; retenir l'export officiel |
| Météo des forêts / BDIFF | Recouvrement | Météo depuis juin 2024 ; BDIFF depuis 2006 | Croiser sur 2024 à 2026 seulement |
| BDIFF / Admin Express | Clé commune | Code commune INSEE vs nom (à vérifier dans l'export) | Joindre sur le code INSEE ; recoder les fusions de communes |

## 7. Conformité

| Champ | Source | Question qui le justifie | Décision (garder, pseudonymiser, écarter) | Technique |
|---|---|---|---|---|
| `Commune` | BDIFF | D1 | Garder | Aucune : donnée publique non personnelle |
| `Alerte` (date et heure) | BDIFF | A3, D2 | Garder | Aucune |
| `Nature` (cause) | BDIFF | Aucune question retenue | Écarter en Silver | Ne pas charger la colonne dans les tables d'analyse |
| `camera`, `partner` | Pyronear | A3 | Garder | Aucune : identifiants de caméras |
| Images | Pyronear | Aucune | Écarter | Ne pas stocker les images, seulement les métadonnées |
| Autres champs | Météo des forêts, Interventions SDIS, Admin Express, BD Forêt V2 | Questions D1 à D3 | Garder | Aucune : données agrégées ou géographiques |

Risque de ré-identification par croisement : faible, aucune donnée nominative. Une petite commune croisée avec la date, l'heure et la cause d'un feu pourrait toutefois désigner un événement précis ou une personne ; d'où le retrait de `Nature` et l'agrégation par mois ou par zone en restitution. À confirmer en groupe.

## 8. Historisation

| Source | Ce qui change dans le temps | Exemple | Ce que l'on garde |
|---|---|---|---|
| BDIFF | Campagne annuelle validée de décembre à avril N+1 ; corrections possibles | Données partielles de l'année N-1 | Chaque export daté (une copie par date de téléchargement) |
| Météo des forêts | Un fichier annuel, saison de juin à octobre ; nouveau fichier chaque année | 2024 du 3 juin au 30 septembre ; 2026 du 28 mai au 5 octobre | Tous les fichiers annuels ; réponses de l'API conservées chaque jour |
| Interventions SDIS | Un CSV par année, noms de région différents avant 2016 | `interventions2014.csv` vs `interventions2024.csv` | Tous les millésimes, clé `Numéro` |
| Admin Express | Mise à jour mensuelle, fusions de communes | Éditions depuis 2017 | L'édition utilisée, avec sa date |
| BD Forêt V2 | Millésimes 2007 à 2018 | Millésime par département | Le millésime utilisé |

## 9. Entrées attendues et qualité

Pour chaque source retenue, ce que vous exigez d'elle :

| Source | Champs requis | Champs pouvant être vides (raison) | Clé et grain | Référentiel attendu | Période attendue |
|---|---|---|---|---|---|
| BDIFF | `Alerte`, `Département`, `Commune`, `Surface` | `Surface` pour les données partielles ou non valides | Un incendie, identifiant à confirmer | Admin Express (code commune) | 2006 à N-1 (2020 à 2025 pour l'analyse) |
| Météo des forêts (archives) | `date`, `num_dep`, `niveau_j1` | `niveau_j2` en fin de saison (à confirmer) | Un département par jour | Admin Express (96 départements) | 2024 à 2026, juin à octobre |
| Interventions SDIS | `Numéro`, `Département`, `Année`, `Feux de végétations` | Aucun attendu | Un service d'incendie par année (99 lignes) | Admin Express (départements) | 2008 à 2024 |
| Admin Express | Code et nom des communes, départements | Aucun | Une commune | — | Édition la plus récente |
| BD Forêt V2 | Type de formation, géométrie | Essence | Un polygone | Admin Express | 2007 à 2018 |
| Pyronear | `date`, `camera`, `partner` | `partner` (à vérifier) | Une image | — | 2024 |
| PDPFCI | Document unique | — | Un document | — | 2019 à 2029 |

Profil de chaque source : taux de remplissage des champs requis, entités présentes comparées au référentiel, bornes des dates. Chaque chiffre vient du fichier de votre région. Fichier ou requête qui l'a produit : à produire (notebook ou requête DuckDB sur le Bronze). Chiffres déjà vérifiés : Météo des forêts 2024 du 3 juin au 30 septembre et 96 départements ; Interventions SDIS 2024 avec 99 lignes et 71 colonnes, Haute-Garonne à 403 feux de végétation. Le profil de la BDIFF reste à faire (export CSV non ouvert).

Règles de qualité (trois au minimum, sur deux niveaux de complétude et une autre dimension) :

| N° | Source | Niveau ou dimension | Sélecteur | Prédicat | Seuil (et sa justification) | Décision (bloquer, alerter, tolérer) |
|---|---|---|---|---|---|---|
| R1 | Météo des forêts | Complétude des entités | Chaque jour de saison | Les 96 départements sont présents | 100 % : D3 compare les territoires | Bloquer |
| R2 | Météo des forêts | Complétude des valeurs | Colonne `niveau_j1` | Non vide et entre 1 et 4 | 99 % : un jour sans niveau fausse D2 | Alerter |
| R3 | BDIFF | Complétude des valeurs | Colonnes `Alerte`, `Commune`, `Surface` | Non vides | 95 % : en dessous, D1 et A2 sont biaisées | Alerter |
| R4 | BDIFF | Cohérence (autre dimension) | Colonne `Commune` | Le code existe dans Admin Express | 98 % : jointure nécessaire à D1 | Alerter |
| R5 | Interventions SDIS | Validité | Colonne `Feux de végétations` | Entier positif ou nul | 100 % | Bloquer |
| R6 | Météo des forêts, BDIFF | Fraîcheur et période | Date | Dates dans l'intervalle attendu (2024 à 2026 pour la météo) | 100 % | Bloquer |

Les seuils sont des propositions de la V0, à ajuster une fois les profils produits.

Ce que ces indicateurs de qualité ne permettent pas d'affirmer : qu'un feu non déclaré est absent des données (l'exhaustivité de la BDIFF avant 2020 hors aire méditerranéenne est mise en garde par l'éditeur), ni que les surfaces sont exactes (estimées ou mesurées), ni que les niveaux de danger correspondent au seuil réellement appliqué par le SDIS 31.

## 10. Architecture

Schéma dans `docs/architecture.md`

| Couche | Rôle | Contenu envisagé | Outil | Questions servies | Fréquence de mise à jour |
|---|---|---|---|---|---|
| Sources | Ce que vous recevez, tel quel | BDIFF, Météo des forêts, Interventions SDIS, Admin Express, BD Forêt V2, Pyronear, PDPFCI | data.gouv.fr, API, sites IGN | Toutes | Météo : quotidienne en saison ; BDIFF : annuelle ; SDIS : annuelle |
| Données brutes (Bronze) | Conservées sans modification | Fichiers CSV, CSV.gz, Shapefile, réponses API, avec date de téléchargement | Python, fichiers hors Git | Toutes | À chaque téléchargement |
| Données nettoyées (Silver) | Types, formats, doublons, valeurs manquantes traitées | Tables Parquet : séparateurs, encodage, `num_dep`, dates UTC vers date locale | DuckDB, Parquet (Pandas si besoin) | Toutes | À chaque nouveau Bronze |
| Données consolidées | Sources croisées au même grain | Feux par commune et par jour joints aux niveaux de danger ; départements joints à Admin Express | DuckDB SQL | A2, D1, D2, D3, M1, M3 | À la demande |
| Données prêtes pour l'analyse (Gold) | Ce que lisent les indicateurs | Feux par niveau de danger, par commune, par mois ; distribution des surfaces ; comparaison des départements | DuckDB, Parquet | A2, D1 à D3, M1, M3 | À la demande |
| Restitution | Ce que lit le commanditaire | Tableaux de bord, cartes, synthèses | Power BI, Jupyter Notebook | Toutes | À chaque livraison |

Hypothèses : 

- Architecture Bronze / Silver / Gold avec Python, DuckDB, Parquet et Power BI : choix du groupe, le cours ne pose aucune restriction (à saisir dans le journal).
- dbt : facultatif, à décider plus tard ; commencer par des fichiers SQL versionnés dans Git.
- Pandas ou Polars : un seul des deux ; Pandas suffit pour les volumes.
- Power BI lit mal DuckDB et Parquet : export du Gold en CSV ou connecteur ODBC à tester.

## 11. Contraintes

| Contrainte | Comment l'architecture la respecte |
|---|---|
| Outils gratuits uniquement | Python, DuckDB, Parquet, Git/GitHub, Jupyter sont gratuits ; Power BI Desktop est gratuit (alternative : Metabase ou Streamlit) |
| Conserver les données brutes | Couche Bronze en lecture seule, un fichier par date de téléchargement |
| Pouvoir retraiter sans rappeler les API | Les réponses sont stockées en Bronze ; Silver et Gold se reconstruisent depuis Bronze |
| Données incomplètes | Règles R1 à R6 ; décisions collecter / approximer / renoncer au journal ; limites déclarées en section 14 |
| Accès à une source limité ou interrompu | Dernière version en Bronze ; script de téléchargement relançable ; source de secours (EFFIS) possible |

## 12. Planning de réalisation

| Jalon | Couche | Responsable | Date | Preuve qu'il est atteint |
|---|---|---|---|---|
| J1 Ingestion des sources en Bronze | Données brutes | à définir | à définir | Fichiers présents avec date de téléchargement |
| J2 Ouverture de l'export BDIFF et profil | Données brutes | Ange | à définir | Rapport de profil (colonnes, taux de remplissage, bornes) |
| J3 Tables Silver (Météo des forêts, SDIS, BDIFF) | Données nettoyées | à définir | à définir | Tables Parquet qui se chargent, règles R1 à R6 qui passent |
| J4 Jointures (Admin Express, feux et niveaux de danger) | Données consolidées | à définir | à définir | Table feux × niveau de danger |
| J5 Tables Gold (D1 à D3, A2) | Prêtes pour l'analyse | à définir | à définir | Tables d'indicateurs prêtes |
| J6 Restitution | Restitution | à définir | à définir | Tableau de bord ou notebook |

Exemple de preuve : une table qui se charge, un test qui passe, une table prête pour l'analyse.
Ce qui est prévu pendant les trois semaines sans cours : à définir en groupe (ingestion et profils J1, J2 ; matrice de Mouad ; demande au SDIS 31 pour A1).

## 13. Glossaire

Lien : `docs/Glossaire.md` · Nombre de termes : à compter · Termes encore « à vérifier » : feu de forêt, fausse alerte, date d'alerte, surface brûlée (divergences entre BDIFF, SDIS et EFFIS).

## 14. Limites connues

Ce que cette spécification ne permettra pas de dire au commanditaire, et pourquoi :

- Le seuil réel du SDIS 31 et ses coûts : aucune source ouverte ne les donne (A1).
- Le délai de détection réel : seule l'heure d'alerte au CODIS existe, pas l'arrivée des équipes (A3).
- Une relation causale entre niveau de danger et départs de feu : historique commun de 2 à 3 saisons (D2, M1).
- Les feux non déclarés ou mal renseignés, surtout avant 2020 hors aire méditerranéenne (D1, A2).
- Des surfaces comparables sur toute la période : définitions différentes avant et après 2023.
- Les questions M1 à M3 n'ont pas été confrontées aux sources ; leur couverture est donc non établie.
