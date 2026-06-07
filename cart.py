import streamlit as st
import pandas as pd

from database.db import get_cart

st.title("🛒 My Cart")

if "user" not in st.session_state:

    st.warning(
        "Please Login"
    )

    st.stop()

cart = get_cart(
    st.session_state["user"]
)

products = pd.read_csv(
    "data/products.csv"
)

cart_ids = [
    item[0]
    for item in cart
]

cart_products = products[
    products["product_id"]
    .isin(cart_ids)
]

if cart_products.empty:

    st.info(
        "Cart Empty"
    )

else:

    total = 0

    for _, product in cart_products.iterrows():

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

        total += product["price"]

        st.divider()

    st.success(
        f"Total Amount: ₹ {total}"
    )