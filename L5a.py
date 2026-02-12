# Decision Tree Classifier on Iris Dataset

# 1. Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 2. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
feature_names = iris.feature_names

# 3. Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create the Decision Tree model
dt = DecisionTreeClassifier(criterion='gini', random_state=42)

# 5. Train the model
dt.fit(X_train, y_train)

# 6. Make predictions
y_pred = dt.predict(X_test)

# 7. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))

# 8. Visualize the Decision Tree
plt.figure(figsize=(18, 10))
plot_tree(
    dt,
    feature_names=feature_names,
    class_names=class_names,
    filled=True
)
plt.title("Decision Tree for Iris Dataset")
plt.show()
