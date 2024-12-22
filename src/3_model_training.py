import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle
import os

# Check current working directory
print("Current Working Directory:", os.getcwd())

# Load processed data
X_train = pd.read_csv('data\X_train.csv')  # Adjusted path
X_test = pd.read_csv('data\X_test.csv')  # Adjusted path
y_train = pd.read_csv('data\y_train.csv').squeeze()  # Adjusted path
y_test = pd.read_csv('data\y_test.csv').squeeze()  # Adjusted path

# Train Logistic Regression
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
lr_preds = lr_model.predict(X_test)

# Train Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

# Evaluate models
def evaluate_model(name, y_true, y_pred):
    print(f"Performance of {name}:")
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.2f}")
    print(f"Precision: {precision_score(y_true, y_pred):.2f}")
    print(f"Recall: {recall_score(y_true, y_pred):.2f}")
    print(f"F1 Score: {f1_score(y_true, y_pred):.2f}")
    print("-" * 30)

evaluate_model("Logistic Regression", y_test, lr_preds)
evaluate_model("Random Forest", y_test, rf_preds)

# Save the better model
with open('models/delay_prediction_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)

print("Model training completed.")
