#program to normalise values of an array between 0 and 1
# Import NumPy library
import numpy as np  
# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# Normalise the array
# (arr - min) / (max - min)
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
# Print original and normalised arrays
print("Original Array:", arr)
print("Normalised Array:", normalized_arr)



#output
Original Array: [ 10  20  30  40  50  60  70  80  90 100]
Normalised Array: [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556 0.66666667 0.77777778 0.88888889 1.        ]   
