# streamlit run src/moin_moin/frontend/__main__.py

import numpy as np
import streamlit as st
from PIL import Image


def main() -> None:
    st.sidebar.title("Tell us about the issue...")

    image = st.sidebar.file_uploader(
        label="Upload an image",
        type=["png", "jpg"],
    )
    location = st.sidebar.text_input(label="Location")
    tags = st.sidebar.selectbox(label="Tags", options=["Tag 1", "Tag 2", "Tag 3"])
    notes = st.sidebar.text_area(
        label="Additional information",
        placeholder="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    )

    # Submit button
    if st.sidebar.button("Submit"):
        # Process the form data here
        if image is not None:
            st.write("Image uploaded:", image.name)
            pilimage = Image.open(image)
            arr_img = np.asarray(pilimage)
            print(arr_img.shape, arr_img)

        st.write("Location:", location)
        st.write("Tags:", tags)
        st.write("Additional information:", notes)

        # Geolocate the location
        # geolocator = Nominatim(user_agent="geoapiExercises")
        # location_data = geolocator.geocode(location)

        # if location_data:
        #     latitude = location_data.latitude
        #     longitude = location_data.longitude
        #     st.write("Coordinates:", (latitude, longitude))

        #     # Create a map
        #     map_ = folium.Map(location=[latitude, longitude], zoom_start=12)
        #     folium.Marker([latitude, longitude], popup=location).add_to(map_)

        #     # Display the map on the main page
        #     st_folium(map_, width=700, height=500)
        # else:
        #     st.write("Location not found")


if __name__ == "__main__":
    main()
