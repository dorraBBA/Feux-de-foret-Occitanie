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


LOADERS = {"csv_gz": load_csv_gz, "api_json": load_api_json}
REFRESH = {"meteo_foret": "silver.refresh_meteo_foret", "communes_geo_api": "silver.refresh_commune"}


def main(selected):
    sources = yaml.safe_load((HERE / "sources.yml").read_text(encoding="utf-8"))
    with connect() as conn, conn.cursor() as cur:
        for name, cfg in sources.items():
            if selected and name not in selected:
                continue
            for url in cfg["urls"]:
                LOADERS[cfg["type"]](cur, name, url)
            cur.execute(f"select {REFRESH[name]}()")
            print(f"{name}: silver mis à jour ({cur.fetchone()[0]} lignes)")
        conn.commit()


if __name__ == "__main__":
    main(sys.argv[1:])
