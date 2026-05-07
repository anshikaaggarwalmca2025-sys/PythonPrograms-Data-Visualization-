import numpy as np

# Generate 10 random numbers between 0 and 1
arr = np.random.rand(10)

# Normalize the array between 0 and 1
normalized = (arr - arr.min()) / (arr.max() - arr.min())

print("Original Array:\n", arr)
print("\nNormalized Array:\n", normalized)


#output

Original Array:

 [0.52796779 0.60934189 0.25675436 0.50746196 0.02298723 0.46193791
 0.28283417 0.26864338 0.41690985 0.86872655]

Normalized Array:

 [0.59708771 0.69330425 0.27640565 0.57284167 0.         0.51901416
 0.30724235 0.2904632  0.46577309 1.        ]