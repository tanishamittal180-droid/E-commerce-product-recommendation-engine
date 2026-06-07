import streamlit as st
import sqlite3
import pandas as pd

st.title(
    "👥 User Management"
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

users = pd.read_sql_query(
    "SELECT * FROM users",
    conn
)

conn.close()

st.dataframe(
    users,
    use_container_width=True
)