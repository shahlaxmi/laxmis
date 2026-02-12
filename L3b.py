import numpy as np
import matplotlib.pyplot as plt

# Given data
age = np.array([43, 21, 25, 42, 57, 59])
glucose = np.array([99, 65, 79, 75, 87, 81])

# Calculate mean values
mean_x = np.mean(age)
mean_y = np.mean(glucose)

# Calculate slope (m) and intercept (c)
m = np.sum((age - mean_x) * (glucose - mean_y)) / np.sum((age - mean_x) ** 2)
c = mean_y - m * mean_x

# Regression line
x_line = np.linspace(min(age), max(age), 100)
y_line = m * x_line + c

# Plot
plt.scatter(age, glucose)
plt.plot(x_line, y_line)
plt.xlabel("Age (x)")
plt.ylabel("Glucose Level (y)")
plt.title("Age vs Glucose Level")
plt.show()

