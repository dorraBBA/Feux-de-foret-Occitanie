-- 0002 : couches silver (nettoyée) et gold pour la Météo des forêts et les communes.

create table if not exists silver.meteo_foret (
    date_jour date     not null,
    code_dep  char(2)  not null,
    nom_dep   text,
    niveau_j1 smallint check (niveau_j1 between 1 and 4),
    niveau_j2 smallint check (niveau_j2 between 1 and 4),
    primary key (date_jour, code_dep)
);

create table if not exists silver.commune (
    code_insee char(5) primary key,
    nom        text not null,
    code_dep   char(2) not null,
    centre     extensions.geometry(Point, 4326)
);

-- Les CSV annuels et l'API n'ont pas les mêmes noms de colonnes ni les mêmes formats (num_dep « 1 » ou « 01 », date UTC avec heure)
create or replace function silver.refresh_meteo_foret() returns bigint
language plpgsql as $$
declare n bigint;
begin
    insert into silver.meteo_foret (date_jour, code_dep, nom_dep, niveau_j1, niveau_j2)
    select distinct on (d, c)
           d, c, nom, j1, j2
    from (
        select left(coalesce(row->>'date', row->>'Reference_time'), 10)::date            as d,
               lpad(coalesce(row->>'num_dep', row->>'dep_code'), 2, '0')                 as c,
               nullif(row->>'nom_dep', '')                                               as nom,
               nullif(row->>'niveau_j1', '')::numeric::smallint                          as j1,
               nullif(row->>'niveau_j2', '')::numeric::smallint                          as j2,
               loaded_at
        from bronze.raw_rows
        where source = 'meteo_foret'
    ) t
    where d is not null and c is not null
    order by d, c, loaded_at desc
    on conflict (date_jour, code_dep) do update
        set nom_dep = excluded.nom_dep, niveau_j1 = excluded.niveau_j1, niveau_j2 = excluded.niveau_j2;
    get diagnostics n = row_count;
    return n;
end $$;

create or replace function silver.refresh_commune() returns bigint
language plpgsql as $$
declare n bigint;
begin
    insert into silver.commune (code_insee, nom, code_dep, centre)
    select distinct on (e->>'code')
           e->>'code', e->>'nom', left(e->>'code', 2),
           extensions.st_setsrid(extensions.st_geomfromgeojson((e->'centre')::text), 4326)
    from bronze.api_calls a, jsonb_array_elements(a.payload) e
    where a.source = 'communes_geo_api'
    order by e->>'code', a.fetched_at desc
    on conflict (code_insee) do update
        set nom = excluded.nom, code_dep = excluded.code_dep, centre = excluded.centre;
    get diagnostics n = row_count;
    return n;
end $$;

-- Gold : Occitanie uniquement, prêt pour Power BI
create or replace view gold.meteo_occitanie as
select date_jour, code_dep, nom_dep, niveau_j1, niveau_j2
from silver.meteo_foret
where code_dep in ('09','11','12','30','31','32','34','46','48','65','66','81','82');

create or replace view gold.commune_haute_garonne as
select code_insee, nom, code_dep,
       extensions.st_x(centre) as longitude, extensions.st_y(centre) as latitude
from silver.commune
where code_dep = '31';
