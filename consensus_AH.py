"""
Scanning the human protein sequences to find Lipid binding helices using HeliQuest server"
Created by: Abhirup Paul and Robert Newberry | Newberry Lab | University of Texas, Austin
https://www.newberrylab.com/
"""
#########################################################################################
########## FInding AH consensus HeliQuest Vs. In-house results ##########################
#########################################################################################

"""Here, we will be finding the consensus sequences of the AH segments as predicted by HeliQuest and In-house code.
We will do this for both the lipid binding and possible lipid binding helices."""

#################### Lipid binding helices #########################

import pandas as pd
#File paths
lipid_overlap_IDs = r"Change your path accordingly\[In_house] + [Heli - Lipid]_structure.xlsx"
inhouse_data = r"Change your path accordingly\[In_house] + [Heli - Lipid]_structure_info.xlsx"
heliquest_data = r"Change your path accordingly\HELIQUEST - [In_house + Heli - Lipid] structure_info.xlsx"
output_path = r"Change your path accordingly\COMPARE [In-house + Heli - lipid_bind]_structure_info.xlsx"

#Loading gene IDs to be matched
gene_ids = pd.read_excel(lipid_overlap_IDs)['Gene'].dropna().astype(str).str.strip().unique()
#Reading both source files
inhouse_df = pd.read_excel(inhouse_data)
heliquest_df = pd.read_excel(heliquest_data)
#Standardize gene ID columns
inhouse_df['Gene'] = inhouse_df['Gene'].astype(str).str.strip()
heliquest_df['Gene'] = heliquest_df['Gene'].astype(str).str.strip()

#Collector for final data
final_rows = []

for gene in gene_ids:
    inhouse_hits = inhouse_df[inhouse_df['Gene'] == gene]
    heliquest_hits = heliquest_df[heliquest_df['Gene'] == gene]

    #Reset index to help with horizontal merge
    inhouse_hits = inhouse_hits.reset_index(drop=True)
    heliquest_hits = heliquest_hits.reset_index(drop=True)

    #Determine the maximum number of rows between both sources
    max_len = max(len(inhouse_hits), len(heliquest_hits))

    #Pad smaller dataframe to match length
    inhouse_hits = inhouse_hits.reindex(range(max_len), fill_value=None)
    heliquest_hits = heliquest_hits.reindex(range(max_len), fill_value=None)

    #Combine side-by-side and append
    merged = pd.concat([inhouse_hits, heliquest_hits.drop(columns='Gene')], axis=1)
    final_rows.append(merged)

#Final concatenation
final_df = pd.concat(final_rows, ignore_index=True)
#Save
final_df.to_excel(output_path, index=False)
print(f"Combined info for {len(final_df)} entries saved to:")
print(output_path)

#################### Possible lipid binding helices #########################

import pandas as pd
#File paths
lipid_overlap_IDs = r"Change your path accordingly\[In_house] + [Heli - Poss_lipid]_structure.xlsx"
inhouse_data = r"Change your path accordingly\[In_house] + [Heli - Poss_lipid]_structure_info.xlsx"
heliquest_data = r"Change your path accordingly\HELIQUEST - [In_house + Heli - Poss_lipid] structure_info.xlsx"
output_path = r"Change your path accordingly\COMPARE [In-house + Heli - Poss_lipid_bind]_structure_info.xlsx"

#Loading gene IDs to be matched
gene_ids = pd.read_excel(lipid_overlap_IDs)['Gene'].dropna().astype(str).str.strip().unique()
#Reading both source files
inhouse_df = pd.read_excel(inhouse_data)
heliquest_df = pd.read_excel(heliquest_data)
#Standardize gene ID columns
inhouse_df['Gene'] = inhouse_df['Gene'].astype(str).str.strip()
heliquest_df['Gene'] = heliquest_df['Gene'].astype(str).str.strip()

#Collector for final data
final_rows = []

for gene in gene_ids:
    inhouse_hits = inhouse_df[inhouse_df['Gene'] == gene]
    heliquest_hits = heliquest_df[heliquest_df['Gene'] == gene]

    #Reset index to help with horizontal merge
    inhouse_hits = inhouse_hits.reset_index(drop=True)
    heliquest_hits = heliquest_hits.reset_index(drop=True)

    #Determine the maximum number of rows between both sources
    max_len = max(len(inhouse_hits), len(heliquest_hits))

    #Pad smaller dataframe to match length
    inhouse_hits = inhouse_hits.reindex(range(max_len), fill_value=None)
    heliquest_hits = heliquest_hits.reindex(range(max_len), fill_value=None)

    #Combine side-by-side and append
    merged = pd.concat([inhouse_hits, heliquest_hits.drop(columns='Gene')], axis=1)
    final_rows.append(merged)

#Final concatenation
final_df = pd.concat(final_rows, ignore_index=True)

# Save output
final_df.to_excel(output_path, index=False)
print(f"Combined info for {len(final_df)} entries saved to:")
print(output_path)
