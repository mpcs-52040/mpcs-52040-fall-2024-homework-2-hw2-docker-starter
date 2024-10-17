import os
import json
from collections import Counter

def combine_word_counts(directory):
    combined_counts = Counter()

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)

            # Open each JSON file and update the combined word counts
            with open(file_path, 'r') as json_file:
                word_counts = json.load(json_file)
                combined_counts.update(word_counts)

    return combined_counts

def save_combined_counts(output_file, combined_counts):
    # Write the combined word counts to the output JSON file
    with open(output_file, 'w') as json_file:
        json.dump(combined_counts, json_file, indent=4)
    print(f"Combined word counts saved to {output_file}")

if __name__ == "__main__":
    counts_directory = '/counts'
    output_file = '/counts/total_counts.json'

    # Combine the word counts from all JSON files in the directory
    combined_counts = combine_word_counts(counts_directory)

    # Save the combined word counts to the output JSON file
    save_combined_counts(output_file, combined_counts)
