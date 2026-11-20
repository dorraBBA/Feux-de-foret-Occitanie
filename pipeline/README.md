# Pipeline de données

Les données passent par trois couches dans Supabase (PostgreSQL), de la plus brute à la plus prête pour Power BI.

| Couche | Rôle | Exemple | Règle |
|---|---|---|---|
| **Bronze** | Copie brute de la source, telle que reçue | `bronze.raw_rows`, `bronze.api_calls` | On n'y modifie jamais rien |
| **Silver** | Données nettoyées et typées | `silver.meteo_foret`, `silver.commune` | Dates en `date`, codes sur 2 ou 5 caractères, doublons supprimés |
| **Gold** | Vues prêtes pour les KPIs et Power BI | `gold.meteo_occitanie` | Lecture seule, filtrées sur Occitanie |

## Vue d'ensemble

```mermaid
flowchart LR
    A[Sources<br/>CSV, API, exports] -->|Python<br/>load_bronze.py| B[(Bronze<br/>brut)]
    B -->|SQL<br/>silver.refresh_*| C[(Silver<br/>nettoyé)]
    C -->|Vues SQL| D[(Gold<br/>KPIs)]
    D -->|Connecteur PostgreSQL| E[Power BI]
```

## Séquence d'un chargement

```mermaid
sequenceDiagram
    actor U as Utilisateur
    participant P as load_bronze.py
    participant S as Source (CSV ou API)
    participant B as Bronze
    participant Si as Silver
    participant G as Gold
    participant PB as Power BI

    U->>P: python pipeline/load_bronze.py
    P->>S: Télécharge le fichier ou appelle l'API
    S-->>P: Données brutes
    P->>B: Insère telles quelles (source, date, contenu)
    P->>Si: select silver.refresh_*()
    Si->>B: Lit le brut
    Si->>Si: Nettoie (dates, codes, doublons)
    Note over G: Vues SQL, aucune copie
    PB->>G: Lit les vues gold
    G->>Si: Lit les données nettoyées
    G-->>PB: Tables prêtes pour les KPIs
```

## Pourquoi trois couches

- **Bronze** garde la preuve de ce qu'on a reçu : on peut tout retraiter sans retélécharger.
- **Silver** corrige les formats une seule fois, au même endroit pour tout le monde.
- **Gold** calcule les KPIs en SQL, donc Power BI n'a plus qu'à afficher.

## Utilisation

1. Copier `.env.example` en `.env` et renseigner le mot de passe (le fichier est ignoré par Git).
2. `pip install -r pipeline/requirements.txt`
3. `python pipeline/load_bronze.py` (ou `python pipeline/load_bronze.py meteo_foret` pour une seule source).

Les sources sont listées dans `sources.yml`. Les migrations SQL sont dans `supabase/migrations/`.
