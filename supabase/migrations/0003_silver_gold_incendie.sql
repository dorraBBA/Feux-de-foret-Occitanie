-- 0003 : incendies BDIFF (silver et gold)

create table if not exists silver.incendie (
    annee               smallint not null,
    numero              integer  not null,
    code_dep            text     not null,
    code_insee          char(5),
    commune             text,
    date_alerte         timestamp,
    surface_m2          numeric,
    surface_foret_m2    numeric,
    surface_maquis_m2   numeric,
    nature              text,
    precision_surfaces  text,
    primary key (annee, code_dep, numero)
);

create or replace function silver.refresh_incendie() returns bigint
language plpgsql as $$
declare n bigint;
begin
    insert into silver.incendie (annee, numero, code_dep, code_insee, commune, date_alerte,
                                 surface_m2, surface_foret_m2, surface_maquis_m2, nature, precision_surfaces)
    select distinct on (a, num, dep)
           a, num, dep, insee, commune, d, s, sf, sm, nature, prec
    from (
        select nullif(row->>'Année', '')::smallint                                        as a,
               nullif(row->>'Numéro', '')::integer                                        as num,
               upper(lpad(row->>'Département', 2, '0'))                                   as dep,
               nullif(lpad(row->>'Code INSEE', 5, '0'), '00000')                          as insee,
               nullif(row->>'Nom de la commune', '')                                      as commune,
               nullif(row->>'Date de première alerte', '')::timestamp                     as d,
               nullif(replace(row->>'Surface parcourue (m2)', ',', '.'), '')::numeric     as s,
               nullif(replace(row->>'Surface forêt (m2)', ',', '.'), '')::numeric         as sf,
               nullif(replace(row->>'Surface maquis garrigues (m2)', ',', '.'), '')::numeric as sm,
               nullif(row->>'Nature', '')                                                 as nature,
               nullif(row->>'Précision des surfaces', '')                                 as prec,
               loaded_at
        from bronze.raw_rows
        where source = 'bdiff'
    ) t
    where a is not null and num is not null and dep is not null
    order by a, num, dep, loaded_at desc
    on conflict (annee, code_dep, numero) do update
        set code_insee = excluded.code_insee, commune = excluded.commune, date_alerte = excluded.date_alerte,
            surface_m2 = excluded.surface_m2, surface_foret_m2 = excluded.surface_foret_m2,
            surface_maquis_m2 = excluded.surface_maquis_m2, nature = excluded.nature,
            precision_surfaces = excluded.precision_surfaces;
    get diagnostics n = row_count;
    return n;
end $$;

create or replace view gold.incendie_occitanie as
select annee, numero, code_dep, code_insee, commune, date_alerte::date as date_alerte,
       extract(hour from date_alerte)::int as heure_alerte,
       surface_m2, surface_foret_m2, surface_maquis_m2, nature
from silver.incendie
where code_dep in ('09','11','12','30','31','32','34','46','48','65','66','81','82');
