import streamlit as st
import pandas as pd

st.set_page_config(page_title="Easy Group Reviews", page_icon="⭐")

# Corrected URL with Review Intent flag
PLACE_ID = "ChIJu5DwTEWgwzsRi9vx9n8nwxI"
GOOGLE_URL = f"https://search.google.com/local/writereview?placeid={PLACE_ID}&rciv=1"

st.title("Support Easy Group ⭐")
st.write("Tap a review to copy it, then click the button!")

segments = {
    "🧼 Easy Clean": "Excellent housekeeping materials and cleaning chemicals. Very effective!",
    "🍳 Easy Smart": "Great quality kitchen appliances and electronics. Very satisfied with the purchase.",
    "🚚 Easy Trans Link": "Reliable transport and import-export services. Very professional handling.",
    "☀️ GE-Tech": "Top-tier solar and engineering solutions. Highly recommend their expertise."
}

for name, text in segments.items():
    with st.container(border=True):
        st.subheader(name)
        # This code box makes it easy for customers to tap and copy on mobile
        st.code(text, language=None) 
        st.link_button(f"Submit 5-Star Review", GOOGLE_URL, use_container_width=True)

st.divider()
st.info("The 5-star rating is selected by default for your convenience.")
