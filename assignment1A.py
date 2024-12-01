# Input sides of the triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check type of triangle
if a == b and b == c:
    print("The triangle is Equilateral.")
elif a == b or b == c or a == c:
    # Check if any two sides are equal
    if a == b or b == c or a == c:
        print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")
