import streamlit as st
from PIL import Image
import webbrowser
import streamlit_book as stb
import matplotlib
import numpy


with open('style.css') as f:
    st.markdown(f'<style>(f.read())</style>',unsafe_allow_html=True)
image = Image.open('ESpente.jpg')
st.image(image)
video_file = open('/home/user/Documents/VS_Code/ESPENDY/deo2.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

def main_page():
        btn1 = st.button("Get Started->")

        if btn1:
            st.session_state.runpage = open("Csvtograph.py")

main_page()       

url='https://github.com/omals/Hack_Elite'
url2 = 'https://www.google.com/finance/?hl=en'
if st.button ('Github Repo'):
    webbrowser.open_new_tab(url)
if st.button('Finance Details'):
    webbrowser.open_new_tab(url2)




