# app.py

import streamlit as st
from backend import add_idea_to_appwrite

# Custom CSS for gradient background and gradient text
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #f06, #9f6);
        }
        .gradient-text {
            font-size: 3em;
            background: linear-gradient(45deg, #f06, #9f6);
            -webkit-background-clip: text;
            color: transparent;
        }
        .description {
            font-size: 1.2em;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with gradient text
st.markdown('<div class="gradient-text">Startup Idea Submission</div>', unsafe_allow_html=True)

# Description below the title
st.markdown('<div class="description">We value innovative ideas! Share your startup concept in a sentence, and let the world see its potential.</div>', unsafe_allow_html=True)

# Hero text prompting for idea
st.markdown("### Describe your startup idea below:")

# Input for startup idea
idea = st.text_area("", max_chars=250)

# Submission button
if st.button("Submit"):
    response = add_idea_to_appwrite(idea)
    if response:
        st.success("Your idea has been submitted!")
    else:
        st.error("Failed to submit your idea. Please try again.")
