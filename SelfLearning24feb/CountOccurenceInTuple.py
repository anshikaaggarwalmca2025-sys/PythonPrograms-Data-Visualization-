# Problem 69: Count occurrence of element in tuple

# Read tuple elements
tup = tuple(map(int, input("Enter tuple elements: ").split()))

# Read element to count
element = int(input("Enter element to count: "))

# Initialize counter
count = 0

# Traverse tuple and count occurrences
for num in tup:
    if num == element:
        count += 1

# Print count
print("Occurrence of", element, ":", count)



#output:
Enter tuple elements: 1 2 3 2 4 2 5
Enter element to count: 2
Occurrence of 2 : 3