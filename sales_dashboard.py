import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title(
    "💰 Sales Dashboard"
)

if not st.session_state.get(
        "admin",
        False):

    st.warning(
        "Admin Access Required"
    )

    st.stop()

conn = sqlite3.connect(
    "database.db"
)

orders = pd.read_sql_query(
    "SELECT * FROM orders",
    conn
)

conn.close()

if orders.empty:

    st.info(
        "No Orders Available"
    )

else:

    revenue = orders[
        "price"
    ].sum()

    st.metric(
        "Total Revenue",
        f"₹ {revenue}"
    )

    fig = px.histogram(
        orders,
        x="price",
        title="Order Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        orders,
        use_container_width=True
    )