import pandas as pd
import numpy as np

# Data
age_groups = ["2-4", "4-6", "6-8", "8-10"]
frequency = np.array([16, 13, 7, 5])

# Midpoints
midpoints = np.array([3, 5, 7, 9])

# Create Frequency Table
table = pd.DataFrame({
    "Age Group": age_groups,
    "Frequency": frequency,
    "Midpoint": midpoints,
    "f*x": frequency * midpoints
})

print("GROUP FREQUENCY TABLE\n")
print(table)

# Total frequency
N = np.sum(frequency)

# ---------- Mean ----------
mean = np.sum(frequency * midpoints) / N

# ---------- Standard Deviation ----------
variance = np.sum(frequency * (midpoints - mean)**2) / N
sd = np.sqrt(variance)

# ---------- Mode ----------
L = 2          # lower boundary of modal class
fm = 16        # modal frequency
f_prev = 0     # no previous class
f_next = 13
w = 2          # class width

mode = L + ((fm - f_prev) / ((fm - f_prev) + (fm - f_next))) * w

# ---------- Skewness ----------
skewness = (mean - mode) / sd

print("\nMean =", round(mean,2))
print("Standard Deviation =", round(sd,2))
print("Mode =", round(mode,2))
print("Skewness =", round(skewness,2))

if skewness > 0:
    print("Data is Positively Skewed")
else:
    print("Data is Negatively Skewed")


# ---------- Differences ----------
print("\nDifferences between Stratified and Cluster Sampling:\n")

print("1. Stratified sampling divides population into similar groups,")
print("   while cluster sampling divides population into mixed groups.\n")

print("2. Stratified sampling selects samples from every group,")
print("   whereas cluster sampling selects only some clusters.")
