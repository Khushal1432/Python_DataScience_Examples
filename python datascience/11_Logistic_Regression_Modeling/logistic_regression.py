# Performing Logistic Regression using scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample binary classification data
data = {'Age': [22, 25, 47, 52, 46, 56, 34, 22],
        'Income': [25000, 32000, 50000, 55000, 62000, 72000, 38000, 29000],
        'Bought': [0, 0, 1, 1, 1, 1, 0, 0]}

df = pd.DataFrame(data)

# Features and target
X = df[['Age', 'Income']]
y = df['Bought']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build logistic regression model
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Predict and evaluate
y_pred = log_reg.predict(X_test)

print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
