import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Check scikit-learn version
import sklearn
print(sklearn.__version__)

rfr = pickle.load(open('rfr.pkl', 'rb'))
x_train = pd.read_csv('x_train.csv')

def pred(Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp):
    features = pd.DataFrame({'Gender': [Gender], 'Age': [Age], 'Height': [Height], 
                             'Weight': [Weight], 'Duration': [Duration], 
                             'Heart_Rate': [Heart_rate], 'Body_Temp': [Body_temp]})
    prediction = rfr.predict(features)
    return prediction

st.title("Calorie Burn Prediction")

with st.form("input_form"):
    Gender = st.selectbox('Gender', ['Male (1)', 'Female (0)'])
    Gender = 1 if Gender == 'Male (1)' else 0
    Age = st.number_input('Age', min_value=0, max_value=150)
    Height = st.number_input('Height (in cm)', min_value=0, max_value=250)
    Weight = st.number_input('Weight (in kg)', min_value=0, max_value=200)
    Duration = st.number_input('Duration (in minutes)', min_value=0, max_value=360)
    Heart_rate = st.number_input('Heart Rate (bpm)', min_value=0, max_value=250)
    Body_temp = st.number_input('Body Temperature (°C)', min_value=30, max_value=42)
    submitted = st.form_submit_button("Predict")

if submitted:
    result = pred(Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp)
    st.write(f"**You have consumed {result[0]} calories**")  