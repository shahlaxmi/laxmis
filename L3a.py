# Multiple Linear Regression - Student Performance

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ----------------------------
# 1. Load Dataset
# ----------------------------
# Example CSV format:
# StudyHours,Attendance,AssignmentScore,Performance

data = pd.read_csv("student_performance.csv")

# Independent variables
X = data[['StudyHours', 'Attendance', 'AssignmentScore']]

# Dependent variable
y = data['Performance']

# ----------------------------
# 2. Train-Test Split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------
# 3. Model Training
# ----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ----------------------------
# 4. Prediction
# ----------------------------
y_pred = model.predict(X_test)

# ----------------------------
# 5. Performance Metrics
# ----------------------------
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

# ----------------------------
# 6. Scatter Plot (Actual vs Predicted)
# ----------------------------
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Performance")
plt.ylabel("Predicted Performance")
plt.title("Actual vs Predicted Student Performance")
plt.show()
