# Saving a DataFrame to a CSV file using pandas

import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 24, 35], 'Salary': [50000, 48000, 70000]}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file without the index
df.to_csv('output.csv', index=False)

print("Data saved to 'output.csv'")

# Check saved file content:
# Name,Age,Salary
# John,28,50000
# Anna,24,48000
# Peter,35,70000
