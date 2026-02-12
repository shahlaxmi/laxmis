import numpy as np

# Given data
orders = np.array([12, 23, 31, 15, 26, 24, 16, 23])

# Calculate mean
mean = np.mean(orders)

# Calculate average distance from mean (MAD)
average_distance = np.mean(np.abs(orders - mean))

print("Orders:", orders)
print("Mean =", round(mean,2))
print("Average distance from mean =", round(average_distance,2))
