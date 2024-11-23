"""Streamlit app rending the frontend."""

from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="Smart cities", layout="wide", page_icon="🏙️")
create_page = st.Page("_user_input.py", title="Upload Issues", icon="🔧")
overview = st.Page("_overview.py", title="Issue Tracker", icon="🗺️")

pg = st.navigation([create_page, overview])
pg.run()
