# Program to extract diagonal elements from a matrix using NumPy

# Import NumPy
import numpy as np

# Create a 2D NumPy array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Extract diagonal elements
diagonal = np.diag(matrix)

# Print results
print("Matrix:")
print(matrix)

print("Diagonal Elements:", diagonal)


#output
Matrix:
[[1 2 3]    
 [4 5 6]
 [7 8 9]]   
Diagonal Elements: [1 5 9]    