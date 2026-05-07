# Program to count digits in a number

num = 98765
count = 0

while num > 0:
    num = num // 10  # Remove last digit
    count += 1       # Increase counter

print("Number of digits:", count)