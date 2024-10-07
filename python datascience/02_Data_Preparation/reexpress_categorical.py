# Re-expressing categorical field values

import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter'], 'Gender': ['M', 'F', 'M']}
df = pd.DataFrame(data)

# Re-expressing 'Gender' from M/F to Male/Female
df['Gender'] = df['Gender'].map({'M': 'Male', 'F': 'Female'})
print("Re-expressed DataFrame:")
print(df)
