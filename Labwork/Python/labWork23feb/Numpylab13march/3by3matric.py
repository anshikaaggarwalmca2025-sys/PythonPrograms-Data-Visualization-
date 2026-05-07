import numpy as np

# Create two 3×3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrix multiplication
result = np.matmul(A, B)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Result of A * B:\n", result)


#output

Matrix A:

 [[1 2 3]
 [4 5 6]
 [7 8 9]]
Matrix B:

 [[9 8 7]
 [6 5 4]
 [3 2 1]]
Result of A * B:

 [[ 30  24  18]
 [ 84  69  54]
 [138 114  90]]