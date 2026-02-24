# Program to find factorial of a number using for loop

# Taking input
n = int(input("Enter a number: "))

factorial = 1

# Loop from 1 to n
for i in range(1, n + 1):
    factorial *= i  # Multiply each number

print("Factorial of", n, "is:", factorial)



#output:
Enter a number: 5
factorial of 5 is: 120
