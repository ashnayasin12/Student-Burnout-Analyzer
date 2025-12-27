import streamlit as st
import pandas as pd
import pickle


with open("productivity_model.pkl", "rb") as f:
    productivity_model = pickle.load(f)

with open("burnout_model.pkl", "rb") as f:
    burnout_model = pickle.load(f)


def explain_burnout(study_hours, sleep_hours, screen_time, deadlines, caffeine):
    insights = []

    if sleep_hours <= 5:
        insights.append((
            "Low sleep duration",
            "Aim for 7–8 hours of sleep to improve focus, memory, and recovery."
        ))

    if deadlines >= 3:
        insights.append((
            "High academic pressure from deadlines",
            "Break work into smaller tasks and prioritize deadlines to reduce stress."
        ))

    if screen_time >= 7:
        insights.append((
            "Excessive screen time",
            "Take regular screen breaks and limit non-essential usage."
        ))

    if caffeine >= 4:
        insights.append((
            "High caffeine intake",
            "Try reducing caffeine, especially later in the day, to protect sleep quality."
        ))

    if study_hours >= 10:
        insights.append((
            "Overstudying without sufficient recovery",
            "Use focused study sessions with breaks instead of very long hours."
        ))

    if sleep_hours >= 7:
        insights.append((
            "Healthy sleep routine",
            "Consistent sleep is supporting your productivity and wellbeing."
        ))

    if screen_time <= 4:
        insights.append((
            "Controlled screen usage",
            "Good job keeping screen time balanced."
        ))

    if deadlines <= 2:
        insights.append((
            "Low deadline pressure",
            "Your workload appears manageable right now."
        ))

    return insights

st.set_page_config(page_title="Student Burnout Analyzer", layout="centered")

st.title("🎓 Student Burnout & Productivity Analyzer")
st.caption("An explainable ML-based self-check for students")

st.sidebar.header("🧠 Daily Habits Input")

study_hours = st.sidebar.slider("Study hours per day", 0, 14, 6)
sleep_hours = st.sidebar.slider("Sleep hours per night", 1, 9, 7)
screen_time = st.sidebar.slider("Screen time (hours per day)", 0, 12, 5)
deadlines = st.sidebar.slider("Number of active deadlines", 0, 5, 1)
caffeine = st.sidebar.slider("Caffeine intake (cups per day)", 0, 6, 2)


input_df = pd.DataFrame(
    [[study_hours, sleep_hours, screen_time, deadlines, caffeine]],
    columns=["study_hours", "sleep_hours", "screen_time", "deadlines", "caffeine"]
)


predicted_productivity = productivity_model.predict(input_df)[0]
predicted_burnout = burnout_model.predict(input_df)[0]
burnout_insights = explain_burnout(
    study_hours, sleep_hours, screen_time, deadlines, caffeine
)

st.markdown("---")
st.subheader("📊 Results")

st.metric(
    label="Predicted Productivity Score",
    value=f"{predicted_productivity:.1f} / 100"
)

if predicted_burnout == "High":
    st.error(f"🔥 Burnout Level: {predicted_burnout}")
elif predicted_burnout == "Medium":
    st.warning(f"⚠️ Burnout Level: {predicted_burnout}")
else:
    st.success(f"✅ Burnout Level: {predicted_burnout}")


st.markdown("---")
st.subheader("📌 Summary")

if predicted_burnout == "High":
    st.error(
        "You are showing signs of **high burnout**. Your current routine may not be sustainable long-term."
    )
elif predicted_burnout == "Medium":
    st.warning(
        "You have a **moderate burnout risk**. Small changes could improve balance and wellbeing."
    )
else:
    st.success(
        "Your routine looks **healthy and balanced**. Keep maintaining these habits!"
    )


if burnout_insights:
    st.markdown("---")
    st.subheader("🔍 Insights & Suggestions")

    for reason, tip in burnout_insights:
        with st.container():
            st.markdown(f"**• {reason}**")
            st.caption(f"💡 {tip}")
            st.markdown("---")
