#program to create a bar chart product sales
#importing matplotlib library
import matplotlib.pyplot as plt 
# Given data
products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [150, 200, 300, 250]
# Create bar chart
plt.bar(products, sales)
# Add labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")
# Display the chart
plt.show()