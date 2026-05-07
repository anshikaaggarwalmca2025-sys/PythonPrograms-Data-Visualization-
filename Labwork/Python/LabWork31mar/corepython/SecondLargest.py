# Program to find the second largest element in a list without using sort()

# Input list
numbers = [10, 25, 8, 40, 30]

# Initialize largest and second largest
largest = numbers[0]
second_largest = numbers[0]

# First find the largest element
for num in numbers:
    if num > largest:
        largest = num

# Now find second largest
for num in numbers:
    if num > second_largest and num != largest:
        second_largest = num

# Print result
print("Second Largest Element:", second_largest)


#output
Second Largest Element: 30