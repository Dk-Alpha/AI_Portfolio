import streamlit as st
from streamlit_extras.let_it_rain import rain
# Configure the page
st.set_page_config(page_title="Dhruval Patel's Portfolio", layout="wide")

#Start rain
rain(
    emoji="❄️",
    font_size=30,
    falling_speed=5,
    animation_length="infinite",
)

st.image("./project/images/portfolio2.png")
st.markdown(
    """<style>
        div div div div div div div img{
            align:center;
        }
    </style>""", unsafe_allow_html=True
)
# Background styling


# Title and About Me Section
st.title("Dhruval Patel")
st.markdown(
    """<div style='text-align: center;'>
    <b>Master of Computer and Information Sciences</b> | University of Texas at Dallas<br>
    Passionate about <b>Machine Learning</b>, <b>Data Science</b>, and <b>AI</b><br>
    </div>""",
    unsafe_allow_html=True,
)

# Links
st.markdown(
    """<div style='text-align: center;'>
    <a href="https://www.linkedin.com/in/dhruval-patel-7926b3213/" target="_blank">LinkedIn</a> |
    <a href="https://github.com/Dk-Alpha" target="_blank">GitHub</a> |
    <a href="https://ijrar.org/papers/IJRAR23D1477.pdf" target="_blank">Publications</a>
    </div>""",
    unsafe_allow_html=True,
)

# Sections
st.header("Education")
st.markdown("""
- **Master of Computer and Information Sciences**, University of Texas at Dallas, GPA: 3.33 (Aug 2024 - May 2026)<br>
- **Bachelor of Technology in Computer Science and Engineering**, Indus University, GPA: 9.84/10 (Oct 2020 – Apr 2024)
""", unsafe_allow_html=True)

st.header("Professional Experience")
st.markdown("""
- **Computer Science Outreach Instructor | University of Texas at Dallas**<br>
  Taught Python and problem-solving to 50+ students, organized conferences and networking events. 🎓<br><br>
- **Machine Learning Research Intern | ISRO**<br>
  Developed models for ocean chlorophyll prediction, achieving 95% improved accuracy using ML techniques. 🚀<br><br>
- **Data Science Intern | Maxgen Technologies**<br>
  Applied ML techniques to real-world projects, improving accuracy by 15% on a house price prediction project. 💻
""", unsafe_allow_html=True)

st.header("Projects")
st.markdown("""
- **LeetCode Data Scraper**<br>
  Automated problem data collection using Python and Selenium for easier analysis and reference. 📊<br><br>
- **Story Generation from Images**<br>
  Developed an NLP-based tool to generate coherent stories from multiple image inputs. 📖<br><br>
- **Heart Failure Prediction**<br>
  Built ML models achieving 90% accuracy, published in a Web of Science journal. 🩺
""", unsafe_allow_html=True)

st.header("Skills")
st.markdown("""
- **Programming:** Python, SQL, Git, Streamlit<br>
- **Technologies:** Machine Learning, Data Visualization, Big Data Handling, Generative AI<br>
- **Soft Skills:** Teamwork, Communication, Leadership, Social Contribution<br>
""", unsafe_allow_html=True)

st.header("Certifications")
st.markdown("""
- Diploma in Multi-Lingual Programming, C-DAC<br>
- Advanced PHP, C-DAC<br>
- Online Courses: IBM Data Analytics, AWS NLP, Google IT Security<br>
""", unsafe_allow_html=True)
