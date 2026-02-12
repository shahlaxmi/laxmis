# Import libraries
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Step 1: Define the dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Advertising Spend
Y = np.array([1.8, 2.4, 3.2, 3.8, 4.5])      # Sales

# Step 2: Create and fit the model
model = LinearRegression()
model.fit(X, Y)

# Step 3: Predict Y values
Y_pred = model.predict(X)

# Step 4: Get model parameters
print(f"Intercept (b0): {model.intercept_:.2f}")
print(f"Slope (b1): {model.coef_[0]:.2f}")

# Step 5: Calculate errors
mse = mean_squared_error(Y, Y_pred)
mae = mean_absolute_error(Y, Y_pred)
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")

# Optional: Print predictions
print("\nPredicted Sales:", Y_pred)
