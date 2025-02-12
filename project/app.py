import streamlit as st
import chat_engine

#Check once if model is downloaded or not
def ensure_model_downloaded():
    if 'model_downloaded' not in st.session_state:  # Check if the model is already downloaded
        # Call the function to check and download the model if needed
        with st.sidebar:
            chat_engine.download_model()  # This is the function that checks and downloads the model
        st.session_state.model_downloaded = True  # Set the flag to True once downloaded

#PAGE SETUP
portfolio=st.Page(
    page="portfolio.py",
    title="Portfolio",
    default=True
)
about_me=st.Page(
    page="about_me.py",
    title="About Me"
)
stats=st.Page(
    page="stats.py",
    title="My Statistics"
)
ask_ai=st.Page(
    page="ask_ai.py",
    title="Ask Victor"
)

#

#NAVIGATION SETUP
pg=st.navigation(
    {
        "Folio":[portfolio],
        "Pages":[about_me,stats,ask_ai]
    }
)
pg.run()
ensure_model_downloaded()