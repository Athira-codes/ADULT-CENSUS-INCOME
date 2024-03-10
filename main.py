pip install streamlit_option_menu
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(
    page_title="adult census income",
)
import home,about,comment


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

def run():

        with st.sidebar:
            app = option_menu(
                menu_title='',
                options=['Home', 'about','comment'],
                icons=['house-fill','info-circle-fill','chat-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
        "container": {"padding": "5!important", "background-color": 'black'},
        "icon": {"color": "white", "font-size": "23px"},
        "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                     "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"}, }

             )

        if app == "Home":
            home.app()
        if app == "comment":
            comment.app()
        if app == "about":
            about.app()

run()
