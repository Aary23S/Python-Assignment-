def display_poem():
    try:
        with open("poem.txt", "r") as file:
            for line in file:
                print(line.strip())  # Using strip() to remove any extra whitespace or newline characters
    except FileNotFoundError:
        print("The file 'poem.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
display_poem()