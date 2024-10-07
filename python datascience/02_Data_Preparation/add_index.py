# Adding an index field to a DataFrame

import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 24, 35]}
df = pd.DataFrame(data)

# Adding an index column
df['Index'] = df.index
print("DataFrame with Index:")
print(df)
