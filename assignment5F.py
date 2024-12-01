def count_uppercase_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            count = 0

            for line in file:
                for char in line:
                    if char.isupper():
                        count += 1

        return count

    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return 0

file_path = 'notes.txt'  
result = count_uppercase_characters(file_path)
print(f"Number of uppercase characters: {result}")