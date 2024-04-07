import os

# Source directory containing CSV files
source_dir = ""

# Destination directory for files with repeated value 25 in the "Length" column
destination_dir = ""

# Ensure source and destination directories exist
if not os.path.isdir(source_dir):
    print(f"Error: Source directory '{source_dir}' does not exist.")
    exit(1)

os.makedirs(destination_dir, exist_ok=True)

# Loop through files in the source directory
files_found = False
for file_name in os.listdir(source_dir):
    # Check if file is a CSV file
    if file_name.endswith(".csv"):
        files_found = True
        file_path = os.path.join(source_dir, file_name)
        print(f"Found CSV file: {file_name}")
        # Read the file and check if value 25 is repeated in the "Length" column
        try:
            print(f"Processing file: {file_name}")
            repeated_25 = True  # Assume 25 is repeated until proven otherwise
            with open(file_path, "r") as file:
                header_skipped = False
                for line in file:
                    # Skip the header line
                    if not header_skipped:
                        header_skipped = True
                        continue
                    try:
                        columns = line.strip().split("\t")
                        # Extract the "Length" value (assuming it's the fourth column)
                        length_value = int(columns[3])
                        print(f"Length value: {length_value}")
                        if length_value != 25:
                            repeated_25 = False  # If any value is not 25, it's not repeated
                            break  # No need to continue checking
                    except (IndexError, ValueError) as e:
                        print(f"Error processing line: {line}")
            # If 25 is repeated for all lines in the "Length" column, move the file
            if repeated_25:
                destination_path = os.path.join(destination_dir, file_name)
                os.rename(file_path, destination_path)
                print(f"Moved {file_name} to {destination_dir}")
        except Exception as e:
            print(f"Error processing file: {file_name}")
            print(f"Error message: {str(e)}")

if not files_found:
    print("No CSV files found in the source directory.")
