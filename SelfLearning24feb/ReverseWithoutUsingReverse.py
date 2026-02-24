# Function to reverse list
def reverse_list(lst):
    reversed_list = []
    
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    
    return reversed_list

numbers = list(map(int, input().split()))
print(reverse_list(numbers))



#output:
1 2 3 4 2 1 5 6 
[6, 5, 1, 2, 4, 3, 2, 1]