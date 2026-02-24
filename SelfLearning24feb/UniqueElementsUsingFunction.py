# Function to return unique elements from list
def unique_elements(lst):
    unique_list = []
    
    # Loop through list
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

# Read list input (space-separated numbers)
numbers = list(map(int, input().split()))

# Call function and print result
print(unique_elements(numbers))



#output:
3
[3]