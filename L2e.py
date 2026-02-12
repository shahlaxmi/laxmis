import math
classes = [(2, 4), (4, 6), (6, 8), (8, 10)]      #skewness
freq = [3, 4, 2, 1]
midpoints = [(a + b) / 2 for a, b in classes]

n = sum(freq)

fx = [f * x for f, x in zip(freq, midpoints)]
mean = sum(fx) / n

diff = [x - mean for x in midpoints]

f_d2 = [f * (d ** 2) for f, d in zip(freq, diff)]
f_d3 = [f * (d ** 3) for f, d in zip(freq, diff)]
f_d4 = [f * (d ** 4) for f, d in zip(freq, diff)]

sum_f_d2 = sum(f_d2)
sum_f_d3 = sum(f_d3)
sum_f_d4 = sum(f_d4)

sd = math.sqrt(sum_f_d2 / n)

skewness = sum_f_d3 / ((n - 1) * (sd ** 3))
kurtosis = sum_f_d4 / ((n - 1) * (sd ** 4))

print("Midpoints:", midpoints)
print("Mean:", mean)
print("Standard Deviation:", sd)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)


