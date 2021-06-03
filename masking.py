import streamlit as st
from PIL import Image,ImageDraw
def app():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://images.unsplash.com/photo-1516724562728-afc824a36e84?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1351&q=80") no-repeat center fixed;
            background-size: cover;
        }
    .sidebar .sidebar-content {
            background: url("url_goes_here")
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("MASKING")
    im1=st.file_uploader(label="UPLOAD IMAGE 1")
    im2=st.file_uploader(label="UPLOAD IMAGE 2")
    
    choice=st.selectbox("",("Composite the whole area at a uniform rate","Create mask image by drawing"))
    if choice=="Composite the whole area at a uniform rate":
        if im1 and im2:
            im1=Image.open(im1)
            im2=Image.open(im2)
            im2=im2.resize(im1.size)
            mask = Image.new("L", im1.size, 128)
            im = Image.composite(im1, im2, mask)
            st.title("FINAL IMAGE")
            st.image(im)
    else:
        if im1 and im2:
            im1=Image.open(im1)
            im2=Image.open(im2)
            im2=im2.resize(im1.size)
            mask = Image.new("L", im1.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((140, 50, 260, 170), fill=255)
            im = Image.composite(im1, im2, mask)
            st.image(im)