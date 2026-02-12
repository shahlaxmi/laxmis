values = [0, 1, 2, 3, 4, 5]      #mean,median,mode
frequencies = [27, 96, 58, 54, 18, 7]

total_freq = sum(frequencies)

mean = sum(v * f for v, f in zip(values, frequencies)) / total_freq

cum_freq = []
cumulative = 0
for f in frequencies:
    cumulative += f
    cum_freq.append(cumulative)

if total_freq % 2 == 0:
    mid1 = total_freq // 2
    mid2 = mid1 + 1
else:
    mid1 = (total_freq + 1) // 2
    mid2 = mid1

def find_value_at_position(position):
    for i, cf in enumerate(cum_freq):
        if position <= cf:
            return values[i]

median_val1 = find_value_at_position(mid1)
median_val2 = find_value_at_position(mid2)
median = (median_val1 + median_val2) / 2

max_freq = max(frequencies)
mode = values[frequencies.index(max_freq)]

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
