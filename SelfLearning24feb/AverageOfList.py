# Problem 63: Find average of list elements

# Read list elements
lst = list(map(int, input("Enter list elements: ").split()))

# Calculate sum
total = sum(lst)

# Calculate average
average = total / len(lst)

# Print average
print("Average of elements:", average)



#output:
Enter list elements: 10 20 30 40
Average of elements: 25.0