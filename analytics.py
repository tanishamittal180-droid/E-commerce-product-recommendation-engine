import streamlit as st
import pandas as pd
import plotly.express as px

products = pd.read_csv(
    "data/products.csv"
)

st.title(
    "📊 Analytics Dashboard"
)

st.metric(
    "Total Products",
    len(products)
)

st.metric(
    "Categories",
    products["category"].nunique()
)

category_count = (
    products["category"]
    .value_counts()
)

fig = px.bar(
    category_count,
    title="Products By Category"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

price_fig = px.pie(
    products,
    names="category",
    values="price",
    title="Category Share"
)

st.plotly_chart(
    price_fig,
    use_container_width=True
)