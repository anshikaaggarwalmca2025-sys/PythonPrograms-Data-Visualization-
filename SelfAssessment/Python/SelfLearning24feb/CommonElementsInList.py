# Function to find common elements
def common_elements(lst1, lst2):
    common = []
    
    # Loop through first list
    for item in lst1:
        if item in lst2 and item not in common:
            common.append(item)
    
    return common

# Read first list
list1 = list(map(int, input().split()))

# Read second list
list2 = list(map(int, input().split()))

# Call function and print result
print(common_elements(list1, list2))


#output:
1 2 3 4 5 6 7 8 9 1 24 1 1 1 2  2 2
1 2 3 4  6 7 8 76 43 21 23 45 67 87
[1, 2, 3, 4, 6, 7, 8]