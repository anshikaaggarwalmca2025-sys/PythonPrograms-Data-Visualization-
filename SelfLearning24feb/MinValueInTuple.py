# Problem 67: Find minimum value in a tuple

# Read tuple elements (space separated)
tup = tuple(map(int, input("Enter tuple elements: ").split()))

# Assume first element is minimum
minimum = tup[0]

# Traverse tuple to find minimum
for num in tup:
    if num < minimum:
        minimum = num

# Print minimum value
print("Minimum value:", minimum)


#output:
Enter tuple elements: 10 25 5 40 15
Minimum value: 5