#program to count digits in a number
# Read number from user
num = int(input("Enter a number: "))

# Make number positive
num = abs(num)

# Initialize counter
count = 0

# Special case for 0
if num == 0:
    count = 1
else:
    # Count digits using while loop
    while num > 0:
        num //= 10   # Remove last digit
        count += 1   # Increase counter

# Print result
print("Number of digits:", count)



#output:
Enter a number: 1234
Number of digits: 4

Enter a number: -567
Number of digits: 3

Enter a number: 0
Number of digits: 1