#program to reverse a number using while loop
# Read number from user
num = int(input("Enter a number: "))

# Store original number
original = num

# Make number positive (handle negative case)
num = abs(num)

# Initialize reverse variable
reverse = 0

# Reverse the number using while loop
while num > 0:
    digit = num % 10           # Get last digit
    reverse = reverse * 10 + digit
    num //= 10                 # Remove last digit

# Restore sign if original number was negative
if original < 0:
    reverse = -reverse

# Print reversed number
print("Reversed number is:", reverse)



#output
Enter a number: 1234
Reversed number is: 4321

Enter a number: -567
Reversed number is: -765

