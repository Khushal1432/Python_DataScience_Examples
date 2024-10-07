# Constructing a bar graph with overlay using matplotlib and seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
data = {'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
        'Count': [50, 80, 45, 60, 85, 40],
        'Type': ['X', 'X', 'X', 'Y', 'Y', 'Y']}

df = pd.DataFrame(data)

# Plot bar graph with overlay using seaborn
sns.barplot(x='Category', y='Count', hue='Type', data=df)

# Set title and labels
plt.title('Bar Graph with Overlay')
plt.xlabel('Category')
plt.ylabel('Count')

# Show plot
plt.show()
