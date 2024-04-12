import numpy as np

def random_seq(gl=1000000, GC=50, seq_id=None, line_length=60):
    """Generate a random sequences with line breaks."""
    base = ['A', 'T', 'C', 'G']
    base_distr = [(1 - float(GC / 100)) / 2, (1 - float(GC / 100)) / 2, float(GC / 100) / 2, float(GC / 100) / 2]
    seq = ''.join(np.random.choice(base, gl, p=base_distr))

    # Insert line breaks every line_length nucleotides
    seq_with_linebreaks = '\n'.join([seq[i:i+line_length] for i in range(0, len(seq), line_length)])

    if seq_id:
        return f'>{seq_id}\n{seq_with_linebreaks}\n'
    else:
        return seq_with_linebreaks if seq_with_linebreaks else ''  # Return empty string if sequence is empty

def write_fasta(file_path, fasta_content):
    """Write FASTA content to a file."""
    try:
        with open(file_path, 'w') as f:
            f.write(fasta_content)
        print("FASTA file written successfully.")
    except Exception as e:
        print(f"Error occurred while writing the file: {e}")

# Example usage:
random_genome_seq = random_seq(gl=2000000, GC=50, seq_id='random_genome_1d')
write_fasta('/home/zia/data/New_script/random_genome.fasta', random_genome_seq)
