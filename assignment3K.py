'''
Write a Python program to create the multiplication
table(from1to10) of a number
'''

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, 'x', i, '=', number * i)