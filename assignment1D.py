# Input three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Check Pythagorean triplet
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("The given triplet is a Pythagorean triplet.")
else:
    print("The given triplet is NOT a Pythagorean triplet.")
