#Program to print star pattern using for loop

# Taking number of rows as input
rows = int(input("Enter number of rows: "))

# Outer loop for rows
for i in range(1, rows + 1):
    # Print stars equal to row number
    for j in range(i):
        print("*", end=" ")
    print()  # Move to next line



#output:
Enter number of rows: 5
*
* *
* * *
* * * *
* * * * *

