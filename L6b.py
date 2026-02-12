# Confusion Matrix Values
TP = 22   # Predicted YES, Actual YES
FP = 10   # Predicted YES, Actual NO
FN = 8    # Predicted NO, Actual YES
TN = 60   # Predicted NO, Actual NO

# Accuracy
accuracy = (TP + TN) / (TP + TN + FP + FN)

# Recall (Sensitivity)
recall = TP / (TP + FN)

# Precision
precision = TP / (TP + FP)

# F1 Score
f1_score = 2 * (precision * recall) / (precision + recall)

print("Accuracy =", round(accuracy,2))
print("Recall =", round(recall,2))
print("Precision =", round(precision,2))
print("F1 Score =", round(f1_score,2))
