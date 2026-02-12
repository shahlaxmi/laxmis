import math
actual = [42, 45, 49, 55, 57, 60, 62, 58, 54, 50, 44, 40]
forecasted = [44, 46, 48, 50, 55, 60, 64, 60, 53, 48, 42, 38]

# Calculate Error and Squared Error
errors = [a - f for a, f in zip(actual, forecasted)]
squared_errors = [e**2 for e in errors]

# Sum of Squared Errors
sum_squared_error = sum(squared_errors)

# Mean Squared Error (MSE)
mse = sum_squared_error / len(actual)

# Root Mean Squared Error (RMSE)
rmse = math.sqrt(mse)

print("Errors:", errors)
print("Squared Errors:", squared_errors)
print("Sum of Squared Errors:", sum_squared_error)
print("MSE:", mse)
print("RMSE:", rmse)
