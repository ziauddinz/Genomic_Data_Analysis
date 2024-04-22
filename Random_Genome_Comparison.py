import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_combined_scatter_plots(folder_path, second_file_path):
    # Reading data from the second file
    second_df = pd.read_csv(second_file_path)

    files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    num_files = len(files)

    num_cols = 2  # Number of columns for subplots
    num_rows = (num_files + num_cols - 1) // num_cols  # Calculate number of rows

    plt.figure(figsize=(10, 4*num_rows))  # Set the size of the entire figure

    for i, item in enumerate(files, start=1):
        item_path = os.path.join(folder_path, item)
        phylum_name = os.path.splitext(os.path.basename(item))[0]
        df = pd.read_csv(item_path)
        if 'GC%' in df.columns and 'PQS FREQUENCY' in df.columns:
            plt.subplot(num_rows, num_cols, i)  # Create subplot
            plt.scatter(df['GC%'], df['PQS FREQUENCY'], color='blue', label='Original Data', s=20)  # Plot original data
            plt.scatter(second_df['GC%'], second_df['PQS FREQUENCY'], color='red', label='Random Genome Data', s=20)  # Plot data from second file
            plt.xlabel('GC%')
            plt.ylabel('PQS Frequency')
            plt.title(f'Scatter Plot for {phylum_name}')
            plt.grid(False)
            plt.legend()

    plt.tight_layout()
    plt.savefig('combined_scatter_plots.png', dpi=700)
    plt.show()

# Example usage:
folder_path = '/home/zia/data/Directory/Analysed.Phylum.csv'
second_file_path = '/home/zia/data/Directory/Results_data/Random_Genome_PQS_Frequency.csv'
generate_combined_scatter_plots(folder_path, second_file_path)
