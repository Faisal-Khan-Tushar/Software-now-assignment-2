# Importing required libraries
from collections import Counter
import csv

# Defining the file path for the text file
file_path = r'W:\VSCODE\Software Now Assessment 2\all_combined_texts.txt'

# Opening and reading the content of the text file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Splitting the text into individual words and counting their occurrences
word_count = Counter(text.split())

# Extracting the top 30 most common words along with their counts
top_30_common_words = word_count.most_common(30)

# Defining the output CSV file path
csv_file_path = r'W:\VSCODE\Software Now Assessment 2\top_30_common_words.csv'

# Writing the top 30 common words and their counts into the CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    # Creating the CSV writer object
    writer = csv.writer(csvfile)
    
    # Writing the header row
    writer.writerow(['Word', 'Count'])
    
    # Writing the top 30 common words and their counts
    writer.writerows(top_30_common_words)

# Printing completion message
print("Top 30 common words have been written to the CSV file successfully.")
