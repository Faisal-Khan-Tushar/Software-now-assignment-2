#ei file er sathe >env file ta add hoise toh delete korte hoile just oi duita delete korlei 
#hobe
import spacy

# Load the scispaCy model for detecting diseases and drugs
nlp = spacy.load("en_ner_bc5cdr_md")

# Input and output file paths
input_file_path = r"W:\VSCODE\Software Now Assessment 2\all_combined_texts.txt"
output_file_path = r"W:\VSCODE\Software Now Assessment 2\detected_diseases_drugs.txt"

# Read the input text file
with open(input_file_path, 'r') as file:
    text = file.read()

# Process the text with the scispaCy model
doc = nlp(text)

# Dictionary to store detected diseases and drugs for each HADM_ID
patient_data = {}

current_hadm_id = None

# Iterate through the detected entities
for ent in doc.ents:
    # Check if it's a HADM_ID
    if ent.label_ == "HADM_ID":
        current_hadm_id = ent.text
        if current_hadm_id not in patient_data:
            patient_data[current_hadm_id] = {'diseases': set(), 'drugs': set()}
    
    # Check if it's a disease or drug and add to the current patient's data
    if current_hadm_id:
        if ent.label_ == "DISEASE":
            patient_data[current_hadm_id]['diseases'].add(ent.text)
        elif ent.label_ == "DRUG":
            patient_data[current_hadm_id]['drugs'].add(ent.text)

# Write the output to the new text file
with open(output_file_path, 'w') as output_file:
    for hadm_id, data in patient_data.items():
        output_file.write(f"HADM_ID: {hadm_id}\n")
        output_file.write("Diseases:\n")
        for disease in data['diseases']:
            output_file.write(f" - {disease}\n")
        output_file.write("Drugs:\n")
        for drug in data['drugs']:
            output_file.write(f" - {drug}\n")
        output_file.write("\n")

print(f"Detection complete. Results saved to {output_file_path}")
