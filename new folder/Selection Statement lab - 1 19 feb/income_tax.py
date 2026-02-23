age = int(input("Enter age: "))
income = float(input("Enter annual income: "))
#set exemption limit
exemption_limit = 300000 if age >= 60 else 250000
tax = 0
if income <= exemtion_limit:
    tax = 0
elif income <= 500000:
    tax = (income - exemption_limit) * 0.05
elif income <= 1000000:
    tax = (500000 - exemption_limit) * 0.05 + (income - 500000) * 0.20
else:
    tax = (500000 - exemption_limit) * 0.05 + (500000 * 0.20) + (income - 1000000) * 0.30
print(f"Total Income Tax: rs{tax}")            