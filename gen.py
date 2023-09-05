import itertools
import random

# Function to read words from a file
def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file]
    return words

# Function to generate combinations and write them to a file
def generate_combinations_and_write_file(words, output_file_path, num_combinations):
    if len(words) < 12:
        print("Error: There are not enough words in the input file to generate 12-word combinations.")
        return

    with open(output_file_path, 'w') as output_file:
        combination_count = 0
        while combination_count < num_combinations:
            random.shuffle(words)  # Shuffle the words randomly
            combo = words[:12]  # Take the first 12 shuffled words
            combo_str = ' '.join(combo)
            output_file.write(combo_str + '\n')
            combination_count += 1

if __name__ == "__main__":
    input_file_path = "words.txt"  # Change this to your input file path
    output_file_path = "combinations.txt"  # Change this to your output file path
    num_combinations = 5000000  # Number of combinations to generate and export

    words = read_words_from_file(input_file_path)

    generate_combinations_and_write_file(words, output_file_path, num_combinations)

    print(f"{num_combinations} combinations have been generated and saved to {output_file_path}")

