# Function to sort list using Bubble Sort
def sort_list(lst):
    n = len(lst)
    
    # Outer loop for passes
    for i in range(n):
        # Inner loop for comparison
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap elements
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst

# Read input (space-separated values)
numbers = list(map(int, input().split()))

# Call function and print result
print(sort_list(numbers))



#output:
5 2 8 1 3
[1, 2, 3, 5, 8]