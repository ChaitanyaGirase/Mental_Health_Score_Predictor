import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Mental Health Score Predictor",
    page_icon="🧠",
    layout="centered"
)

model = joblib.load("model/Mental_Health_RandomForest.pkl")

st.title("Mental Health Score Predictor")

st.write("Enter the students information to predict the mental health score.")

st.write(
    "This application predicts a Mental Health Score using a machine learning model "
    "based on the student's lifestyle, study habits, social media usage, and stress level."
)



st.header("🧑 Student Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age", 
        min_value= 18,
        max_value = 100, 
    )

    gender = st.selectbox(
        "Gender", 
        ["Male", "Female"]
    )

with col2:
    academic_level = st.selectbox(
        "Academic Level",
        ["High School", "Undergraduate", "Graduate"]
    )

    grouped_country = st.selectbox(
        "Country",
        ["Other",
         "India",
         "USA",
         "Canada",
         "Australia",
         "UK",
         "Germany",
         "Mexico",
         "Turkey",
         "France"]
    )

st.header("📱 Social Media Usage")
col1, col2 = st.columns(2)

with col1:
    platform = st.selectbox(
        "Most Used Platform",
        ["Instagram",
         "TikTok",
         "Facebook",
         "LinkedIn",
         "YouTube",
         "Twitter",
         "Snapchat",
         "WhatsApp",
         "LINE",
         "VKontakte",
         "KakaoTalk",
         "WeChat"]
    )

    usage_hours = st.number_input(
        "Average Daily Usage Hours",
        min_value = 1.0,
        max_value = 9.0,
        value = 5.0,
        step = 0.1
    )

with col2:
    purpose = st.selectbox(
        "Purpose Of Use",
        ["Entertainment", 
         "Education",
         "Networking",
         "News"]
    )

    daily_unlocks = st.number_input(
        "Daily Unlocks",
        min_value = 20,
        max_value = 300,
        step = 1
    )


st.header("📚 Lifestyle & Wellbeing")
col1, col2 = st.columns(2)

with col1:
    study_hours = st.number_input(
        "Study Hours",
        min_value = 0.3,
        max_value = 24.0,
        step = 0.1
    )

    physical_activity = st.number_input(
        "Physical Activity Hours", 
        min_value = 0.0,
        max_value = 10.0
    )

with col2:
    sleep_hours = st.number_input(
        "Sleep Hours Per Night",
        min_value = 3.0,
        max_value = 24.0
    )

    stress_level = st.selectbox(
        "Stress Level",
        ["Low", "Medium", "High", "Very High"]
    )

input_data = pd.DataFrame([{

    "Age": age,
    "Gender": gender,
    "Academic_Level": academic_level,
    "Most_Used_Platform": platform,
    "Purpose_Of_Use": purpose,
    "Avg_Daily_Usage_Hours": usage_hours,
    "Daily_Unlocks": daily_unlocks,
    "Study_Hours": study_hours,
    "Physical_Activity_Hours": physical_activity,
    "Sleep_Hours_Per_Night": sleep_hours,
    "Stress_Level": stress_level,
    "grouped_country": grouped_country
}])


st.divider()

st.divider()

if st.button(
    "🧠 Predict Mental Health Score",
    use_container_width=True
):
    prediction = model.predict(input_data)[0]

    st.subheader("📊 Prediction Result")

    st.metric(
        label="Predicted Mental Health Score",
        value=f"{prediction:.2f}"
    )

    st.progress(
        min(max(prediction / 10, 0.0), 1.0)
    )

