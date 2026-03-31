# Program to customize a plot

import matplotlib.pyplot as plt

# Monthly revenue data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [2000, 2500, 2200, 3000, 2800]

# Plot data
plt.plot(months, revenue)

# Add title
plt.title("Monthly Revenue")

# Add axis labels
plt.xlabel("Months")
plt.ylabel("Revenue")

# Add grid
plt.grid()

# Show plot
plt.show()