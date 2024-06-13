from dotenv import load_dotenv
load_dotenv() # load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load Google Gemini Model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the SQL database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    for row in rows:
        print(row)
    return rows

# data = read_sql_query(sql="SELECT * FROM STUDENT", db="student.db") # testing purposes

# Define your prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!\n
    The SQL database has the table named STUDENT and has the following columns - NAME, CLASS, SECTION \n\n
    For example,\n
    Example 1 - How many entries of records are present?,the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;\n
    Example 2 - Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS="Data Science";\n
    Also the SQL code should not have ``` in beginning or end and SQL word in output

    """


]

# Streamlit Application
st.set_page_config(page_title="I can Retrieve Any SQL Query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The response is")
    for row in response:
        print(row) 
        st.header(row)   