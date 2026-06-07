import streamlit as st
import pandas as pd

st.title("⚙️ Admin Dashboard")

if not st.session_state.get(
        "admin",
        False):

    st.warning(
        "Admin Login Required"
    )

    st.stop()

products = pd.read_csv(
    "data/products.csv"
)

st.metric(
    "Total Products",
    len(products)
)

st.metric(
    "Categories",
    products["category"].nunique()
)

st.dataframe(
    products,
    use_container_width=True
)