import streamlit as st
import chat_engine
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

st.subheader("Motivation for Choosing my Career Path", divider=True)
st.write("""
During my formative years in school, my active engagement in social work programs exposed me to the stark realities of individuals battling chronic diseases, grappling with the harsh challenge of securing a single meal. Witnessing the poignant struggles of those afflicted by relentless illnesses, particularly cancer, left an indelible impact on me, sparking a deep sense of empathy and a profound desire to contribute meaningfully. This reflection prompted profound introspection, leading me to question: What could I do to alleviate their suffering? It was during this contemplation that my interest in Artificial Intelligence (AI) and its transformative potential burgeoned.
 The prospect of employing technology to reanimate non-functional parts of the human body, offering the possibility for paralyzed individuals to regain mobility by rejuvenating dormant nerve cells, fuelled my curiosity. The untapped potential of AI resonated with the conviction that it could unlock concealed realms within the human brain, catapulting cognitive abilities to unprecedented heights. This revelation became particularly poignant as I contemplated its potential role in not only healing but also eradicating cancer cells within the human body. 
Embarking on the journey to pursue an undergraduate program in Computer Science was not just a choice; it was a culmination of early fascination coupled with a discerning observation of the field's meteoric rise and unwavering confidence in its future prospects.
""")
st.subheader("Studies",divider=True)
st.markdown("#### Bachelor of Technology in Computer Science and Engineering", unsafe_allow_html=True)
st.write("""
Indus University, Ahmedabad, India
Cumulative GPA: 9.84/10

During my Bachelor’s, I concentrated on exploring and mastering Data Science and Machine Learning pathways. My journey in Machine Learning began with classic models using Sci-kit Learn, Seaborn, and Matplotlib. I utilized Kaggle as a data source, experimenting with various models and data pre-processing techniques to uncover what information was necessary and what was extraneous.

This exploration taught me the importance of detecting and addressing inconsistencies in data beyond merely handling null values. It was through iterative practice that I learned to manipulate and transform data to extract valuable insights. My interest extended to data visualization, where I gained the ability to compare model outputs with original datasets, helping to refine and evaluate model performance.

In addition to my focus on Machine Learning, my coursework provided a strong foundation in:
<nbsp><nbsp>
- Programming Languages: C++, Java, and Python
- Core Subjects: Operating Systems, Database Design, Theory of Computation, Finite Automata, and Machine Learning Theory
- Web Development: HTML, CSS, and JavaScript
<nbsp><nbsp>
My dedication to practical learning led me to undertake numerous hands-on projects that honed my skills in data handling, visualization, and model evaluation. These experiences culminated in an internship at the Indian Space Research Organization (ISRO), marking the beginning of my journey into impactful and research-oriented work.
""", unsafe_allow_html=True)

st.markdown("#### Master of Science in Computer Science", unsafe_allow_html=True)
st.write("""
University of Texas at Dallas, USA

My journey to the University of Texas at Dallas wasn’t a straightforward one—it was built on determination and the willingness to take risks. Back in May 2022, while many of my peers were focused on placements, I decided to pursue something different. I withdrew from the placement process and set my sights on higher studies in the USA.

The preparation wasn’t easy. Balancing my final year of undergrad while studying for the GRE and English proficiency tests demanded focus and discipline. By October 2023, I had successfully completed both and began applying to universities. When I received an admit from UTD, I was thrilled. However, one significant hurdle remained—the visa.

The visa process was nerve-wracking; I had put everything on the line for this dream. But in May 2024, I was granted the visa, a moment that marked the start of a new chapter. Leaving behind my internship, I packed my bags and arrived in Texas with a mix of excitement and apprehension.

The first semester was challenging as I adjusted to a new education system. I studied courses like Statistics for Data Science, Discrete Mathematics, and Database Design, earning a GPA of 3.33. Though I wasn’t fully satisfied with my grades, I saw it as an opportunity to grow and improve.

Alongside my studies, I became a Computer Science Outreach Instructor, a role that taught me so much beyond academics. I learned to communicate effectively, manage events, and even organize a conference. These experiences helped me adapt to this new environment while developing leadership and teamwork skills.

Looking back, the journey has been anything but easy. Yet, each step—from leaving placements behind to achieving my first semester at UTD—has strengthened my resolve. I’m excited for the semesters ahead and committed to giving my absolute best.
""", unsafe_allow_html=True)

#Work Experience

st.subheader("Work Experience", divider=True)
st.write("""
Ahmedabad, India <nbsp>

Landing my first internship was no easy task, especially without prior experience. Driven by a desire to learn, I began going door-to-door to every startup I could find in Ahmedabad, India, pitching myself as a motivated student eager to work. Eventually, my persistence led me to Maxgen Technologies, a Pune-based startup offering opportunities for freshers.

As a second-year bachelor’s student, I wasn’t their typical candidate, and they initially hesitated to bring me on board. Undeterred, I explained my passion for learning, emphasizing that I wasn’t looking for monetary compensation but rather an opportunity to gain real-world experience. My enthusiasm and budding knowledge impressed the hiring manager, who saw potential in me and agreed to train me for six months.

Balancing college and the internship was challenging yet rewarding. Every day, after attending my classes, I would head to the company around 4 PM and stay until 8 PM, dedicating those four hours to learning and contributing. While the internship was unpaid, the value I gained in terms of skills and exposure was priceless.

During my time at Maxgen, I worked on multiple projects and gained hands-on experience with essential tools like Seaborn, Scikit-learn, and basic TensorFlow. I learned the theoretical foundations and practical applications of classic machine learning models such as K-Nearest Neighbors (KNN), Support Vector Machines (SVM), and Decision Trees. This experience not only introduced me to the world of data science but also instilled the confidence to tackle real-life problems.

My internship at Maxgen was more than just training; it was the foundation of my journey into machine learning and data science. It taught me the importance of persistence, the value of hands-on learning, and the dynamics of working within an organization.

During my Bachelor’s, I concentrated on exploring and mastering Data Science and Machine Learning pathways. My journey in Machine Learning began with classic models using Sci-kit Learn, Seaborn, and Matplotlib. I utilized Kaggle as a data source, experimenting with various models and data pre-processing techniques to uncover what information was necessary and what was extraneous.

This exploration taught me the importance of detecting and addressing inconsistencies in data beyond merely handling null values. It was through iterative practice that I learned to manipulate and transform data to extract valuable insights. My interest extended to data visualization, where I gained the ability to compare model outputs with original datasets, helping to refine and evaluate model performance.

In addition to my focus on Machine Learning, my coursework provided a strong foundation in:
<nbsp><nbsp>
- Programming Languages: C++, Java, and Python
- Core Subjects: Operating Systems, Database Design, Theory of Computation, Finite Automata, and Machine Learning Theory
- Web Development: HTML, CSS, and JavaScript
<nbsp><nbsp>
My dedication to practical learning led me to undertake numerous hands-on projects that honed my skills in data handling, visualization, and model evaluation. These experiences culminated in an internship at the Indian Space Research Organization (ISRO), marking the beginning of my journey into impactful and research-oriented work.
""", unsafe_allow_html=True)

st.markdown("#### Indian Space Research Organization (ISRO)", unsafe_allow_html=True)
st.markdown("<strong>Atmospheric and Oceanic Sciences Group (AOSG), Scientific Research and Training Division (SRTD)</strong>", unsafe_allow_html=True)
st.write("""
Working as a Machine Learning Intern at the Indian Space Research Organization (ISRO) was a once-in-a-lifetime experience. It’s not every day that someone gets the opportunity to contribute to such a prestigious organization, and the memories of this internship remain close to my heart.

Under the guidance of Dr. Smitha Ratheesh, I was entrusted with a project titled "Reconstruction of Ocean Chlorophyll Using Machine Learning Techniques." This work required me to address the challenges of reconstructing oceanic data—particularly chlorophyll concentrations—using a combination of satellite and in-situ observation data.

In oceanic research, both in-situ sensors and satellite imaging are indispensable but come with limitations. In-situ measurements, while accurate, are expensive, time-intensive, and cannot cover large areas. Conversely, satellite imaging, though extensive, often suffers from inaccuracies due to sunlight interference, pixel resolution, and other environmental factors. My role was to leverage machine learning models to improve the accuracy of data reconstruction while minimizing the time required compared to traditional numerical models.

For this project, I used five years of data (2015-2019) collected over the Bay of Bengal, sourced from the Regional Ocean Modeling System (ROMS). Employing machine learning techniques, I tested and compared three models:

Sequential Artificial Neural Network (ANN)
Multilayer Perceptron (MLP)
Gradient Boosting Regression (GBR)
Through meticulous data preprocessing, visualization, and wrangling of multi-dimensional oceanic datasets, the Sequential ANN emerged as the most effective model. It demonstrated a lower Root Mean Square Error (RMSE) compared to the others. Furthermore, I conducted a sensitivity analysis on the Sequential ANN to evaluate the impact of individual variables on reconstruction accuracy. For example, removing nitrate data led to a 13% increase in error, highlighting its critical role in chlorophyll reconstruction.

This research underscored the value of machine learning in addressing ocean data's inherent complexities and showed how adaptive these techniques can be compared to traditional methods. An excerpt from the abstract of my paper summarizes the findings:

"This study underscores the efficacy of machine learning techniques in reconstructing ocean chlorophyll, offering faster and more adaptive solutions to enhance oceanographic research."

Beyond the technical aspects, this internship broadened my understanding of oceanic physics, geospatial data, and cloud masking techniques. It also allowed me to work alongside scientists, enhancing my professional collaboration and communication skills. Presenting my work to experts and receiving appreciation for my contributions bolstered my confidence.

As a recognition of my efforts, I received a Letter of Recommendation from the Head of SRTD. Completing this research project before coming to the U.S. was a proud milestone in my academic and professional journey.
""", unsafe_allow_html=True)

#Sidebar
with st.sidebar:
    with st.container():
        col1,col2=st.columns([0.3,0.7], gap="small",vertical_alignment="center")
        with col1:
          st.image("project/images/current_page.png")
        with col2:
          st.write("Portfolio")
    b1=st.button("Motivation summary")
    b2=st.button("Studies summary")
    b3=st.button("Work experience summary")
    if b1:
      #Summary of Motivation
      context="""
    During my formative years in school, my active engagement in social work programs exposed me to the stark realities of individuals battling chronic diseases, grappling with the harsh challenge of securing a single meal. Witnessing the poignant struggles of those afflicted by relentless illnesses, particularly cancer, left an indelible impact on me, sparking a deep sense of empathy and a profound desire to contribute meaningfully. This reflection prompted profound introspection, leading me to question: What could I do to alleviate their suffering? It was during this contemplation that my interest in Artificial Intelligence (AI) and its transformative potential burgeoned. The prospect of employing technology to reanimate non-functional parts of the human body, offering the possibility for paralyzed individuals to regain mobility by rejuvenating dormant nerve cells, fuelled my curiosity. The untapped potential of AI resonated with the conviction that it could unlock concealed realms within the human brain, catapulting cognitive abilities to unprecedented heights. This revelation became particularly poignant as I contemplated its potential role in not only healing but also eradicating cancer cells within the human body. Embarking on the journey to pursue an undergraduate program in Computer Science was not just a choice; it was a culmination of early fascination coupled with a discerning observation of the field's meteoric rise and unwavering confidence in its future prospects.
"""
      resp=chat_engine.generate_response("Give me a short summary of"+context+" , highlight only the main information to a third person")
      st.write(resp)
    if b2:
        #Studies summary
        context="""
    Bachelor of Technology in Computer Science and Engineering
Indus University, Ahmedabad, India Cumulative GPA: 9.84/10

During my Bachelor’s, I concentrated on exploring and mastering Data Science and Machine Learning pathways. My journey in Machine Learning began with classic models using Sci-kit Learn, Seaborn, and Matplotlib. I utilized Kaggle as a data source, experimenting with various models and data pre-processing techniques to uncover what information was necessary and what was extraneous.

This exploration taught me the importance of detecting and addressing inconsistencies in data beyond merely handling null values. It was through iterative practice that I learned to manipulate and transform data to extract valuable insights. My interest extended to data visualization, where I gained the ability to compare model outputs with original datasets, helping to refine and evaluate model performance.

In addition to my focus on Machine Learning, my coursework provided a strong foundation in:

Programming Languages: C++, Java, and Python
Core Subjects: Operating Systems, Database Design, Theory of Computation, Finite Automata, and Machine Learning Theory
Web Development: HTML, CSS, and JavaScript My dedication to practical learning led me to undertake numerous hands-on projects that honed my skills in data handling, visualization, and model evaluation. These experiences culminated in an internship at the Indian Space Research Organization (ISRO), marking the beginning of my journey into impactful and research-oriented work.
Master of Science in Computer Science
University of Texas at Dallas, USA

My journey to the University of Texas at Dallas wasn’t a straightforward one—it was built on determination and the willingness to take risks. Back in May 2022, while many of my peers were focused on placements, I decided to pursue something different. I withdrew from the placement process and set my sights on higher studies in the USA.

The preparation wasn’t easy. Balancing my final year of undergrad while studying for the GRE and English proficiency tests demanded focus and discipline. By October 2023, I had successfully completed both and began applying to universities. When I received an admit from UTD, I was thrilled. However, one significant hurdle remained—the visa.

The visa process was nerve-wracking; I had put everything on the line for this dream. But in May 2024, I was granted the visa, a moment that marked the start of a new chapter. Leaving behind my internship, I packed my bags and arrived in Texas with a mix of excitement and apprehension.

The first semester was challenging as I adjusted to a new education system. I studied courses like Statistics for Data Science, Discrete Mathematics, and Database Design, earning a GPA of 3.33. Though I wasn’t fully satisfied with my grades, I saw it as an opportunity to grow and improve.

Alongside my studies, I became a Computer Science Outreach Instructor, a role that taught me so much beyond academics. I learned to communicate effectively, manage events, and even organize a conference. These experiences helped me adapt to this new environment while developing leadership and teamwork skills.

Looking back, the journey has been anything but easy. Yet, each step—from leaving placements behind to achieving my first semester at UTD—has strengthened my resolve. I’m excited for the semesters ahead and committed to giving my absolute best.
"""
        resp=chat_engine.generate_response("Give me a short summary of"+context+" , highlight only the main information to a third person")
        st.write(resp)
    
    if b3:
        # Internship summary
        context="""
    Ahmedabad, India

Landing my first internship was no easy task, especially without prior experience. Driven by a desire to learn, I began going door-to-door to every startup I could find in Ahmedabad, India, pitching myself as a motivated student eager to work. Eventually, my persistence led me to Maxgen Technologies, a Pune-based startup offering opportunities for freshers.

As a second-year bachelor’s student, I wasn’t their typical candidate, and they initially hesitated to bring me on board. Undeterred, I explained my passion for learning, emphasizing that I wasn’t looking for monetary compensation but rather an opportunity to gain real-world experience. My enthusiasm and budding knowledge impressed the hiring manager, who saw potential in me and agreed to train me for six months.

Balancing college and the internship was challenging yet rewarding. Every day, after attending my classes, I would head to the company around 4 PM and stay until 8 PM, dedicating those four hours to learning and contributing. While the internship was unpaid, the value I gained in terms of skills and exposure was priceless.

During my time at Maxgen, I worked on multiple projects and gained hands-on experience with essential tools like Seaborn, Scikit-learn, and basic TensorFlow. I learned the theoretical foundations and practical applications of classic machine learning models such as K-Nearest Neighbors (KNN), Support Vector Machines (SVM), and Decision Trees. This experience not only introduced me to the world of data science but also instilled the confidence to tackle real-life problems.

My internship at Maxgen was more than just training; it was the foundation of my journey into machine learning and data science. It taught me the importance of persistence, the value of hands-on learning, and the dynamics of working within an organization.

During my Bachelor’s, I concentrated on exploring and mastering Data Science and Machine Learning pathways. My journey in Machine Learning began with classic models using Sci-kit Learn, Seaborn, and Matplotlib. I utilized Kaggle as a data source, experimenting with various models and data pre-processing techniques to uncover what information was necessary and what was extraneous.

This exploration taught me the importance of detecting and addressing inconsistencies in data beyond merely handling null values. It was through iterative practice that I learned to manipulate and transform data to extract valuable insights. My interest extended to data visualization, where I gained the ability to compare model outputs with original datasets, helping to refine and evaluate model performance.

In addition to my focus on Machine Learning, my coursework provided a strong foundation in:

Programming Languages: C++, Java, and Python
Core Subjects: Operating Systems, Database Design, Theory of Computation, Finite Automata, and Machine Learning Theory
Web Development: HTML, CSS, and JavaScript My dedication to practical learning led me to undertake numerous hands-on projects that honed my skills in data handling, visualization, and model evaluation. These experiences culminated in an internship at the Indian Space Research Organization (ISRO), marking the beginning of my journey into impactful and research-oriented work.
Indian Space Research Organization (ISRO)
Atmospheric and Oceanic Sciences Group (AOSG), Scientific Research and Training Division (SRTD)

Working as a Machine Learning Intern at the Indian Space Research Organization (ISRO) was a once-in-a-lifetime experience. It’s not every day that someone gets the opportunity to contribute to such a prestigious organization, and the memories of this internship remain close to my heart.

Under the guidance of Dr. Smitha Ratheesh, I was entrusted with a project titled "Reconstruction of Ocean Chlorophyll Using Machine Learning Techniques." This work required me to address the challenges of reconstructing oceanic data—particularly chlorophyll concentrations—using a combination of satellite and in-situ observation data.

In oceanic research, both in-situ sensors and satellite imaging are indispensable but come with limitations. In-situ measurements, while accurate, are expensive, time-intensive, and cannot cover large areas. Conversely, satellite imaging, though extensive, often suffers from inaccuracies due to sunlight interference, pixel resolution, and other environmental factors. My role was to leverage machine learning models to improve the accuracy of data reconstruction while minimizing the time required compared to traditional numerical models.

For this project, I used five years of data (2015-2019) collected over the Bay of Bengal, sourced from the Regional Ocean Modeling System (ROMS). Employing machine learning techniques, I tested and compared three models:

Sequential Artificial Neural Network (ANN) Multilayer Perceptron (MLP) Gradient Boosting Regression (GBR) Through meticulous data preprocessing, visualization, and wrangling of multi-dimensional oceanic datasets, the Sequential ANN emerged as the most effective model. It demonstrated a lower Root Mean Square Error (RMSE) compared to the others. Furthermore, I conducted a sensitivity analysis on the Sequential ANN to evaluate the impact of individual variables on reconstruction accuracy. For example, removing nitrate data led to a 13% increase in error, highlighting its critical role in chlorophyll reconstruction.

This research underscored the value of machine learning in addressing ocean data's inherent complexities and showed how adaptive these techniques can be compared to traditional methods. An excerpt from the abstract of my paper summarizes the findings:

"This study underscores the efficacy of machine learning techniques in reconstructing ocean chlorophyll, offering faster and more adaptive solutions to enhance oceanographic research."

Beyond the technical aspects, this internship broadened my understanding of oceanic physics, geospatial data, and cloud masking techniques. It also allowed me to work alongside scientists, enhancing my professional collaboration and communication skills. Presenting my work to experts and receiving appreciation for my contributions bolstered my confidence.

As a recognition of my efforts, I received a Letter of Recommendation from the Head of SRTD. Completing this research project before coming to the U.S. was a proud milestone in my academic and professional journey.
"""
        resp=chat_engine.generate_response("Give me a short summary of"+context+" , highlight only the main information to a third person")
        st.write(resp)

