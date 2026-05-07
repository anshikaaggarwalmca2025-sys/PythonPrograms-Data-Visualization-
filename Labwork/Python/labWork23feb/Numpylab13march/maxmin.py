#Create a 5×5 matrix with random integers between 1 and 100 and find:
#• Minimum value
#• Maximum value

import numpy as np

matrix = np.random.randint(1, 101, (5,5))
print(matrix)

print("Minimum value:", matrix.min())
print("Maximum value:", matrix.max())

#output

[[ 73  73  81  13  13]
 [ 75 100  44  89  44]
 [ 77  73  88  99  49]
 [ 47  40  65  53  64]
 [ 74   1  82  47  48]]
Minimum value: 1

Maximum value: 100
