

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


X = np.array([500, 750, 1000, 1250, 1500, 1750, 2000]).reshape(-1, 1)

y = np.array([15, 25, 35, 45, 55, 65, 75])

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

plt.scatter(X, y)
plt.plot(X, y_pred)
plt.xlabel("Area (sq ft)")
plt.ylabel("House Price (Lakhs)")
plt.title("Simple Linear Regression - House Price Prediction")
plt.show()
