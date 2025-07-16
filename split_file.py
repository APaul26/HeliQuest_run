"""
Scanning the human protein sequences to find Lipid binding helices using HeliQuest server"
Created by: Abhirup Paul and Robert Newberry | Newberry Lab | University of Texas, Austin
https://www.newberrylab.com/
"""
#########################################################################################
"""Here, we will divide the trimmed human protein sequence file to 42 parts, i.e 20644 seq into 42 file, each containing 500 sequences.
The final file (#42) will contain the remaining 144 sequences. 
Each protein sequence generates a no. of segemnts which HeliQuest predicts as Lipid binding helices, possible lipid binding helices,
random coils, helices, high beta sheet propensity, and TM segments. Each of these segments is considered as a processed sequence by the tool 
The max number of sequences that HeliQuest can process in one run is 10k. Therefore, the initial input has been reduced to 500 sequences per file.
"""
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
input_path = r"Change your path accordingly\human_prot_seq_trimmed.txt"
#Run
split_fasta_file(input_path, sequences_per_file=500)