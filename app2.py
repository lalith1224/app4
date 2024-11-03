from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie



st.set_page_config(page_title="HAPPY BIRTHDAY KAVIN",page_icon=":tada:",layout="wide")

def load_lottieurl(ur1):
    r=requests.get(ur1)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding=load_lottieurl("https://lottie.host/315c8d71-03f3-480f-b59a-8268fa0f424d/7Ji69i0XyT.json")

img_contact_form= Image.open("C:\\Users\\Hp\\Desktop\\birthday\\images\\kavin.png.png")
img_contact_form2=Image.open("C:\\Users\\Hp\\Desktop\\birthday\\images\\kavin2.jpg")
img_contact_form3=Image.open("C:\\Users\\Hp\\Desktop\\birthday\\images\\Kkavin3.jpg")

with st.container():

    st.header("HAPPY BIRTHDAY KAVIN ",)
    
    
    st.write(" ")
    st.header("MANY MORE RETURNS OF THE DAY DA  ") 


with st.container():
    st.write("-----------")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("TREAT MUKKAYAM DA")
with right_column:
    st_lottie(lottie_coding,height=500,key="happy birthday")

image_column, text_column=st.columns((1,2))
with image_column:
           st.image(img_contact_form)

           

        
        
    
                             
with st.container():
    st.write("--------")
    st.header("HAPPY BIRTHDAY")
    st.write("##")
    st.header("MEMRIES WE CREATED")
    image_column, image_column2=st.columns((1,2))
    with image_column:
           st.image(img_contact_form2)
    with image_column2:
           st.image(img_contact_form3)
           

    
    image_column, text_column=st.columns((1,2))
    with text_column:
        st.subheader("Y0UR BLOG  ")
        st.write("IS HERE CLICK HERE")
        st.markdown("[SEE THIS .....](http://debugdaires.blogspot.com)")

        contact_form = """
        <form action="https://formsubmit.co/727624bcs025@mcet.in" method="POST">
           <input type="hidden" name="_captcha" value="false"> 
           <input type="text" name="name"placeholder="Your name" required>
           <input type="email" name="email"placeholder="Your email"required>
           <textarea name="message"placeholder="Your message here "required></textarea>
           <button type="submit">Send</button>
        </form>
        """
        left_column,right_column =st.columns(2)
        with left_column:
            st.markdown(contact_form,unsafe_allow_html=True)
        with right_column:
            st.empty

