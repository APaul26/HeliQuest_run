"""
Scanning the human protein sequences to find Lipid binding helices using HeliQuest server"
Created by: Abhirup Paul and Robert Newberry | Newberry Lab | University of Texas, Austin
https://www.newberrylab.com/
"""
#########################################################################################

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
################################################# 1st module #####################################################################
# Filtering out the gene IDs and their respective information - No structure
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################


"""Here, we will filter out the gene IDs from the in-house compiled results that are exclusively predicted only by the in_house code and not HeliQuest.
The code will also extract the information of these gene IDs that are already present in the compiled results file.
"""
import pandas as pd
#File paths
exclusive_gene_IDs = r"Change your path accordingly\In_house_[Exclusive]_no_structure.xlsx"
compiled_results = r"Change your path accordingly\in_house_compiled.xlsx"
output_path = r"Change your path accordingly\In_house_[Exclusive]_no_structure_info.xlsx"
#Reading both Excel files
exclusive_df = pd.read_excel(exclusive_gene_IDs)
compiled_df = pd.read_excel(compiled_results)

#Cleaning and extract gene IDs from the exclusive list
exclusive_genes = set(exclusive_df['Gene'].dropna().astype(str).str.strip())
#Filtering the compiled dataframe for matching gene IDs
filtered_df = compiled_df[compiled_df['Gene'].astype(str).str.strip().isin(exclusive_genes)]
#Saving the filtered results to a new Excel file
filtered_df.to_excel(output_path, index=False)

print(f"Filtered data for {len(filtered_df)} gene IDs saved to:")
print(output_path)


##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
################################################# 2nd module #####################################################################
# Filtering out the gene IDs and their respective information - with structure
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################


"""Here, we will filter out the gene IDs from the in-house compiled results that are exclusively predicted only by the in_house code and not HeliQuest.
The code will also extract the information of these gene IDs that are already present in the compiled results file.
"""
import pandas as pd
#File paths
exclusive_gene_IDs = r"Change your path accordingly\In_house_[Exclusive]_structure.xlsx"
compiled_results = r"Change your path accordingly\in_house_compiled.xlsx"
output_path = r"Change your path accordingly\In_house_[Exclusive]_structure_info.xlsx"
#Reading both Excel files
exclusive_df = pd.read_excel(exclusive_gene_IDs)
compiled_df = pd.read_excel(compiled_results)

#Cleaning and extract gene IDs from the exclusive list
exclusive_genes = set(exclusive_df['Gene'].dropna().astype(str).str.strip())
#Filtering the compiled dataframe for matching gene IDs
filtered_df = compiled_df[compiled_df['Gene'].astype(str).str.strip().isin(exclusive_genes)]
#Saving the filtered results to a new Excel file
filtered_df.to_excel(output_path, index=False)

print(f"Filtered data for {len(filtered_df)} gene IDs saved to:")
print(output_path)


# Overlaps and info
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
################################################# 3rd module #####################################################################
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

"""Here, we will filter out the gene IDs from the in-house compiled results that are predicted by 
both in_house code and HeliQuest: Lipid binding.
The code will also extract the information of these gene IDs that are already present in the compiled results file.
"""
import pandas as pd
#File paths
exclusive_gene_IDs = r"Change your path accordingly\[In_house] + [Heli - Lipid]_structure.xlsx"
compiled_results = r"Change your path accordingly\in_house_compiled.xlsx"
output_path = r"Change your path accordingly\[In_house] + [Heli - Lipid]_structure_info.xlsx"
#Reading both Excel files
exclusive_df = pd.read_excel(exclusive_gene_IDs)
compiled_df = pd.read_excel(compiled_results)

#Cleaning and extract gene IDs from the exclusive list
exclusive_genes = set(exclusive_df['Gene'].dropna().astype(str).str.strip())
#Filtering the compiled dataframe for matching gene IDs
filtered_df = compiled_df[compiled_df['Gene'].astype(str).str.strip().isin(exclusive_genes)]
#Saving the filtered results to a new Excel file
filtered_df.to_excel(output_path, index=False)

print(f"Filtered data for {len(filtered_df)} gene IDs saved to:")
print(output_path)

############################################################################################################

"""Here, we will filter out the gene IDs from the in-house compiled results that are predicted by 
both in_house code and HeliQuest: possible lipid binding.
The code will also extract the information of these gene IDs that are already present in the compiled results file.
"""
import pandas as pd
#File paths
exclusive_gene_IDs = r"Change your path accordingly\[In_house] + [Heli - Poss_lipid]_structure.xlsx"
compiled_results = r"Change your path accordingly\in_house_compiled.xlsx"
output_path = r"Change your path accordingly\[In_house] + [Heli - poss_lipid]_structure_info.xlsx"
#Reading both Excel files
exclusive_df = pd.read_excel(exclusive_gene_IDs)
compiled_df = pd.read_excel(compiled_results)

#Cleaning and extract gene IDs from the exclusive list
exclusive_genes = set(exclusive_df['Gene'].dropna().astype(str).str.strip())
#Filtering the compiled dataframe for matching gene IDs
filtered_df = compiled_df[compiled_df['Gene'].astype(str).str.strip().isin(exclusive_genes)]
#Saving the filtered results to a new Excel file
filtered_df.to_excel(output_path, index=False)

print(f"Filtered data for {len(filtered_df)} gene IDs saved to:")
print(output_path)

#############################################################################################################

"""Here, we will filter out the gene IDs from the in-house compiled results that are predicted by 
all three: in_house code; HeliQuest: lipid and; Possible lipid binding.
The code will also extract the information of these gene IDs that are already present in the compiled results file.
"""
import pandas as pd
#File paths
exclusive_gene_IDs = r"Change your path accordingly\[In_house] + [Heli - Lipid] + [Heli - Poss_lipid]_structure.xlsx"
compiled_results = r"Change your path accordingly\in_house_compiled.xlsx"
output_path = r"Change your path accordingly\[In_house] + [Heli - Lipid] + [Heli - poss_lipid]_structure_info.xlsx"
#Reading both Excel files
exclusive_df = pd.read_excel(exclusive_gene_IDs)
compiled_df = pd.read_excel(compiled_results)

#Cleaning and extract gene IDs from the exclusive list
exclusive_genes = set(exclusive_df['Gene'].dropna().astype(str).str.strip())
#Filtering the compiled dataframe for matching gene IDs
filtered_df = compiled_df[compiled_df['Gene'].astype(str).str.strip().isin(exclusive_genes)]
#Saving the filtered results to a new Excel file
filtered_df.to_excel(output_path, index=False)

print(f"Filtered data for {len(filtered_df)} gene IDs saved to:")
print(output_path)

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
################################################# 4th module #####################################################################
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

# Extracting info for HeliQuest: Lipid and Possible lipid binding gene IDs overlaps with in-house

"""Here, we will extract infomation of the HeliQuest predictions for the overlapping gene IDs (structure) with in-house results for 
Lipid binding helices and possible lipid binding helices."""

################### Lipid binding helices and In-house results ################################
import pandas as pd
#File paths
overlap_gene_IDs = r"Change your path accordingly\[In_house] + [Heli - Lipid]_structure.xlsx"
Heli_compiled_results = r"Change your path accordingly\HeliQuest_Results\Lipid_binding.xlsx"
output_path = r"Change your path accordingly\HELIQUEST - [In_house + Heli - Lipid] structure_info.xlsx"
#Reading both Excel files
overlap_df = pd.read_excel(overlap_gene_IDs)
compiled_df = pd.read_excel(Heli_compiled_results)

#Cleaning and extract gene IDs from the exclusive list
overlap_genes = set(overlap_df['Gene'].dropna().astype(str).str.strip())
#Filtering the compiled dataframe for matching gene IDs
filtered_df = compiled_df[compiled_df['Gene'].astype(str).str.strip().isin(overlap_genes)]
#Saving the filtered results to a new Excel file
filtered_df.to_excel(output_path, index=False)

print(f"Filtered data for {len(filtered_df)} gene IDs saved to:")
print(output_path)

#################################################################################################

################### Possible lipid binding helices and In-house results ###################
import pandas as pd
#File paths
overlap_gene_IDs = r"Change your path accordingly\[In_house] + [Heli - Poss_lipid]_structure.xlsx"
Heli_compiled_results = r"Change your path accordingly\Possible_lipid_binding.xlsx"
output_path = r"Change your path accordingly\HELIQUEST - [In_house + Heli - Poss_lipid] structure_info.xlsx"
#Reading both Excel files
overlap_df = pd.read_excel(overlap_gene_IDs)
compiled_df = pd.read_excel(Heli_compiled_results)

#Cleaning and extract gene IDs from the exclusive list
overlap_genes = set(overlap_df['Gene'].dropna().astype(str).str.strip())
#Filtering the compiled dataframe for matching gene IDs
filtered_df = compiled_df[compiled_df['Gene'].astype(str).str.strip().isin(overlap_genes)]
#Saving the filtered results to a new Excel file
filtered_df.to_excel(output_path, index=False)

print(f"Filtered data for {len(filtered_df)} gene IDs saved to:")
print(output_path)

#################################################################################################

################### All 3 ###################
import pandas as pd
#File paths
overlap_gene_IDs = r"Change your path accordingly\[In_house] + [Heli - Lipid] + [Heli - Poss_lipid]_structure.xlsx"
Heli_compiled_results = r"Change your path accordingly\Compiled [Lipid & Possible_lipid].xlsx"
output_path = r"Change your path accordingly\HELIQUEST - [In_house + Heli - Lipid + Heli - Poss_lipid] structure_info.xlsx"
#Reading both Excel files
overlap_df = pd.read_excel(overlap_gene_IDs)
compiled_df = pd.read_excel(Heli_compiled_results)

#Cleaning and extract gene IDs from the exclusive list
overlap_genes = set(overlap_df['Gene'].dropna().astype(str).str.strip())
#Filtering the compiled dataframe for matching gene IDs
filtered_df = compiled_df[compiled_df['Gene'].astype(str).str.strip().isin(overlap_genes)]
#Saving the filtered results to a new Excel file
filtered_df.to_excel(output_path, index=False)

print(f"Filtered data for {len(filtered_df)} gene IDs saved to:")
print(output_path)