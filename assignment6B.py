def get_integer():
    try:
        # Prompt the user for input
        user_input = input("Enter an integer: ")
        
        # Attempt to convert the input to an integer
        user_number = int(user_input)

        # If conversion is successful, print the result
        print(f"You entered a valid integer: {user_number}")
    
    except ValueError:
        # Raise ValueError if the input is not a valid integer
        print(f"Error: '{user_input}' is not a valid integer.")

# Example usage
get_integer()