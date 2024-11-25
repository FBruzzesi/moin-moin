"""Streamlit app rending the frontend."""

from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="Moin Moin", layout="wide", page_icon="🏙️")

# Remove whitespace from the top of the page and sidebar
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 5rem;
            padding-right: 5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🏡 Moin Moin")
st.header("Empowering Communities to Build Better Cities")
report_an_issue_page = st.Page("_report_an_issue_page.py", title="Report an issue", icon="🔧")
issue_tracker_page = st.Page("_issue_tracker_page.py", title="Issue tracker", icon="🗺️")

pg = st.navigation([report_an_issue_page, issue_tracker_page])
pg.run()
