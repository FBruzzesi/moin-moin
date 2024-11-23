import pandas as pd
import streamlit as st

st.title("Reported Issues")

st.map(data=pd.DataFrame({"lat": [10, 12], "lon": [50, 51]}))

