#program to find factorial using while loop
# Read number from user
num = int(input("Enter a number: "))

# Initialize factorial as 1
fact = 1

# Store original number for display
original = num

# Check if number is negative
if num < 0:
    print("Factorial does not exist for negative numbers")

else:
    # Calculate factorial using while loop
    while num > 0:
        fact = fact * num
        num -= 1   # Decrease number by 1
    
    # Print result
    print("Factorial is:", fact)



#output:
Enter a number: 5
Factorial is: 120

Enter a number: -3
Factorial does not exist for negative numbers

Enter a number: 0
Factorial is: 1