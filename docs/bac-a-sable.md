Les seuils se calculs en fonctions de l'Indice Forêt Météo  (IFM)
Quatres couleurs : vert, jaune, orange et rouge
Cependant, une même valeur d’IFM peut conduire à une appréciation différente selon le département, la saison, la végétation et la répartition géographique du danger.

## Diagramme de séquence : entrepôt de données (Bronze / Silver / Gold)

```mermaid
sequenceDiagram
    autonumber
    actor Dev as Équipe
    participant Src as Sources (data.gouv.fr, BDIFF, Météo des forêts)
    participant Ing as Ingestion (Python)
    participant Bronze as Bronze (CSV / JSON d'origine)
    participant Silver as Silver (Parquet)
    participant DB as DuckDB (SQL)
    participant Gold as Gold (DuckDB + Parquet)
    participant BI as Power BI / Jupyter

    Dev->>Ing: Lance le script d'ingestion
    Ing->>Src: Télécharge les fichiers
    Src-->>Ing: CSV, CSV.gz, Shapefile
    Ing->>Bronze: Stocke les fichiers bruts, sans modification
    Dev->>DB: Lance les transformations Silver
    DB->>Bronze: Lit les fichiers bruts
    Note over DB: Nettoyage : encodage, séparateurs, num_dep sur 2 caractères, dates UTC, clés département et commune
    DB->>Silver: Écrit les tables nettoyées en Parquet
    Dev->>DB: Lance les transformations métier (SQL)
    DB->>Silver: Lit les tables nettoyées
    Note over DB: Jointures Admin Express, niveaux de danger et feux (BDIFF), agrégats par niveau et par commune
    DB->>Gold: Écrit les tables d'analyse
    BI->>Gold: Interroge les tables Gold
    Gold-->>BI: Résultats (A1 à A3, D1 à D3)
    BI-->>Dev: Tableaux de bord et analyses
```
