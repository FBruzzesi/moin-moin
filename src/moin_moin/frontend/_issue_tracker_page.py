from __future__ import annotations

import httpx
import pandas as pd
import streamlit as st

from moin_moin.frontend._conf import BACKEND_URL
from moin_moin.frontend._conf import INSTITUTION_COLOR_MAPPING


def issue_tracker_page() -> None:
    """Create the issue tracker page."""
    st.sidebar.title("Issue tracker")
    st.sidebar.markdown("This page displays all the issues in the database in a map and on a table")

    result = (
        pd.DataFrame(httpx.get(f"{BACKEND_URL}/load-records").json())
        .drop_duplicates()
        .assign(_color=lambda t: t["prediction"].map(INSTITUTION_COLOR_MAPPING))
    )

    st.write("---")
    st.warning(f"Found {result.shape[0]} issues")

    left_column, right_column = st.columns(2)

    left_column.map(data=result, latitude="latitude", longitude="longitude", color="_color", size=10)
    right_column.dataframe(
        data=(
            result[["prediction", "notes", "timestamp"]].rename(
                columns={"prediction": "Assigned to", "notes": "Notes", "timestamp": "Report created"}
            )
        ),
        hide_index=True,
    )


issue_tracker_page()
