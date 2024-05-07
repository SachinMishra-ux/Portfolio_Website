import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import webbrowser
import re
import sqlite3
import os
import base64
# Import the following modules
import requests
import json

# access values from dictionary
#api_key = st.secrets["api_key"]

df= pd.read_csv("Marks.csv")
df1= pd.read_csv('Higher_secondary.csv')

def main():

    st.set_page_config(
        page_title="Data Scientist Portfolio",
        page_icon=":bar_chart:",
        layout="wide",
    )

    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def get_img_with_href(local_img_path, target_url):
        img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
        bin_str = get_base64_of_bin_file(local_img_path)
        html_code = f'''
            <a href="{target_url}">
                <img src="data:image/{img_format};base64,{bin_str}" />
            </a>'''
        return html_code
    

 
    # Function to send Push Notification
    
    
    def pushbullet_noti(title,body):
    
        TOKEN = api_key  # Pass your Access Token here
        # Make a dictionary that includes, title and body
        msg = {"type": "note", "title": title, "body": body}
        # Sent a posts request
        resp = requests.post('https://api.pushbullet.com/v2/pushes',
                            data=json.dumps(msg),
                            headers={'Authorization': 'Bearer ' + TOKEN,
                                    'Content-Type': 'application/json'})
        if resp.status_code != 200:  # Check if fort message send with the help of status code
            raise Exception('Error', resp.status_code)
        else:
            pass
    
    st.title("Hello there 👋, Welcome to my portfolio!")
    github, linkedin,twitter = st.columns(3)
    gif_html = get_img_with_href('./Assets/github.png', 'https://github.com/SachinMishra-ux')
    github.markdown(gif_html, unsafe_allow_html=True)
    gif_html1 = get_img_with_href('./Assets/linkedin.png', 'https://www.linkedin.com/in/sachin-mishra19566/')
    linkedin.markdown(gif_html1, unsafe_allow_html=True)
    gif_html2 = get_img_with_href('./Assets/twitter.png', 'https://twitter.com/tkwtk1')
    twitter.markdown(gif_html2, unsafe_allow_html=True)
    
    # Add CSS styles
    st.markdown("""
        <style>
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
        portion1,portion2= st.columns(2)
        avatar = Image.open('./Assets/final.png')
        portion1.image(avatar, caption="Sachin Mishra, A curious Data Scientist")
        with portion2.expander("Click Me! 👈"):
            st.write("- Hi, 🙋‍♂️ I'm Sachin Mishra, a curious data scientist based in India with over 2.5 years of experience in the field.")
            st.write("- I specialize in data analysis, machine learning, and data visualization, and I have a passion for using data to solve real-world problems.")
            st.write("- I also have knowledge in Deep learning,Computer Vision and NLP")
            st.write("- For more info please check my About and Project pages as well !")
            st.write("- Fun fact:🙃 I can read your mind through mentalism, want to know more, Let's connect!")
        st.write("Let's get in touch. Send me a message:")
        form = st.form(key='my-form',clear_on_submit=False)
        name = form.text_input('Enter your name')
        email = form.text_input('Enter your mail')
        subject = form.text_input('Enter Subject')
        message = form.text_input('Purpose of Contact')
        submit = form.form_submit_button('Submit')
        email_pattern=re.match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',email)
        
        if submit:
            if email_pattern:
                if email==email_pattern.group(0):
                    pass
            else:
                st.warning('wrong email!')
            if len(name)>3  and len(subject)>5 and len(message)>10 and re.match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',email):

                # Connect to the database (create a new file if it doesn't exist)
                conn = sqlite3.connect('formdata.db')
                # Create a cursor object to execute SQL commands
                c = conn.cursor()
                # Insert the data into the database
                c.execute('INSERT INTO form_data (name, email, subject, message) VALUES (?, ?, ?, ?)', (name, email, subject,message))
                # Commit the transaction (save the changes to the database)
                conn.commit()

                # Close the connection
                conn.close()
                st.success('Success! Will reach you soon!')
                st.balloons()
                pushbullet_noti(name,subject)

            else:
                st.warning("Please fill appropriate information!", icon="⚠️")

    elif choice == "Projects":
        st.title("Projects Page")
        option = st.selectbox( 'Select-Project-Type',
        ('Python-Projects', 'Machine-Learning-Projects', 'Deep-Learning-Projects','Computer-Vision-Projects','NLP-Projects','Tableau-Projects','GenAI','Other-Projects'))

        st.write('You selected:', option)
        if option == 'Python-Projects':
            youtube_img = get_img_with_href('./Assets/youtube.jpeg', 'https://youtubevideo.streamlit.app/')
            st.markdown(youtube_img, unsafe_allow_html=True)
            st.write("YouTube Video downloader")
            st.write("--------")
            pypi_img = get_img_with_href('./Assets/pypi.jpeg', 'https://sachinmishra-ux.github.io/locdataMAC/')
            st.markdown(pypi_img, unsafe_allow_html=True)
            st.write("locdataMAC pypi package")

        if option == 'Machine-Learning-Projects':
            house_img = get_img_with_href('./Assets/House_1.jpeg', 'https://bangalore.streamlit.app/')
            st.markdown(house_img, unsafe_allow_html=True)
            st.write("Bangalore House Price Prediction")
            st.write("--------")
            automl_img = get_img_with_href('./Assets/Slide_4_2.jpeg', 'https://automaticml.streamlit.app/')
            st.markdown(automl_img, unsafe_allow_html=True)
            st.write("Automl regression & classification")
            st.write("--------")
            st.write("Credit_Score_Classification")
            video_file = open('./Assets/Credit_class.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)

        if option == 'Deep-Learning-Projects':
            cat_img = get_img_with_href('./Assets/Cat_1.jpeg', 'https://bangalore.streamlit.app/')
            st.markdown(cat_img, unsafe_allow_html=True)
            st.write("Pet Image classification using Deep-learning")
            st.write("--------")
            automl_img = get_img_with_href('./Assets/House_1.jpeg', 'https://automaticml.streamlit.app/')
            st.markdown(automl_img, unsafe_allow_html=True)

        if option == 'GenAI':
            cat_img = get_img_with_href('./Assets/Cat_1.jpeg', 'https://bangalore.streamlit.app/')
            st.markdown(cat_img, unsafe_allow_html=True)
            st.write("Youtube Personal Subscriber Video Summarization")
            st.write("--------")
            automl_img = get_img_with_href('./Assets/House_1.jpeg', 'https://automaticml.streamlit.app/')
            st.markdown(automl_img, unsafe_allow_html=True)
            st.write("Local RAG for your PDF's")


        if option == 'Tableau-Projects':
            video_file = open('./Assets/Tableau_Video.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)

        if option == 'Computer-Vision-Projects':
            aadhar_img = get_img_with_href('./Assets/mask-aadhaarcard.png', 'https://github.com/SachinMishra-ux/Aadhar_Card_Masking')
            st.markdown(aadhar_img, unsafe_allow_html=True)
            st.write("Aadhar Card Masking")
        
        if option == 'NLP-Projects':
            nlp_img = get_img_with_href('./Assets/EmotionClf-End2End.png', 'https://emotiondetection.streamlit.app/')
            st.markdown(nlp_img, unsafe_allow_html=True)
            st.write("NLP emotion detection in sentences.")
        
        if option == 'Other-Projects':
            airflow_img = get_img_with_href('./Assets/Apache_Airflow.jpeg', 'https://airflow.apache.org/')
            st.markdown(airflow_img, unsafe_allow_html=True)
            st.write("Apache Airflow simple project.")
            st.write("---")
            st.write("Other Ideas I am looking to collaborate with:")
            st.write("- Youtube chaannel data analysis")
            st.write("- Instagram Hashtag Analysis")
            st.write("- Langchain Youtube Script generation tool")
            st.write("- Earworm Application")

    elif choice == "About":
        radio_choice = st.radio("Navigation", ["About Me","Skills","Experience", "Education","Download_Resume", "YouTube"])
        if radio_choice == 'About Me':
            st.title("About Me")
            st.write("Hi, I'm Sachin Mishra, a curious data scientist based in India with over 2 years of experience in the field. I specialize in data analysis, machine learning, and data visualization, and I have a passion for using data to solve real-world problems.")
            st.write("My expertise includes:")
            st.write("- Exploratory data analysis")
            st.write("- Feature engineering")
            st.write("- Data visualization")
            st.write("- Deep learning")
            st.write("- Natural language processing")
            st.write("- Time series analysis")
            st.write("- End to end Machine learning modeling and evaluation i.e MLOP's")
            with st.expander("More! 👈"):
                st.write("- I have experience working with a variety of data types, including structured and unstructured data, and have worked with both small and large datasets.")
                st.write("- I have a track record of delivering impactful projects, such as developing a predictive model to forecast frauduelent transaction, creating an NLP model to classify customer support tickets, and building a dashboard to monitor key business metrics.")
                st.write("- In my free time, I enjoy attending data science conferences, reading technical papers, and participating in online coding communities and building small fun projects")
                st.write("- Prior to my current role, I worked as a Senior Data Analyst at Digikull Corporation, where I led a team of analysts and worked on various projects, including optimizing the company's pricing strategy and developing a customer segmentation model.")
                st.write("- Feel free to contact me at sachin19566@gmail.com.")

        # Add skills
        if radio_choice == 'Skills':
            st.title("Skills:")
            with st.expander("Expand Me! 👈"):
                st.write("- Programming languages: Python, R,C,SQL")
                st.write("- Database: MySQL, Mongodb")
                st.write("- Tools and libraries: Scikit-learn, TensorFlow, Keras, Pandas, NumPy, Docker, Kubernetes(Basics), Apache Airflow(Basics)")
                st.write("- Data analysis: Exploratory data analysis, feature engineering, data cleaning")
                st.write("- Machine learning: Supervised and Unsupervised learning, model evaluation, hyperparameter tuning")
                st.write("- MLOP's: AWS-Sagemaker, Docker, Kubernetes")
                st.write("- Deep learning: Neural networks, CNNs, RNNs, transfer learning")
                st.write("- Natural language processing: Text classification, Sentiment Analysis,Emotion Detection, topic modeling")
                st.write("- Data visualization: Matplotlib, Seaborn,Plotly, Altair")
                st.write("- Frameworks: Langchain, Flask, Streamlit, FastAPI")
                st.write("- Experiment Tracking: Mlflow, DVC, Dagshub")
                st.write("- Big data technologies: Hadoop, Spark")
                st.write("- Cloud platforms: AWS, GCP, Snowflake") 

        if radio_choice == 'Experience':
        # Add previous experience
            st.title("Experience:")
            st.write("- Data Scientist, Data Society (2022 - present): Responsible for developing Corporate training in R and Python for professionals. Worked on Tableau & Other Machine Learning Projects as well to improve customer retention and optimize customer satisfaction.")
            st.write("- Senior Data Analyst Mentor, Digikull (2022 - present): Led a team of analysts and worked on various technical training projects, such as Statistics,SQL, Tableau, Python & Machine Learning")
            st.write("- Data Science Intern, Ineuron (2021 - 2022): Conducted data analysis to support business decisions and improve operational efficiency.")

        if radio_choice == 'Education':
            st.write("Bachelor's of Engineering")
            st.dataframe(df)
            fig = px.line(x=df['Semester'], y=df['CGPI'], color=px.Constant("Line chart"),
                labels=dict(x="Semesters", y="CGPI", color="Time Period"))
            fig.add_bar(x=df['Semester'], y=df['CGPI'], name="Bar chart")
            st.plotly_chart(fig, use_container_width=True)
            st.write("---")
            st.write("Higher Secondary Education")
            st.dataframe(df1)
            fig = px.line(x=df1['Subject'], y=df1['Marks'], color=px.Constant("Line chart"),
                labels=dict(x="Subject", y="Marks", color="Time Period"))
            fig.add_bar(x=df1['Subject'], y=df1['Marks'], name="Bar chart")
            st.plotly_chart(fig, use_container_width=True)
            st.write("---")
            st.write("Graph Shows I am consistent learner & hardworking candidate")

        if radio_choice == 'Download_Resume':
            with open('./Assets/Resume.pdf', 'rb') as f:
                st.download_button('Download Resume',f, 'Sachin_Mishra_Resume.pdf')

        
        if radio_choice == 'YouTube':
            youtube_channel = get_img_with_href('./Assets/youtube_channel.png', 'https://www.youtube.com/@LocData')
            st.markdown(youtube_channel, unsafe_allow_html=True)
            st.write("Locdata Youtube Channel")

if __name__ == '__main__':
    main()
