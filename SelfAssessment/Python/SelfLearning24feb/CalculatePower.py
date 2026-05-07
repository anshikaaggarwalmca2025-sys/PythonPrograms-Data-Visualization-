#program to calculate power without using exponent operator

# Read base and exponent from user
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = 1

# Multiply base exponent number of times
for i in range(exponent):
    result = result * base

# Print result
print("Result:", result)




#output:
Enter base: 3
Enter exponent: 4
Result: 81