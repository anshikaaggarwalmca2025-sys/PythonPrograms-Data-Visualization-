# Problem 70: Check whether tuple elements are unique

# Read tuple elements
tup = tuple(map(int, input("Enter tuple elements: ").split()))

# Convert tuple to set and compare lengths
if len(tup) == len(set(tup)):
    print("All elements are unique")
else:
    print("Tuple contains duplicate elements")


#output:
Enter tuple elements: 1 2 3 4 5
All elements are unique    