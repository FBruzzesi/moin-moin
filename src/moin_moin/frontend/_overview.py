from __future__ import annotations

import httpx
import pandas as pd
import streamlit as st

from moin_moin.frontend._conf import HOST
from moin_moin.frontend._conf import INSTITUTION_MAPPING
from moin_moin.frontend._conf import PORT

result = httpx.get(f"{HOST}:{PORT}/load-records").json()

location_df = (
    pd.DataFrame(result)
    .drop_duplicates()
    .rename(columns={"latitude": "lat", "longitude": "lon"})
    .replace(INSTITUTION_MAPPING)
)

st.title(f"#{location_df.shape[0]} issues reported")
st.map(data=location_df.loc[:, ["lat", "lon", "prediction"]], color="prediction", size=10)
