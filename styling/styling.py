import streamlit as st
from PIL import Image
with open('style.css') as f:
    st.markdown(f'<style>(f.read())</style>',unsafe_allow_html=True)
image = Image.open('ESpente.jpg')
st.image(image)
video_file = open('D:\hackelite\deo2.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.button("Get Started->")
