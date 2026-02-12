# Logistic Regression for Spam Classification

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -------------------------
# Dataset (Emails)
# -------------------------
emails = [
    "Win money now",
    "Limited offer click now",
    "Meeting at office today",
    "Project discussion tomorrow",
    "Congratulations you won prize",
    "Call me later",
    "Cheap loans available",
    "Lunch with manager"
]

labels = [1, 1, 0, 0, 1, 0, 1, 0]  
# 1 = Spam, 0 = Not Spam

data = pd.DataFrame({
    "Email": emails,
    "Label": labels
})

# -------------------------
# Convert text to numbers
# -------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["Email"])
y = data["Label"]

# -------------------------
# Train-Test Split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -------------------------
# Logistic Regression Model
# -------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

# -------------------------
# Prediction
# -------------------------
y_pred = model.predict(X_test)

# -------------------------
# Evaluation
# -------------------------
print("Accuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
