# Problem 84: Create dictionary from two lists

# Read first list (keys)
keys = input("Enter keys (space separated): ").split()

# Read second list (values)
values = input("Enter values (space separated): ").split()

# Create dictionary manually
data = {}

# Ensure both lists have same length
if len(keys) == len(values):
    for i in range(len(keys)):
        data[keys[i]] = values[i]
    print("Created Dictionary:", data)
else:
    print("Error: Keys and values list must be of same length.")


#output:
Enter keys (space separated): a b c
Enter values (space separated): 10 20 30
Created Dictionary: {'a': '10', 'b': '20', 'c': '30'}    