import streamlit as st
import google.generativeai as genai
import os


# Using the GOOGLE_API_KEY environment variable
genai.configure = os.getenv('GOOGLE_API_KEY')

# UI Config and settings
st.set_page_config(page_title="Marmar-Gemini", page_icon="💊")
st.image('img/banner.png', use_column_width=True)

def check_drug_interactions(medications, health_history, gender, age, weight, height):
    model = genai.GenerativeModel('gemini-pro')  
    prompt = f"Given the health history: {health_history}, provide a detailed explanation of the potential risks and interactions among these medications: {medications}. Only if any. Focus on any increased risks, specific side effects, and the mechanism by which these interactions might occur, also consider the health history. Ensure the explanation is comprehensive & easy to understand, covering the pharmacological aspects and clinical implications for patients. Then, based on gender: {gender}, age: {age}, weight: {weight}, height: {height}, and health history {health_history}, offer tailored advice."
    response = model.generate_content(prompt)
    return response.text


# Streamlit app interface 
st.title('Empowering you with the knowledge and tools to safely manage your medications.')
st.write('Welcome to Marmar. Check potential drug interactions and get tailored advice. Please provide the details below to get started.')

# Compulsory field for medications and health history
medications = st.text_area('Enter the names of the medications you are currently taking, separated by commas:', help='Please enter the names of the medications you are currently taking, separated by commas.')
health_history = st.text_area('Enter your health history or describe any ailments:', help='Please include any chronic conditions, recent illnesses, or relevant health issues.')

# Optional fields for personalized advice
options = ['Male', 'Female']
gender = st.selectbox('Choose your gender:', options)
age = st.text_input('Enter your age (Optional):', '')
weight = st.text_input('Enter your weight in kg (Optional):', '')
height = st.text_input('Enter your height in cm (Optional):', '')

# Button to check interactions
if st.button('Check Interactions'):
    if medications and health_history:
        response = check_drug_interactions(medications, health_history, gender, age, weight, height)
        st.write('**Response:**', response)
    else:
        st.warning('Please enter the required information to continue.')


