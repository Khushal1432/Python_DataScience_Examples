# Performing model evaluation (accuracy, precision, recall)

from sklearn.metrics import accuracy_score, precision_score, recall_score
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Sample data
data = {'Feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Feature2': [5, 7, 8, 5, 7, 3, 8, 9, 3, 7],
        'Label': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}

df = pd.DataFrame(data)

# Partition the data
X = df[['Feature1', 'Feature2']]
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
