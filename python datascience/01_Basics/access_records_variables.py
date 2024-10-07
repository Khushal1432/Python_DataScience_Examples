# Accessing specific records and variables from a DataFrame

import pandas as pd

# Sample data
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'James'],
        'Age': [28, 24, 35, 30, 45],
        'Salary': [50000, 48000, 70000, 60000, 55000]}

df = pd.DataFrame(data)

# Access a single column (variable)
print("Accessing 'Age' column:")
print(df['Age'])

# Access specific rows (records) using indexing
print("\nAccessing the first row:")
print(df.iloc[0])  # First row

# Access specific rows and columns
print("\nAccessing the first row's 'Name' and 'Salary':")
print(df.loc[0, ['Name', 'Salary']])

# Accessing rows based on a condition
print("\nAccessing records where Age is greater than 30:")
print(df[df['Age'] > 30])
