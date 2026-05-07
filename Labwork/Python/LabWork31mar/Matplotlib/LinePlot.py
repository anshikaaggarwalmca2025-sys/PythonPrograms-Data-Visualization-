#program to create a line plot using given x and y values
#importing matplotlib library
import matplotlib.pyplot as plt

# Given x and y values
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create line plot
plt.plot(x, y)

for i in range(len(x)):
    plt.text(x[i], y[i], str(y[i]), ha='left', va='bottom')


# Add labels and title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Line Plot")

# Display the plot
plt.show()




