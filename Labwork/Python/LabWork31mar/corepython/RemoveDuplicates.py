# Program to remove duplicates from a list while keeping order same

# Input list
numbers = [1, 2, 2, 3, 4, 3, 5, 1]

# Empty list to store unique elements
unique_list = []

# Loop through the list
for num in numbers:
    
    # If element is not already in unique_list
    if num not in unique_list:
        unique_list.append(num)

# Print list without duplicates
print("List without duplicates:", unique_list)



#output
List without duplicates: [1, 2, 3, 4, 5]