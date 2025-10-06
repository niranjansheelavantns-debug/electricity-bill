
# electricity_bill.py

# Rate per unit
rate_per_unit = 75

# Ask user for units consumed
units = int(input("Enter the number of units consumed: "))

# Calculate total bill
total_bill = units * rate_per_unit

# Display the results
print("Units Consumed:", units)
print("Total Bill: ₹", total_bill)

# electricity_bill.py

# Rate per unit
rate_per_unit = 75

# Ask user for units consumed
units = int(input("Enter the number of units consumed: "))

# Calculate total bill
total_bill = units * rate_per_unit

print("Units Consumed:", units)
print("Total Bill: ₹", total_bill)

# Apply 10% discount if total bill exceeds ₹1000
if total_bill > 1000:
    discount = total_bill * 0.10
    final_bill = total_bill - discount
    print("Discount Applied: ₹", int(discount))
    print("Final Bill: ₹", int(final_bill))
else:
    print("No discount applied.")
    print("Final Bill: ₹", total_bill)
