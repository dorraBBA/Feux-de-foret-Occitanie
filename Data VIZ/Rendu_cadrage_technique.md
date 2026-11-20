# Rendu cadrage technique · Groupe

| Rubrique | Votre réponse |
|---|---|
| Groupe (numéro, membres) | N° : . Membres : Ange-Samuel Brou, Dorra Boucharbia, Mouad Arahal |
| Décideur et décision | Le décideur est le SIDS 31 , la décision porte sur : Où concentrer les moyens et à partir de quel niveau de la Météo des forêts faut-il déclencher le dispositif renforcé|
| Lien GitHub | https://github.com/dorraBBA/Feux-de-foret-Occitanie |
| Accès au dépôt | Notre dépôt est publique |

## Sources prévues

| Source (nom exact) | Producteur | Lien | Période | Champs utilisés |
|---|---|---|---|---|
| BDIFF (Base de Données sur les Incendies de Forêts en France) | Ministère de l'Agriculture / DFCI | https://bdiff.agriculture.gouv.fr/incendies (export CSV) | Depuis 2006 (fin de période à confirmer à l'export) | Date d'alerte, département, commune, surface, nature |
| Archives de la Météo des forêts | Météo-France | https://meteofrance.s3.sbg.io.cloud.ovh.net/data/BULLETIN/MDF/mdf_2024.csv.gz (idem `mdf_2025`, `mdf_2026`) | Depuis juin 2024 | `date`, `num_dep`, `nom_dep`, `niveau_j1`, `niveau_j2` |
| Interventions des SDIS (statistiques annuelles) | Ministère de l'Intérieur (data.gouv.fr) | https://www.data.gouv.fr/datasets/interventions-realisees-par-les-services-d-incendie-et-de-secours(jeu « interventions des SDIS ») | Annuelle, depuis 2008 | Département, année, `Feux de végétations` |
| Admin Express (COG) | IGN | https://data.geopf.fr/wfs/ows (couche `ADMINEXPRESS-COG.LATEST:commune`) et https://geo.api.gouv.fr/communes | Version courante, mise à jour mensuelle | `code_insee`, `nom_officiel`, `code_insee_du_departement`, géométrie, centroïde |
| BD Forêt® V2 | IGN | https://data.geopf.fr/wfs/ows (couche LANDCOVER.FORESTINVENTORY.V2:formation_vegetale) | Version courante | Type de formation végétale, essence, géométrie |
| Carroyage DFCI 2 km | DFCI / data.gouv.fr | https://static.data.gouv.fr/resources/carroyage-dfci-france-2-km/20160607-104129/CARRO_DFCI_2x2_L93.7z  a été filtré sur l'occitanie à cause de la taille des données et de la limite de stockage de notre bdd supabase| Référentiel fixe (2016) | Identifiant de maille, géométrie (Lambert 93) |

Sources écartées après évaluation : Statistiques nationales des SDIS (PDF sans clé commune), EFFIS, NASA FIRMS, Corine Land Cover.

## Outils choisis

| Usage | Outil | Pourquoi ce choix |
|---|---|---|
| Base de données | Supabase (PostgreSQL + PostGIS) | Base partagée par les trois membres, SQL, couches `bronze` (brut), `silver` (nettoyé), `gold` (KPIs). PostGIS sert aux calculs de distance (KPI 4.1) |
| Dataviz | Power BI Desktop | Connecteur PostgreSQL vers les vues `gold` ; outil attendu pour le rendu |
| Langage / pipeline | Python (requests, pandas) + migrations SQL versionnées | Téléchargement et appels API rejouables, chargement dans `bronze`, nettoyage en SQL |
| Autre | Git / GitHub | Versionnement, une branche par chantier, migrations et scripts reproductibles |

## Risques identifiés

- Données manquantes ou non ouvertes : la Météo des forêts n'existe que depuis juin 2024 (historique court pour relier danger et départs de feu) ; l'export BDIFF doit être téléchargé à la main et son exhaustivité est douteuse avant 2020 hors aire méditerranéenne ; le seuil actuel de déclenchement du SDIS 31 n'est pas publié ; aucune source de points d'appui n'est ouverte sous forme d'API simple.
- Volume ou accès : l'offre gratuite Supabase est limitée à environ 500 Mo, donc BD Forêt V2 et BD TOPO ne seront chargées que filtrées (Haute-Garonne / Occitanie) ; la connexion Power BI au pooler Supabase demande un certificat et le pilote Npgsql (testée sur un poste, à reproduire sur les autres).
- Autre : les définitions de surface brûlée de la BDIFF changent avant et après 2023 ; les formats de la Météo des forêts varient d'une année à l'autre (séparateur, codes département) et exigent un nettoyage.
