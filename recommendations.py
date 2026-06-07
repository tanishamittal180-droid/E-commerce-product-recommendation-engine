import streamlit as st

import pandas as pd

from src.recommender import (
    RecommendationEngine
)

engine = RecommendationEngine()

products = pd.read_csv(
    "data/products.csv"
)

st.title(
    "🎯 AI Recommendations"
)

selected = st.selectbox(
    "Choose Product",
    products["product_id"]
)

if st.button(
        "Generate Recommendations"):

    recommendations = (
        engine.get_similar_products(
            selected
        )
    )

    st.success(
        "Recommended Products"
    )

    for item in recommendations:

        st.subheader(
            item["name"]
        )

        st.progress(
            int(item["score"])
        )

        st.write(
            f"Match Score: {item['score']}%"
        )

        st.divider()