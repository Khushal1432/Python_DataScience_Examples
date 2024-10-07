# Constructing histograms with overlay using matplotlib and seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
data = {'Score': [85, 90, 78, 92, 88, 76, 95, 80, 89, 93],
        'Group': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']}

df = pd.DataFrame(data)

# Plot histograms with overlay using seaborn
sns.histplot(data=df, x='Score', hue='Group', element="step", kde=True)

# Set title and labels
plt.title('Histogram with Overlay')
plt.xlabel('Score')
plt.ylabel('Frequency')

# Show plot
plt.show()
