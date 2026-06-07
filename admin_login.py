import streamlit as st

st.title("🔐 Admin Login")

admin_password = st.text_input(
    "Admin Password",
    type="password"
)

if st.button("Login"):

    if admin_password == "admin123":

        st.session_state["admin"] = True

        st.success(
            "Admin Logged In"
        )

    else:

        st.error(
            "Invalid Password"
        )