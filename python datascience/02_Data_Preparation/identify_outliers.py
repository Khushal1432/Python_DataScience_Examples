# Identifying outliers using Z-scores

import pandas as pd
import numpy as np

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'James'],
        'Salary': [50000, 48000, 70000, 60000, 1000000]}  # 1000000 is an outlier
df = pd.DataFrame(data)

# Calculate Z-scores
df['Z_Score'] = (df['Salary'] - df['Salary'].mean()) / df['Salary'].std()

# Identify outliers where the Z-score is greater than 3 or less than -3
outliers = df[np.abs(df['Z_Score']) > 3]

print("Outliers:")
print(outliers)
