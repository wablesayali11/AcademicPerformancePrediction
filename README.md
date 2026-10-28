# Academic Performance Prediction System

A beginner-friendly Machine Learning project that estimates a student's final marks using attendance, daily study hours, and previous marks.

## Features

- Predicts estimated final marks using Linear Regression.
- Loads student data from a CSV dataset.
- Evaluates predictions using Mean Absolute Error (MAE) and R² score.
- Saves and loads the trained model using Joblib.
- Provides an interactive web interface using Streamlit.
- Includes automated tests using Pytest.
- Supports containerization using Docker.

## Tech Stack

- **Programming Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Model Saving:** Joblib
- **Web Application:** Streamlit
- **Testing:** Pytest
- **Containerization:** Docker
- **Version Control:** Git and GitHub

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
│   └── test_model.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## Dataset

The dataset is stored in `data/student_performance.csv`.

It contains the following columns:

| Feature | Description |
|---|---|
| `attendance` | Student attendance percentage |
| `study_hours` | Daily study hours |
| `previous_marks` | Marks obtained previously |
| `final_marks` | Target variable representing final marks |

The current dataset contains 10 illustrative sample records for learning and experimentation.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/wablesayali11/AcademicPerformancePrediction.git
cd AcademicPerformancePrediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Train the model

```bash
python src/train_model.py
```

This command trains the Linear Regression model, evaluates its predictions, and saves the trained model to `models/student_performance_model.pkl`.

### 5. Run the web application

```bash
python -m streamlit run src/app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Making Predictions

To run the example prediction script:

```bash
python src/predict.py
```

To make predictions interactively:

1. Open the Streamlit application.
2. Enter attendance percentage.
3. Enter daily study hours.
4. Enter previous marks.
5. Click **Predict Final Marks** to view the estimated result.

## Model Evaluation

The project uses Linear Regression to estimate final marks.

The evaluation metrics are:

- **Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted marks. Lower values generally indicate smaller prediction errors.
- **R² Score:** Measures how well the predictions fit the target values on the test set. It is not a percentage accuracy measure.

The current sample run produced:

- **MAE:** 1.02 marks
- **R² Score:** 0.73

These results are based on a single train-test split containing 8 training records and 2 testing records. Because the dataset is extremely small, the metrics are not reliable evidence of real-world performance.

## Running Automated Tests

Run the tests from the project root:

```bash
python -m pytest -v
```

The tests check whether the saved model produces valid predictions and can predict marks for multiple student records.

## Running with Docker

Make sure Docker Desktop is installed and running.

### 1. Build the Docker image

From the project root:

```bash
docker build -t academic-performance-app .
```

The `.dockerignore` file excludes unnecessary files such as the virtual environment, Git history, and Python caches from the Docker build context.

### 2. Start the container

```bash
docker run -d -p 8501:8501 --name academic-performance-container academic-performance-app
```

### 3. Open the application

Visit:

http://localhost:8501

### 4. Stop the container

```bash
docker stop academic-performance-container
```

### 5. Start the existing container again

```bash
docker start academic-performance-container
```

If the container name is already in use, remove the stopped container before creating another container with that same name:

```bash
docker rm academic-performance-container
```

## Future Improvements

- Use a larger and more representative student performance dataset.
- Compare multiple machine learning algorithms.
- Improve data validation and error handling.
- Add cross-validation and more evaluation metrics.
- Improve the Streamlit interface.
- Configure automated testing using GitHub Actions.
- Deploy the application to an online hosting platform.

## Disclaimer

This project is intended for educational purposes. Predictions are estimates and are not guaranteed academic results. The model should not be used to make consequential decisions about students.

## Author

Student project developed to learn Machine Learning, Python, testing, Git, GitHub, and Docker.

