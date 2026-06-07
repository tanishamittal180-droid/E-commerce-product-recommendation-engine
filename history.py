import streamlit as st


def add_recent(product_id):

    if "recent" not in st.session_state:

        st.session_state["recent"] = []

    st.session_state["recent"].append(
        product_id
    )


def get_recent():

    return st.session_state.get(
        "recent",
        []
    )