import pandas as pd
import streamlit as st
import httpx

from moin_moin.frontend.app_conf import (
    HOST,
    PORT,
    INSTITUTION_MAPPING,
)

st.title("Reported Issues")


result = httpx.get(
    f"{HOST}:{PORT}/load-records",
).json()

location_df = (
    pd.DataFrame(result)
    .drop_duplicates()
    .rename(columns={"latitude": "lat", "longitude": "lon"})
    .replace(INSTITUTION_MAPPING)
)

st.map(data=location_df.loc[:, ["lat", "lon", "prediction"]], color="prediction", size=10)
