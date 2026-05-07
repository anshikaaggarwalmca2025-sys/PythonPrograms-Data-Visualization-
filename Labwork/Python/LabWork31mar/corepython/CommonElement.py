# Program to find common elements between two lists

# Input lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9]

# Empty list to store common elements
common = []

# Check each element of list1 in list2
for item in list1:
    if item in list2:
        common.append(item)

# Print result
print("Common Elements:", common)



#output
Common Elements: [3, 5]