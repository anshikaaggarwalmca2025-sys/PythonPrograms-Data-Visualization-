import numpy as np

# Create array from 1 to 25
arr = np.arange(1, 26)

# Reshape into 5×5 matrix
matrix = arr.reshape(5, 5)

# Extract the middle 3×3 sub-matrix
sub_matrix = matrix[1:4, 1:4]

print("5×5 Matrix:\n", matrix)
print("\nMiddle 3×3 Sub-matrix:\n", sub_matrix)


#output

5×5 Matrix:

 [[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]

Middle 3×3 Sub-matrix:

 [[ 7  8  9]
 [12 13 14]
 [17 18 19]]