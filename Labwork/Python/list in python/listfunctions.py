#----------------------------------
#list functions in python
#----------------------------------
#count(x)- returns the number of items (x) apperas in the list.
#reverse()- reverses the elements of the list in place.
#create a list of 20 numbers given by user
numbers = []
print("Enter any 20 numbers: ")
for i in range(20):
    num = int(input())
    numbers.append(num)
#display the list
print("------------------------------")
print()
remove_number = int(input("Enter the number you want to remove from list:"))
#--------------------------------------------
print("list is:")
print(numbers)
print("-------------------------------------")
#frequency of number
frequency = numbers.count(remove_number)
if(frequency == 0):
    print(remove_number, "is not found in list")
elif(frequency == 1):
    print("as it is unique so, cannot be removed from list")
else:
    #to reverse the list
    numbers.reverse()
    print("after removing",remove_number,"the list is: ")
    print(numbers)
