def divide_numbers():
    try:
        # Take input from the user
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        # Perform division
        result = numerator / denominator

        # Display result
        print(f"The result of division is: {result}")

    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Division by zero is not allowed.")

    except ValueError:
        # Handle invalid input error
        print("Error: Please enter valid numbers.")

divide_numbers()