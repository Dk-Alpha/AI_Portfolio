import streamlit as st
from forms.contact_form import show_contact_form
from forms.contact_form import show_connection_form

#Define callables

st.title("About Me")
with st.container():
    col1,col2=st.columns(2, gap="small", vertical_alignment="center")
    with col1:
        st.image(image="./project/images/about_me_self.jpg" )
    with col2:
        st.title("Dhruval Patel")
        st.write("Master's student in Computer Science at the University of Texas at Dallas, with a strong passion for Machine Learning and Data Science. My academic journey and professional experiences have equipped me with a solid foundation in predictive modeling, data analysis, and generative AI technologies. I enjoy exploring how cutting-edge algorithms can solve real-world problems")
        ic1,ic2=st.columns(2,gap="small",vertical_alignment="center")
        with ic1:
            if st.button("Contact Me"):
                show_contact_form()
        with ic2:
            if st.button("Connect Here"):
                show_connection_form()