import streamlit as st;
from PIL import Image
image = Image.open('ESpente.jpg')
st.sidebar.image(image);
st.sidebar.header("Options")
st.sidebar.add_rows("About")
