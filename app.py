import streamlit as st
from PIL import Image
from model import classify_clothes
from outfits import generate_outfit
from tryon import virtual_tryon

st.title("AI Outfit Generator")

user_file = st.file_uploader("صورتك", type=["jpg","png"])
cloth_file = st.file_uploader("اللبس", type=["jpg","png"])

if user_file and cloth_file:
    user_img = Image.open(user_file)
    cloth_img = Image.open(cloth_file)

    st.image(user_img)
    st.image(cloth_img)

    if st.button("Generate"):
        item = classify_clothes(cloth_img)
        outfit = generate_outfit(item)
        result = virtual_tryon(user_img, cloth_img)

        st.write("النوع:", item)
        st.write("الأوتفيت:", outfit)
        st.image(result)
