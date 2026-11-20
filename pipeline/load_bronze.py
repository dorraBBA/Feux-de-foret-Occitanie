"""Charge les sources brutes dans Supabase (schéma bronze), puis rafraîchit silver.

Usage : python pipeline/load_bronze.py [meteo_foret] [communes_geo_api]
Sans argument, toutes les sources de sources.yml sont chargées. Relançable sans doublons.
"""
import csv
import gzip
import hashlib
import io
import json
import os
import sys
import zipfile
from pathlib import Path

import psycopg
import requests
import truststore
import yaml
from dotenv import load_dotenv
from psycopg.types.json import Jsonb

truststore.inject_into_ssl()  # utilise les certificats Windows (proxy d'entreprise)

HERE = Path(__file__).parent
load_dotenv(HERE.parent / ".env")
load_dotenv(HERE / ".env")


def connect():
    return psycopg.connect(os.environ["SUPABASE_DB_URL"], sslmode="require")


def load_csv_gz(cur, source, url):
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    text = gzip.decompress(resp.content).decode("utf-8-sig")
    first = text.splitlines()[0]
    sep = ";" if first.count(";") > first.count(",") else ","
    rows = list(csv.DictReader(io.StringIO(text), delimiter=sep))
    file_name = url.rsplit("/", 1)[-1]
    cur.execute("delete from bronze.raw_rows where source = %s and source_file = %s", (source, file_name))
    cur.executemany(
        "insert into bronze.raw_rows (source, source_file, row) values (%s, %s, %s)",
        [(source, file_name, Jsonb(r)) for r in rows],
    )
    print(f"{source}: {file_name} -> {len(rows)} lignes")


def load_api_json(cur, source, url):
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    payload = resp.json()
    digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    cur.execute(
        """insert into bronze.api_calls (source, url, http_status, payload, payload_hash)
           values (%s, %s, %s, %s, %s) on conflict (source, payload_hash) do nothing""",
        (source, url, resp.status_code, Jsonb(payload), digest),
    )
    print(f"{source}: {url} -> HTTP {resp.status_code}")


def load_zip_csv(cur, source, path):
    full = (HERE.parent / path).resolve()
    with zipfile.ZipFile(full) as z:
        name = next(n for n in z.namelist() if n.lower().endswith(".csv"))
        lines = z.read(name).decode("utf-8-sig").splitlines()
    # L'export BDIFF a 2 lignes de critères avant la ligne d'en-têtes
    header = next(i for i, l in enumerate(lines) if l.startswith("Année"))
    rows = list(csv.DictReader(lines[header:], delimiter=";"))
    cur.execute("delete from bronze.raw_rows where source = %s and source_file = %s", (source, full.name))
    cur.executemany(
        "insert into bronze.raw_rows (source, source_file, row) values (%s, %s, %s)",
        [(source, full.name, Jsonb(r)) for r in rows],
    )
    print(f"{source}: {full.name} -> {len(rows)} lignes")


def load_shapefile(cur, source, path):
    import geopandas as gpd  # import local : dépendance lourde, utile pour cette source seulement

    full = (HERE.parent / path).resolve()
    region_file = HERE.parent / "data" / "occitanie.geojson"
    if not region_file.exists():
        url = ("https://data.geopf.fr/wfs/ows?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature"
               "&TYPENAMES=ADMINEXPRESS-COG.LATEST:region&OUTPUTFORMAT=application/json"
               "&SRSNAME=EPSG:2154&CQL_FILTER=code_insee='76'")
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        region_file.write_text(resp.text, encoding="utf-8")
    region = gpd.read_file(region_file).to_crs(2154)
    grid = gpd.read_file(full)
    # On ne garde que les mailles qui touchent l'Occitanie (le fichier national dépasse la limite de la base)
    grid = grid[grid.intersects(region.union_all())]
    cur.execute("delete from bronze.raw_rows where source = %s and source_file = %s", (source, full.name))
    cur.executemany(
        "insert into bronze.raw_rows (source, source_file, row) values (%s, %s, %s)",
        [(source, full.name, Jsonb({"nom": r.NOM, "wkt": r.geometry.wkt, "srid": 2154})) for r in grid.itertuples()],
    )
    print(f"{source}: {full.name} -> {len(grid)} mailles (Occitanie)")


def load_csv_url(cur, source, url):
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    text = resp.content.decode("cp1252")  # fichiers SDIS en Windows-1252
    rows = list(csv.DictReader(io.StringIO(text), delimiter=";"))
    file_name = url.rsplit("/", 1)[-1]
    cur.execute("delete from bronze.raw_rows where source = %s and source_file = %s", (source, file_name))
    cur.executemany(
        "insert into bronze.raw_rows (source, source_file, row) values (%s, %s, %s)",
        [(source, file_name, Jsonb(r)) for r in rows],
    )
    print(f"{source}: {file_name} -> {len(rows)} lignes")


def get_wfs_json(params, retries=3):
    for attempt in range(retries):
        try:
            resp = requests.get("https://data.geopf.fr/wfs/ows", params=params, timeout=300)
            resp.raise_for_status()
            return resp.json()
        except (requests.RequestException, ValueError):
            if attempt == retries - 1:
                raise


def load_bdforet(cur, source, dep):
    """BD Forêt V2 : trop volumineuse pour la base (87 000 polygones pour la Haute-Garonne).
    On la découpe par commune (WFS IGN) et on ne charge que les surfaces agrégées."""
    import geopandas as gpd

    communes = gpd.GeoDataFrame.from_features(
        get_wfs_json({
            "SERVICE": "WFS", "VERSION": "2.0.0", "REQUEST": "GetFeature",
            "TYPENAMES": "ADMINEXPRESS-COG.LATEST:commune", "OUTPUTFORMAT": "application/json",
            "SRSNAME": "EPSG:2154", "CQL_FILTER": f"code_insee_du_departement='{dep}'",
        })["features"], crs=2154)
    communes["geometry"] = communes.geometry.make_valid()
    communes["surface_commune_m2"] = communes.geometry.area
    minx, miny, maxx, maxy = communes.to_crs(4326).total_bounds
    bbox = f"{miny},{minx},{maxy},{maxx},urn:ogc:def:crs:EPSG::4326"

    parts, start, page = [], 0, 5000
    while True:
        feats = get_wfs_json({
            "SERVICE": "WFS", "VERSION": "2.0.0", "REQUEST": "GetFeature",
            "TYPENAMES": "LANDCOVER.FORESTINVENTORY.V2:formation_vegetale", "OUTPUTFORMAT": "application/json",
            "SRSNAME": "EPSG:2154", "BBOX": bbox, "SORTBY": "id", "COUNT": page, "STARTINDEX": start,
        })["features"]
        if not feats:
            break
        forest = gpd.GeoDataFrame.from_features(feats, crs=2154)
        forest["geometry"] = forest.geometry.make_valid()
        cut = gpd.overlay(
            forest[["tfv_g11", "essence", "geometry"]],
            communes[["code_insee", "surface_commune_m2", "geometry"]],
            how="intersection", keep_geom_type=True,
        )
        cut["surface_m2"] = cut.geometry.area
        parts.append(cut.drop(columns="geometry"))
        start += page
        print(f"  {source}: {start} polygones traités")
        if len(feats) < page:
            break

    import pandas as pd
    agg = (pd.concat(parts).groupby(["code_insee", "surface_commune_m2", "tfv_g11", "essence"], dropna=False)
           ["surface_m2"].sum().reset_index())
    file_name = f"bdforet_v2_dep{dep}"
    cur.execute("delete from bronze.raw_rows where source = %s and source_file = %s", (source, file_name))
    cur.executemany(
        "insert into bronze.raw_rows (source, source_file, row) values (%s, %s, %s)",
        [(source, file_name, Jsonb({
            "code_insee": r.code_insee, "tfv_g11": r.tfv_g11, "essence": r.essence,
            "surface_m2": round(r.surface_m2, 1), "surface_commune_m2": round(r.surface_commune_m2, 1),
        })) for r in agg.itertuples()],
    )
    print(f"{source}: département {dep} -> {len(agg)} lignes agrégées")


LOADERS = {
    "csv_gz": load_csv_gz,
    "csv_url": load_csv_url,
    "api_json": load_api_json,
    "zip_csv": load_zip_csv,
    "shapefile": load_shapefile,
    "wfs_foret": load_bdforet,
}
REFRESH = {
    "meteo_foret": "silver.refresh_meteo_foret",
    "communes_geo_api": "silver.refresh_commune",
    "bdiff": "silver.refresh_incendie",
    "carroyage_dfci": "silver.refresh_carroyage_dfci",
    "interventions_sdis": "silver.refresh_intervention_sdis",
    "bdforet_v2": "silver.refresh_foret_commune",
}


def main(selected):
    sources = yaml.safe_load((HERE / "sources.yml").read_text(encoding="utf-8"))
    with connect() as conn, conn.cursor() as cur:
        for name, cfg in sources.items():
            if selected and name not in selected:
                continue
            for item in cfg.get("urls") or cfg["paths"]:
                LOADERS[cfg["type"]](cur, name, item)
            cur.execute(f"select {REFRESH[name]}()")
            print(f"{name}: silver mis à jour ({cur.fetchone()[0]} lignes)")
        conn.commit()


if __name__ == "__main__":
    main(sys.argv[1:])
