# Problem 76: Create student marks dictionary and find topper

# Read number of students
n = int(input("Enter number of students: "))

# Create empty dictionary
marks = {}

# Read student name and marks
for i in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter marks: "))
    marks[name] = score

# Assume first student is topper
topper = list(marks.keys())[0]
highest = marks[topper]

# Find highest marks
for name in marks:
    if marks[name] > highest:
        highest = marks[name]
        topper = name

# Print topper details
print("Topper:", topper)
print("Marks:", highest)


#output:
Enter number of students: 3
Enter student name: Asha
Enter marks: 85
Enter student name: Ravi
Enter marks: 92
Enter student name: Neha
Enter marks: 88
Topper: Ravi
Marks: 92