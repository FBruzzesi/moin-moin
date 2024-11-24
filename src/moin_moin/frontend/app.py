"""Streamlit app rending the frontend."""

from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="Smart cities", layout="wide", page_icon="🏙️")
st.title("🏡 Moin Moin")
create_page = st.Page("_user_input.py", title="Report an issue", icon="🔧")
overview = st.Page("_overview.py", title="Issue tracker", icon="🗺️")

pg = st.navigation([create_page, overview])
pg.run()
