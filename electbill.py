
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
