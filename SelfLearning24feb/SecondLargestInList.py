# Function to find second largest element
def second_largest(lst):
    first = second = float('-inf')
    
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second

numbers = list(map(int, input().split()))
print(second_largest(numbers))



#output:
1 3 4 2 5 6 
5