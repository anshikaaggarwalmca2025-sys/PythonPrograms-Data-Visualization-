# Function to calculate sum of digits
def sum_of_digits(n):
    total = 0
    
    # Convert number to positive if negative
    n = abs(n)
    
    # Loop until number becomes 0
    while n > 0:
        digit = n % 10       # Get last digit
        total += digit       # Add digit to total
        n = n // 10          # Remove last digit
    
    return total

# Read input from standard input
num = int(input())

# Call function and print result
print(sum_of_digits(num))



output:
4324
13