# app.py
import streamlit as st
from reference_data import load_reference_data

st.set_page_config(page_title="Maritime Business Game Companion", layout="wide")

st.title("The Official Austin Buck MBG Cheat machine 9000")

# Load data using our cached loader
data = load_reference_data()

# Create clean navigation tabs
tab_dashboard, tab_vessels, tab_contracts, tab_finances, tab_reference_data = st.tabs([
    "Dashboard", "Vessels", "Contracts", "Finances", "Reference Data"
])

with tab_dashboard:
    st.subheader("Coming Soon!")

with tab_vessels:
    st.subheader("Coming Soon!")

with tab_contracts:
    st.subheader("Coming Soon!")

with tab_finances:
    st.subheader("Coming Soon!")

with tab_reference_data:
    st.subheader("System Status")
    st.success("Reference data successfully loaded and mapped to dataclasses!")

    col1, col2, col3 = st.columns(3)
    col1.metric("Loaded Ports", len(data["ports"]))
    col2.metric("Cargo Types", len(data["cargos"]))
    col3.metric("Active Brokers", len(data["brokers"]))

    st.subheader("Global Port Infrastructure")
    port_list = [vars(p) for p in data["ports"].values()]
    st.dataframe(port_list, use_container_width=True)

    st.subheader("Cargo Profiles")
    cargo_list = [vars(c) for c in data["cargos"].values()]
    st.dataframe(cargo_list, use_container_width=True)

    st.subheader("Broker Network & Preferences")
    broker_list = [vars(b) for b in data["brokers"].values()]
    st.dataframe(broker_list, use_container_width=True)