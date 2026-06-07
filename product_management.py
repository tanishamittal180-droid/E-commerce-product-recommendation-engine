import streamlit as st
import pandas as pd

st.title("📦 Product Management")

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

st.subheader(
    "Add New Product"
)

product_id = st.text_input(
    "Product ID"
)

name = st.text_input(
    "Product Name"
)

category = st.text_input(
    "Category"
)

price = st.number_input(
    "Price",
    min_value=0
)

rating = st.slider(
    "Rating",
    1.0,
    5.0,
    4.0
)

description = st.text_area(
    "Description"
)

image = st.text_input(
    "Image Name"
)

if st.button(
        "Add Product"):

    new_row = pd.DataFrame(
        [[
            product_id,
            name,
            category,
            price,
            rating,
            image,
            description
        ]],
        columns=products.columns
    )

    products = pd.concat(
        [products, new_row],
        ignore_index=True
    )

    products.to_csv(
        "data/products.csv",
        index=False
    )

    st.success(
        "Product Added"
    )

st.divider()

st.subheader(
    "Delete Product"
)

delete_id = st.text_input(
    "Product ID To Delete"
)

if st.button(
        "Delete Product"):

    products = products[
        products["product_id"]
        != delete_id
    ]

    products.to_csv(
        "data/products.csv",
        index=False
    )

    st.success(
        "Product Deleted"
    )