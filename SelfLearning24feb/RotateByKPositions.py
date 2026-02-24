# Problem 61: Rotate a list by K positions

# Read list elements (space separated)
lst = list(map(int, input("Enter list elements: ").split()))

# Read value of K
k = int(input("Enter value of K: "))

# Handle cases where K is greater than list length
k = k % len(lst)

# Rotate list to the right by K positions
rotated_list = lst[-k:] + lst[:-k]

# Print rotated list
print("Rotated List:", rotated_list)




#output:
Enter list elements: 1 2 3 4 5
Enter value of K: 2
Rotated List: [4, 5, 1, 2, 3]