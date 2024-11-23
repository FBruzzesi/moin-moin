import pandas as pd
import streamlit as st
from PIL import Image
from geopy.geocoders import Nominatim
import httpx
from io import BytesIO


HOST = "http://127.0.0.1"
PORT = 8091


GEOLOCATOR = Nominatim(user_agent="location_sharing_app")
MAX_COMMENT_CHARS = 250
TAGS = [
    "Street",
    "Lights",
    "Rubish",
    "Crime",
    "Broken",
]


def load_image(image):
    return Image.open(image).convert("RGB")


def parse_location(raw_loc: str):
    if not raw_loc:
        print("No location given")
        return None
    loc = GEOLOCATOR.geocode(raw_loc)
    return loc


def main() -> None:
    st.sidebar.title("Tell us about the issue...")

    raw_image = st.sidebar.file_uploader(
        label="Upload an image",
        type=["png", "jpg"],
    )

    raw_loc = st.sidebar.text_input(
        "Enter your location (e.g., city name, street, number):"
    )
    loc = parse_location(raw_loc)


    tags = st.sidebar.multiselect("Select tags for the image:", TAGS)

    notes = st.sidebar.text_area(
        label="Additional information",
        placeholder=f"{MAX_COMMENT_CHARS} characters max",
        max_chars=MAX_COMMENT_CHARS,
    )

    if st.sidebar.button("Submit"):
        if raw_image is not None:
            image = load_image(raw_image)

            try:
                buffer = BytesIO()
                image.save(buffer, format="jpeg")
                buffer.seek(0)
                result = httpx.post(
                    f"{HOST}:{PORT}/predict",
                    data={"height": image.height, "width": image.width},
                    files={"file": ("image.jpg", buffer, "image/jpeg")},
                ).json()["prediction"]
            except:
                from moin_moin.backend.api import institutions
                from moin_moin.backend.ml import ClipModel

                model = ClipModel().fit(institutions)
                result = model.predict(image)

        st.header(f"Assigned Institution: {result}")
        st.write("---")
        left_column, right_column = st.columns(2,)
        if loc:
            right_column.map(data=pd.DataFrame({"lat": [loc.latitude], "lon": [loc.longitude]}))
            right_column.write(loc)
        else:
            right_column.write("Location not found. Please try again.")

        left_column.image(image)

main()
