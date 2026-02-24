# Function to count frequency of elements
def count_frequency(lst):
    frequency = {}
    
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    return frequency

numbers = list(map(int, input().split()))
print(count_frequency(numbers))



#output:
2 3 4 5 6
{2: 1, 3: 1, 4: 1, 5: 1, 6: 1}