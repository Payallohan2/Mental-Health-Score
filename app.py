import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset (upload or use Kaggle dataset path)
@st.cache_data
def load_data():
    return pd.read_csv("Health_data.csv")  # replace with your dataset file

df = load_data()

st.title("🧠 Mental Health Score Analysis")
st.write("Interactive dashboard based on my Kaggle project")

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df.head())

# Histogram of Mental Health Score
st.subheader("Distribution of Mental Health Scores")
fig, ax = plt.subplots()
sns.histplot(df['Mental_Health_Score'], kde=True, ax=ax)
st.pyplot(fig)

# Boxplot: Stress Level vs Mental Health Score
st.subheader("Stress Level vs Mental Health Score")
order = ['Low', 'Medium', 'High', 'Very High']
fig, ax = plt.subplots()
sns.boxplot(x='Stress_Level', y='Mental_Health_Score', data=df, order=order, ax=ax)
st.pyplot(fig)

# Scatterplot: Daily Usage vs Mental Health Score
st.subheader("Daily Usage Hours vs Mental Health Score")
fig, ax = plt.subplots()
sns.scatterplot(x='Avg_Daily_Usage_Hours', y='Mental_Health_Score', data=df, ax=ax)
st.pyplot(fig)

st.write("📊 This app lets you explore how stress levels and daily usage hours relate to mental health scores.")
