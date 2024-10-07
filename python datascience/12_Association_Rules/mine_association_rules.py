# Mining association rules using the Apriori algorithm (mlxtend library)

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Sample dataset: a list of transactions
data = {'Milk': [1, 1, 0, 1, 0],
        'Bread': [1, 0, 0, 1, 1],
        'Eggs': [1, 0, 1, 0, 1],
        'Butter': [0, 1, 0, 1, 1]}

df = pd.DataFrame(data)

# Mining frequent itemsets using Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

print("Frequent Itemsets:\n", frequent_itemsets)

# Generating association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print("\nAssociation Rules:\n", rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
