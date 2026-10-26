
import pandas as pd

# Load the student dataset
df = pd.read_csv("data/student_performance.csv")

# Input features (X)
X = df[["attendance", "study_hours", "previous_marks"]]

# Target variable (y)
y = df["final_marks"]

# Display the results
print("Input Features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

print("\nTotal records:", len(df))
print("Number of input features:", X.shape[1])
