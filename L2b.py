classes = [                     
    (59.95, 61.95), (61.95, 63.95), (63.95, 65.95),(65.95, 67.95),(67.95, 69.95),(69.95, 71.95),
    (71.95, 73.95),(73.95, 75.95)
    ]
                                        #table rep of height
frequencies = [5, 3, 15, 40, 17, 12, 7, 1]

total = sum(frequencies)

freq_less_than_65_95 = sum(frequencies[:3])
percent_less_than_65_95 = (freq_less_than_65_95 / total) * 100

freq_between_61_95_65_95 = sum(frequencies[1:3])
percent_between = (freq_between_61_95_65_95 / total) * 100

num_between_61_95_71_95 = sum(frequencies[1:6])

print("(a) Percentage < 65.95 inches:", percent_less_than_65_95, "%")
print("(b) Percentage between 61.95 and 65.95 inches:", percent_between, "%")
print("(c) Number of players between 61.95 and 71.95 inches:", num_between_61_95_71_95)
