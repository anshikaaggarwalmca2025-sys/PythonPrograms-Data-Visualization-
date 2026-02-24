# Function to merge two lists and remove duplicates
def merge_lists(lst1, lst2):
    merged = lst1 + lst2
    unique_list = []
    
    for item in merged:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

print(merge_lists(list1, list2))



#output:
23 43 52 23 65 34 43
34 45 65 76 87 23 43
[23, 43, 52, 65, 34, 45, 76, 87]