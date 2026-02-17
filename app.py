import streamlit as st

# The clean, working Place ID link
PLACE_ID = "ChIJu5DwTEWgwzsRi9vx9n8nwxI"
GOOGLE_URL = f"https://search.google.com/local/writereview?placeid={PLACE_ID}"

st.set_page_config(page_title="Review Us", page_icon="⭐")

st.title("Share Your Feedback")
st.write("Select your service to get a suggested review:")

# Segment options
segments = {
    "Easy Clean": "The best cleaning materials and housekeeping supplies. Very effective products!",
    "Easy Smart": "Excellent range of home and kitchen appliances. High quality and reliable.",
    "Easy Trans Link": "Professional transport and logistics services. Everything arrived on time.",
    "GE-Tech Engineering": "Expert engineering and solar solutions. Very knowledgeable team."
}

# Display buttons
for name, review_text in segments.items():
    with st.expander(f"Click for {name} Review"):
        st.write(f"**Suggested Text:** {review_text}")
        # A simple button to open the link
        st.link_button(f"Write 5-Star Review for {name}", GOOGLE_URL, use_container_width=True)

st.divider()
st.caption("Thank you for supporting our local business!")
