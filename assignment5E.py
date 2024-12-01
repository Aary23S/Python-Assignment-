def count_words_ending_with_e(file_path):
    try:
        with open(file_path, 'r') as file:
            count = 0

            for line in file:
                words = line.split()

                for word in words:
                    if word.lower().endswith('e'):
                        count += 1

        return count

    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return 0


file_path = 'poem.txt' 
result = count_words_ending_with_e(file_path)
print(f"Number of words ending with 'e': {result}")