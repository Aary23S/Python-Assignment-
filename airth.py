# AIRT_OP/airth.py

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def sub(a, b):
    """Returns the difference between two numbers."""
    return a - b

def mul(a, b):
    """Returns the product of two numbers."""
    return a * b

def div(a, b):
    """Returns the division of two numbers."""
    if b == 0:
        return "Division by zero is not allowed."
    return a / b
