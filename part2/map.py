import sys
import os
import json
from collections import Counter

def count_words_in_file(file_number):
    # Construct the input and output file paths
    input_file_path = f"./titles/{file_number}.txt"
    output_file_path = f"./counts/count{file_number}.json"
    
    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print(f"Error: {input_file_path} does not exist.")
        return

    # Read the contents of the file
    with open(input_file_path, 'r') as file:
        text = file.read().lower()

    # Tokenize the text into words (split by whitespace)
    words = text.split()

    # Count the occurrences of each word
    word_count = Counter(words)

    # Write the word counts to the output JSON file
    with open(output_file_path, 'w') as json_file:
        json.dump(word_count, json_file, indent=4)

    print(f"Word counts saved to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_words.py <file_number>")
    else:
        file_number = sys.argv[1]
        count_words_in_file(file_number)
