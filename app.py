import streamlit as st
import random

# List of pre-set reviews for your segments
reviews = [
    "Highly impressed with the Easy Clean housekeeping materials. Top quality!",
    "GE-Tech Engineering provided excellent solar solutions. Very professional.",
    "The Easy Smart kitchen appliances are modern and work perfectly.",
    "Easy Trans Link made our transport logistics so much smoother. Great service!",
    "Best place for industrial cleaning chemicals. Highly recommended!",
    "Great experience with GE-Tech for our mechanical engineering needs."
]

st.set_page_config(page_title="Review Us!", page_icon="⭐")

st.title("Thank you for choosing us!")
st.subheader("We value your feedback.")

# Generate a random review for this session
if 'random_review' not in st.session_state:
    st.session_state.random_review = random.choice(reviews)

st.info(f"**Suggested Review:**\n\n{st.session_state.random_review}")

# Instruction for the user
st.write("1. Copy the text above.")
st.write("2. Click the button below.")
st.write("3. Paste and Submit!")

# The magic 5-star link
google_url = "https://search.google.com/local/writereview?placeid=ChIJu5DwTEWgwzsRi9vx9n8nwxI,5"

st.link_button("⭐⭐⭐⭐⭐ Leave a 5-Star Review", google_url, use_container_width=True)

if st.button("Get a different suggestion"):
    st.session_state.random_review = random.choice(reviews)
    st.rerun()
