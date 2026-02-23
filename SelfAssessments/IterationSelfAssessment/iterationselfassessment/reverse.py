# Program to reverse a number using while loop

num = 1234
reverse = 0

while num > 0:
    digit = num % 10       # Get last digit
    reverse = reverse * 10 + digit
    num = num // 10        # Remove last digit

print("Reversed Number:", reverse)