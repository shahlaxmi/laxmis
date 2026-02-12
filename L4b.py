# Actual and Forecasted Demand
actual = [42, 45, 49, 55, 57, 60, 62, 58, 54, 50, 44, 40]
forecast = [44, 46, 48, 50, 55, 60, 64, 60, 53, 48, 42, 38]

# Calculate errors
errors = []
squared_errors = []

for a, f in zip(actual, forecast):
    error = a - f
    errors.append(error)
    squared_errors.append(error ** 2)

# Mean Square Error
mse = sum(squared_errors) / len(actual)

print("Errors:", errors)
print("Squared Errors:", squared_errors)
print("Sum of Squared Errors:", sum(squared_errors))
print("Mean Square Error (MSE):", mse)
