#Program to calculate the total bill amount for notebooks and pens, and the remaining balance after payment
cost_notebook = 45
cost_pen = 20
quantity_notebooks = 3
quantity_pens = 2
amount_paid = 500
#Calculating total cost for notebooks and pens
totat_notebooks_cost = Quantity_notebooks * cost_notebooks
total_pens_cost = quantity_pens * cost_pen 
toatl_bill = toatl_notebooks_cost + total_pens_cost
print(f "Total bill amount : rs {total_bill}")
remaining_balance = amount_paid - toatl_bill
print(f "Amount paid : rs {amount_paid}")
print(f "Remaining balance : rs{remaining_balance}")