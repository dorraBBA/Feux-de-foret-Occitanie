-- 0004 : carroyage DFCI 2 km (mailles qui touchent l'Occitanie), en Lambert 93

create table if not exists silver.carroyage_dfci (
    maille text primary key,
    geom   extensions.geometry(Polygon, 2154) not null
);
create index if not exists carroyage_dfci_geom_idx on silver.carroyage_dfci using gist (geom);

create or replace function silver.refresh_carroyage_dfci() returns bigint
language plpgsql as $$
declare n bigint;
begin
    insert into silver.carroyage_dfci (maille, geom)
    select distinct on (row->>'nom')
           row->>'nom', extensions.st_setsrid(extensions.st_geomfromtext(row->>'wkt'), 2154)
    from bronze.raw_rows
    where source = 'carroyage_dfci'
    order by row->>'nom', loaded_at desc
    on conflict (maille) do update set geom = excluded.geom;
    get diagnostics n = row_count;
    return n;
end $$;
