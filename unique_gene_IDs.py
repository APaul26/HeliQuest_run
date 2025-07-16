"""
Scanning the human protein sequences to find Lipid binding helices using HeliQuest server"
Created by: Abhirup Paul and Robert Newberry | Newberry Lab | University of Texas, Austin
https://www.newberrylab.com/
"""
#########################################################################################
#These codes from here on are to be used after we have compiled all the HeliQuest prediction data and filtered out the lipid binding and possible lipid binding predictions.

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
################################################# 1st module #####################################################################
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

"""Here, we will filter out the unique gene ids from the compiled lipid binding, possible lipid binding helices and in_house AH prediction files.
The code basically goes through the "Gene" column and spits out only the unique gene ids in a text file. This is needed for making
comparisons between the HeliQuest results and in-house code results.
"""
import pandas as pd
file_path = r"Change your path accordingly\Lipid_binding.xlsx"
data = pd.read_excel(file_path)
#Extracting unique gene IDs from the 'Gene' column
unique_genes = data['Gene'].dropna().unique() #checking for NaN values and extracting only the unique IDs
output_file = r"Change your path accordingly\Heli_lipid_binding_IDs.txt"
#Writing each unique gene ID to a new line of a .txt file
with open(output_file, 'w') as f:
    for gene_id in unique_genes:
        f.write(f"{gene_id}\n")        
print(f"{len(unique_genes)} unique gene IDs to: {output_file}")

#################################################################################################################################
"""Now we will do the same thing for the possible lipid binding helices results as well"""
file_path = r"Change your path accordingly\Possible_lipid_binding.xlsx"
data = pd.read_excel(file_path)
#Extracting unique gene IDs from the 'Gene' column
unique_genes = data['Gene'].dropna().unique() #checking for NaN values and extracting only the unique IDs
output_file = r"Change your path accordingly\Heli_possible_lipid_binding_IDs.txt"
#Writing each unique gene ID to a new line of a .txt file
with open(output_file, 'w') as f:
    for gene_id in unique_genes:
        f.write(f"{gene_id}\n")        
print(f"{len(unique_genes)} unique gene IDs to: {output_file}")

#################################################################################################################################
"""Now we will do the same thing for the in-house code results as well"""
file_path = r"Change your path accordingly\in_house_compiled.xlsx"
data = pd.read_excel(file_path)
#Extracting unique gene IDs from the 'Gene' column
unique_genes = data['Gene'].dropna().unique() #checking for NaN values and extracting only the unique IDs
output_file = r"Change your path accordingly\in_house_IDs.txt"
#Writing each unique gene ID to a new line of a .txt file
with open(output_file, 'w') as f:
    for gene_id in unique_genes:
        f.write(f"{gene_id}\n")        
print(f"{len(unique_genes)} unique gene IDs to: {output_file}")


##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
################################################# 2nd module #####################################################################
# Filtering out HeliQuest lipid binding and possible lipid biding Gene IDs with structural info 
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################


"""Filtering out HeliQuest lipid binding and possible lipid biding Gene IDs with structural info"""
"""Here, we will filter out the HeliQuest predicted lipid binding gene IDs that have experimentally derived structures available in the PDB.
This is done to extract and save the IDs that do not have any structures available."""
import os
#File paths
heliquest_lipid_binding_file = r"Change your path accordinglys\Heli_lipid_binding_IDs.txt"
structure_file = r"Change your path accordingly\Gene_IDs_with_structure_available.txt"
output_file = r"Change your path accordingly\HeliQuest_lipid_binding_no_structure.txt"
with open(heliquest_lipid_binding_file, 'r') as f:
    heliquest_ids = set(line.strip() for line in f if line.strip())

with open(structure_file, 'r') as f:
    structure_ids = set(line.strip() for line in f if line.strip())

#Filtering out IDs that don't have structural info
no_structure_ids = sorted(heliquest_ids - structure_ids)
#Saving the filtered IDs to a new file
with open(output_file, 'w') as f:
    for gene_id in no_structure_ids:
        f.write(f"{gene_id}\n")

print(f"{len(no_structure_ids)} gene IDs without structural data were saved to:")
print(output_file)

#################################################################################################
"""Now, we will do the same thing for the possible lipid binding helices results as well"""

heliquest_poss_lipid_binding_file = r"Change your path accordingly\Heli_possible_lipid_binding_IDs.txt"
structure_file = r"Change your path accordingly\Gene_IDs_with_structure_available.txt"
output_file = r"Change your path accordingly\HeliQuest_possible_lipid_binding_no_structure.txt"
with open(heliquest_poss_lipid_binding_file, 'r') as f:
    heliquest_poss_ids = set(line.strip() for line in f if line.strip())

with open(structure_file, 'r') as f:
    structure_ids = set(line.strip() for line in f if line.strip())

#Filtering out IDs that don't have structural info
no_structure_ids = sorted(heliquest_poss_ids - structure_ids)
#Saving the filtered IDs to a new file
with open(output_file, 'w') as f:
    for gene_id in no_structure_ids:
        f.write(f"{gene_id}\n")

print(f"{len(no_structure_ids)} gene IDs without structural data were saved to:")
print(output_file)


##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
################################################# 3rd module #####################################################################
# Filtering out HeliQuest lipid binding and possible lipid biding Gene IDs with no structural info 
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

"""Here, we will filter out the HeliQuest predicted lipid binding gene IDs that have no experimentally derived structures available in the PDB.
This is done to extract and save the IDs that have structures available."""
import os
#File paths
heliquest_lipid_binding_file = r"Change your path accordingly\Heli_lipid_binding_IDs.txt"
structure_file = r"Change your path accordingly\Gene_IDs_with_structure_available.txt"
output_file = r"Change your path accordingly\HeliQuest_lipid_binding_with_structure.txt"
with open(heliquest_lipid_binding_file, 'r') as f:
    heliquest_ids = set(line.strip() for line in f if line.strip())

with open(structure_file, 'r') as f:
    structure_ids = set(line.strip() for line in f if line.strip())

#Finding IDs that are in both sets (i.e., have structure)
with_structure_ids = sorted(heliquest_ids & structure_ids)

#Saving the filtered IDs to a new file
with open(output_file, 'w') as f:
    for gene_id in with_structure_ids:
        f.write(f"{gene_id}\n")

print(f"{len(with_structure_ids)} HeliQuest-predicted lipid binding gene IDs with structural data were saved to:")
print(output_file)

#################################################################################################################
"""Now, we will do the same thing for the possible lipid binding helices results as well"""

heliquest_poss_lipid_binding_file = r"Change your path accordingly\Heli_possible_lipid_binding_IDs.txt"
structure_file = r"Change your path accordingly\Gene_IDs_with_structure_available.txt"
output_file = r"Change your path accordingly\HeliQuest_possible_lipid_binding_with_structure.txt"
with open(heliquest_poss_lipid_binding_file, 'r') as f:
    heliquest_poss_ids = set(line.strip() for line in f if line.strip())

with open(structure_file, 'r') as f:
    structure_ids = set(line.strip() for line in f if line.strip())

#Filtering out IDs that don't have structural info
no_structure_ids = sorted(heliquest_poss_ids & structure_ids)
#Saving the filtered IDs to a new file
with open(output_file, 'w') as f:
    for gene_id in no_structure_ids:
        f.write(f"{gene_id}\n")

print(f"{len(no_structure_ids)} HeliQuest-predicted possible lipid binding gene IDs with structural data were saved to:")
print(output_file)


##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
################################################# 4th module #####################################################################
# Removing duplicates
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

"""Here, we will clean the gene ID text files that we generated earlier to remove duplicate gene IDs. 
This is needed for making the overlapping venn diagrams between HeliQuest and in-house code results."""

########## HeliQuest_lipid_binding_IDs.txt ###############
import os
#File paths
input_file = r"Change your path accordingly\HeliQuest_lipid_binding_IDs.txt"
cleaned_output_file = r"Change your path accordingly\HeliQuest_lipid_binding_IDs_clean.txt"
with open(input_file, 'r') as f:
    all_ids = [line.strip() for line in f if line.strip()]
#Deduplicate and sort
unique_ids = sorted(set(all_ids))
#Write cleaned list
with open(cleaned_output_file, 'w') as f:
    for gene_id in unique_ids:
        f.write(f"{gene_id}\n")
#Logging (optional)
total_ids = len(all_ids)
unique_count = len(unique_ids)
duplicates_removed = total_ids - unique_count

print(f"{unique_count} unique gene IDs saved to:")
print(cleaned_output_file)
print(f"{duplicates_removed} duplicate entries were removed.")

########## HeliQuest_possible_lipid_binding_IDs.txt ###############
import os
#File paths
input_file = r"Change your path accordingly\HeliQuest_possible_lipid_binding_IDs.txt"
cleaned_output_file = r"Change your path accordingly\HeliQuest_possible_lipid_binding_IDs_clean.txt"
with open(input_file, 'r') as f:
    all_ids = [line.strip() for line in f if line.strip()]
#Deduplicate and sort
unique_ids = sorted(set(all_ids))
#Write cleaned list
with open(cleaned_output_file, 'w') as f:
    for gene_id in unique_ids:
        f.write(f"{gene_id}\n")
#Logging (optional)
total_ids = len(all_ids)
unique_count = len(unique_ids)
duplicates_removed = total_ids - unique_count

print(f"{unique_count} unique gene IDs saved to:")
print(cleaned_output_file)
print(f"{duplicates_removed} duplicate entries were removed.")

########## HeliQuest_lipid_binding_no_structure_IDs.txt ###############
import os
#File paths
input_file = r"Change your path accordingly\HeliQuest_lipid_binding_no_structure_IDs.txt"
cleaned_output_file = r"Change your path accordingly\HeliQuest_lipid_binding_no_structure_IDs_clean.txt"
with open(input_file, 'r') as f:
    all_ids = [line.strip() for line in f if line.strip()]
#Deduplicate and sort
unique_ids = sorted(set(all_ids))
#Write cleaned list
with open(cleaned_output_file, 'w') as f:
    for gene_id in unique_ids:
        f.write(f"{gene_id}\n")
#Logging (optional)
total_ids = len(all_ids)
unique_count = len(unique_ids)
duplicates_removed = total_ids - unique_count

print(f"{unique_count} unique gene IDs saved to:")
print(cleaned_output_file)
print(f"{duplicates_removed} duplicate entries were removed.")

########## HeliQuest_lipid_binding_with_structure_IDs.txt ###############
import os
#File paths
input_file = r"Change your path accordingly\HeliQuest_lipid_binding_with_structure_IDs.txt"
cleaned_output_file = r"Change your path accordingly\HeliQuest_lipid_binding_with_structure_IDs_clean.txt"
with open(input_file, 'r') as f:
    all_ids = [line.strip() for line in f if line.strip()]
#Deduplicate and sort
unique_ids = sorted(set(all_ids))
#Write cleaned list
with open(cleaned_output_file, 'w') as f:
    for gene_id in unique_ids:
        f.write(f"{gene_id}\n")
#Logging (optional)
total_ids = len(all_ids)
unique_count = len(unique_ids)
duplicates_removed = total_ids - unique_count

print(f"{unique_count} unique gene IDs saved to:")
print(cleaned_output_file)
print(f"{duplicates_removed} duplicate entries were removed.")

########## HeliQuest_possible_lipid_binding_no_structure_IDs.txt ###############
import os
#File paths
input_file = r"Change your path accordingly\HeliQuest_possible_lipid_binding_no_structure_IDs.txt"
cleaned_output_file = r"Change your path accordingly\HeliQuest_possible_lipid_binding_no_structure_IDs_clean.txt"
with open(input_file, 'r') as f:
    all_ids = [line.strip() for line in f if line.strip()]
#Deduplicate and sort
unique_ids = sorted(set(all_ids))
#Write cleaned list
with open(cleaned_output_file, 'w') as f:
    for gene_id in unique_ids:
        f.write(f"{gene_id}\n")
#Logging (optional)
total_ids = len(all_ids)
unique_count = len(unique_ids)
duplicates_removed = total_ids - unique_count

print(f"{unique_count} unique gene IDs saved to:")
print(cleaned_output_file)
print(f"{duplicates_removed} duplicate entries were removed.")

########## HeliQuest_possible_lipid_binding_with_structure_IDs.txt ###############
import os
#File paths
input_file = r"Change your path accordingly\HeliQuest_possible_lipid_binding_with_structure_IDs.txt"
cleaned_output_file = r"Change your path accordingly\HeliQuest_possible_lipid_binding_with_structure_IDs_clean.txt"
with open(input_file, 'r') as f:
    all_ids = [line.strip() for line in f if line.strip()]
#Deduplicate and sort
unique_ids = sorted(set(all_ids))
#Write cleaned list
with open(cleaned_output_file, 'w') as f:
    for gene_id in unique_ids:
        f.write(f"{gene_id}\n")
#Logging (optional)
total_ids = len(all_ids)
unique_count = len(unique_ids)
duplicates_removed = total_ids - unique_count

print(f"{unique_count} unique gene IDs saved to:")
print(cleaned_output_file)
print(f"{duplicates_removed} duplicate entries were removed.")

########## In_house_IDs.txt ###############
import os
#File paths
input_file = r"Change your path accordingly\In_house_IDs.txt"
cleaned_output_file = r"Change your path accordingly\In_house_IDs_clean.txt"
with open(input_file, 'r') as f:
    all_ids = [line.strip() for line in f if line.strip()]
#Deduplicate and sort
unique_ids = sorted(set(all_ids))
#Write cleaned list
with open(cleaned_output_file, 'w') as f:
    for gene_id in unique_ids:
        f.write(f"{gene_id}\n")
#Logging (optional)
total_ids = len(all_ids)
unique_count = len(unique_ids)
duplicates_removed = total_ids - unique_count

print(f"{unique_count} unique gene IDs saved to:")
print(cleaned_output_file)
print(f"{duplicates_removed} duplicate entries were removed.")

########## In_house_no_structure_IDs.txt ###############
""" The inhouse IDs were filtered out from the in-house compiled file."""

import os
#File paths
input_file = r"Change your path accordingly\In_house_no_structure_IDs.txt"
cleaned_output_file = r"Change your path accordingly\In_house_no_structure_IDs_clean.txt"
with open(input_file, 'r') as f:
    all_ids = [line.strip() for line in f if line.strip()]
#Deduplicate and sort
unique_ids = sorted(set(all_ids))
#Write cleaned list
with open(cleaned_output_file, 'w') as f:
    for gene_id in unique_ids:
        f.write(f"{gene_id}\n")
#Logging (optional)
total_ids = len(all_ids)
unique_count = len(unique_ids)
duplicates_removed = total_ids - unique_count

print(f"{unique_count} unique gene IDs saved to:")
print(cleaned_output_file)
print(f"{duplicates_removed} duplicate entries were removed.")

########## In_house_structure_IDs.txt ###############
import os
#File paths
input_file = r"Change your path accordingly\In_house_structure_IDs.txt"
cleaned_output_file = r"Change your path accordingly\In_house_structure_IDs_clean.txt"
with open(input_file, 'r') as f:
    all_ids = [line.strip() for line in f if line.strip()]
#Deduplicate and sort
unique_ids = sorted(set(all_ids))
#Write cleaned list
with open(cleaned_output_file, 'w') as f:
    for gene_id in unique_ids:
        f.write(f"{gene_id}\n")
#Logging (optional)
total_ids = len(all_ids)
unique_count = len(unique_ids)
duplicates_removed = total_ids - unique_count

print(f"{unique_count} unique gene IDs saved to:")
print(cleaned_output_file)
print(f"{duplicates_removed} duplicate entries were removed.")

#####################################################################################################################
############################## End of this code #####################################################################
