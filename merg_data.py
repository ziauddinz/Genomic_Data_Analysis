import pandas as pd

# Load the CSV files
file1 = pd.read_csv('')
file2 = pd.read_csv('')

# Extract common characters
file1['Common ID'] = file1['File Name'].str.extract(r'(GCA_\d+\.\d+)')
file2['Common ID'] = file2['Assembly Accession'].str.extract(r'(GCA_\d+\.\d+)')

# Merge based on the common ID
merged = pd.merge(file2, file1, on='Common ID', how='inner')

# Drop the redundant columns
merged = merged.drop(columns=['Common ID'])

# Save the merged DataFrame to a new CSV file
merged.to_csv('merged_file.csv', index=False)
