-- 0001 : schémas, PostGIS et tables brutes (bronze). Ne jamais modifier les données bronze.
create extension if not exists postgis with schema extensions;

create schema if not exists bronze;
create schema if not exists silver;
create schema if not exists gold;

-- Réponses d'API brutes : une ligne par appel (ou par page)
create table if not exists bronze.api_calls (
    id           bigint generated always as identity primary key,
    source       text        not null,
    url          text        not null,
    fetched_at   timestamptz not null default now(),
    http_status  integer,
    payload      jsonb       not null,
    payload_hash text        not null,
    unique (source, payload_hash)
);

-- Lignes de fichiers brutes (CSV, exports) : une ligne par enregistrement, colonnes d'origine conservées en JSON
create table if not exists bronze.raw_rows (
    id          bigint generated always as identity primary key,
    source      text        not null,
    source_file text        not null,
    loaded_at   timestamptz not null default now(),
    row         jsonb       not null
);
create index if not exists raw_rows_source_file_idx on bronze.raw_rows (source, source_file);
