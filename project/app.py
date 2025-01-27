import streamlit as st
import streamlit_card as sc

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

#NAVIGATION SETUP
pg=st.navigation(
    {
        "Folio":[portfolio],
        "Pages":[about_me,stats,ask_ai]
    }
)
pg.run()