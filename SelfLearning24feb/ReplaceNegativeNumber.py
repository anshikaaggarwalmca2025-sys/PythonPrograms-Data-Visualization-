# Problem 64: Replace negative numbers with zero

# Read list elements
lst = list(map(int, input("Enter list elements: ").split()))

# Replace negative numbers with 0
for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0

# Print updated list
print("Updated List:", lst)


#output
Enter list elements: 5 -3 8 -1 2
Updated List: [5, 0, 8, 0, 2]