#program to print multiplication table using while loop
# Read number from user
num = int(input("Enter a number: "))

# Initialize counter
i = 1

print("Multiplication Table of", num)

# Use while loop to print table up to 10
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1   # Increase counter



#output:
Enter a number: 5
Multiplication Table of 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50