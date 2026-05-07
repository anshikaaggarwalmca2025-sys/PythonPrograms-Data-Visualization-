#a list of five numbers
numbers = [45,47,89,34,56]
#displaying list    
print("Numbers are :", numbers)
print("---------------------------")
#to insert 150 at end
numbers.append(150)
print("After inserting 150 at end:", numbers)   
print("---------------------------")
#creating a list of 5 names
list2 = [23,56,78,90,12]
#to insert list2 at end of numbers list
numbers.append(list2)
print("list2 is : ", list2)
print("After inserting list2 at end of numbers list:", numbers)
print("---------------------------")
#creating a list of 5 numbers
list3 = [100,200,300,400,500]
print("list3 is : ", list3)
#to insert list3 at index 2 of numbers list 
numbers.extend(list3)
print("After inserting list3 at index 2 of numbers list:", numbers)
#to insert 240 at the index 3 in numbers list
numbers.insert(3, 240)
print("\n---------------------------")
print("After inserting 240 at index 3 in numbers list:", numbers)