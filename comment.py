
import streamlit as st

# Define a class to hold session state
class SessionState:
    def __init__(self):
        self.reviews = []

# Create a session state object
session_state = SessionState()

def app():
    st.title("Comment Your Reviews...")

    # Text area for the review
    review = st.text_area("Write your review:")

    # Slider for rating (from 1 to 5)
    rating = st.slider("Rate the product (1 - Worst, 5 - Best)", 1, 5)

    # Button to submit the review
    if st.button("Submit Review"):
        # Add the review and rating to the list of reviews in session state
        session_state.reviews.append({"review": review, "rating": rating})
        st.success("Review submitted successfully!")

    # Display all submitted reviews and ratings
    if session_state.reviews:
        st.subheader("Submitted Reviews:")
        for i, entry in enumerate(session_state.reviews, 1):
            st.write(f"Review {i}: {entry['review']} (Rating: {entry['rating']})")


