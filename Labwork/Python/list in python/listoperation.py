#creating a list of 5 numbers
numbers = [45,47,89,34,56]
#displaying list
print("Numbers are :", numbers)
print("---------------------------")
#displaying data without square brackets
print("Numbers are :", *numbers)
#------------------------------------
#displaying elements by using for loop
print("---------------------------")
for num in numbers:
    print(num)
#------------------------------------
#----finding number of elements in a list
# len()- it returns number of elements in a list
length = len(numbers)
print("Number of elements in the list:", len)  
#displaying elements in reverse order by using forward indexing
print("Numbers in reverse order")
for index in range(length-1, -1, -1):
    print(numbers[index],end=',') 
#------------------------------------
#finding sum of all the numbers in the list
sum = 0
for num in numbers:
    sum = sum + num
    print("\n---------------------------")
print("Sum of all the numbers in the list:", sum)
#finding greatest number in the list
max = numbers[0]
for index in range(1, length):
    if(max < numbers[index]):
        max = numbers[index]
print("\n---------------------------")
print("Greatest number in the list:", max)