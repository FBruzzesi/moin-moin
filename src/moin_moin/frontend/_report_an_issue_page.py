from __future__ import annotations

from io import BytesIO
from typing import Any
from typing import Final

import httpx
import pandas as pd
import streamlit as st
from geopy.geocoders import Nominatim
from PIL import Image

from moin_moin.frontend._conf import BACKEND_URL

GEOLOCATOR = Nominatim(user_agent="location_sharing_app")

MAX_COMMENT_CHARS: Final[str] = 250

TAGS: Final[list[str]] = [
    "Street",
    "Lights",
    "Rubish",
    "Crime",
    "Broken",
]


def parse_location(raw_loc: str) -> None | Any:  # noqa: ANN401
    if not raw_loc:
        return None
    return GEOLOCATOR.geocode(raw_loc)


def user_input_page() -> None:
    """Render user input page."""
    st.sidebar.title("Tell us about your issue!")
    st.sidebar.markdown(
        "This page allows a citizen to report issues found around a city by just uploading an image and location."
    )

    raw_image = st.sidebar.file_uploader(
        label="Upload an image",
        type=["png", "jpg"],
    )

    raw_loc = st.sidebar.text_input("Enter your location:", placeholder="Street, number, city name")

    notes = st.sidebar.text_area(
        label="Additional information",
        placeholder=f"{MAX_COMMENT_CHARS} characters max",
        max_chars=MAX_COMMENT_CHARS,
    )

    if st.sidebar.button("Submit"):
        loc = parse_location(raw_loc)
        if loc is None:
            st.error("Location not found. Please try again.")
            return

        if raw_image is not None:
            image = Image.open(raw_image).convert("RGB")
            buffer = BytesIO()
            image.save(buffer, format="jpeg")
            buffer.seek(0)

            record_id = httpx.post(
                f"{BACKEND_URL}/save",
                data={
                    "latitude": getattr(loc, "latitude", None),
                    "longitude": getattr(loc, "longitude", None),
                    "notes": notes,
                },
                files={"image_bytes": ("image.jpg", buffer, "image/jpeg")},
                timeout=10,
            ).json()["record-id"]

            result = httpx.post(
                f"{BACKEND_URL}/predict",
                data={"record_id": record_id, "notes": notes},
                files={"file": ("image.jpg", buffer, "image/jpeg")},
                timeout=10,
            ).json()["prediction"]

        st.write("---")
        st.success(f"Assigned to: {result}")
        left_column, right_column = st.columns(2)
        if loc:
            right_column.map(data=pd.DataFrame({"lat": [loc.latitude], "lon": [loc.longitude]}))
            right_column.write(loc)
        else:
            right_column.write("Location not found. Please try again.")

        left_column.image(image)


user_input_page()
