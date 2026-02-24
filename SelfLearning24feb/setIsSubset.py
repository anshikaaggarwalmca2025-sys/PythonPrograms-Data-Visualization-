# Problem 74: Check whether one set is subset of another

# Read first set elements
set1 = set(map(int, input("Enter first set elements: ").split()))

# Read second set elements
set2 = set(map(int, input("Enter second set elements: ").split()))

# Check subset condition
if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")



#output:
    Enter first set elements: 1 2
Enter second set elements: 1 2 3 4
Set1 is a subset of Set2