# 1-Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import fetch_openml

# 2-Load MNIST Dataset
mnist = fetch_openml('mnist_784', version=1)

X, y = mnist.data, mnist.target.astype(int)

# 3-Preprocess the Data
X = X / 255.0   # Normalize

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4-Train the SVM Model
svm_model = SVC(kernel='linear', C=1.0)
svm_model.fit(X_train, y_train)

# 5-Predictions
y_pred = svm_model.predict(X_test)

# 6-Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# 7-Visualize Confusion Matrix
plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
