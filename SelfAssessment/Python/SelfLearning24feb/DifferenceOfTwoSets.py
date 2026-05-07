# Problem 73: Perform difference of two sets

# Read first set elements
set1 = set(map(int, input("Enter first set elements: ").split()))

# Read second set elements
set2 = set(map(int, input("Enter second set elements: ").split()))

# Perform difference (set1 - set2)
result = set1.difference(set2)

# Print result
print("Difference of sets (set1 - set2):", result)



#output:

Enter first set elements: 1 2 3 4
Enter second set elements: 3 4 5
Difference of sets (set1 - set2): {1, 2}