import numpy as np

# Age class midpoints
midpoints = np.array([4.5, 14.5, 24.5, 34.5, 44.5, 54.5, 64.5, 74.5, 84.5])

# Frequencies
freq = np.array([20, 21, 23, 16, 11, 10, 7, 3, 1])

# ---------- MEAN ----------
mean = np.sum(midpoints * freq) / np.sum(freq)
print("Estimated Mean =", round(mean, 2))


# ---------- MEDIAN ----------
n = np.sum(freq)
cum_freq = np.cumsum(freq)

# Find median class
median_index = np.where(cum_freq >= n/2)[0][0]

L = 19.5   # lower boundary of median class (20-29)
B = cum_freq[median_index - 1]  # cumulative freq before median class
G = freq[median_index]         # frequency of median class
w = 10                         # class width

median = L + ((n/2 - B) / G) * w
print("Estimated Median =", round(median, 2))


# ---------- MODE ----------
fm = 23     # modal class frequency
f_prev = 21
f_next = 16
L = 19.5
w = 10

mode = L + ((fm - f_prev) / ((fm - f_prev) + (fm - f_next))) * w
print("Estimated Mode =", round(mode, 2))
