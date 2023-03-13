import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import webbrowser

df= pd.read_csv("Marks.csv")

def main():
    st.set_page_config(
        page_title="Data Scientist Portfolio",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    github, linkedin,twitter = st.columns(3)
    github.markdown("[![Foo](https://img.icons8.com/material-outlined/96/000000/github.png)](https://github.com/mludwig137/gini-microloan-recommender-system)")
    linkedin.markdown("[![Foo](https://img.icons8.com/material-outlined/96/000000/github.png)](https://github.com/mludwig137/gini-microloan-recommender-system)")
    twitter.markdown("[![Foo](https://img.icons8.com/material-outlined/96/000000/github.png)](https://github.com/mludwig137/gini-microloan-recommender-system)")
    # Add CSS styles
    st.markdown("""
        <style>
            .main {
                background-color: #f5f5f5;
            }
            .sidebar .sidebar-content {
                background-color: #d3d3d3;
            }
            .stButton button {
                background-color: #008CBA;
            }
            .stButton:hover button {
                background-color: #00547C;
            }
        </style>
        """, unsafe_allow_html=True)
    
    # Add navigation bar
    menu = ["Home", "Projects", "About"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Home":
        st.title("Home Page")
        st.write("Welcome to my portfolio!")

    elif choice == "Projects":
        st.title("Projects Page")
        option = st.selectbox(
        'How would you like to be contacted?',
        ('Python-Projects', 'Machine-Learning-Projects', 'Deep-Learning_Projects','Computer-Vision-Projects','NLP-Projects','Tableau-Projects'))

        st.write('You selected:', option)
        if option == 'Python-Projects':
            p1, p2 = st.columns(2)
            image3 = Image.open('./Assets/3.png')
            image2 = Image.open('./Assets/2.png')
            p1.image(image2, caption='Youtube Video Downloader')
            p2.image(image3, caption='locdata PYPI package')
            if p1.button('Check-Project'):
                webbrowser.open_new_tab("https://youtubevideo.streamlit.app/")
            if p2.button('CheckProject'):
                webbrowser.open_new_tab("https://youtubevideo.streamlit.app/")

        if option == 'Machine-Learning-Projects':
            p1, p2 = st.columns(2)
            image4 = Image.open('./Assets/4.png')
            image1 = Image.open('./Assets/2.png')
            p1.image(image4, caption='AutoML Webapp')
            p2.image(image1, caption='Bangalore House Price Prediction')
            if p1.button('Check-Project'):
                webbrowser.open_new_tab("https://automaticml.streamlit.app/")
            if p2.button('CheckProject'):
                webbrowser.open_new_tab()

        if option == 'Deep-Learning-Projects':
            p1, p2 = st.columns(2)
            image4 = Image.open('./Assets/4.png')
            image1 = Image.open('./Assets/2.png')
            p1.image(image4, caption='Pet-Image Classification using Transfer Learning Approach')
            p2.image(image1, caption='Bangalore House Price Prediction')
            if p1.button('Check-Project'):
                webbrowser.open_new_tab("https://automaticml.streamlit.app/")
            if p2.button('CheckProject'):
                webbrowser.open_new_tab()
        
        if option == 'Tableau-Projects':
            p1, p2 = st.columns(2)
            image4 = Image.open('./Assets/4.png')
            image1 = Image.open('./Assets/2.png')
            p1.image(image4, caption='Pet-Image Classification using Transfer Learning Approach')
            p2.image(image1, caption='Bangalore House Price Prediction')
            if p1.button('Check-Project'):
                webbrowser.open_new_tab("https://automaticml.streamlit.app/")
            if p2.button('CheckProject'):
                webbrowser.open_new_tab()
        
        if option == 'Computer-Vision-Projects':
            p1, p2 = st.columns(2)
            image4 = Image.open('./Assets/4.png')
            image1 = Image.open('./Assets/2.png')
            p1.image(image4, caption='Pet-Image Classification using Transfer Learning Approach')
            p2.image(image1, caption='Bangalore House Price Prediction')
            if p1.button('Check-Project'):
                webbrowser.open_new_tab("https://automaticml.streamlit.app/")
            if p2.button('CheckProject'):
                webbrowser.open_new_tab()
        
        if option == 'NLP-Projects':
            p1, p2 = st.columns(2)
            image4 = Image.open('./Assets/4.png')
            image1 = Image.open('./Assets/2.png')
            p1.image(image4, caption='Pet-Image Classification using Transfer Learning Approach')
            p2.image(image1, caption='Bangalore House Price Prediction')
            if p1.button('Check-Project'):
                webbrowser.open_new_tab("https://automaticml.streamlit.app/")
            if p2.button('CheckProject'):
                webbrowser.open_new_tab()


    elif choice == "About":
        if st.button('About'):
            st.title("About Me")
            st.write("Hi, I'm Jane Doe, a data scientist based in San Francisco with over 5 years of experience in the field. I specialize in data analysis, machine learning, and data visualization, and I have a passion for using data to solve real-world problems.")
            st.write("My expertise includes:")
            st.write("- Exploratory data analysis")
            st.write("- Feature engineering")
            st.write("- Machine learning modeling and evaluation")
            st.write("- Data visualization")
            st.write("- Deep learning")
            st.write("- Natural language processing")
            st.write("- Time series analysis")
            st.write("I have experience working with a variety of data types, including structured and unstructured data, and have worked with both small and large datasets.")
            st.write("I have a track record of delivering impactful projects, such as developing a predictive model to forecast customer churn, creating an NLP model to classify customer support tickets, and building a dashboard to monitor key business metrics.")
            st.write("In my free time, I enjoy attending data science conferences, reading technical papers, and participating in online coding communities.")
            st.write("Prior to my current role, I worked as a Senior Data Analyst at DEF Corporation, where I led a team of analysts and worked on various projects, including optimizing the company's pricing strategy and developing a customer segmentation model.")
            st.write("Feel free to contact me at jane.doe@gmail.com.")

        # Add separator
        st.write("---")
        # Add skills
        if st.button('Skills'):
            st.write("Skills:")
            st.write("- Programming languages: Python, R, SQL")
            st.write("- Tools and libraries: Scikit-learn, TensorFlow, Keras, PyTorch, Pandas, NumPy, Matplotlib, Seaborn")
            st.write("- Data analysis: Exploratory data analysis, feature engineering, data cleaning")
            st.write("- Machine learning: Supervised and unsupervised learning, model evaluation, hyperparameter tuning")
            st.write("- Deep learning: Neural networks, CNNs, RNNs, transfer learning")
            st.write("- Natural language processing: Text classification, sentiment analysis, topic modeling")
            st.write("- Data visualization: Matplotlib, Seaborn, Altair")
            st.write("- Big data technologies: Hadoop, Spark")
            st.write("- Cloud platforms: AWS, GCP") 

        # Add separator
        st.write("---")
        if st.button('Experience'):
        # Add previous experience
            st.write("Previous Experience:")
            st.write("- Data Scientist, ABC Company (2019 - present): Responsible for developing predictive models to improve customer retention and optimize marketing campaigns.")
            st.write("- Senior Data Analyst, DEF Corporation (2017 - 2019): Led a team of analysts and worked on various projects, including optimizing the company's pricing strategy and developing a customer segmentation model.")
            st.write("- Data Analyst, GHI Industries (2015 - 2017): Conducted data analysis to support business decisions and improve operational efficiency.")

        # Add separator
        st.write("---")
        if st.button('Education'):
            st.dataframe(df)
            fig = px.line(x=df['Semester'], y=df['CGPI'], color=px.Constant("Line chart"),
                labels=dict(x="Semesters", y="CGPI", color="Time Period"))
            fig.add_bar(x=df['Semester'], y=df['CGPI'], name="Bar chart")
            st.plotly_chart(fig, use_container_width=True)

if __name__ == '__main__':
    main()