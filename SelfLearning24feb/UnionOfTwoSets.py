# Problem 71: Perform union of two sets

# Read first set elements
set1 = set(map(int, input("Enter first set elements: ").split()))

# Read second set elements
set2 = set(map(int, input("Enter second set elements: ").split()))

# Perform union operation
result = set1.union(set2)

# Print result
print("Union of sets:", result)



#output:
Enter first set elements: 1 2 3
Enter second set elements: 3 4 5
Union of sets: {1, 2, 3, 4, 5}