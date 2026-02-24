#program to assign grades based on marks
marks = float(input("Enter the marks: "))
#cheching the grade based on marks
if marks >= 90:
    print("Grade: A")
elif(marks >= 80):
    print("Grade: B")
elif(marks >= 70):
    print("Grade: C")
elif(marks >= 60):
    print("Grade: D")
else:
    print("Grade: E")



#output
Enter the marks: 95
Grade: A
Enter the marks: 85
Grade: B
Enter the marks: 75
Grade: C
Enter the marks: 65
Grade: D
Enter the marks: 55
Grade: E
Enter the marks: 24
Grade: E
    