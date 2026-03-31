# Program to plot a histogram

# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Generate random dataset
data = np.random.randint(10, 100, 50)

# Create histogram
plt.hist(data)

# Add title and labels
plt.title("Histogram of Random Data")
plt.xlabel("Values")
plt.ylabel("Frequency")

# Display the plot
plt.show()