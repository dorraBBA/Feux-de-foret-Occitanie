# Préparation des données

Comment les données passent de `bronze` (brut) à `silver` (nettoyé), puis à `gold` (prêt pour les KPIs et Power BI).

Chaque passage est écrit en SQL dans `supabase/migrations/`. Le script `load_bronze.py` charge `bronze`, puis appelle la fonction `silver.refresh_*()` de la source.

## Bronze → Silver : nettoyage

Chaque source a sa fonction `silver.refresh_*()`. Elle lit `bronze.raw_rows` (ou `bronze.api_calls`), corrige, puis fait un `INSERT … ON CONFLICT DO UPDATE`. On peut donc la relancer sans créer de doublons.

| Problème dans les données brutes | Traitement | Sources |
|---|---|---|
| Tout est du texte (JSON) | Conversion vers `date`, `timestamp`, `integer`, `numeric`, `smallint` | toutes |
| Code département « 1 » ou « 01 » | `lpad(…, 2, '0')` | météo, BDIFF, SDIS |
| Code INSEE sur 4 caractères | `lpad(…, 5, '0')` | BDIFF |
| Date UTC avec heure (`2024-06-03T00:00…`) | On garde les 10 premiers caractères (`left(…, 10)::date`) | météo |
| Noms de colonnes différents selon l'année ou l'API (`date` / `Reference_time`, `num_dep` / `dep_code`) | `coalesce(…)` sur les deux noms | météo |
| Milliers séparés par une espace (`1 234`) | `regexp_replace(…, '\D', '', 'g')` : on ne garde que les chiffres | SDIS |
| Virgule décimale | `replace(',', '.')` | BDIFF |
| Chaînes vides | `nullif(…, '')` donne `NULL` | toutes |
| Codes `2a`, `2b` en minuscules, `BSPP`, `BMPM` | `upper()`, conservés comme codes texte | SDIS |
| Fichiers rechargés (doublons) | `distinct on (clé) … order by loaded_at desc` : on garde la ligne la plus récente | toutes |
| Lignes sans clé (totaux) | Filtre `where code is not null` : explique les 40 lignes SDIS écartées (950 sur 990) | SDIS |
| Géométrie en texte (WKT) | `st_geomfromtext` avec le bon système (Lambert 93, EPSG:2154) | carroyage DFCI |
| Centre de commune en GeoJSON | `st_geomfromgeojson` en WGS84 (EPSG:4326) | communes |

Les contraintes servent de contrôle : clés primaires (pas de doublon) et `check (niveau between 1 and 4)` sur la météo.

### Traitements faits au chargement (Python)

Ces points sont gérés dans `load_bronze.py`, avant `bronze` :

- Encodage Windows-1252 des CSV SDIS.
- Séparateur `;` ou `,` de la météo, détecté automatiquement.
- Deux lignes d'en-tête de critères dans l'export BDIFF.
- BD Forêt V2 : découpée par commune et agrégée avant chargement, car trop volumineuse (environ 75 000 polygones pour la Haute-Garonne).
- Carroyage DFCI : filtré sur l'Occitanie (18 988 mailles sur 339 264).

## Silver → Gold : pas de nettoyage

Les vues `gold` ne copient rien. Elles filtrent et calculent à partir de `silver`.

| Vue | Traitement |
|---|---|
| `gold.meteo_occitanie`, `gold.incendie_occitanie`, `gold.intervention_sdis_occitanie` | Filtre sur les 13 départements d'Occitanie |
| `gold.incendie_occitanie` | Extrait la date et l'heure d'alerte |
| `gold.commune_haute_garonne` | Filtre le 31, extrait longitude et latitude du point |
| `gold.foret_commune` | Somme des surfaces de forêt et de landes, taux de boisement plafonné à 100 % |

Les KPIs seront calculés à cette étape : formules, jointures entre sources et agrégations.

## Limites connues

- Les surfaces BDIFF ne sont pas corrigées de la différence de définition avant et après 2023.
- Pas de gestion des valeurs aberrantes ni des surfaces à 0.
- La date de la Météo des forêts est la date UTC, sans conversion en heure de Paris.
- La BD Forêt V2 n'est chargée qu'agrégée par commune : la réponse brute de l'API n'est pas conservée.
- Les interventions SDIS s'arrêtent en 2024 (pas de fichier 2025 publié).
