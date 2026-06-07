import streamlit as st
import os

st.title(
    "🖼 Product Image Upload"
)

uploaded = st.file_uploader(
    "Upload Product Image",
    type=[
        "png",
        "jpg",
        "jpeg"
    ]
)

if uploaded:

    save_path = os.path.join(
        "assets/products",
        uploaded.name
    )

    with open(
            save_path,
            "wb") as f:

        f.write(
            uploaded.getbuffer()
        )

    st.success(
        "Image Uploaded"
    )