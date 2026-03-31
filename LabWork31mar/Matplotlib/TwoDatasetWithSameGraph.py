# Program to plot two datasets on the same graph

import matplotlib.pyplot as plt

# Dataset 1
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

# Dataset 2
y2 = [1, 3, 5, 7, 9]

# Plot first dataset
plt.plot(x, y1, label="Dataset 1")

# Plot second dataset
plt.plot(x, y2, label="Dataset 2")

# Add legend
plt.legend()

# Add title
plt.title("Two Datasets on Same Graph")

# Show plot
plt.show()