# Problem 72: Perform intersection of two sets

# Read first set elements
set1 = set(map(int, input("Enter first set elements: ").split()))

# Read second set elements
set2 = set(map(int, input("Enter second set elements: ").split()))

# Perform intersection operation
result = set1.intersection(set2)

# Print result
print("Intersection of sets:", result)



#output:
Enter first set elements: 1 2 3 4
Enter second set elements: 3 4 5 6
Intersection of sets: {3, 4}