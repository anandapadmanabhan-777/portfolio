import streamlit as st
import os
from streamlit_option_menu import option_menu
from keras.models import load_model
import about as ab
import connect as co
import home2 as h2
import projects as pr


# Set up page configuration
st.set_page_config(
    page_title="AI Portfolio", 
    page_icon="https://github.com/anandapadmanabhan-777/JustAnImage/raw/main/ai_brain.png", 
    layout="wide")

# Get the path of the current working directory
#css_path = os.path.join(os.getcwd(), "styles.css")

# Read the CSS file and apply styles
#with open(css_path) as f:
    #st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Injecting custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navbar menu
selected = option_menu(
    menu_title=None,
    options=["Home", "AI/ML Projects", "About Me", "Get in Touch"],
    icons=["house-door-fill", "server", "person-vcard-fill", "telephone-fill"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#ffffff", "border-radius": "7px", },
        "icon": {"color": "#fe6601", "font-size": "23px", },  # Default icon color
        "nav-link": {"font-size": "23px", "text-align": "center", "margin": "0px", "color": "black", "border-radius": "7px",},  # Default link color
        "nav-link-selected": {"background-color": "#ffe9c9", "color": "black",},        
    }   
)

# Render content based on navigation
if selected == "Home":
    h2.home2()

elif selected == "AI/ML Projects":
    pr.projects()

elif selected == "About Me":
    ab.about()

elif selected == "Get in Touch":
    co.connect()
