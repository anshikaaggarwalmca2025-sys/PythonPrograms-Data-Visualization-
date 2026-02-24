# Function to separate even and odd numbers
def separate_even_odd(lst):
    even = []
    odd = []
    
    # Loop through each element
    for num in lst:
        if num % 2 == 0:
            even.append(num)   # Add to even list
        else:
            odd.append(num)    # Add to odd list
    
    return even, odd

# Read input (space-separated numbers)
numbers = list(map(int, input().split()))

# Call function
even_list, odd_list = separate_even_odd(numbers)

# Print result
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)



#output:
2 3 4 5 6 7 8 
Even numbers: [2, 4, 6, 8]
Odd numbers: [3, 5, 7]