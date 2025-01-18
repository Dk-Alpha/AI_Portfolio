import streamlit as st

@st.dialog("Contact Me")
def show_contact_form():
    st.text_input("First Name")
    st.text_input("Enter E-mail")
    st.text_area("Your message")

    if st.button("Send"):
        st.write("Message sent Thankyou!")

@st.dialog("Connect here")
def show_connection_form():
    st.link_button("LinkedIN",url="https://www.linkedin.com/in/dhruval-patel-7926b3213/")
    st.write("or")
    st.link_button("Github Profile", url="https://github.com/Dk-Alpha")

    st.image("./project/images/linkedin_qr.png",caption="LinkedIN")
    st.write("or")
    st.image("./project/images/github_qr.png", caption="Github")
    