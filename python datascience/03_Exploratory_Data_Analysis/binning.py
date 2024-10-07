# Performing binning based on predictive value using pandas

import pandas as pd
import numpy as np

# Sample data
data = {'Score': [85, 90, 78, 92, 88, 76, 95, 80, 89, 93]}

df = pd.DataFrame(data)

# Binning the 'Score' column into 3 bins based on quantiles
df['Score_Bin'] = pd.qcut(df['Score'], q=3, labels=["Low", "Medium", "High"])

print("Binned Data:\n", df)
