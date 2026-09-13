import streamlit as st
import pandas as pd
import joblib

# Load your trained model (make sure you saved it as .pkl or .joblib from Kaggle)
model = joblib.load("Mental_Health_Model.pkl")

st.title("🧠 Mental Health Score Predictor")
st.write("Enter your details below to predict your mental health score:")

# Collect user inputs
age = st.slider("Age", 10, 80, 25)
gender = st.selectbox("Gender", ["Male", "Female"])
stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High", "Very High"])
avg_daily_usage = st.slider("Average Daily Usage (hours)", 0, 24, 4)
sleep_hours = st.slider("Sleep Hours per Day", 0, 12, 7)
exercise = st.selectbox("Exercise Frequency", ["Never", "Rarely", "Sometimes", "Often", "Daily"])

# Convert inputs into a dataframe (matching your dataset’s columns)
input_data = pd.DataFrame({
    "Age": [age],
    "Gender": [1 if gender == "Male" else 0],  # Example encoding
    "Stress_Level": [stress_level],
    "Avg_Daily_Usage_Hours": [avg_daily_usage],
    "Sleep_Hours": [sleep_hours],
    "Exercise_Frequency": [exercise]
})

# Apply preprocessing if needed (e.g., label encoding for Stress_Level/Exercise)
# Example: map categories to numbers
stress_map = {"Low": 0, "Medium": 1, "High": 2, "Very High": 3}
exercise_map = {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3, "Daily": 4}

input_data["Stress_Level"] = input_data["Stress_Level"].map(stress_map)
input_data["Exercise_Frequency"] = input_data["Exercise_Frequency"].map(exercise_map)

# Predict
if st.button("Predict Mental Health Score"):
    prediction = model.predict(input_data)[0]
    st.success(f"🧾 Predicted Mental Health Score: {prediction}")


