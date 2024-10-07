# Constructing contingency tables using pandas

import pandas as pd

# Sample data
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Outcome': ['Pass', 'Fail', 'Pass', 'Fail', 'Pass', 'Fail']}

df = pd.DataFrame(data)

# Constructing a contingency table (cross-tabulation)
contingency_table = pd.crosstab(df['Category'], df['Outcome'])

print("Contingency Table:\n", contingency_table)
