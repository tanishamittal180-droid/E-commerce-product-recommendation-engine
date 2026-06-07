import streamlit as st
import pandas as pd

from database.db import (
    add_review,
    get_reviews
)

products = pd.read_csv(
    "data/products.csv"
)

st.title(
    "⭐ Product Reviews"
)

selected_product = st.selectbox(
    "Select Product",
    products["product_id"]
)

rating = st.slider(
    "Rating",
    1,
    5,
    5
)

review = st.text_area(
    "Write Review"
)

if st.button(
        "Submit Review"):

    if "user" in st.session_state:

        add_review(
            st.session_state["user"],
            selected_product,
            rating,
            review
        )

        st.success(
            "Review Added"
        )

reviews = get_reviews(
    selected_product
)

st.subheader(
    "Customer Reviews"
)

for item in reviews:

    st.write(
        f"👤 {item[0]}"
    )

    st.write(
        f"⭐ {item[1]}"
    )

    st.write(
        item[2]
    )

    st.divider()