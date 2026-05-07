# Program to create scatter plot and highlight maximum point

import matplotlib.pyplot as plt

# Data points
x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

# Scatter plot
plt.scatter(x, y)

# Find maximum value
max_y = max(y)
max_x = x[y.index(max_y)]

# Highlight maximum point
plt.scatter(max_x, max_y, s=200)

# Add title
plt.title("Scatter Plot with Maximum Point")

# Show plot
plt.show()