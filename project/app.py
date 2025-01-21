# import streamlit as st
# import streamlit_card as sc
# import ollama

# #callables
# def generate_response(inp):
#     resp=ollama.generate(model="victor", prompt=inp)
#     return resp["response"]

# def about_me():
#     st.empty()
#     st.write("working on it!")
# def ask_ai():
#     st.empty()
#     options = ["Publications?", "Professional Profile Links?", "Internship at ISRO", "About Communication Skills"]
#     selection = st.segmented_control(
#         "", options, selection_mode="single"
#     )
#     if selection!=None:
#         built_in_resp=generate_response(selection)
#         st.write(built_in_resp)
#     with st.sidebar:
#         # st.image("")
#         st.write("Ask anything about my professional journey")
#         question=st.text_area("Questions here")
#         submitted=st.button("ask")

#     if submitted:
#         q_resp=generate_response(question)
#         st.write(q_resp)

# st.title("Portfolio")

# with st.container():
#     col1,col2=st.columns(2)
#     with col1:
#         c1=sc.card(title="About Me!",text="About Dhruval",on_click=about_me)
#     with col2:
#         c2=sc.card(title="Ask AI!", text="Ask AI about Dhruval",on_click=ask_ai)

import streamlit as st
import streamlit_card as sc

#PAGE SETUP
about_me=st.Page(
    page="about_me.py",
    title="About Me",
    default=True
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
        "Pages":[about_me,stats,ask_ai]
    }
)
pg.run()