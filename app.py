import streamlit as st
import pandas as pd
import joblib

# Load the full pipeline
model = joblib.load("Mental_Health_Model.pkl")

st.title("🧠 Mental Health Score Predictor")
st.write("Enter your details below to predict your mental health score:")

# Collect inputs (raw strings/numbers, no manual encoding)
age = st.slider("Age", 10, 80, 25)
gender = st.selectbox("Gender", ["Male", "Female"])
grouped_country = st.selectbox("Country Group", ["Asia", "Europe", "America", "Other"])
academic_level = st.selectbox("Academic Level", ["High School", "Undergraduate", "Postgraduate"])
study_hours = st.slider("Study Hours per Day", 0, 12, 3)
sleep_hours = st.slider("Sleep Hours per Night", 0, 12, 7)
physical_activity = st.slider("Physical Activity Hours", 0, 10, 1)
daily_unlocks = st.slider("Daily Phone Unlocks", 0, 500, 50)
most_used_platform = st.selectbox("Most Used Platform", ["Instagram", "YouTube", "WhatsApp", "Other"])
purpose_of_use = st.selectbox("Purpose of Use", ["Study", "Entertainment", "Socializing", "Other"])
stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High", "Very High"])
avg_daily_usage = st.slider("Average Daily Usage (hours)", 0, 24, 4)

# Build dataframe with raw values
input_data = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "Grouped_country": [grouped_country],
    "Academic_Level": [academic_level],
    "Study_Hours": [study_hours],
    "Sleep_Hours_Per_Night": [sleep_hours],
    "Physical_Activity_Hours": [physical_activity],
    "Daily_Unlocks": [daily_unlocks],
    "Most_Used_Platform": [most_used_platform],
    "Purpose_Of_Use": [purpose_of_use],
    "Stress_Level": [stress_level],
    "Avg_Daily_Usage_Hours": [avg_daily_usage]
})

# Predict using the pipeline
if st.button("Predict Mental Health Score"):
    prediction = model.predict(input_data)[0]
    st.success(f"🧾 Predicted Mental Health Score: {prediction}")


