def count_the_occurrences():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
        
        word_list = content.split()
        the_count = sum(1 for word in word_list if word.lower() == "the")
        
        print(f"The word 'the' appears {the_count} times in the file.")
    except FileNotFoundError:
        print("The file 'notes.txt' does not exist. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_the_occurrences()