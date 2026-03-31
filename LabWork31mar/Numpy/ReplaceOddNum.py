# Program to replace all odd numbers in a NumPy array with -1

# Import NumPy
import numpy as np

# Create NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Replace odd numbers with -1
# arr % 2 != 0 checks for odd numbers
arr[arr % 2 != 0] = -1

# Print modified array
print("Modified Array:", arr)



#output
Modified Array: [-1  2 -1  4 -1  6 -1]