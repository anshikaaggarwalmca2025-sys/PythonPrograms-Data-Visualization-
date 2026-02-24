# Problem 81: Find key with maximum value

# Read number of elements
n = int(input("Enter number of elements: "))

# Create dictionary
data = {}

# Input key-value pairs
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

# Assume first key has maximum value
max_key = list(data.keys())[0]
max_value = data[max_key]

# Find key with maximum value
for key in data:
    if data[key] > max_value:
        max_value = data[key]
        max_key = key

print("Key with maximum value:", max_key)
print("Maximum value:", max_value)


#output:
Enter number of elements: 3
Enter key: Asha
Enter value: 85
Enter key: Ravi
Enter value: 92
Enter key: Neha
Enter value: 88
Key with maximum value: Ravi
Maximum value: 92