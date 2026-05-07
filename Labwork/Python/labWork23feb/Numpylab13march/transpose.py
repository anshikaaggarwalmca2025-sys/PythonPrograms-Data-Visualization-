import numpy as np

# Create a 3×3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate transpose
transpose_matrix = matrix.T

print("Original Matrix:\n", matrix)
print("\nTranspose Matrix:\n", transpose_matrix)


#output

Original Matrix:

 [[1 2 3]
 [4 5 6]
 [7 8 9]]

Transpose Matrix:

 [[1 4 7]
 [2 5 8]
 [3 6 9]]