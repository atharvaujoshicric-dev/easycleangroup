import streamlit as st

# The most stable link for Google Reviews
PLACE_ID = "ChIJu5DwTEWgwzsRi9vx9n8nwxI"
GOOGLE_URL = f"https://search.google.com/local/writereview?placeid={PLACE_ID}"

st.set_page_config(page_title="Easy Group Review", page_icon="⭐")

st.header("Select Your Service")

# Specific reviews for your segments
reviews = {
    "Easy Clean": "Excellent quality cleaning chemicals and housekeeping materials. Highly recommended!",
    "Easy Smart": "Great range of home and kitchen appliances. Very satisfied with the service.",
    "Easy Trans Link": "Professional transport and logistics services. Very reliable!",
    "GE-Tech Engineering": "Expert solar and engineering solutions. Top-tier stockist and service."
}

# Create a clean UI for the customer
for segment, text in reviews.items():
    with st.container(border=True):
        st.subheader(segment)
        # st.code makes the text "Tap to Copy" on most mobile devices
        st.code(text, language=None)
        st.link_button("⭐⭐⭐⭐⭐ Open Google & Paste", GOOGLE_URL, use_container_width=True)

st.caption("Step 1: Tap the text to copy. Step 2: Tap the button and paste!")
