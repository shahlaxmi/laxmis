import math

# Given values
mean = 550
standard_deviation = 180
sample_size = 200

# Standard Error formula
standard_error = standard_deviation / math.sqrt(sample_size)

print("Mean:", mean)
print("Standard Deviation:", standard_deviation)
print("Sample Size:", sample_size)
print("Standard Error =", round(standard_error, 2))
