# Program to flatten a nested list

# Nested list
nested_list = [[1, 2], [3, 4], [5, 6]]

# Empty list to store flattened elements
flat_list = []

# Loop through each sublist
for sublist in nested_list:
    
    # Loop through each element in sublist
    for item in sublist:
        flat_list.append(item)

# Print flattened list
print("Flattened List:", flat_list)



#output
Flattened List: [1, 2, 3, 4, 5, 6]