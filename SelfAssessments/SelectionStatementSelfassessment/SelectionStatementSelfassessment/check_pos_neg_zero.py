# Program to check whether a number is positive, negative, or zero

# Take input from user
num = float(input("Enter a number: "))

# Check conditions using if-elif-else
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")