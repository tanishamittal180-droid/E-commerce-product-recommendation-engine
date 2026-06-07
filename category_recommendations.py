import streamlit as st

import pandas as pd

from src.category_recommender import (
    recommend_category
)

products = pd.read_csv(
    "data/products.csv"
)

st.title(
    "📦 Category Recommendations"
)

category = st.selectbox(
    "Select Category",
    products["category"].unique()
)

if st.button(
        "Show Products"):

    recs = recommend_category(
        category
    )

    st.dataframe(
        recs
    )