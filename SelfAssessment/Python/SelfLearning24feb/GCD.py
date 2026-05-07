#program to calculate GCD of two numbers using while loop
# Read two numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Make numbers positive
a = abs(a)
b = abs(b)

# Use Euclidean Algorithm
while b != 0:
    remainder = a % b
    a = b
    b = remainder

# When b becomes 0, a contains GCD
print("GCD is:", a)




#output:
Enter first number: 48
Enter second number: 18 
GCD is: 6

Enter first number: -56
Enter second number: 98
GCD is: 14