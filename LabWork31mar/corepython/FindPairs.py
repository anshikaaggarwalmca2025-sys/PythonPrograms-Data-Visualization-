# Program to find all pairs whose sum equals a target value

# Input list
numbers = [2, 4, 3, 5, 7, 8]

# Target value
target = 9

# Empty list to store pairs
pairs = []

# Loop through list
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        
        # Check if sum equals target
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

# Print result
print("Pairs with sum", target, ":", pairs)



#output
Pairs with sum 9 : [(2, 7), (4, 5)]