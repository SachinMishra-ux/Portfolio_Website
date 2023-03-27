import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import webbrowser
import sqlite3
import os
import base64
import platform
# Import the following modules
import requests
import json
import yaml

# load yml file to dictionary
credentials = yaml.full_load(open('./credentials.yml'))

# access values from dictionary
api_key = credentials['api']['apikey']


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
    
    
    def pushbullet_noti(title, body):
    
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
            print('Message sent')
    

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
        st.write("---")
        form = portion2.form(key='my-form',clear_on_submit=True)
        name = form.text_input('Enter your name')
        email = form.text_input('Enter your mail')
        subject = form.text_input('Enter Subject')
        message = form.text_input('Purpose of Contact')
        submit = form.form_submit_button('Submit')

        if submit:
            if name and email and subject and message is not None:
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
                portion2.write("Success! Will reach you soon!")
                pushbullet_noti(name,subject)
            else:
                portion2.write("Please fill all the information!")

    elif choice == "Projects":
        st.title("Projects Page")
        option = st.selectbox( 'Select-Project-Type',
        ('Python-Projects', 'Machine-Learning-Projects', 'Deep-Learning-Projects','Computer-Vision-Projects','NLP-Projects','Tableau-Projects'))

        st.write('You selected:', option)
        if option == 'Python-Projects':
            #p1, p2 = st.columns(2)
            youtube_img = get_img_with_href('./Assets/youtube.png', 'https://youtubevideo.streamlit.app/')
            st.markdown(youtube_img, unsafe_allow_html=True)
            st.write("--------")
            pypi_img = get_img_with_href('./Assets/pypi.png', 'https://sachinmishra-ux.github.io/locdataMAC/')
            st.markdown(pypi_img, unsafe_allow_html=True)

        if option == 'Machine-Learning-Projects':
            p1, p2 = st.columns(2)
            house_img = get_img_with_href('./Assets/house.png', 'https://bangalore.streamlit.app/')
            p1.markdown(house_img, unsafe_allow_html=True)
            automl_img = get_img_with_href('./Assets/automl.png', 'https://automaticml.streamlit.app/')
            p2.markdown(automl_img, unsafe_allow_html=True)

        if option == 'Deep-Learning-Projects':
            p1, p2 = st.columns(2)
            cat_img = Image.open('./Assets/cat.png')
            bangalore = Image.open('./Assets/house.png')
            p1.image(cat_img, caption='Pet-Image Classification using Transfer Learning Approach')
            p2.image(bangalore, caption='Bangalore House Price Prediction')
            if p1.button('Check-Project'):
                webbrowser.open_new_tab("https://automaticml.streamlit.app/")
            if p2.button('CheckProject'):
                webbrowser.open_new_tab("https://bangalore.streamlit.app/")
        
        if option == 'Tableau-Projects':
            p1, p2 = st.columns(2)
            video_file = open('./Assets/Tableau_Video.mp4', 'rb')
            video_bytes = video_file.read()

            p1.video(video_bytes)
            image1 = Image.open('./Assets/cat.png')
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
        radio_choice = st.radio("Navigation", ["About Me","Skills","Experience", "Education","Download_Resume"])
        if radio_choice == 'About Me':
            st.title("About Me")
            st.write("Hi, I'm Sachin Mishra, a curious data scientist based in Bangalore with over 2 years of experience in the field. I specialize in data analysis, machine learning, and data visualization, and I have a passion for using data to solve real-world problems.")
            st.write("My expertise includes:")
            st.write("- Exploratory data analysis")
            st.write("- Feature engineering")
            st.write("- Data visualization")
            st.write("- Deep learning")
            st.write("- Natural language processing")
            st.write("- Time series analysis")
            st.write("- End to end Machine learning modeling and evaluation i.e MLOP's")
            st.write("I have experience working with a variety of data types, including structured and unstructured data, and have worked with both small and large datasets.")
            st.write("I have a track record of delivering impactful projects, such as developing a predictive model to forecast frauduelent transaction, creating an NLP model to classify customer support tickets, and building a dashboard to monitor key business metrics.")
            st.write("In my free time, I enjoy attending data science conferences, reading technical papers, and participating in online coding communities and building small fun projects")
            st.write("Prior to my current role, I worked as a Senior Data Analyst at Digikull Corporation, where I led a team of analysts and worked on various projects, including optimizing the company's pricing strategy and developing a customer segmentation model.")
            st.write("Feel free to contact me at sachin19566@gmail.com.")

        # Add skills
        if radio_choice == 'Skills':
            st.write("Skills:")
            st.write("- Programming languages: Python, R,C,SQL")
            st.write("- Tools and libraries: Scikit-learn, TensorFlow, Keras, Pandas, NumPy, Docker, Kubernates(Basics)")
            st.write("- Data analysis: Exploratory data analysis, feature engineering, data cleaning")
            st.write("- Machine learning: Supervised and Unsupervised learning, model evaluation, hyperparameter tuning")
            st.write("- Deep learning: Neural networks, CNNs, RNNs, transfer learning")
            st.write("- Natural language processing: Text classification, Sentiment Analysis,Emotion Detection, topic modeling")
            st.write("- Data visualization: Matplotlib, Seaborn, Altair")
            st.write("- Big data technologies: Hadoop, Spark")
            st.write("- Cloud platforms: AWS, GCP") 

        if radio_choice == 'Experience':
        # Add previous experience
            st.write("Previous Experience:")
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

        if radio_choice == 'Download_Resume':
            with open('./Assets/Resume.pdf', 'rb') as f:
                st.download_button('Download Resume',f, 'Sachin_Mishra_Resume.pdf')

if __name__ == '__main__':
    main()
