# Demonstrating stepwise regression using statsmodels library

import pandas as pd
import statsmodels.api as sm
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

# Load the Boston housing dataset
boston = load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.Series(boston.target)

# Add a constant to the features (for intercept)
X = sm.add_constant(X)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build an initial model with all features
model = sm.OLS(y_train, X_train).fit()

# Perform stepwise regression (forward or backward elimination)
# For simplicity, we demonstrate backward elimination by removing least significant features

while True:
    p_values = model.pvalues
    max_p_value = p_values.max()  # Get the maximum p-value
    if max_p_value > 0.05:  # Remove features with p-value > 0.05
        max_p_feature = p_values.idxmax()
        X_train = X_train.drop(columns=[max_p_feature])
        model = sm.OLS(y_train, X_train).fit()
    else:
        break

# Final model summary
print(model.summary())
