heart_rate_abnormal = input("Is heart rate abnormal? (yes/no): ")
severe_injury = input("Is there severe injury? (yes/no): ")
age = int(input("Enter patient age: "))
condition = input("Condition (moderate/normal): ")

if heart_rate_abnormal.lower() == "yes" or severe_injury.lower() == "yes":
    category = "Critical"
elif condition.lower() == "moderate":
    if age > 65:
        category = "Critical"
    else:
        category = "Moderate"
else:
    category = "Normal"

print("Patient Category:", category)
