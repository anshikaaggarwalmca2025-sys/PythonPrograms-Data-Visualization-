# Function to calculate factorial
def factorial(n):
    result = 1
    
    # If number is negative
    if n < 0:
        return "Factorial does not exist for negative numbers"
    
    # Loop from 1 to n
    for i in range(1, n + 1):
        result = result * i
    
    return result

# Read input from standard input
num = int(input())

# Call function and print result
print(factorial(num))



#output:
Enter a number: 43
43 is a Prime number