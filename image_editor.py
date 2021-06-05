import streamlit as st
from PIL import Image, ImageFilter,ImageFont,ImageDraw,ImageOps
import base64
from io import BytesIO
def app():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://images.unsplash.com/photo-1542124292-60272943a355?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1351&q=80") no-repeat center fixed;
            background-size: cover;
        }
    .sidebar .sidebar-content {
            background: url("url_goes_here")
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('image editor')
    img_file=st.file_uploader('upload image')
    def get_image():
        return img_file
    img_file=get_image()
    if img_file:
        img=Image.open(img_file)
        
        st.title("FILTERS")
        option=st.selectbox("...",("none",'SHARPEN','SMOOTH','EMBOSS','CONTOUR','BLUR','BOX BLUR','EDGE ENHANCE'))
        if option=='SHARPEN':
            img=img.filter(ImageFilter.SHARPEN())
        elif option=='SMOOTH':
            img=img.filter(ImageFilter.SMOOTH())
        elif option=='EMBOSS':
            img=img.filter(ImageFilter.EMBOSS())
        elif option=='CONTOUR':
            img=img.filter(ImageFilter.CONTOUR())
        elif option=='BLUR':
            img=img.filter(ImageFilter.BLUR())
        elif option=="BOX BLUR":
            img=img.filter(ImageFilter.BoxBlur(),radius=1)
        elif option=="EDGE ENHANCE":
            img=img.filter(ImageFilter.EDGE_ENHANCE())
        st.title("ROTATE")
        d=st.number_input(" enter degree")
        img=img.rotate(int(d))
        st.title("paste image")
        p=st.file_uploader("")
        if p:
            width=st.slider("enter x1",0,img.width)
            height=st.slider("enter x2",0,img.height)
            p=Image.open(p)
            img.paste(p,(int(width),int(height)))
            # st.header("BLENDING")
            # st.slider("",1,10)
            # img=Image.blend(img, p.convert(img.format), 0.6)
        st.title("RESIZE")
        w=st.slider("enter width",1920,1)
        h=st.slider("enter height",1080,1)
        img=img.resize((int(w),int(h)))
        st.title("CROP IMAGE")
        x1=st.slider('x1',0,img.width)
        y1=st.slider('y1',0,img.height)
        x2=st.slider('x2',img.width,0)
        y2=st.slider('y2',img.height,0)
        img=img.crop((x1,y1,x2,y2))
        st.title("ADD TEXT")
        t=st.text_input("enter text")
        
        # st.header("choose text color")
        # color_picker = ColorPicker(color="#ff4466", title="Choose color:", width=200)
        # st.bokeh_chart(color_picker)
        # # a=st.color_picker(label="choose color")
        choice=st.selectbox("choose font",("OdibeeSans-Regular","RobotoMono-VariableFont_wght","ZCOOLKuaiLe-Regular"))
        f=st.number_input("enter font size")
        if choice=="RobotoMono-VariableFont_wght":
            font=ImageFont.truetype('RobotoMono-VariableFont_wght.ttf',int(f))
        elif choice=="OdibeeSans-Regular":
            font=ImageFont.truetype('OdibeeSans-Regular.ttf',int(f))
        elif choice=="ZCOOLKuaiLe-Regular":
            font=ImageFont.truetype('ZCOOLKuaiLe-Regular.ttf',int(f))
        writer=ImageDraw.Draw(img)
        writer.text((100,100),t,font=font,fill=(255,0,255))
        
        st.title("FLIP THE IMAGE")
        option2=st.selectbox("",("none",'FLIP_LEFT_RIGHT','FLIP_TOP_BOTTOM','ROTATE_90'))
        if option2 == 'FLIP_LEFT_RIGHT':
            img=img.transpose(Image.FLIP_LEFT_RIGHT)
        elif option2=='FLIP_TOP_BOTTOM':
            img=img.transpose(Image.FLIP_TOP_BOTTOM)
        elif option2=='ROTATE_90':
            img=img.transpose(Image.ROTATE_90)
        st.title("Add border")
        a=st.slider("border width",1,100)
        img = ImageOps.expand(img, border=int(a), fill=(75, 100, 0))
        st.image(img)
        st.subheader("size")
        st.text(img.size)
        st.subheader("mode")
        st.text(img.mode)

        # st.text(img.format)
        buffered = BytesIO()
        if img.format=='JPEG':
            img.save(buffered, format="JPEG")
        elif img.format=='PNG':
            img.save(buffered,format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        href = f'<a href="data:file/jpg;base64,{img_str}" download="final image.jpg"><h1>Download final image</h1></a>'
        st.markdown(href, unsafe_allow_html=True)
        