# Performing Poisson regression using statsmodels

import statsmodels.api as sm
import numpy as np
import pandas as pd

# Sample data
data = {'Hours_Studied': [3, 4, 5, 6, 7, 8, 9, 10],
        'Grades': [1, 2, 2, 3, 3, 4, 4, 5]}

df = pd.DataFrame(data)

# Features and target
X = df[['Hours_Studied']]
y = df['Grades']

# Add a constant to features
X = sm.add_constant(X)

# Build the Poisson regression model
poisson_model = sm.GLM(y, X, family=sm.families.Poisson()).fit()

# Print the summary
print(poisson_model.summary())
