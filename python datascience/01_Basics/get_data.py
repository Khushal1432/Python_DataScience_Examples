# Loading data from a CSV file using pandas

import pandas as pd

# Assuming 'data.csv' is a file in the same directory
# Example file content:
# Name,Age,Salary
# John,28,50000
# Anna,24,48000
# Peter,35,70000

df = pd.read_csv('data.csv')
print("Loaded Data:")
print(df)

# Show first few rows
print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))
