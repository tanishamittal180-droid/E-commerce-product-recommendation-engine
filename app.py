import streamlit as st

st.set_page_config(
    page_title="E-Commerce Recommendation Engine",
    page_icon="🛒",
    layout="wide"
)

st.title(
    "🛒 E-Commerce Product Recommendation Engine"
)

st.image(
    "assets/banner.jpg",
    use_container_width=True
)

st.write(
    """
    Welcome to the
    AI Powered Product
    Recommendation System.
    """
)

st.success(
    "Use the sidebar to navigate."
)