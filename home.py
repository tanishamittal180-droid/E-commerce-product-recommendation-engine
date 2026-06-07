import streamlit as st

st.title(
    "🏠 Home"
)

if "user" in st.session_state:

    st.success(
        f"Welcome {st.session_state['user']}"
    )

else:

    st.warning(
        "Login First"
    )

st.image(
    "assets/banner.jpg",
    use_container_width=True
)