import streamlit as st

from src.customers_bought import (
    customers_also_bought
)

st.title(
    "🛒 Customers Also Bought"
)

products = customers_also_bought()

for _, product in products.iterrows():

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