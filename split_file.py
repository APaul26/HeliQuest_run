"""
Created by: Abhirup Paul and Robert Newberry | Newberry Lab | University of Texas, Austin
https://www.newberrylab.com/
"""
"""Here, we will divide the trimmed human protein sequence file to 11 parts, i.e 20644 seq into 10 file, each containing 2000 sequences.
The final file (#11) will contain the remaining 644 sequences."""
import os

def split_fasta_file(input_file, sequences_per_file=500):
    folder = os.path.dirname(input_file)
    file_index = 1
    header_count = 0
    file_sequence_counts = {}

    output_filename = os.path.join(folder, f"#{file_index}.txt")
    outfile = open(output_filename, 'w')
    file_sequence_counts[output_filename] = 0

    with open(input_file, 'r') as infile:
        for line in infile:
            if line.lstrip().startswith('>'):
                if header_count > 0 and header_count % sequences_per_file == 0:
                    outfile.close()
                    print(f"{os.path.basename(output_filename)} → {file_sequence_counts[output_filename]} sequences")
                    file_index += 1
                    output_filename = os.path.join(folder, f"#{file_index}.txt")
                    outfile = open(output_filename, 'w')
                    file_sequence_counts[output_filename] = 0
                header_count += 1
                file_sequence_counts[output_filename] += 1
            outfile.write(line.strip() + '\n')

    outfile.close()
    print(f"{os.path.basename(output_filename)} → {file_sequence_counts[output_filename]} sequences")
    print(f"\n {header_count} sequences into {file_index} file(s) in: {folder}")

#Input
input_path = r"C:\WORK\P.hD\Newberry_Lab\Research\RDPs\RDP_3\Data\HeliQuest\human_prot_seq_trimmed.txt"
#Run
split_fasta_file(input_path, sequences_per_file=500)