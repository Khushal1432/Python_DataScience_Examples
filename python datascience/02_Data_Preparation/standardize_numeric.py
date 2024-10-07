# Standardizing numeric fields (Z-score normalization)

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter'], 'Salary': [50000, 48000, 70000]}
df = pd.DataFrame(data)

# Standardizing the Salary column
scaler = StandardScaler()
df['Salary_Standardized'] = scaler.fit_transform(df[['Salary']])

print("Standardized DataFrame:")
print(df)
