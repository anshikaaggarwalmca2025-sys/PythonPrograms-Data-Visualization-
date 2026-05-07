# Problem 66: Find maximum value in a tuple

# Read tuple elements (space separated)
tup = tuple(map(int, input("Enter tuple elements: ").split()))

# Assume first element is maximum
maximum = tup[0]

# Traverse tuple to find maximum
for num in tup:
    if num > maximum:
        maximum = num

# Print maximum value
print("Maximum value:", maximum)



#output
Enter tuple elements: 10 25 5 40 15
Maximum value: 40