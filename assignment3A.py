'''
 Write a Python program to find those numbers which are 
 divisibleby 7 and multiple of 5,between 1500 and 2700(both included).
'''
 
numbers = []

for i in range(1500, 2701):
    if (i % 7 == 0) and (i % 5 == 0):
        numbers.append(i)

print("Numbers divisible by 7 and multiple of 5 between 1500 and 2700 are :\n",numbers)