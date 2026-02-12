import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Sample dataset (similar pattern to the image)
X = np.array([
    [2,3],[3,3],[3,2],[2,2],[4,3],[3,4],   # Class 0 (circles)
    [6,6],[7,7],[6,7],[7,6],[5,6]          # Class 1 (diamonds)
])

y = np.array([0,0,0,0,0,0, 1,1,1,1,1])

# Train KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Create meshgrid for boundary
h = 0.1
x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1

xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.contourf(xx, yy, Z, alpha=0.3)

# Plot data points
plt.scatter(X[y==0][:,0], X[y==0][:,1], label="Class 0")
plt.scatter(X[y==1][:,0], X[y==1][:,1], marker='D', label="Class 1")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Decision Boundary (KNN)")
plt.legend()
plt.show()
