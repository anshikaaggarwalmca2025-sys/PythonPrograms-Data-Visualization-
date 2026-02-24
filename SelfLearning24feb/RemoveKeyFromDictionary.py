# Problem 82: Safely remove a key from dictionary

# Read number of elements
n = int(input("Enter number of elements: "))

# Create dictionary
data = {}

# Input key-value pairs
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

# Read key to remove
remove_key = input("Enter key to remove: ")

# Safely remove key
if remove_key in data:
    del data[remove_key]
    print("Key removed successfully.")
else:
    print("Key not found.")

print("Updated Dictionary:", data)



#output:
Enter number of elements: 2
Enter key: a
Enter value: 10
Enter key: b
Enter value: 20
Enter key to remove: a
Key removed successfully.
Updated Dictionary: {'b': '20'}