# Function to find GCD using Euclidean Algorithm
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b   # Swap and find remainder
    return a

# Read input from standard input
num1 = int(input())
num2 = int(input())

# Call function and print result
print(find_gcd(num1, num2))




#output:
3
4
1