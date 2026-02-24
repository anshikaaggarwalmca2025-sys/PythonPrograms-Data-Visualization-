#program to swap two numbers without third variable
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
#printing the numbers before swapping
print("Before swapping: a =", a, "b =", b)
#swapping the numbers
a = a + b
b = a - b
a = a - b
#printing the numbers after swapping
print("After swapping: a =", a, "b =", b)   


  output:

Enter the first number: 5
Enter the second number: 10 
Before swapping: a = 5 b = 10
After swapping: a = 10 b = 5
