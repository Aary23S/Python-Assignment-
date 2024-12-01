# Write a function in Python to count the words "this" and" these" present in a text file "article.txt". 
# [Note that the words "this" and "these" are complete words]

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()  
            words = content.split()  
            count_this = words.count("this")
            count_these = words.count("these")
            
            print(f"'this': {count_this}")
            print(f"'these': {count_these}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_words_in_file("article.txt")