'''
Write a program to display following pattern
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''
rows = 6  

for i in range(rows, 0, -1):  
    for j in range(i):  
        print('*', end=' ') 
    print()  