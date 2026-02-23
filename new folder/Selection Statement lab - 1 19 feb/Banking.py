amount = float(input("Enter transaction amount: "))
account_age_months = int(input ("Enter account age in months: "))
is_international = input ("is the transaction international? (yes\no): ").lower() == "yes"
if amount > 200000 and account_age_months < 6 and is_international:
    print("Flagged: Manual verification required.")
else:
    print("Transaction approved.")    