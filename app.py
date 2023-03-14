import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import webbrowser
import sqlite3

df= pd.read_csv("Marks.csv")

def main():
    st.set_page_config(
        page_title="Data Scientist Portfolio",
        page_icon=":bar_chart:",
        layout="wide",
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
        portion1,portion2= st.columns(2)
        avatar = Image.open('./Assets/final.png')
        portion1.image(avatar, caption="Sachin Mishra, A curious Data Scientist")
        st.write("---")
        
        form = portion2.form(key='my-form')
        name = form.text_input('Enter your name')
        email = form.text_input('Enter your mail')
        subject = form.text_input('Enter Subject')
        message = form.text_input('Purpose of Contact')
        submit = form.form_submit_button('Submit')

        if submit:
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
            portion2.write("Success!!")

    elif choice == "Projects":
        st.title("Projects Page")
        option = st.selectbox(
        'How would you like to be contacted?',
        ('Python-Projects', 'Machine-Learning-Projects', 'Deep-Learning_Projects','Computer-Vision-Projects','NLP-Projects','Tableau-Projects'))

        st.write('You selected:', option)
        if option == 'Python-Projects':
            p1, p2 = st.columns(2)
            youtube_img = Image.open('./Assets/youtube.png')
            pypi_img = Image.open('./Assets/pypi.png')
            p1.image(youtube_img, caption='Youtube Video Downloader')
            p2.image(pypi_img, caption='locdata PYPI package')
            if p1.button('Check-Project'):
                webbrowser.open_new_tab("https://youtubevideo.streamlit.app/")
            if p2.button('CheckProject'):
                webbrowser.open_new_tab("https://sachinmishra-ux.github.io/locdataMAC/")

        if option == 'Machine-Learning-Projects':
            p1, p2 = st.columns(2)
            house_img = Image.open('./Assets/house.png')
            automl_img = Image.open('./Assets/automl.png')
            p1.image(automl_img, caption='AutoML Webapp')
            p2.image(house_img, caption='Bangalore House Price Prediction')
            if p1.button('Check-Project'):
                webbrowser.open_new_tab("https://automaticml.streamlit.app/")
            if p2.button('CheckProject'):
                webbrowser.open_new_tab("https://bangalore.streamlit.app/")

        if option == 'Deep-Learning-Projects':
            p1, p2 = st.columns(2)
            cat_img = Image.open('./Assets/cat.png')
            image1 = Image.open('./Assets/2.png')
            p1.image(cat_img, caption='Pet-Image Classification using Transfer Learning Approach')
            p2.image(image1, caption='Bangalore House Price Prediction')
            if p1.button('Check-Project'):
                webbrowser.open_new_tab("https://automaticml.streamlit.app/")
            if p2.button('CheckProject'):
                webbrowser.open_new_tab("https://bangalore.streamlit.app/")
        
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