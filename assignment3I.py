'''
Write a Python program to print alphabet pattern 'U'.
ExpectedOutput:
*     *
*     *
*     *
*     *
*     *
*     *
  ***

'''


height = 7  
width = 7 

for i in range(height - 1):
    print('*' + ' ' * (width - 2) + '*')

print(' ' * 2 + '*' * 3)
