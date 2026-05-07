#program to find largest of three numbers 
num1 = float(input("Enter thye First Number:"))
num2 = float(input("Enter the Second Number:"))
num3 = float(input("Enter the Third Number:"))
#comparing the numbers to find the largest
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
#printing the largest number    
print("The largest number is:", largest)



output
Enter the First Number: 768.0
Enter the Second Number: 345.0
Enter the Third Number: 890.0
The largest number is: 890.0