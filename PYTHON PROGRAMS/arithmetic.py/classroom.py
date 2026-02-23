# Total students and capacity per class
total_students = 125
students_per_class = 30

# Calculate number of full classes
full_classes = total_students // students_per_class

# Calculate remaining students
remaining_students = total_students % students_per_class

# Display results
print("Number of full classes:", full_classes)
print("Number of remaining students:", remaining_students)
