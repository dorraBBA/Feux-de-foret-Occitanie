-- 0006 : BD Forêt V2 agrégée par commune (surface par type de formation et essence)

create table if not exists silver.foret_commune (
    code_insee          char(5)  not null,
    tfv_g11             text     not null,
    essence             text     not null,
    surface_m2          numeric  not null,
    surface_commune_m2  numeric  not null,
    primary key (code_insee, tfv_g11, essence)
);

create or replace function silver.refresh_foret_commune() returns bigint
language plpgsql as $$
declare n bigint;
begin
    insert into silver.foret_commune (code_insee, tfv_g11, essence, surface_m2, surface_commune_m2)
    select distinct on (row->>'code_insee', coalesce(row->>'tfv_g11', 'Inconnu'), coalesce(row->>'essence', 'Inconnue'))
           row->>'code_insee', coalesce(row->>'tfv_g11', 'Inconnu'), coalesce(row->>'essence', 'Inconnue'),
           (row->>'surface_m2')::numeric, (row->>'surface_commune_m2')::numeric
    from bronze.raw_rows
    where source = 'bdforet_v2'
    order by row->>'code_insee', coalesce(row->>'tfv_g11', 'Inconnu'), coalesce(row->>'essence', 'Inconnue'), loaded_at desc
    on conflict (code_insee, tfv_g11, essence) do update
        set surface_m2 = excluded.surface_m2, surface_commune_m2 = excluded.surface_commune_m2;
    get diagnostics n = row_count;
    return n;
end $$;

-- Gold : surface boisée et de landes par commune (les landes sont un combustible important)
create or replace view gold.foret_commune as
select f.code_insee,
       c.nom,
       max(f.surface_commune_m2) as surface_commune_m2,
       sum(f.surface_m2) filter (where f.tfv_g11 like 'Forêt%' or f.tfv_g11 = 'Peupleraie') as surface_foret_m2,
       sum(f.surface_m2) filter (where f.tfv_g11 = 'Lande') as surface_lande_m2,
       least(100, round(100 * coalesce(sum(f.surface_m2) filter (where f.tfv_g11 like 'Forêt%' or f.tfv_g11 = 'Peupleraie'), 0)
                         / max(f.surface_commune_m2), 1)) as taux_boisement_pct
from silver.foret_commune f
left join silver.commune c using (code_insee)
group by f.code_insee, c.nom;
