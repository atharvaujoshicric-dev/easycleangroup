import streamlit as st
from streamlit_extras.stylable_container import stylable_container

# Place ID for your business
PLACE_ID = "ChIJu5DwTEWgwzsRi9vx9n8nwxI"
GOOGLE_REVIEW_URL = f"https://search.google.com/local/writereview?placeid={PLACE_ID},5"

# Reviews categorized by your business segments
review_options = {
    "Easy Clean (Housekeeping)": "Top-notch cleaning materials and chemicals. Highly recommended for quality!",
    "Easy Smart (Appliances)": "Great range of home and kitchen appliances. Excellent service and support.",
    "Easy Trans Link (Logistics)": "Reliable transport and import/export services. Very professional team!",
    "GE-Tech Engineering (Solar)": "Expert solar and mechanical engineering solutions. High quality stockist."
}

st.title("Quick 5-Star Review ⭐")
st.write("Pick your service, tap to copy, and paste on Google!")

# Create buttons for each segment
for segment, text in review_options.items():
    with stylable_container(key=segment, css_styles="button { background-color: #f0f2f6; }"):
        if st.button(f"Review for {segment}"):
            # This uses a JavaScript hack to copy to clipboard and then open the link
            st.code(text, language=None) # Shows the text clearly for a manual tap-and-hold
            st.success("Text shown above! Now click the button below to paste.")
            
            # The direct link button
            st.link_button("Go to Google Maps", GOOGLE_REVIEW_URL, use_container_width=True)
