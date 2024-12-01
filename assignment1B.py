# Input number of units
units = float(input("Enter the number of electricity units consumed: "))

# Calculate bill
if units <= 100:
    bill = units * 5  # Rs. 5 per unit
elif units <= 300:
    bill = 100 * 5 + (units - 100) * 7  # Rs. 7 per unit for next 200 units
else:
    bill = 100 * 5 + 200 * 7 + (units - 300) * 10  # Rs. 10 per unit after 300 units

print(f"Your electricity bill is: Rs. {bill}")
