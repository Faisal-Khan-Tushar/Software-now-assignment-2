import transformers

def count_unique_tokens(text_file_path):
  """Counts unique tokens in a text file using the AutoTokenizer function from the Transformers library.

  Args:
    text_file_path: The path to the text file.

  Returns:
    A list of tuples, where each tuple contains a token and its count. The list is sorted in descending order by count.
  """

  # Load the AutoTokenizer
  tokenizer = transformers.AutoTokenizer.from_pretrained("bert-base-uncased")

  # Read the text from the file
  with open(text_file_path, "r") as f:
    text = f.read()

  # Tokenize the text
  tokens = tokenizer.tokenize(text)

  # Count the frequency of each token
  token_counts = {}
  for token in tokens:
    token_counts[token] = token_counts.get(token, 0) + 1

  # Sort the token counts by frequency in descending order
  sorted_token_counts = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)

  return sorted_token_counts[:30]

# Example usage
text_file_path = "W:\\VSCODE\\Software Now Assessment 2\\all_combined_texts.txt"
top_30_tokens = count_unique_tokens(text_file_path)

# Print the top 30 tokens
for token, count in top_30_tokens:
  print(f"{token}: {count}")