#program to find the greatest of four numbers
# Read four numbers from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

# Assume first number is greatest initially
greatest = a

# Compare with second number
if b > greatest:
    greatest = b

# Compare with third number
if c > greatest:
    greatest = c

# Compare with fourth number
if d > greatest:
    greatest = d

# Print the greatest number
print("Greatest number is:", greatest)



#output:
Enter first number: 12
Enter second number: 45 
Enter third number: 30
Enter fourth number: 60
Greatest number is: 60

Enter first number: 5
Enter second number: 10 
Enter third number: 3
Enter fourth number: 8
Greatest number is: 10