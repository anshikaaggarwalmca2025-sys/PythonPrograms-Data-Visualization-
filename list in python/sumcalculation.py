#creating a blank list 
numbers = []
#to ask user to input number of elements in the list
n = int(input("Enter number of elements in the list: "))
#to ask user to input elements in the list
for i in range(n):
    num = int(input("number: "))
    print("----------------------------")
    #appending number to the list
    numbers.append(num) 
#displaying list
print("Numbers in the list are:", numbers)
#to find sum of all the numbers in the list
sum = 0
for num in numbers:
    sum += num
print("Sum of all numbers in the list is:", sum)    