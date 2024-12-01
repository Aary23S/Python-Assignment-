'''
Write a Python program to construct the following pattern,using a
nested for loop.

*
**
***
****
*****
****
***
**
*
'''

rows = 5

for i in range(1, rows + 1):
    print('*' * i)

for i in range(rows - 1, 0, -1):
    print('*' * i)