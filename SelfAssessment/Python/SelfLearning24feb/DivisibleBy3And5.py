#program to check whether a number is divisible by both 3 and 5
# Read number from user
num = int(input("Enter a number: "))

# Check divisibility by 3 and 5 using modulus operator
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")



output:
Enter a number: 15
Divisible by both 3 and 5
Enter a number: 10
Not divisible by both 3 and 5
Enter a number: 9
Not divisible by both 3 and 5
Enter a number: 30
Divisible by both 3 and 5