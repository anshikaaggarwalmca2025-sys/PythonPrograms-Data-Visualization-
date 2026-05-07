#program to calculate the sum of even numbers from 1 to N using while loop
# Read value of N
n = int(input("Enter a number: "))

# Initialize variables
i = 1
sum_even = 0

# Use while loop
while i <= n:
    
    # Check if number is even
    if i % 2 == 0:
        sum_even += i
    
    i += 1   # Increase counter

# Print result
print("Sum of even numbers:", sum_even)




#output:
Enter a number: 10
Sum of even numbers: 30

Enter a number: 15
Sum of even numbers: 56

Enter a number: 0
Sum of even numbers: 0