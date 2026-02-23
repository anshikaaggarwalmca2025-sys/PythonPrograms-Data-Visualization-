# Prices and quantities
notebook_price = 45
pen_price = 20

notebook_quantity = 3
pen_quantity = 2

# Calculating total cost
total_notebooks = notebook_price * notebook_quantity
total_pens = pen_price * pen_quantity
total_bill = total_notebooks + total_pens

# Amount given by customer
amount_given = 500

# Calculating remaining balance
remaining_balance = amount_given - total_bill

# Display results
print("Total bill amount: ₹", total_bill)
print("Remaining balance: ₹", remaining_balance)
