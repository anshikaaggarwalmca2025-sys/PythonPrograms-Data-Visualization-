# Program to check whether a year is a leap year

year = int(input("Enter year: "))

# Leap year condition:
# 1. Divisible by 4 AND not divisible by 100
# OR
# 2. Divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")