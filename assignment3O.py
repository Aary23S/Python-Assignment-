'''
Write a program to display following pattern
0
0 1
0 1 2
0 1 2 3
'''
for i in range(4):  
    for j in range(i + 1):  
        print(j, end=' ') 
    print() 