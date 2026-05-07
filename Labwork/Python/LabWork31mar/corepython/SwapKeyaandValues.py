# Program to swap keys and values in a dictionary

# Input dictionary
data = {"A": 1, "B": 2, "C": 3}

# Create an empty dictionary for swapped values
swapped = {}

# Loop through dictionary items
for key, value in data.items():
    
    # Assign value as key and key as value
    swapped[value] = key

# Print the swapped dictionary
print("Swapped Dictionary:", swapped)



#output
Swapped Dictionary: {1: 'A', 2: 'B', 3: 'C'}