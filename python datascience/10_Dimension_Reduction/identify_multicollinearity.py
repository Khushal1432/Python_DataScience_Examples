# Identifying multicollinearity using the Variance Inflation Factor (VIF)

import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.datasets import load_boston

# Load the Boston housing dataset
boston = load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)

# Add a constant column (for intercept)
X['Intercept'] = 1

# Calculate VIF for each feature
vif_data = pd.DataFrame()
vif_data['feature'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print("Variance Inflation Factor (VIF) for each feature:\n", vif_data)
