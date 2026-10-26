
import joblib
import pandas as pd
import streamlit as st

# Load the trained model
model = joblib.load("models/student_performance_model.pkl")

st.title("Academic Performance Prediction System")
st.write("Enter student details to estimate final marks.")

attendance = st.slider("Attendance (%)", 0, 100, 82)
study_hours = st.number_input(
    "Daily Study Hours", min_value=0.0, max_value=24.0, value=3.0
)
previous_marks = st.number_input(
    "Previous Marks", min_value=0.0, max_value=100.0, value=70.0
)

if st.button("Predict Final Marks"):
    student = pd.DataFrame([{
        "attendance": attendance,
        "study_hours": study_hours,
        "previous_marks": previous_marks
    }])

    prediction = model.predict(student)[0]

    st.success(f"Estimated Final Marks: {prediction:.2f} / 100")
    st.caption(
        "This is an educational estimate from a small sample dataset, "
        "not a guarantee of actual performance."
    )
