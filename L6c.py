import pandas as pd

# Given sorted data
data = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]

df = pd.DataFrame({"Sales Price": data})

# ---------- Equal Frequency ----------
df["Equal_Frequency_Bins"] = pd.qcut(df["Sales Price"], q=3)

print("Equal Frequency Partition:\n")
print(df[["Sales Price", "Equal_Frequency_Bins"]])

# ---------- Equal Width ----------
df["Equal_Width_Bins"] = pd.cut(df["Sales Price"], bins=3)

print("\nEqual Width Partition:\n")
print(df[["Sales Price", "Equal_Width_Bins"]])
