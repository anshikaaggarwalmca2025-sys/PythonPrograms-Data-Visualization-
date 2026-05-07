# Problem 78: Merge two dictionaries manually

# Read size of first dictionary
n1 = int(input("Enter number of elements in first dictionary: "))
dict1 = {}

# Input key-value pairs for first dictionary
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

# Read size of second dictionary
n2 = int(input("Enter number of elements in second dictionary: "))
dict2 = {}

# Input key-value pairs for second dictionary
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

# Manually merge dictionaries
merged = {}

# Add elements from first dictionary
for key in dict1:
    merged[key] = dict1[key]

# Add elements from second dictionary
for key in dict2:
    merged[key] = dict2[key]

# Print merged dictionary
print("Merged Dictionary:", merged)


#output:
Enter number of elements in first dictionary: 2
Enter key: a
Enter value: 10
Enter key: b
Enter value: 20
Enter number of elements in second dictionary: 2
Enter key: c
Enter value: 30
Enter key: d
Enter value: 40
Merged Dictionary: {'a': '10', 'b': '20', 'c': '30', 'd': '40'}