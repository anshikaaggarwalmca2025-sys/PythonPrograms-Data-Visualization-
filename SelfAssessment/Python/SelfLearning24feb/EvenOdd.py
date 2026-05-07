#program to check whether a number is even or odd without modulus operator
num = int(float("Enter a number: "))
#checking if the number is even or odd
if (num // 2) * 2 == num:
    print("The number is even.")
else:
    print("The number is odd.")



output:
Enter a number: 7
The number is odd.
Enter a number: 12
The number is even.    