# Function to remove duplicates from list
def remove_duplicates(lst):
    unique_list = []
    
    # Loop through each element
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

# Read input (space-separated values)
numbers = list(map(int, input().split()))

# Call function and print result
print(remove_duplicates(numbers))




#output:
3 4 5 6 3 4 5 2 1
[3, 4, 5, 6, 2, 1]