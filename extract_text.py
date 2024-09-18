import pandas as pd
from collections import defaultdict
import os

# Path to the directory containing the CSV files
directory_path = r'W:\VSCODE\Software Now Assessment 2'

# List of CSV file names
csv_files = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']

# Dictionary to store combined text for each HADM_ID
combined_texts = defaultdict(list)

# Process each CSV file
for file in csv_files:
    # Construct the full path to the CSV file
    file_path = os.path.join(directory_path, file)
    
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Check if the 'HADM_ID' and 'TEXT' columns exist in the dataframe
    if 'HADM_ID' in df.columns and 'TEXT' in df.columns:
        # Iterate through each row in the dataframe
        for _, row in df.iterrows():
            hadm_id = row['HADM_ID']
            text = row['TEXT']
            # Append the text to the corresponding HADM_ID
            combined_texts[hadm_id].append(text)

# Path for the single output text file
output_file_path = os.path.join(directory_path, 'all_combined_texts.txt')

# Write all texts to a single output file
with open(output_file_path, 'w') as outfile:
    for hadm_id, texts in combined_texts.items():
        # Combine texts for the current HADM_ID
        combined_text = ' '.join(texts)
        # Write the HADM_ID and the combined text to the file
        outfile.write(f"HADM_ID {hadm_id}:\n{combined_text}\n\n")

print(f"All combined texts stored in {output_file_path}")





