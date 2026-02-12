import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Sample dataset( This is sample dataset, we can use realtime .csv file dataset)

data = {
    "Area": [750, 800, 1200, 1500, 2000],
    "Rooms": [2, 3, 3, 4, 5],
    "Price": [150000, 180000, 250000, 300000, 400000],
}
df = pd.DataFrame(data)

# Features (Area, Rooms) and Target (Price)

X = df[["Area", "Rooms"]]
y = df["Price"]

