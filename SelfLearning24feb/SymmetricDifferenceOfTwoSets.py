# Problem 75: Find symmetric difference of two sets

# Read first set elements
set1 = set(map(int, input("Enter first set elements: ").split()))

# Read second set elements
set2 = set(map(int, input("Enter second set elements: ").split()))

# Perform symmetric difference
result = set1.symmetric_difference(set2)

# Print result
print("Symmetric Difference of sets:", result)



#output:
Enter first set elements: 1 2 3
Enter second set elements: 3 4 5
Symmetric Difference of sets: {1, 2, 4, 5}