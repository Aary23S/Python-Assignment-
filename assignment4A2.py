# testrectangle.py

# Importing the rectangle module
import assignment4A
# Input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Using the area and perimeter functions from the rectangle module
rect_area = assignment4A.area(length, width)
rect_perimeter = assignment4A.perimeter(length, width)

# Displaying the results
print(f"Area of the rectangle: {rect_area}")
print(f"Perimeter of the rectangle: {rect_perimeter}")