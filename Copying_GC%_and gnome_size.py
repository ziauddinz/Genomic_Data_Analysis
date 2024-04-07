import pandas as pd

try:
    # Read the first CSV file
    print("Reading the first CSV file...")
    df1 = pd.read_csv("")
    print("First CSV file read successfully.")

    # Read the second CSV file
    print("Reading the second CSV file...")
    df2 = pd.read_csv("")
    print("Second CSV file read successfully.")

    # Iterate through each row in the first DataFrame
    print("Processing data...")
    for index, row in df1.iterrows():
    
        file_name = row['File Name']
        
       
        pattern = file_name.split('_')[0] + '_' + file_name.split('_')[1]
        
        # Find the corresponding row in the second DataFrame where the 'File Name' matches the pattern
        matched_row = df2[df2['File Name'].str.contains(pattern)]
        
        
        if not matched_row.empty:
            df1.at[index, 'GC Count'] = matched_row.iloc[0]['GC Count']
            df1.at[index, 'GC%'] = matched_row.iloc[0]['GC%']
            df1.at[index, 'Total Size'] = matched_row.iloc[0]['Total Size']

    # Overwrite the first CSV file with the updated data
    print("Writing the updated data to the first CSV file...")
    df1.to_csv("", index=False)

    # Print a message indicating that the process is complete
    print("Process complete. The CSV file has been updated.")

except Exception as e:
    # Print any error that occurs
    print("An error occurred:", e)

print("End of script.")
