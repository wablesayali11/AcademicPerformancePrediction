
import joblib
import pandas as pd

# 1. Load the saved model
model = joblib.load("models/student_performance_model.pkl")

# 2. Enter a new student's details
new_student = pd.DataFrame([{
    "attendance": 82,
    "study_hours": 3,
    "previous_marks": 70
}])

# 3. Predict final marks
predicted_marks = model.predict(new_student)

print("New Student Details:")
print("Attendance: 82%")
print("Daily Study Hours: 3")
print("Previous Marks: 70")

print("\nPredicted Final Marks:", round(predicted_marks[0], 2))
