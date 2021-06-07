import streamlit as st
from PIL import Image,ImageDraw
import base64 
from io import BytesIO
def app():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://images.unsplash.com/photo-1576502200916-3808e07386a5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1046&q=80") no-repeat center fixed;
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
            st.text(im.format)
            # rgb_im = im.convert("RGB")
            buffered = BytesIO()
            im.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            href = f'<a href="data:file/png;base64,{img_str}" download="final image.png"><h1>Download final image</h1></a>'
            st.markdown(href, unsafe_allow_html=True)
            
    else:
        if im1 and im2:
            im1=Image.open(im1)
            im2=Image.open(im2)
            im2=im2.resize(im1.size)
            mask = Image.new("L", im1.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((100, 100, 200, 200), fill=255)
            im = Image.composite(im1, im2, mask)
            
            st.image(im)
            # rgb_im = im.convert("RGB")
            buffered = BytesIO()
            im.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            href = f'<a href="data:file/png;base64,{img_str}" download="final image.png"><h1>Download final image</h1></a>'
            st.markdown(href, unsafe_allow_html=True)
    