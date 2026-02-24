# Problem 79: Sort dictionary by keys

# Read number of elements
n = int(input("Enter number of elements: "))

# Create dictionary
data = {}

# Input key-value pairs
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

# Sort dictionary by keys
sorted_keys = sorted(data.keys())

print("Dictionary sorted by keys:")
for key in sorted_keys:
    print(key, ":", data[key])


#output:
Enter number of elements: 3
Enter key: b
Enter value: 20
Enter key: a
Enter value: 10
Enter key: c
Enter value: 30
Dictionary sorted by keys:
a : 10
b : 20
c : 30    