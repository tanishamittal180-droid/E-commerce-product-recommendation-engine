import streamlit as st

st.title("👤 User Profile")

if "user" not in st.session_state:

    st.warning(
        "Please Login"
    )

    st.stop()

st.success(
    f"Welcome {st.session_state['user']}"
)

st.info(
    "Manage your account and view activity."
)

st.write(
    "Username:",
    st.session_state["user"]
)

st.metric(
    "Account Status",
    "Active"
)