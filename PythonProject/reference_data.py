# reference_data.py
import pandas as pd
import streamlit as st
from models import Cargo, Port, Route, Flag, Country, Broker


def clean_dataframe_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Strips whitespace, lowercases, replaces spaces with underscores, and fixes reserved keywords."""
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace('"', "")
        .str.replace("-", "_")
    )

    # Map CSV terms that conflict with Python keywords or model naming conventions
    rename_mapping = {
        "import": "import_val",
        "export": "export_val"
    }
    df = df.rename(columns=rename_mapping)

    return df


@st.cache_data
def load_reference_data():
    """Loads immutable reference data (ports, cargo, flags, routes, countries, and brokers)."""

    # 1. Load DataFrames from your round0 folder
    df_ports = clean_dataframe_columns(pd.read_csv("data/round0/Port Data.csv", sep=";"))
    df_cargos = clean_dataframe_columns(pd.read_csv("data/round0/Cargo Data.csv", sep=";"))
    df_flags = clean_dataframe_columns(pd.read_csv("data/round0/Flag Data.csv", sep=";"))
    df_routes = clean_dataframe_columns(pd.read_csv("data/round0/Port Distances.csv", sep=";"))
    df_countries = clean_dataframe_columns(pd.read_csv("data/round0/Country Data.csv", sep=";"))
    df_brokers = clean_dataframe_columns(pd.read_csv("data/round0/Broker Data.csv", sep=";"))

    # 2. Cargos (Lookup by name)
    cargos = {
        row["cargo_type"]: Cargo(**row.to_dict())
        for _, row in df_cargos.iterrows()
    }

    # 3. Ports (Lookup by name)
    ports = {
        row["name"]: Port(**row.to_dict())
        for _, row in df_ports.iterrows()
    }

    # 4. Flags
    flags = {
        row["flag"]: Flag(**row.to_dict())
        for _, row in df_flags.iterrows()
    }

    # 5. Countries (Indexed by region and week)
    countries = {
        (row["region"], row["week"]): Country(**row.to_dict())
        for _, row in df_countries.iterrows()
    }

    # 6. Brokers (Linking focus countries and cargos)
    brokers = {
        row["broker_name"]: Broker(**row.to_dict())
        for _, row in df_brokers.iterrows()
    }

    # 7. Routes (Linking start and end port objects)
    routes = []
    for _, row in df_routes.iterrows():
        routes.append(Route(
            canal=bool(row["canal"]),
            canal_width=float(row["canal_width"]),
            canal_depth=float(row["canal_depth"]),
            canal_fee=float(row["canal_fee"]),
            distance_using_canal=float(row["distance_using_canal"]),
            distance_not_using_canal=float(row["distance_not_using_canal"]),
            risk_of_piracy=float(row["risk_of_piracy"]),
            applicable_loadline=str(row["applicable_loadline"]),
            start_port=ports.get(row["start_port"]),
            end_port=ports.get(row["end_port"])
        ))

    return {
        "ports": ports,
        "cargos": cargos,
        "flags": flags,
        "routes": routes,
        "countries": countries,
        "brokers": brokers
    }