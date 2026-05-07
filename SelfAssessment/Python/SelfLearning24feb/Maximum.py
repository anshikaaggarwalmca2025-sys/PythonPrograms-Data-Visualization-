# Function to find maximum of three numbers
def find_max(a, b, c):
    # Compare numbers using conditional statements
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Read input from standard input
a = int(input())
b = int(input())
c = int(input())

# Call function and print result
print(find_max(a, b, c))



output
345
543
654
654