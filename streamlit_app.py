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

def set_bg_hack(image):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png_file"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<\style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/9c93ef77-0238-419f-9df2-ba3d2371f360/IU6MBRUGKX.json")
img_cs16 = Image.open("Images/mqdefault.webp")
img_andres = Image.open("Images/andres.jpg")
png_file = Image.Open("Images/Background.png")

# ---- HEADER SECTION ----
st.subheader("Hi, I am Andres :wave:")
st.title("A Student, Gamer From Philippines")
st.write("I am passionate about trying to figure out how to spend more time doing what makes me and my family happy.")
st.write("[Learn More >](https://www.facebook.com/profile.php?id=100084117730201)")

# ---- MY PROFILE ----
st.subheader("Hi, I am Andres Luis Francisco but u can call me Andres or Luis :wave:")
st.title("I am 17 years old")
st.write("I was born in 2006 November 30th.")
st.write("I am a grade 10 student from CCS (Canlubang Christian School).")
st.write("I am interested in 3d modeling, becoming a youtuber, gaming, coding, building a pc.")
st.write("My profile while it doesnt seem much. i hope you all people get to know me better with this infomation.")
image_column, = st.columns((1))
with image_column:
        st.image(img_andres)



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
