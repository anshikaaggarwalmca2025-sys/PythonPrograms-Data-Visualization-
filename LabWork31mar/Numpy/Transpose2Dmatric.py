# Program to transpose a 2D matrix using NumPy

# Import NumPy library
import numpy as np

# Create a 2D NumPy array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Transpose the matrix
# .T is used to convert rows into columns
transpose_matrix = matrix.T

# Print original matrix
print("Original Matrix:")
print(matrix)

# Print transposed matrix
print("Transposed Matrix:")
print(transpose_matrix)



#output
Original Matrix:
[[1 2 3]
 [4 5 6]]
Transposed Matrix:
[[1 4]
 [2 5]
 [3 6]]
