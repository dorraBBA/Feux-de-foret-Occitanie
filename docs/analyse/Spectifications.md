
# Spécification — [Occitanie]

Groupe : Occitanie classe 2 · Version du 18-11-2026

## 1. La décision

Le commanditaire, la décision à éclairer et l'échéance, en trois phrases.

## 2. Les questions retenues

| N° | Question | Décision qu'elle éclaire | Proposée par |
|---|---|---|---|

Questions écartées, avec la raison et le renvoi au journal :

## 3. Les sources retenues

| Source | Fiche | Localisation (URL, API, fichier) | Mode de récupération | Champs utiles | Questions servies |
|---|---|---|---|---|---|

Sources écartées, avec la raison :

## 4. Les sources de référence

Pour chaque donnée présente dans plusieurs sources :

| Donnée | Sources concernées | Source de référence | Pourquoi |
|---|---|---|---|

## 5. Les manques

Matrice complète : `docs/sources/matrice.md`

| Question | Ce qui manque | Décision | Ce que la décision coûte | Journal |
|---|---|---|---|---|

## 6. Les incohérences repérées et les transformations nécessaires

| Sources | Nature (format de date, unité, recouvrement, clé) | Exemple tiré du fichier | Transformation nécessaire |
|---|---|---|---|

## 7. Conformité

| Champ | Source | Question qui le justifie | Décision (garder, pseudonymiser, écarter) | Technique |
|---|---|---|---|---|

Risque de ré-identification par croisement : 

## 8. Historisation

| Source | Ce qui change dans le temps | Exemple | Ce que l'on garde |
|---|---|---|---|

## 9. Entrées attendues et qualité

Pour chaque source retenue, ce que vous exigez d'elle :

| Source | Champs requis | Champs pouvant être vides (raison) | Clé et grain | Référentiel attendu | Période attendue |
|---|---|---|---|---|---|

Profil de chaque source : taux de remplissage des champs requis, entités présentes comparées au référentiel, bornes des dates. Chaque chiffre vient du fichier de votre région. Fichier ou requête qui l'a produit : 

Règles de qualité (trois au minimum, sur deux niveaux de complétude et une autre dimension) :

| N° | Source | Niveau ou dimension | Sélecteur | Prédicat | Seuil (et sa justification) | Décision (bloquer, alerter, tolérer) |
|---|---|---|---|---|---|---|

Ce que ces indicateurs de qualité ne permettent pas d'affirmer :

## 10. Architecture

Schéma : `docs/architecture.md` (diagramme Mermaid ou image)

| Couche | Rôle | Contenu envisagé | Outil | Questions servies |
|---|---|---|---|---|
| Sources | Ce que vous recevez, tel quel | | | |
| Données brutes | Conservées sans modification | | | |
| Données nettoyées | Types, formats, doublons, valeurs manquantes traitées | | | |
| Données consolidées | Sources croisées au même grain | | | |
| Données prêtes pour l'analyse | Ce que lisent les indicateurs | | | |
| Restitution | Ce que lit le commanditaire | | | |

Si la fréquence de mise à jour des données est importante pour votre projet, ajoutez une colonne au tableau. De même pour toute autre dimension qui vous paraît utile.

Hypothèses : ce que vous pensez construire sans l'avoir encore vu en cours, et pourquoi :

## 11. Contraintes

| Contrainte | Comment l'architecture la respecte |
|---|---|
| Outils gratuits uniquement | |
| Conserver les données brutes | |
| Pouvoir retraiter sans rappeler les API | |
| Données incomplètes | |
| Accès à une source limité ou interrompu | |

## 12. Planning de réalisation

| Jalon | Couche | Responsable | Date | Preuve qu'il est atteint |
|---|---|---|---|---|

Exemple de preuve : une table qui se charge, un test qui passe, une table prête pour l'analyse.
Ce qui est prévu pendant les trois semaines sans cours :

## 13. Glossaire

Lien : `docs/glossaire.md` · Nombre de termes : · Termes encore « à vérifier » :

## 14. Limites connues

Ce que cette spécification ne permettra pas de dire au commanditaire, et pourquoi.
