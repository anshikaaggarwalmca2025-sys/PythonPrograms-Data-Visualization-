# Program to check if a number is divisible by both 5 and 11

num = int(input("Enter a number: "))

# Check divisibility condition
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")