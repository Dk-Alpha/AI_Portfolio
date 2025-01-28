import streamlit as st
from chat_engine import generate_response
st.title("Ask VICTOR")

#I am using Session state for maintaining chat history. No other option
if "messages" not in st.session_state:
    st.toast("Note: I am still working on the chat bot to provide full fledged information and each and every single detail of my projects and folios. STILL WORKING")
    st.session_state.messages = []  # List to store message history

# Welcome message from Victor
if len(st.session_state.messages) == 0:
    intro=generate_response("Victor you will act as a chatbot to answer all the queries of people visitng this portfolio website about Dhruval Patel. Welcome them and ask how you can help them today.")
    st.session_state.messages.append({"role": "ai", "content": intro})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "ai":
        st.chat_message("ai").write(message["content"])

inp=st.chat_input("Ask here")
if inp:
    #User chat
    user=st.chat_message("user")
    st.session_state.messages.append({"role": "user", "content": inp})
    user.write(inp)

    #Victor Bot
    victor=st.chat_message("ai")
    bot_resp=generate_response(inp)
    st.session_state.messages.append({"role": "ai", "content": bot_resp})
    victor.write(bot_resp)
