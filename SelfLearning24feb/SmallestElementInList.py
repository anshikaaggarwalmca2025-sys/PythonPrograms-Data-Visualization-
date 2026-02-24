# Function to find smallest element in list
def find_smallest(lst):
    # Assume first element is smallest
    smallest = lst[0]
    
    # Loop through each element
    for num in lst:
        # Compare current element with smallest
        if num < smallest:
            smallest = num
    
    # Return smallest value
    return smallest

# Read list input (space-separated numbers)
numbers = list(map(int, input().split()))

# Call function and print result
print(find_smallest(numbers))



#output:
5432 5431 6541 
5431