"""
Scanning the human protein sequences to find Lipid binding helices using HeliQuest server"
Created by: Abhirup Paul and Robert Newberry | Newberry Lab | University of Texas, Austin
https://www.newberrylab.com/
"""
#########################################################################################
"""Here, we will trim the FASTA sequence headers to only keep the gene name. 
   Additionally, we will also count the number of sequences.
   The human protein sequence has been downloaded from Uniprot and has all the human protein sequences."""
import os
def trim_fasta_headers(input_file, output_file):
    header_count = 0

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                try:
                    gene_name = line.split('|')[1].strip() #Extract the gene names only
                except IndexError:
                    gene_name = line[1:].split()[0]
                outfile.write(f'>{gene_name}\n')
                header_count += 1
            else:
                outfile.write(line.strip() + '\n')
    
    print(f"Trimmed sequences written to: {output_file}")
    print(f"Total headers processed: {header_count}")
    
#File paths
input_path = r"Change your path accordingly\human_prot_seq.txt"
output_path = r"Change your path accordingly\human_prot_seq_trimmed.txt"
#Run
trim_fasta_headers(input_path, output_path)