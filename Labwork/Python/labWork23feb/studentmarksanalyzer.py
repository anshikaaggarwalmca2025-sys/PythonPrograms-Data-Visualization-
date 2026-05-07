# List of student marks (some are invalid)
marks = [95, 102, 67, -5, 88, 76, 95, 54]

# Step 1: Remove invalid marks (less than 0 or greater than 100)
valid_marks = []
for m in marks:
    if 0 <= m <= 100:
        valid_marks.append(m)

# Step 2: Calculate average of valid marks
if len(valid_marks) > 0:
    average = sum(valid_marks) / len(valid_marks)
else:
    average = 0

# Step 3: Find topper(s)
if valid_marks:
    top_score = max(valid_marks)      # Highest mark
    toppers = []
    for m in valid_marks:
        if m == top_score:
            toppers.append(m)
else:
    top_score = None
    toppers = []

# Step 4: Assign grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

# Display results
print("Valid Marks:", valid_marks)
print("Average:", round(average, 2))
print("Topper Score(s):", toppers)
print("Grade Based on Average:", grade)