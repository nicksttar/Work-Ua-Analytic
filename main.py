from analytic import analitics
from reader import write_file
import streamlit as st

# Setting up the Streamlit app
st.title('Work Ua Analytic')
st.markdown('''_This project is a web scraper for Work.ua, a popular Ukrainian job search website. 
Its aim is to provide users with data analytics on job vacancies of a chosen profession in a chosen city. 
The program allows users to enter the desired job position and city, collects and processes data from Work.ua, 
and presents the resulting analysis, which includes 3 graphs (responses, kde of viewers, salaries by experience), 
as well as a report containing the number of vacancies, average salary, viewers per vacancy, and a breakdown of salaries by experience level. 
The user can also download the data in CSV format. The project was implemented using Python and Streamlit._''')

# Creating text input and select box widgets
button = st.text_input('Write job to analyze:')
with open('cities.txt', 'r') as f:
    list_cities = [i.strip() for i in f.readlines()]
button1 = st.selectbox('Choose your city: ', list_cities)

# Defining a function to get the data from the website and write it to a file
def data_get(button):
    return write_file(button, button1)

# Creating a button to trigger the data retrieval and analysis
if st.button('Analize'):
    df = data_get(button)

    # Running three types of analytics on the retrieved data
    analitics(df, mode=1)
    analitics(df, mode=2)
    analitics(df, mode=3)

    # Generating a quick report of the data
    report = f"""
## Quick Report:
Vacancies counter: {len(df)}

Average salary: {df["salaries"].mean():.2f}

Viewers per vacancy: {df["viewers"].mean():.2f}

NA salary: {df["salaries"].isnull().sum()}
"""
    st.markdown(report)

    # Creating a download button for the retrieved data as CSV
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)
    b1 = st.download_button(
         label="Download data as CSV",
         data=csv,
         file_name='large_df.csv',
         mime='text/csv')
