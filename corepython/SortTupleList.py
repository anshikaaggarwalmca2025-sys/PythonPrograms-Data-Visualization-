# Program to sort list of tuples based on marks using lambda function

# List of tuples (name, marks)
students = [("Anshika", 85), ("Rahul", 78), ("Priya", 92), ("Amit", 80)]

# Sorting the list based on the second element (marks)
# lambda x: x[1] means take marks from each tuple
sorted_students = sorted(students, key=lambda x: x[1])

# Print the sorted list
print("Sorted List Based on Marks:")
print(sorted_students)



#output
Sorted List Based on Marks: [('Rahul', 78), ('Amit', 80), ('Anshika', 85), ('Priya', 92)]