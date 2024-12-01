'''
Write a Python program to find numbers between 100 and
400 (bothincluded)where each digit of a number is an even
number.The numbers obtained should be printed in a commaseparated sequence
'''


def all_digits_even(number):
    return all(int(digit) % 2 == 0 for digit in str(number))

# Find even digit numbers between 100 and 400
even_digit_numbers = [num for num in range(100, 401) if all_digits_even(num)]

# Print the result as a comma-separated sequence
print("Numbers with all even digits:", ', '.join(map(str, even_digit_numbers)))