balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

daily_limit = 50000

if withdraw_amount > daily_limit:
    print("Withdrawal failed: Exceeds daily limit of ₹50,000.")
elif withdraw_amount > balance:
    print("Withdrawal failed: Insufficient account balance.")
elif withdraw_amount > atm_cash:
    print("Withdrawal failed: ATM has insufficient cash.")
else:
    balance -= withdraw_amount
    print("Withdrawal successful.")
    print("Remaining balance: ₹", balance)
