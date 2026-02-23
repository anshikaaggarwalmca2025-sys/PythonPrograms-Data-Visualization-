percentage = float(input("Enter 12th percentage: "))
maths = input("Studied Mathematics? (yes/no): ")
entrance_score = float(input("Enter entrance exam score: "))

if percentage < 75:
    print("Not Eligible: 12th percentage is below 75%.")
elif maths.lower() != "yes":
    print("Not Eligible: Mathematics not studied.")
elif entrance_score < 80:
    print("Not Eligible: Entrance exam score below 80.")
else:
    print("Eligible for admission.")
