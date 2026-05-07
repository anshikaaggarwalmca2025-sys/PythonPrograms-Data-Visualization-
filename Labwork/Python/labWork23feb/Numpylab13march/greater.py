import numpy as np

# Create array from 1 to 15
arr = np.arange(1, 16)

# Find numbers greater than 10
result = arr[arr > 10]

print("Array:", arr)
print("Numbers greater than 10:", result)


#output

Array: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]

Numbers greater than 10: [11 12 13 14 15]