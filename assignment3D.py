'''Write a Python program that prints all the numbers from 0 to 7 except 3 and
   Note:Use 'continue' statement.

   Expected Output: 012457
'''
for num in range(8):
    if num == 3 or num == 6:
        continue
    print(num, end="")