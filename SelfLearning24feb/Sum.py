#program to find sum of digits of a numbers
#read number from user
num = int(input())

#make number positive (in case of negative input)
num = abs(num)

sum_digits = 0

#calculate sum of digits
while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

#print result
print(sum_digits)



output:
Enter a number: 1234
10
Enter a number: -567
18
Enter a number: 0
0