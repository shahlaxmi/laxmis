# 1. Import libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 2. Create dataset (from the image)
data = {
    'Weather': ['Sunny','Cloudy','Sunny','Cloudy','Rainy','Rainy','Rainy','Sunny','Cloudy','Rainy'],
    'Temperature': ['Hot','Hot','Mild','Mild','Mild','Cool','Mild','Hot','Hot','Mild'],
    'Humidity': ['High','High','Normal','High','High','Normal','High','High','Normal','High'],
    'Wind': ['Weak','Weak','Strong','Strong','Strong','Strong','Weak','Strong','Weak','Strong'],
    'Play': ['No','Yes','Yes','Yes','No','No','Yes','No','Yes','No']
}

df = pd.DataFrame(data)

# 3. Encode categorical values
encoder = LabelEncoder()
for col in df.columns:
    df[col] = encoder.fit_transform(df[col])

# 4. Split features and target
X = df.drop('Play', axis=1)
y = df['Play']

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Train Decision Tree model
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_train, y_train)

# 7. Predictions
y_pred = model.predict(X_test)

# 8. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 9. Visualize the Decision Tree
plt.figure(figsize=(16, 8))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=['No', 'Yes'],
    filled=True
)
plt.title("Decision Tree for Play Prediction")
plt.show()
