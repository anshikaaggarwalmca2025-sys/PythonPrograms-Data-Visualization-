# Problem 80: Sort dictionary by values

# Read number of elements
n = int(input("Enter number of elements: "))

# Create dictionary
data = {}

# Input key-value pairs
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

# Sort dictionary by values
sorted_items = sorted(data.items(), key=lambda x: x[1])

print("Dictionary sorted by values:")
for key, value in sorted_items:
    print(key, ":", value)



#output:
Enter number of elements: 3
Enter key: a
Enter value: 30
Enter key: b
Enter value: 10
Enter key: c
Enter value: 20
Dictionary sorted by values:
b : 10
c : 20
a : 30    