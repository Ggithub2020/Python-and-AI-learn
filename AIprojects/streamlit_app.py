import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("student_data.csv")

# Encode data
df_encoded = df.copy()
le = LabelEncoder()
df_encoded['parental_engagement'] = le.fit_transform(df_encoded['parental_engagement'])
df_encoded['dropout'] = df_encoded['dropout'].map({'No': 0, 'Yes': 1})

# Train model
X = df_encoded.drop(['student_id', 'dropout'], axis=1)
y = df_encoded['dropout']
model = RandomForestClassifier()
model.fit(X, y)

# UI
st.title("🎓 Student Dropout Risk Predictor")

st.sidebar.header("Enter Student Info")

attendance = st.sidebar.slider("Attendance Rate (%)", 50, 100, 85)
grade = st.sidebar.slider("Average Grade", 40, 100, 75)
assignments = st.sidebar.slider("Assignment Completion (%)", 30, 100, 80)
discipline = st.sidebar.number_input("Discipline Incidents", min_value=0, max_value=10, value=1)
engagement = st.sidebar.selectbox("Parental Engagement", ['High', 'Medium', 'Low'])

# Prediction
input_data = pd.DataFrame([{
    "attendance_rate": attendance,
    "average_grade": grade,
    "assignment_completion": assignments,
    "discipline_incidents": discipline,
    "parental_engagement": le.transform([engagement])[0]
}])

prediction = model.predict(input_data)[0]
probability = model.predict_proba(input_data)[0][1]

# Output
if prediction == 1:
    st.error(f"❌ At Risk of Dropping Out (Confidence: {probability:.2%})")
else:
    st.success(f"✅ Not at Risk (Confidence: {1 - probability:.2%})")

st.markdown("---")
st.subheader("📊 Feature Importance")
importances = pd.Series(model.feature_importances_, index=X.columns)
st.bar_chart(importances.sort_values(ascending=True))
