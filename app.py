import streamlit as st  
import sklearn
import pickle 



import numpy as np 

# Loading the model from the storage to the code
with open('Logistic Regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

#Title of the web app
st.title("Credit Card Prediction App")


 # Define UI elements for user input
gender = st.sidebar.radio('Gender', ['Male', 'Female'])
has_car = st.sidebar.radio('Has a car', ['Yes', 'No'])
has_property = st.sidebar.radio('Has a property', ['Yes', 'No'])
children_count = st.sidebar.number_input('Children count', min_value=0, step=1)
income = st.sidebar.number_input('Income', min_value=0, step=1000)
employment_status = st.sidebar.selectbox('Employment status', ['Commercial Associate', 'Pensioner', 'Student', 'Working', 'State Servant'])
education_level = st.sidebar.selectbox('Education level', ['Academic Degree', 'Higher Education', 'Incomplete Higher', 'Lower Secondary', 'Secondary Special'])
marital_status = st.sidebar.selectbox('Marital status', ['Civil marriage', 'Separated', 'Married/Not married', 'Widow'])
dwelling_age = st.sidebar.number_input('Dwelling Age', min_value=0, step=1)
employment_length = st.sidebar.number_input('Employment length', min_value=0, step=1)
has_mobile_phone = st.sidebar.radio('Has a mobile phone', ['Yes', 'No'])
has_work_phone = st.sidebar.radio('Has a work phone', ['Yes', 'No'])
has_phone = st.sidebar.radio('Has a phone', ['Yes', 'No'])
has_email = st.sidebar.radio('Has an email', ['Yes', 'No'])
job_title = st.sidebar.number_input('Job title', min_value=0, step=1)
family_member_count = st.sidebar.number_input('Family member count', min_value=0, step=1)
account_age = st.sidebar.number_input('Account age', min_value=0, step=1)

encoded_data = {

    'Gender': 1 if data['Gender'] == 'Male' else 0,
    'Has a car': 1 if data['Has a car'] == 'Yes' else 0,
    'Has a property': 1 if data['Has a property'] == 'Yes' else 0,
    'Children count': data['Children count'],
    'Income': data['Income'],
    'Employment status': data['Employment status'],
    'Education level': data['Education level'],
    'Marital status': data['Marital status'],
    'Dwelling Age': data['Dwelling Age'],
    'Employment length': data['Employment length'],
    'Has a mobile phone': 1 if data['Has a mobile phone'] == 'Yes' else 0,
    'Has a work phone': 1 if data['Has a work phone'] == 'Yes' else 0,
    'Has a phone': 1 if data['Has a phone'] == 'Yes' else 0,
    'Has an email': 1 if data['Has an email'] == 'Yes' else 0,
    'Job title': data['Job title'],
    'Family member count': data['Family member count'],
    'Account age': data['Account age']
 }

return encoded_data

Is high risk_mapping = {0:'Not High Risk', 1: 'High Risk'}
if st.button("Predict button"):
    
    st.write(f"User input data is {ID,Gender,Has a car,Has a property,Children count,Income,Employment status,Education level,Marital status,Dwelling,Age,Employment length,Has a mobile phone,Has a work phone,Has a phone,Has an email,Job title,Family member count,Account age}")
    st.write(f"The application is predicted to be {not_high_risk[0]}")
    st.write(f"The application is predicted to be {high_risk[[0]]}")
    




    
