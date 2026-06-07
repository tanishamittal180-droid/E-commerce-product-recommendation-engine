import streamlit as st
import pandas as pd

from database.db import get_wishlist

st.title("❤️ Wishlist")

if "user" not in st.session_state:

    st.warning(
        "Please Login"
    )

    st.stop()

wishlist = get_wishlist(
    st.session_state["user"]
)

products = pd.read_csv(
    "data/products.csv"
)

wishlist_ids = [
    item[0]
    for item in wishlist
]

wishlist_products = products[
    products["product_id"]
    .isin(wishlist_ids)
]

if wishlist_products.empty:

    st.info(
        "Wishlist Empty"
    )

else:

    for _, product in wishlist_products.iterrows():

        st.image(
            "assets/products/"
            + product["image"],
            width=200
        )

        st.subheader(
            product["name"]
        )

        st.write(
            f"₹ {product['price']}"
        )

        st.divider()