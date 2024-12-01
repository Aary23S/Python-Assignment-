# Q. 1. Create user defined module for given problem and demonstrate use of
# import.
# • Create module named rectangle.py
# • Create two user defined functions named area and perimeter
# • Create testrectangle.py module and import rectangle.py module.

# this is the rectangle.py

def area(length, width):
    
    return length * width

def perimeter(length, width):
    
    return 2 * (length + width)