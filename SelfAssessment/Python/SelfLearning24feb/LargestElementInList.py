# Function to find largest element in list
def find_largest(lst):
    largest = lst[0]   # Assume first element is largest
    
    # Compare with remaining elements
    for num in lst:
        if num > largest:
            largest = num
    
    return largest

# Read list input (space-separated numbers)
numbers = list(map(int, input().split()))

# Call function and print result
print(find_largest(numbers))



#output:
4 5 6 7
7
