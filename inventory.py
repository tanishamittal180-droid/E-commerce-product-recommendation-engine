import streamlit as st
import pandas as pd

from database.db import (
    add_inventory,
    get_inventory
)

st.title(
    "📦 Inventory"
)

if not st.session_state.get(
        "admin",
        False):

    st.warning(
        "Admin Access Required"
    )

    st.stop()

products = pd.read_csv(
    "data/products.csv"
)

product = st.selectbox(
    "Product",
    products["product_id"]
)

stock = st.number_input(
    "Stock",
    min_value=0
)

if st.button(
        "Save Stock"):

    add_inventory(
        product,
        stock
    )

    st.success(
        "Inventory Updated"
    )

inventory = get_inventory()

if inventory:

    df = pd.DataFrame(
        inventory,
        columns=[
            "ID",
            "Product",
            "Stock"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )