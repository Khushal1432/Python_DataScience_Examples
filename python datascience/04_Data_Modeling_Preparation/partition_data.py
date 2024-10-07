# Partitioning data into training and testing sets using sklearn

import pandas as pd
from sklearn.model_selection import train_test_split

# Sample data
data = {'Feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Feature2': [5, 7, 8, 5, 7, 3, 8, 9, 3, 7],
        'Label': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}

df = pd.DataFrame(data)

# Partition the data (70% training, 30% testing)
X = df[['Feature1', 'Feature2']]
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Training Features:\n", X_train)
print("Testing Features:\n", X_test)
print("Training Labels:\n", y_train)
print("Testing Labels:\n", y_test)
