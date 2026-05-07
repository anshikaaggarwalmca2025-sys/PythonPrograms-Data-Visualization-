#program to calculate BMI category
# Read weight in kilograms
weight = float(input("Enter weight (kg): "))

# Read height in meters
height = float(input("Enter height (m): "))

# Calculate BMI using formula
bmi = weight / (height ** 2)

# Display BMI value
print("BMI:", round(bmi, 2))

# Determine BMI category
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("Normal Weight")
elif bmi >= 25 and bmi < 29.9:
    print("Overweight")
else:
    print("Obese")


#output:
Enter weight (kg): 70
Enter height (m): 1.75
BMI: 22.86
Normal Weight

Enter weight (kg): 50
Enter height (m): 1.75
BMI: 16.33
Underweight

Enter weight (kg): 80
Enter height (m): 1.75
BMI: 26.12
Overweight

Enter weight (kg): 95
Enter height (m): 1.75
BMI: 31.02
Obese