import os
import pandas as pd

def analyze_file(file_path):
    try:
        # Load the data from the specified path
        df = pd.read_csv(file_path, delimiter='\t', skiprows=1)
        
        # Remove leading and trailing spaces from column names
        df.columns = df.columns.str.strip()
        
        # Convert 'Score' and 'Length' columns to numeric, handling errors
        df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
        df['Length'] = pd.to_numeric(df['Length'], errors='coerce')
        
        # Filter out rows where 'Score' or 'Length' is NaN
        df = df.dropna(subset=['Score', 'Length'])
        
        # Filter the DataFrame based on the score ranges
        range_1 = df[(df['Score'] >= 1.2) & (df['Score'] <= 1.39)]
        range_2 = df[(df['Score'] >= 1.4) & (df['Score'] <= 1.59)]
        range_3 = df[(df['Score'] >= 1.6) & (df['Score'] <= 1.79)]
        range_4 = df[(df['Score'] >= 1.8) & (df['Score'] <= 2.0)]
        range_5 = df[df['Score'] > 2.0]  # Range 5: Scores above 2.0

        # Sum the sequence lengths for the values in each range
        sum_length_range_1 = range_1['Length'].sum()
        sum_length_range_2 = range_2['Length'].sum()
        sum_length_range_3 = range_3['Length'].sum()
        sum_length_range_4 = range_4['Length'].sum()
        sum_length_range_5 = range_5['Length'].sum()

        # Count the number of filtered values in each range
        count_range_1 = len(range_1)
        count_range_2 = len(range_2)
        count_range_3 = len(range_3)
        count_range_4 = len(range_4)
        count_range_5 = len(range_5)

        # Sum the number of sequences for the entire DataFrame
        total_sequence_count = len(df)

        # Extracting the file name without extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Return the results
        return {
            'File Name': file_name,
            'Range 1 (1.2 to 1.39)': count_range_1,
            'Range 2 (1.4 to 1.59)': count_range_2,
            'Range 3 (1.6 to 1.79)': count_range_3,
            'Range 4 (1.8 to 2.0)': count_range_4,
            'Range 5 (Above 2.0)': count_range_5,
            'LEN 1.2-1.4': sum_length_range_1,
            'LEN 1.4-1.6': sum_length_range_2,
            'LEN 1.6-1.8': sum_length_range_3,
            'LEN 1.8-2.0': sum_length_range_4,
            'LEN 2.0-MORE': sum_length_range_5,
            'Sequence Sum': total_sequence_count
        }
    except Exception as e:
        print(f"Error processing file '{file_path}': {e}")
        return None

# Specify the folder path containing the files
folder_path = ""

# List all files in the folder
files = os.listdir(folder_path)

# Store the results of each file
results = []

# Iterate over each file
for file in files:
    # Analyze the file and append the results
    result = analyze_file(os.path.join(folder_path, file))
    if result is not None:
        results.append(result)

# Convert the results to a DataFrame
results_df = pd.DataFrame(results)

# Save the DataFrame to a CSV file
results_df.to_csv("D:/results.csv", index=False)

# Display the message
print("Analysis results saved successfully!")
