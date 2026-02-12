data=[46.69,32,60,52,41]        #stdev
n=len(data)
mean=sum(data)/n
sq_dev=[(x-mean)** 2 for x in data]
sum_sqdev=sum(sq_dev)
sample_variance= sum_sqdev/(n-1)
import math
std_dev = math.sqrt(sample_variance)
print("Data:", data)
print("Mean:", mean)
print("Squared Deviations:", sq_dev)
print("Sum of Squared Deviations:", sum_sqdev)
print("Sample Variance:", sample_variance)
print("Standard Deviation:", std_dev)