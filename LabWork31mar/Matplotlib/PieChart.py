#program to create a pie chart showing percentage distribution
#importing matplotlib library
import matplotlib.pyplot as plt
# Given data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 30, 20, 25]
# Create pie chart
plt.pie(values, labels=categories, autopct='%1.1f%%')
# Display the chart
plt.show()