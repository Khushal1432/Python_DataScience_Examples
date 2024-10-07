# Applying the Confidence Quotient Criterion for association rules

from mlxtend.frequent_patterns import association_rules

# Reusing the frequent_itemsets generated earlier
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# Calculating the confidence quotient (Confidence / (1 - Confidence))
rules['confidence_quotient'] = rules['confidence'] / (1 - rules['confidence'])

# Display rules with a confidence quotient greater than a certain threshold
high_conf_quotient_rules = rules[rules['confidence_quotient'] > 1.5]

print("Association Rules with Confidence Quotient Criterion:\n", high_conf_quotient_rules[['antecedents', 'consequents', 'confidence', 'confidence_quotient']])
