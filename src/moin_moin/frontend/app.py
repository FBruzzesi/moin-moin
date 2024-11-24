"""Streamlit app rending the frontend."""

from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="Smart cities", layout="wide", page_icon="🏙️")
st.title("🏡 Moin Moin")
report_an_issue_page = st.Page("_report_an_issue_page.py", title="Report an issue", icon="🔧")
issue_tracker_page = st.Page("_issue_tracker_page.py", title="Issue tracker", icon="🗺️")

pg = st.navigation([report_an_issue_page, issue_tracker_page])
pg.run()
