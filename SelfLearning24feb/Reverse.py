#program to reverse a number
#read number from user
num = int(input("Enter a number: "))
reverse = 0
#make number positive (in case of negative input)
num = abs(num)
#calculate reverse of the number
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)



output:
Enter a number: 1234
Reversed number: 4321
Enter a number: -567
Reversed number: 765
Enter a number: 0
Reversed number: 0