import numpy as np

# Create a 4×4 matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

# Row-wise sum
row_sum = matrix.sum(axis=1)

# Column-wise sum
col_sum = matrix.sum(axis=0)

print("Matrix:\n", matrix)
print("\nRow-wise Sum:", row_sum)
print("Column-wise Sum:", col_sum)


#output

Matrix:

 [[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]

Row-wise Sum:
 [10 26 42 58]

Column-wise Sum: [28 32 36 40]