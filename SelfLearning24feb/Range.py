#program to check if a number lies within a given range
# Read the number from user
num = int(input("Enter a number: "))

# Read lower limit of range
lower = int(input("Enter lower limit: "))

# Read upper limit of range
upper = int(input("Enter upper limit: "))

# Check if number lies within the range (inclusive)
if lower <= num <= upper:
    print("Number lies within the range")
else:
    print("Number does not lie within the range")




#output:
Enter a number: 5
Enter lower limit: 1
Enter upper limit: 10
Number lies within the range

Enter a number: 15
Enter lower limit: 1
Enter upper limit: 10
Number does not lie within the range
