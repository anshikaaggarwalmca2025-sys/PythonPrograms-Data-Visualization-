# Recursive function to calculate power
def power(base, exponent):
    # Base condition
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# Read input from standard input
base = int(input())
exponent = int(input())

# Call function and print result
print(power(base, exponent))




#output:
3
4
81
