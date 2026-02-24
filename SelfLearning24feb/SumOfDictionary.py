# Problem 85: Find sum of all dictionary values

# Read number of elements
n = int(input("Enter number of elements: "))

# Create empty dictionary
data = {}

# Input key-value pairs
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

# Initialize sum variable
total = 0

# Add all dictionary values
for value in data.values():
    total += value

# Print sum
print("Sum of all values:", total)



#output:
Enter number of elements: 3
Enter key: a
Enter value: 10
Enter key: b
Enter value: 20
Enter key: c
Enter value: 30
Sum of all values: 60