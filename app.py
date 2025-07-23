import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Salary Classification App")
st.subheader("Predict if Salary is >50K or <=50K")

# Input form
age = st.slider("Age", 18, 90, 30)
education_num = st.slider("Education Number", 1, 16, 10)
hours_per_week = st.slider("Hours per Week", 1, 99, 40)
capital_gain = st.number_input("Capital Gain", min_value=0, value=0)
capital_loss = st.number_input("Capital Loss", min_value=0, value=0)

workclass = st.selectbox("Workclass", [
    'Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov',
    'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'
])

education = st.selectbox("Education", [
    'Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school',
    'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th',
    'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th',
    'Preschool'
])

marital_status = st.selectbox("Marital Status", [
    'Married-civ-spouse', 'Divorced', 'Never-married',
    'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'
])

occupation = st.selectbox("Occupation", [
    'Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial',
    'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical',
    'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv',
    'Armed-Forces'
])

relationship = st.selectbox("Relationship", [
    'Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'
])

race = st.selectbox("Race", [
    'White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'
])

sex = st.selectbox("Sex", ['Male', 'Female'])

native_country = st.selectbox("Native Country", [
    'United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada',
    'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece',
    'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy',
    'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland',
    'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti',
    'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand',
    'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong',
    'Holand-Netherlands'
])

# Predict button
if st.button("Predict"):
    input_data = [[
        age, workclass, education, education_num, marital_status,
        occupation, relationship, race, sex, capital_gain,
        capital_loss, hours_per_week, native_country
    ]]
    prediction = model.predict(input_data)
    if prediction[0] == '>50K':
        st.success("Prediction: Salary is > 50K")
    else:
        st.warning("Prediction: Salary is <= 50K")
