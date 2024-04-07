import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_combined_box_plot(folder_path):
    combined_data = []  # List to store combined data from all CSV files
    phylum_names = []   # List to store phylum names
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item.endswith('.csv'):
            phylum_name = os.path.splitext(os.path.basename(item))[0]
            phylum_name_parts = phylum_name.split('_')  # Splitting by underscore
            if len(phylum_name_parts) > 1:  # Check if there is a '_' in the file name
                extracted_name = phylum_name_parts[-1]  # Take the last part after the last '_'
                phylum_names.append(extracted_name)
                df = pd.read_csv(item_path)
                if 'PQS FREQUENCY' in df.columns:
                    combined_data.append(df['PQS FREQUENCY'])

    plt.figure(figsize=(12, 8))
    plt.boxplot(combined_data, labels=phylum_names, flierprops=dict(marker='o', markersize=3, markerfacecolor='black'))  # Set marker style to dots
    # plt.xlabel('Phylum Name')
    plt.ylabel('PQS Frequency per 1000 bp')
    plt.title('Distribution of PQS in Archaea Sub Phylums')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('combined_boxplot,dpi = 800.png')
    plt.show()

# Example usage:
folder_path = ''
generate_combined_box_plot(folder_path)
