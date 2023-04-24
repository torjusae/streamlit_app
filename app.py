from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":imp:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# load assets
lottie_coding = load_lottieurl(
    "https://assets6.lottiefiles.com/packages/lf20_dj2iGEFiUX.json"
)
img_contact_form = Image.open("images/grom.jpg")
img_lottie_animation = Image.open("images/chicken.jpg")

with st.container():
    # Header section
    st.subheader("Hei, jeg er Torjus :wave:")
    st.title("En datascientist i Å Energi")
    st.write(
        "Jeg vil utforske FastAI og måter for å bruke python til å raskt trene dyplæringsmodeller."
    )
    st.write("[Lær mer >](https://vg.no)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
        På fritiden liker jeg å:
        - lage middager fra bunnen av ved å følge mealprep oppskrifter for store kvanta med proteiner.
        - Spise boller og brus i sus og i dus.
        - programmere sideprosjekter i react, python, fastai, notebooks og med workflow verktøy.

        Hvis dette høres interessant ut, subscribe til youtube channelen til Asbjørn
        
        """
        )

        st.write("[Youtube Channel >](https://youtube.com)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation, width=400)
    with text_column:
        st.subheader("Wow raid boss mists of pandaria dlc tutorial")
        st.write(
            """
            Learn how to use Lottie files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie files are the easiest way to do it.
            In this turoial, I'll show you exactly how to do it.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=jfKfPfyJRdk)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form, width=400)
    with text_column:
        st.subheader("Placeholder text 1")
        st.write(
            """
            Lorem ipsum Lottie x streamlit tutorial
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=jfKfPfyJRdk)")
