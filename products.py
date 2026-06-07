import streamlit as st
import pandas as pd

from database.db import (
    add_to_cart,
    add_to_wishlist,
    place_order
)

from src.recommender import RecommendationEngine
from src.history import add_recent

# -------------------------
# PAGE SETTINGS
# -------------------------

st.set_page_config(
    page_title="Products",
    page_icon="🛍",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

.product-card{
    background:#ffffff;
    padding:15px;
    border-radius:15px;
    border:1px solid #e0e0e0;
    margin-bottom:20px;
}

.price{
    color:green;
    font-size:22px;
    font-weight:bold;
}

.rating{
    color:orange;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# LOGIN CHECK
# -------------------------

if "user" not in st.session_state:

    st.warning(
        "Please login first."
    )

    st.stop()

# -------------------------
# LOAD DATA
# -------------------------

products = pd.read_csv(
    "data/products.csv"
)

engine = RecommendationEngine()

# -------------------------
# HEADER
# -------------------------

st.title(
    "🛍 Product Catalog"
)

st.write(
    "Browse products and receive AI-powered recommendations."
)

# -------------------------
# SEARCH
# -------------------------

search = st.text_input(
    "🔍 Search Products"
)

# -------------------------
# CATEGORY FILTER
# -------------------------

categories = ["All"] + list(
    products["category"].unique()
)

selected_category = st.selectbox(
    "Category",
    categories
)

# -------------------------
# PRICE FILTER
# -------------------------

max_price = int(
    products["price"].max()
)

price_range = st.slider(
    "Maximum Price",
    min_value=0,
    max_value=max_price,
    value=max_price
)

# -------------------------
# APPLY FILTERS
# -------------------------

filtered = products.copy()

if search:

    filtered = filtered[
        filtered["name"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

if selected_category != "All":

    filtered = filtered[
        filtered["category"]
        == selected_category
    ]

filtered = filtered[
    filtered["price"]
    <= price_range
]

# -------------------------
# PRODUCT COUNT
# -------------------------

st.info(
    f"{len(filtered)} products found"
)

# -------------------------
# DISPLAY PRODUCTS
# -------------------------

cols = st.columns(3)

for index, product in filtered.iterrows():

    with cols[index % 3]:

        st.markdown(
            '<div class="product-card">',
            unsafe_allow_html=True
        )

        image_path = (
            "assets/products/"
            + product["image"]
        )

        try:

            st.image(
                image_path,
                use_container_width=True
            )

        except:

            st.image(
                "assets/logo.png",
                use_container_width=True
            )

        st.subheader(
            product["name"]
        )

        st.markdown(
            f'<p class="price">₹ {product["price"]}</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<p class="rating">⭐ {product["rating"]}</p>',
            unsafe_allow_html=True
        )

        st.write(
            "**Category:**",
            product["category"]
        )

        st.write(
            product["description"]
        )

        # ---------------------
        # VIEW PRODUCT
        # ---------------------

        if st.button(
            f"👁 View {product['product_id']}"
        ):

            add_recent(
                product["product_id"]
            )

            st.success(
                "Added to recently viewed"
            )

        # ---------------------
        # CART
        # ---------------------

        if st.button(
            f"🛒 Cart {product['product_id']}"
        ):

            add_to_cart(
                st.session_state["user"],
                product["product_id"]
            )

            st.success(
                "Added to cart"
            )

        # ---------------------
        # WISHLIST
        # ---------------------

        if st.button(
            f"❤️ Wishlist {product['product_id']}"
        ):

            add_to_wishlist(
                st.session_state["user"],
                product["product_id"]
            )

            st.success(
                "Added to wishlist"
            )

        # ---------------------
        # BUY NOW
        # ---------------------

        if st.button(
            f"⚡ Buy {product['product_id']}"
        ):

            place_order(
                st.session_state["user"],
                product["product_id"],
                product["price"]
            )

            st.success(
                "Order placed successfully"
            )

        # ---------------------
        # SIMILAR PRODUCTS
        # ---------------------

        with st.expander(
            "🎯 Similar Products"
        ):

            try:

                recommendations = (
                    engine.get_similar_products(
                        product["product_id"],
                        top_n=3
                    )
                )

                for item in recommendations:

                    st.write(
                        f"✅ {item['name']}"
                    )

                    st.progress(
                        int(item["score"])
                    )

                    st.caption(
                        f"Match Score: {item['score']}%"
                    )

            except Exception:

                st.warning(
                    "No recommendations found."
                )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

# -------------------------
# FOOTER
# -------------------------

st.divider()

st.caption(
    "E-Commerce Product Recommendation Engine"
)
