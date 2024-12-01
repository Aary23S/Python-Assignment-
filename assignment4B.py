#assignment4B.py

# Importing the airth module from the AIRT_OP package
from AIRT_OP import airth

# Testing the arithmetic functions
if __name__ == "__main__":
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    print(f"Addition: {airth.add(x, y)}")
    print(f"Subtraction: {airth.sub(x, y)}")
    print(f"Multiplication: {airth.mul(x, y)}")
    print(f"Division: {airth.div(x, y)}")
