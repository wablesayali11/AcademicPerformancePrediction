
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Load the dataset
df = pd.read_csv("data/student_performance.csv")

# 2. Separate inputs and target
X = df[["attendance", "study_hours", "previous_marks"]]
y = df["final_marks"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# 4. Create the model
model = LinearRegression()

# 5. Train the model
model.fit(X_train, y_train)

# 6. Predict marks for testing data
predictions = model.predict(X_test)

# 7. Evaluate the model
mae = mean_absolute_error(y_test, predictions)

print("\nActual marks:", y_test.tolist())
print("Predicted marks:", predictions.round(2).tolist())
print("Mean Absolute Error (MAE):", round(mae, 2))

# 8. Save the trained model
joblib.dump(model, "models/student_performance_model.pkl")

print("\nModel saved successfully!")
