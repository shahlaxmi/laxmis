# Actual and Forecasted Demand values from the slide
actual_demand = [42, 45, 49, 55, 57, 60, 62, 58, 54, 50, 44, 40]
forecasted_demand = [44, 46, 48, 50, 55, 60, 64, 60, 53, 48, 42, 38]

# Number of data points
n = len(actual_demand)

# Calculate MAPE
mape = (100 / n) * sum(abs(f - a) / a for a, f in zip(actual_demand, forecasted_demand))

print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
