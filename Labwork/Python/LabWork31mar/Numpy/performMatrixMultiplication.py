#program to perform matrix multiplication
# Import NumPy library
import numpy as np
# Create two 2D NumPy arrays (matrices)
matrix_a = np.array([[1, 2, 3],
                        [4, 5, 6]])
matrix_b = np.array([[7, 8],
                        [9, 10],
                        [11, 12]])
# Perform matrix multiplication
result = np.dot(matrix_a, matrix_b)
# Print the result
print("Result of Matrix Multiplication:")
print(result)



#output
Result of Matrix Multiplication:
[[ 58  64]
 [139 154]]