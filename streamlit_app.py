from PIL import Image
import requests
import base64
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


    
set_background("Images/Test.gif")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<\style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/9c93ef77-0238-419f-9df2-ba3d2371f360/IU6MBRUGKX.json")
img_cs16 = Image.open("Images/mqdefault.webp")
img_andres = Image.open("Images/andres1.jpg")
gif_file = Image.open("Images/Test.gif")
img_m16 = Image.open("Images/m16.webp")
img_mp5 = Image.open("Images/mp5.webp")
img_ak47 = Image.open("Images/ak47.jpg")

# ---- MY PROFILE ----
st.subheader("Hi, I am Andres Luis Francisco, but u can call me Andres or Luis :wave:")
st.title("I am 17 years old")
st.title("A Grade 10 Student, that is studying from Canlubang Christian School")
st.title("I am currently interested in learning, Coding, Modelling, Mapping, Gaming, ICT, Building Personal Computers, And Doing Youtube Videos")
st.title("I hope we can be friends, or best friends if u want, also below picture is myself hehe")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(img_andres)

# ---- MY ACTIVE PROFILE LINKS ----
st.subheader("ACTIVE PROFILES")
st.title("[Facebook Profile] (https://www.facebook.com/profile.php?id=100084117730201)")
st.title("[Steam Profile] (https://steamcommunity.com/profiles/76561198849072479/)")
st.title("[Youtube Profile] (https://www.youtube.com/channel/UCvYY3knD1bfT_S7sooNRxHQ)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my Youtube channel Im creating Gaming videos, Tutorials, Showcases for people who:
            - are looking for a way to be interested in my works.
            - are interested in what i am doing.
            - want to know and appreciate how i did this
            
            If this sounds interesting to you, consider subscribing and turning on the notifications so that u people get to know what time i will release my vids
            """
        )
        st.write("[Youtube Channel >](https://www.youtube.com/channel/UCvYY3knD1bfT_S7sooNRxHQ)")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
image_column, text_column = st.columns((1,2))
with image_column:
        st.image(img_cs16)
with text_column:
        st.subheader("Cs 1.6 knife and Cs 1.6 hands on cs 1.5 animation")
        st.write(
            """
            Watch to understand the skin i created for counter strike!
            this is one of my nicest projects i created in the free time i have.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=Mo753haFhaA)")

image_column, text_column = st.columns((1,2))
with image_column:
        st.image(img_ak47)
with text_column:
        st.subheader("MW2 AK47")
        st.write(
            """
            a skin that i created during free time once again
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=UlQwzbtPks4)")

image_column, text_column = st.columns((1,2))
with image_column:
        st.image(img_m16)
with text_column:
        st.subheader("COD4 M16")
        st.write(
            """
            another skin that i created during free time once again
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=8clYpTciZDE)")

image_column, text_column = st.columns((1,2))
with image_column:
        st.image(img_mp5)
with text_column:
        st.subheader("COD 4 MP5 ON LYNX'S MP5 ANIMATION")
        st.write(
            """
            once again another skin that i created during free time
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=j1Q31G5IJzg)")
        
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/totallynotpro302@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value ="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
            st.empty()
