import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Dataset
data = {
    'Weather': ['Sunny','Cloudy','Sunny','Cloudy','Rainy','Rainy','Rainy','Sunny','Cloudy','Rainy'],
    'Humidity': ['High','High','Normal','High','High','Normal','High','High','Normal','High'],
    'Wind': ['Weak','Weak','Strong','Strong','Strong','Strong','Weak','Strong','Weak','Strong'],
    'Play': ['No','Yes','Yes','Yes','No','No','Yes','No','Yes','No']
}

df = pd.DataFrame(data)

# Encode categorical data
encoder = LabelEncoder()
for col in df.columns:
    df[col] = encoder.fit_transform(df[col])

X = df.drop('Play', axis=1)
y = df['Play']

# Train model (entropy → information gain)
model = DecisionTreeClassifier(criterion='entropy', max_depth=3)
model.fit(X, y)

# Plot tree
plt.figure(figsize=(14,7))
plot_tree(model,
          feature_names=X.columns,
          class_names=['No','Yes'],
          filled=True)
plt.show()
