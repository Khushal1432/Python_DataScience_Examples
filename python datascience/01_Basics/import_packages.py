# Example of importing and using common Python packages

# Importing numpy for numerical computations
import numpy as np

# Importing pandas for data manipulation
import pandas as pd

# Creating a simple numpy array
arr = np.array([1, 2, 3, 4, 5])
print(f"Numpy Array: {arr}")

# Creating a pandas DataFrame
data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 24, 35]}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

