# Problem 83: Check whether key exists in dictionary

# Read number of elements
n = int(input("Enter number of elements: "))

# Create dictionary
data = {}

# Input key-value pairs
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

# Read key to check
check_key = input("Enter key to check: ")

# Check if key exists
if check_key in data:
    print("Key exists in dictionary.")
else:
    print("Key does not exist in dictionary.")



#output:
Enter number of elements: 2
Enter key: x
Enter value: 100
Enter key: y
Enter value: 200
Enter key to check: x
Key exists in dictionary.    