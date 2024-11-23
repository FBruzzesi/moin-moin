import streamlit as st

st.set_page_config(page_title="Smart cities", layout="wide")  # TODO: page_icon=":material/edit:"
create_page = st.Page("user_input_layer.py", title="Upload Issues")  # TODO: icon
overview = st.Page("general_overview.py", title="Issue Tracker")

pg = st.navigation([create_page, overview])
pg.run()
