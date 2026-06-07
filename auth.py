import streamlit as st

from database.db import register_user, login_user

st.set_page_config(
    page_title="Authentication",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Login / Register System")

# ------------------------
# SESSION STATE
# ------------------------
if "user" not in st.session_state:
    st.session_state["user"] = None

# ------------------------
# TOGGLE
# ------------------------
choice = st.radio(
    "Choose Action",
    ["Login", "Register"]
)

# ------------------------
# LOGIN
# ------------------------
if choice == "Login":

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = login_user(username, password)

        if user:
            st.session_state["user"] = username
            st.success(f"Welcome {username}")
            st.rerun()

        else:
            st.error("Invalid username or password")

# ------------------------
# REGISTER
# ------------------------
else:

    username = st.text_input("New Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):

        success = register_user(username, email, password)

        if success:
            st.success("Account created successfully! Now login.")
        else:
            st.error("Username or email already exists")