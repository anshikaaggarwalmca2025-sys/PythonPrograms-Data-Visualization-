credit_score = int(input("Enter credit score: "))
income = float(input("Enter monthly income: "))
existing_loan = float(input("Enter existing loan amount: "))

if credit_score < 600:
    print("Loan Rejected: Credit score too low.")
elif 600 <= credit_score <= 750:
    if income < 30000 and existing_loan > 500000:
        print("Loan Rejected: Low income and high existing loan.")
    else:
        print("Loan requires further income verification.")
else:  # credit_score > 750
    if income < 30000 and existing_loan > 500000:
        print("Loan Rejected: Low income and high existing loan.")
    else:
        print("Loan Approved.")
