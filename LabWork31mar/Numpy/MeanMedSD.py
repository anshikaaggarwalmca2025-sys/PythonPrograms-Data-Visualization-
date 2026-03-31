# Program to find mean, median, and standard deviation using NumPy

# Import NumPy library
import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Calculate mean
mean_value = np.mean(arr)

# Calculate median
median_value = np.median(arr)

# Calculate standard deviation
std_value = np.std(arr)

# Print results
print("Array:", arr)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_value)



#output
Array: [10 20 30 40 50]
Mean: 30.0
Median: 30.0
Standard Deviation: 14.142135623730951
