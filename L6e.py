import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Dataset
# Features: [Weight, Height]
X = np.array([
    [4,35],
    [6,40],
    [3,25],
    [7,45],
    [5,30],
    [8,50],
    [2,20],
    [5,35]
])

# Labels
y = np.array(["Cat","Dog","Cat","Dog","Cat","Dog","Cat","Dog"])

# Create KNN model (K=5)
model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

# Train the model
model.fit(X, y)

# New animal
new_animal = np.array([[4,30]])

# Prediction
prediction = model.predict(new_animal)

print("The new animal is predicted as:", prediction[0])
