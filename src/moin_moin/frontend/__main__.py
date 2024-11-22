# streamlit run src/moin_moin/frontend/__main__.py
from typing import NamedTuple

import pandas as pd
import streamlit as st
from PIL import Image
from geopy.geocoders import Nominatim

GEOLOCATOR = Nominatim(user_agent="location_sharing_app")
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


def get_prediction(img, tags, notes):
    # TODO: call model Prediction
    return "A very accurate prediction"


def main() -> None:
    st.sidebar.title("Tell us about the issue...")

    image = st.sidebar.file_uploader(
        label="Upload an image",
        type=["png", "jpg"],
    )

    raw_loc = st.sidebar.text_input(
        "Enter your location (e.g., city name, street, number):"
    )
    loc = parse_location(raw_loc)

    if loc:
        st.write(loc)
    else:
        st.write("Location not found. Please try again.")

    tags = st.sidebar.multiselect("Select tags for the image:", TAGS)

    notes = st.sidebar.text_area(
        label="Additional information",
        placeholder="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    )

    if st.sidebar.button("Submit"):
        if image is not None:
            st.write("This is your image:")
            img = load_image(image)
            st.image(img)
    st.map(data=pd.DataFrame({"lat": [loc.latitude], "lon": [loc.longitude]}))

    st.write("Prediction: ", get_prediction(image, tags, notes))


if __name__ == "__main__":
    main()
