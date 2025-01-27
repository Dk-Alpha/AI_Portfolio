import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import chat_engine

st.title("My Statistics")

st.header("Undergraduate Studies", divider=True)
#callables
def show_sem_bar(data,semester):
    # Give entire data  [ "mydata" in my case ] as input and the semester values "Semester 1"
    #Fetch all data of that semester
    req_data=data.drop(columns=["Semester"])[data.Semester==semester]
    req_data.index=np.arange(len(req_data["Subject"]))
    req_dict={"Pass year":req_data["Exam Pass Year"][0],"SGPA":req_data["SGPA"][0],"CGPA":req_data["CGPA"][0]}
    req_data["Normalized Score"]=(req_data["Marks Achieved"]/req_data["Total Marks"])*100 # Normalized scores to a range of 100
    fig=px.bar(req_data,x="Subject", y="Normalized Score", color_discrete_sequence=[ 'red','blue','green'], title="Performance Breakdown by Subject: Semester "+semester.split(" ")[1], color="Subject")

    fig.update_layout(
        yaxis=dict(range=[0, 100])
    )

    st.write(fig)
    st.write("<nbsp>",unsafe_allow_html=True)
    return [req_data.Subject,req_data["Normalized Score"],req_dict]

def generate_insight(subject, score, extra_data, type="u"): #Subject name list, score (Normalized or Points anything), extra data, type of scores Grad or Undergrad
    #AI Generated Analysis
    sys="""Your task is to analyze the provided data plot and generate key insights based on the following criteria. Focus on the main trends, outliers, patterns, and correlations, while highlighting any significant points that stand out.
Steps to Follow:
Overview of the Plot:
Provide a brief description of the plot, mentioning the type of plot (e.g., bar chart, line chart, scatter plot, etc.).
Explain what the x-axis and y-axis represent, including the units (if applicable).
Identify the data range or the time period covered by the plot (e.g., semesters, years, etc.).
Key Insights:

Highlight any major trends observed in the data, such as increasing/decreasing values, seasonal patterns, or consistency over time.
Point out any significant peaks, valleys, or plateaus that are notable.
Identify outliers or anomalies, and explain their potential implications (e.g., a sudden spike in values or an unexpected drop).
Compare different categories or variables represented in the plot (if applicable), and identify any patterns or relationships (e.g., correlation between two variables).
Statistical Summary:

If relevant, include basic statistical information such as the mean, median, mode, standard deviation, or any other statistical measures that would help explain the data.
Mention the distribution of the data (e.g., is it normally distributed, skewed, etc.?).
Highlights:

Clearly point out the most important or surprising aspects of the plot. For example:
Trends: Is the data increasing or decreasing over time? Is there a cyclical or periodic pattern?
Outliers: Are there any data points that stand far away from the others? What might explain them?
Anomalies: Did anything unexpected happen in the data (e.g., a drop or surge)?
Comparison: Are there any subjects, categories, or data series that stand out more than others in the plot?
Actionable Recommendations (Optional):

Based on the insights derived from the data, suggest any potential actions or decisions that could be made.
For example, if the plot is about sales over several years, you could recommend focusing efforts on the periods with the highest growth."""
    if type=="u": #this is for undergrad
        instructions="""Analyze the data plot information below and provide key highlights: \n Subject name: {} \n Respective Scores: {} \n Extra data: {}""".format(subject,score,extra_data)
    elif type=="g": #this is for grad
        instructions="""Analyze the data plot information below and provide key highlights: \n Subject name: {} \n Respective Scores: {} \n Extra data with grades for each subject: {}""".format(subject,score,extra_data)
    resp=chat_engine.generate_response(inp=sys+instructions)
    st.write(resp)

def show_sem_bar_grad(data,semester):
    # Give entire data  [ "mydata" in my case ] as input and the semester values "Semester 1"
    #Fetch all data of that semester
    req_data=data.drop(columns=["Semester"])[data.Semester==semester]
    req_data.index=np.arange(len(req_data["Subject"]))
    req_dict={"Pass year":req_data["Exam Pass Year"][0],"SGPA":req_data["SGPA"][0],"Grades":req_data["Grade"]}
    fig=px.bar(req_data,x="Subject", y="Points", title="Performance Breakdown by Subject: Semester "+semester.split(" ")[1], color="Grade")

    fig.update_layout(
        yaxis=dict(range=[0, 12])
    )

    st.write(fig)
    st.write("<nbsp>",unsafe_allow_html=True)
    return [req_data.Subject, req_data.Points, req_dict]

def all_sem_score(data):
    unique_sem=data.Semester.unique()
    CPA_list=[]
    for sem in unique_sem:
        SGPA=data[data.Semester==sem]["SGPA"]
        SGPA.index=np.arange(len(SGPA))
        CPA_list.append(SGPA[0])
    gpa=pd.DataFrame({"Semesters": np.arange(1,9), "GPA":CPA_list})
    fig=px.line(gpa,x="Semesters",y="GPA", markers=True)

    # Customize layout
    fig.update_layout(
        title=dict(
            text="GPA Comparison Across Semesters in Undergraduate Computer Science",
            x=0.05,  # Center the title
            # font=dict(size=20, color='white'),
            font=dict(color='white'),
        ),
        legend=dict(title="Legend"),
         annotations=[
        dict(
            x=0.95, 
            y=0.07,
            xref="paper", 
            yref="paper", 
            text="Note: GPA is on a scale of 0-10",  # Adding caption
            showarrow=False,
            font=dict(size=15, color="gray")
        )
    ]
    )
    st.write(fig)




# Read data UNDERGRAD
mydata=pd.read_csv("project\docs\All_Semesters_Results_Undergrad.csv")
st.write(mydata.head())

with st.container():
    all_sem_score(mydata)
with st.container():
    slider_val=st.slider("Select Semester Wise Report", min_value=1, max_value=8)
    insight_data=show_sem_bar(mydata, semester="Semester "+str(slider_val))
    if st.button("Generate Insights",key="undergrad"):
        st.write("Victor is Generating Insights:")
        generate_insight(insight_data[0],insight_data[1],insight_data[2])

st.header("Graduate Studies", divider=True)
mygraddata=pd.read_csv("project\docs\All_Semesters_Results_Grad.csv")
st.write(mydata.head())

with st.container():
    # all_sem_score(mydata) (NOT AVAILABLE RN)
    pass
with st.container():
    slider_val=st.slider("Select Semester Wise Report", min_value=1, max_value=4)
    current_sem=2
    if slider_val>=current_sem:
        st.write("DATA NOT AVAILABLE BECAUSE I AM CURRENTLY STUDYING IN THAT SEMESTER OR NOT REACHED THAT SEMESTER")
    else:
        insight_data=show_sem_bar_grad(mygraddata, semester="Semester "+str(slider_val))
        if st.button("Generate Insights", key="grad"):
            st.write("Victor is Generating Insights:")
            generate_insight(insight_data[0],insight_data[1],insight_data[2])
