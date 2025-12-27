🎓 Student Burnout & Productivity Analyzer

A Streamlit app using machine learning to predict student productivity and burnout from everyday study and lifestyle habits.

📌 Overview

This project analyzes daily student habits such as study hours, sleep, screen time, deadlines, and caffeine intake to:
- Predict a productivity score
- Assess burnout level (Low / Medium / High)
- Provide practical suggestions to improve balance and wellbeing
- The goal is to demonstrate an end-to-end machine learning workflow, from data preparation to deployment as an interactive web application.

⚙️ Tech Stack

- Python
- scikit-learn – machine learning models
- pandas – data handling
- Streamlit – interactive web interface
- pickle – model saving and loading

🧠 How It Works

1. A custom dataset was created using realistic rules based on student behavior.
2. Two machine learning models were trained:
   - A regression model to predict productivity score
   - A classification model to predict burnout level
3. User inputs are collected through sliders in the Streamlit app.
4. The app displays:
   - Predicted productivity score
   - Burnout level with visual feedback
   - Reasons contributing to burnout
   - Actionable tips based on habits

📊 Features

- Interactive sliders for daily habits
- Live productivity prediction
- Burnout assessment with clear status indicators
- Personalized suggestions for improvement
- Clean and user-friendly UI

▶️ Running the App Locally

1. Install dependencies:
       pip install streamlit pandas scikit-learn
2. Run the app:
       python -m streamlit run app.py

🎯 Learning Outcomes

- Built and evaluated regression and classification models
- Understood overfitting and model generalization
- Connected ML models to a real user interface
- Designed a simple, usable ML-powered application


