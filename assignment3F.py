'''
Write a Python program which accepts a sequence of comma
separated 4 digit binary numbers as its input and print the numbers that
are divisible by 5 in a comma separated sequence.

Sample Data: 0100,0011,1010,1001,1100,1001
Expected Output: 1010
'''

binary_numbers = input("Enter a sequence of 4-digit binary numbers separated by commas: ")
binary_list = binary_numbers.split(',')
result = []
for binary in binary_list:
    if int(binary, 2) % 5 == 0:
        result.append(binary)

print("Binary numbers divisible by 5:", ",".join(result))
