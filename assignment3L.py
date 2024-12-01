'''
Write a Python program to print alphabet pattern 'T'.
Expected Output:
*****
  *
  *
  *
  *
  *
  * 
'''
width = 5  
height = 7 

print('*' * width)

for i in range(1, height):
    print(' ' * (width // 2) + '*')