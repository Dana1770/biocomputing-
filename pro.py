from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import Counter
import pandas as pd


# File path for the existing Biopython file
existing_file_path = "C:/Users/Dana/Documents/projects/data.fasta"

# Read the existing file
records = list(SeqIO.parse(existing_file_path, "fasta"))

## Manually specify new sequences
#new_sequences = [
#    "ATCGATCGATCGATCG",
#    "GCTAGCTAGCTAGCTA",
#    "AGAGAGAGAGAGAGAG",
#    "CTCTCTCTCTCTCTCT",
#    "GGGGGGGGGGGGGGGG",
#    "CCCCCCCCCCCCCCCC",
#    "TATATATATATATATA",
#    "ACACACACACACACAC",
#    "TGTGTGTGTGTGTGTG",
#    "CATCATCATCATCATC",
#]

## Create SeqRecord objects for the new sequences and append to records
# for i, sequence in enumerate(new_sequences, start=len(records) + 1):
#    record_id = f"Sequence{i}"
#    record_description = f"Manually added sequence {i}"
#    new_record = SeqRecord(Seq(sequence), id=record_id, description=record_description)
#    records.append(new_record)

## Write the updated records back to the file
#with open(existing_file_path, "w") as file:
#    SeqIO.write(records, file, "fasta")
#
#print(f"Manually added ten sequences to {existing_file_path}")
#
# #Read the existing file
#records = list(SeqIO.parse(existing_file_path, "fasta"))
# #Reverse complement sequences from the third to thirteenth record in-place
#for i in range(2, 12):  # records are zero-indexed
#    records[i].seq = records[i].seq.reverse_complement()
#
## Write the updated records back to the same file
#with open(existing_file_path, "w") as file:
#    SeqIO.write(records, file, "fasta")
#################################################################################################
#################
#update the records from 15 to 24 and print part of them 
#def update_and_print_partial_sequences(file_path):
#    # Load the sequences from the file
#    records = list(SeqIO.parse(file_path, "fasta"))
#
#    # Update the IDs and descriptions for records 14 to 24
#    for i in range(14, 24):  # Indices are 0-based
#        records[i].id = f"NewID_{i + 1}"  # Modify the ID as needed
#        records[i].description = f"Updated Description for {records[i].id}"  # Modify the description as needed
#
#       
#
#    # Write the updated records back to the same file
#    SeqIO.write(records, file_path, "fasta")
#
#
# Call the function to update records and print partial sequences
##update_and_print_partial_sequences(existing_file_path)
###################################################################################
# Print the middle five records
##middle_records = records[14:24]  # Slice the records from index 13 to 24 (inclusive)
##for record in middle_records:
##    print(record.id)
##    print(record.seq[:10])
print("First five records:")
for record in records[:5]:
    print(record.id)
    print(record.seq)

# Print the last five records
print("\nLast five records:")
for record in records[-5:]:
    print(record.id)
    print(record.seq)

# Print the middle five records
print("\nMiddle five records:")
middle_start = (len(records) - 5) // 2
for record in records[middle_start:middle_start + 5]:
    print(record.id)
    print(record.seq)


record_ids = []
record_lengths = []
nucleotide_counts = {'A': [], 'C': [], 'G': [], 'T': []}

# Iterate through records and collect information
for record in records:
    # Record ID
    record_ids.append(record.id)
    
    # Record length
    record_lengths.append(len(record.seq))
    
    # Nucleotide counts
    counts = Counter(record.seq)
    nucleotide_counts['A'].append(counts['A'])
    nucleotide_counts['C'].append(counts['C'])
    nucleotide_counts['G'].append(counts['G'])
    nucleotide_counts['T'].append(counts['T'])
print('\n')
# Display the collected information
#print("Record ID\tLength\tA\tC\tG\tT")
#for i in range(len(records)):
#    print(f"{record_ids[i]}\t{record_lengths[i]}\t{nucleotide_counts['A'][i]}\t{nucleotide_counts['C'][i]}\t{nucleotide_counts['G'][i]}\t{nucleotide_counts['T'][i]}")    
data = {
    'Record ID': record_ids,
    'Length': record_lengths,
    'A': nucleotide_counts['A'],
    'C': nucleotide_counts['C'],
    'G': nucleotide_counts['G'],
    'T': nucleotide_counts['T']
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)
##excel_file_path = "C:/Users/Dana/Documents/projects/result.xlsx"
##df.to_excel(excel_file_path, index=False)
