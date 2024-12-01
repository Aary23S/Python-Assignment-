def count_words_in_poem():
    try:
        with open('poem.txt', 'r') as file:
            content = file.read()  # Read the file content
            words = content.split()  # Split the content into words
            word_count = len(words)  # Count the words
            print(f"The file 'poem.txt' contains {word_count} words in it.")
    except FileNotFoundError:
        print("Error: The file 'poem.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
count_words_in_poem()