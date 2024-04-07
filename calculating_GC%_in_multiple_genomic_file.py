import os
import csv

def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    total_bases = len(sequence)
    gc_percentage = (gc_count / total_bases) * 100
    return gc_count, gc_percentage, total_bases

def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        header = file.readline().strip()[1:]
        sequence = ''.join(line.strip() for line in file)
    return header, sequence

def write_to_csv(file_path, file_name, gc_count, gc_percentage, total_bases):
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['File Name', 'GC Count', 'GC%', 'Total Size'])  # Write header without any additional values
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([file_name, gc_count, gc_percentage, total_bases])


def process_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.fna'):  # Process only .fna files
            fasta_file_path = os.path.join(folder_path, file_name)
            print("Processing file:", fasta_file_path)
            header, sequence = read_fasta_file(fasta_file_path)
            if header and sequence:
                gc_count, gc_percentage, total_bases = calculate_gc_content(sequence)
                if not os.path.exists("output.csv") or os.stat("output.csv").st_size == 0:
                    print("GC Count,GC%,Total Size")  # Print headers
                print(f"{file_name},{gc_count},{gc_percentage},{total_bases}")
                write_to_csv("output.csv", file_name, gc_count, gc_percentage, total_bases)
                print(f"Processed file: {file_name}")

def main():
    folder_path = input("Enter the path to the folder containing FASTA files: ")
    print("Provided folder path:", folder_path)
    if not os.path.isdir(folder_path):
        print("Invalid folder path. Please provide a valid path to the folder containing FASTA files.")
        return
    print("Processing folder...")
    process_folder(folder_path)
    print("CSV file updated successfully.")

if __name__ == "__main__":
    main()
