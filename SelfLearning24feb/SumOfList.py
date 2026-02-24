# Problem 62: Find sum of list elements

# Read list elements
lst = list(map(int, input("Enter list elements: ").split()))

# Initialize sum variable
total = 0

# Add each element to total
for num in lst:
    total += num

# Print sum
print("Sum of elements:", total)



#output
Enter list elements: 10 20 30 40
Sum of elements: 100