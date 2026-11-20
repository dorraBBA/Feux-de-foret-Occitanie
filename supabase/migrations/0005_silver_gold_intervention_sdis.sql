-- 0005 : interventions des SDIS (statistiques annuelles par département)

create table if not exists silver.intervention_sdis (
    annee            smallint not null,
    code_dep         text     not null,
    departement      text,
    feux_vegetation  integer,
    fausses_alertes  integer,
    primary key (annee, code_dep)
);

-- Les milliers sont séparés par une espace (parfois insécable) : on ne garde que les chiffres
create or replace function silver.refresh_intervention_sdis() returns bigint
language plpgsql as $$
declare n bigint;
begin
    insert into silver.intervention_sdis (annee, code_dep, departement, feux_vegetation, fausses_alertes)
    select distinct on (a, dep)
           a, dep, nom, fv, fa
    from (
        select nullif(regexp_replace(row->>'Année', '\D', '', 'g'), '')::smallint        as a,
               case when trim(row->>'Numéro') ~ '^\d+$' then lpad(trim(row->>'Numéro'), 2, '0')
                    else upper(trim(row->>'Numéro')) end                                  as dep,
               nullif(trim(row->>'Département'), '')                                      as nom,
               nullif(regexp_replace(row->>'Feux de végétations', '\D', '', 'g'), '')::integer as fv,
               nullif(regexp_replace(row->>'Fausses alertes', '\D', '', 'g'), '')::integer     as fa,
               loaded_at
        from bronze.raw_rows
        where source = 'interventions_sdis'
    ) t
    where a is not null and dep is not null and dep <> ''
    order by a, dep, loaded_at desc
    on conflict (annee, code_dep) do update
        set departement = excluded.departement, feux_vegetation = excluded.feux_vegetation,
            fausses_alertes = excluded.fausses_alertes;
    get diagnostics n = row_count;
    return n;
end $$;

create or replace view gold.intervention_sdis_occitanie as
select annee, code_dep, departement, feux_vegetation, fausses_alertes
from silver.intervention_sdis
where code_dep in ('09','11','12','30','31','32','34','46','48','65','66','81','82');
