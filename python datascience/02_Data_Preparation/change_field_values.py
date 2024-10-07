# Changing misleading field values

import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [28, -24, 35]}
df = pd.DataFrame(data)

# Identifying and changing invalid negative ages
df['Age'] = df['Age'].apply(lambda x: abs(x) if x < 0 else x)
print("Corrected DataFrame:")
print(df)
