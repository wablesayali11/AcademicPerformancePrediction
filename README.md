# Academic Performance Prediction System

A beginner-friendly Machine Learning project that estimates a student's final marks using attendance, daily study hours, and previous marks.

## Features

- Predicts estimated final marks using Linear Regression.
- Uses student data stored in a CSV file.
- Evaluates model predictions using Mean Absolute Error (MAE).
- Saves and reloads the trained model using Joblib.
- Provides an interactive web interface using Streamlit.

## Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Model Saving:** Joblib
- **Web App:** Streamlit
- **Planned:** Docker, GitHub Actions CI/CD

## Project Structure

```text
AcademicPerformancePrediction/
├── data/
│   └── student_performance.csv
├── models/
│   └── student_performance_model.pkl
├── src/
│   ├── main.py
│   ├── prepare_data.py
│   ├── train_model.py
│   ├── predict.py
│   └── app.py
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Train the model:

```bash
python src/train_model.py
```

5. Launch the web application:

```bash
python -m streamlit run src/app.py
```

6. Open the local URL displayed in the terminal.

## Input Features

- Attendance percentage
- Daily study hours
- Previous marks

The model uses these features to estimate final marks.

## Model Evaluation

The project currently uses Linear Regression and Mean Absolute Error (MAE) to evaluate predictions.

**Dataset limitation:** The current dataset contains only 10 illustrative sample records. The reported evaluation results are for learning purposes and do not establish real-world predictive accuracy.

## Future Improvements

- Use a larger, suitable dataset.
- Compare multiple machine learning models.
- Add data validation and automated tests.
- Containerize the application using Docker.
- Configure automated testing with GitHub Actions.

## Disclaimer

Predictions are educational estimates, not guaranteed academic results. The model should not be used to make consequential decisions about students.

## Author

Student project developed for learning Machine Learning, Python, and DevOps fundamentals.
