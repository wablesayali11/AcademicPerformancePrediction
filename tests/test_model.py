
import joblib
import pandas as pd


def test_model_prediction_is_valid():
    model = joblib.load("models/student_performance_model.pkl")

    student = pd.DataFrame([{
        "attendance": 82,
        "study_hours": 3,
        "previous_marks": 70
    }])

    prediction = model.predict(student)[0]

    assert 0 <= prediction <= 100

def test_model_predicts_for_multiple_students():
    model = joblib.load("models/student_performance_model.pkl")

    students = pd.DataFrame([
        {
            "attendance": 60,
            "study_hours": 1,
            "previous_marks": 50
        },
        {
            "attendance": 95,
            "study_hours": 5,
            "previous_marks": 88
        }
    ])

    predictions = model.predict(students)

    assert len(predictions) == 2
    assert all(pd.notna(prediction) for prediction in predictions)
