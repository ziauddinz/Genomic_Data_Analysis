import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Read data from CSV file
df = pd.read_csv("/home/zia/data/G4_count_whole_genoem.csv")

# Create a figure and axis object for both plots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plotting the scatter plot for GC% vs PQS Found
gc_pqs_plot = axs[0].scatter(df['GC%'], df['Range Above 1.2'], color='green', label='Other Points', s=50)  # Increase size with 's' parameter
axs[0].set_xlabel('GC%')
axs[0].set_ylabel('PQS Found')
axs[0].grid(False)
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)

# Outlining the scatter plot area
for spine in axs[0].spines.values():
    spine.set_edgecolor('black')

# Find the indices of the two maximum values in the 'Range Above 1.2' column
max_indices = df['Range Above 1.2'].nlargest(2).index
# Annotate the corresponding 'File Name' values for these indices
for idx in max_indices:
    axs[0].annotate(df.loc[idx, 'File Name'], (df.loc[idx, 'GC%'], df.loc[idx, 'Range Above 1.2']), textcoords="offset points", xytext=(0,10), ha='center', color='blue')  # Assign blue color for maximum values

# Plotting the scatter plot for Genome Size vs PQS Found
genome_pqs_plot = axs[1].scatter(df['Total Size'], df['Range Above 1.2'], color='blue', label='Other Points', s=50)  # Increase size with 's' parameter
axs[1].set_xlabel('Genome Size')
axs[1].set_ylabel('PQS Found')
axs[1].grid(False)
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)

# Outlining the scatter plot area
for spine in axs[1].spines.values():
    spine.set_edgecolor('black')

# Find the indices of the three maximum values in the 'Total Size' column
max_size_indices = df['Total Size'].nlargest(3).index
# Annotate the corresponding 'File Name' values for these indices
label_list = ["Archaeon genome assembly ASM414622v1", "Candidatus Pacearchaeota archaeon", "Candidatus Bathyarchaeota archaeon"]
for idx, label in zip(max_size_indices, label_list):
    axs[1].annotate(f"{label}\nGC% = {df.loc[idx, 'GC%']:.4f}", (df.loc[idx, 'Total Size'], df.loc[idx, 'Range Above 1.2']), textcoords="offset points", xytext=(0,10), ha='center', color='red')  # Assign red color for maximum values

# Define a custom tick formatter function
def format_ticks(x, pos):
    return f"{x / 10**6:.0f}M"  # Format the tick labels to represent millions

# Apply the custom tick formatter to the x-axis of the second plot
axs[1].xaxis.set_major_formatter(FuncFormatter(format_ticks))
# Improve layout
plt.tight_layout()

# Save the figure with higher quality
plt.savefig("comparison_plot.png", bbox_inches='tight', dpi=800)

# Show the plot
plt.show()
