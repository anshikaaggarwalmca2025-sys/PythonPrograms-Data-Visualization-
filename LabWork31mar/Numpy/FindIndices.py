# Program to find indices of elements greater than a given value

# Import NumPy
import numpy as np

# Create array
arr = np.array([10, 25, 30, 5, 18])

# Given value
value = 20

# Find indices
indices = np.where(arr > value)

# Print results
print("Array:", arr)
print("Indices of elements greater than", value, ":", indices)



#output
Array: [10 25 30  5 18]
Indices of elements greater than 20: (array([1, 2]),)