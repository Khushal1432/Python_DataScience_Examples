# Applying the Confidence Difference Criterion for association rules

from mlxtend.frequent_patterns import association_rules

# Reusing the frequent_itemsets generated in the previous example
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# Applying the confidence difference criterion: confidence > 0.6
confidence_difference_rules = rules[rules['confidence'] > 0.6]

print("Association Rules with Confidence Difference Criterion:\n", confidence_difference_rules[['antecedents', 'consequents', 'support', 'confidence']])
