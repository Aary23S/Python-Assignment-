'''
Write a Python program to print alphabet pattern 'Z'.

Expected Output:
*******
     *
    *
   *
  *
 *
*******

'''
# Program to print alphabet pattern 'Z'

# Number of rows for the 'Z' pattern
rows = 7

# Print the top horizontal line of 'Z'
print("*" * rows)

# Print the diagonal part of 'Z'
for i in range(rows - 2, 0, -1):
    print(" " * (i) + "*")

# Print the bottom horizontal line of 'Z'
print("*" * rows)
