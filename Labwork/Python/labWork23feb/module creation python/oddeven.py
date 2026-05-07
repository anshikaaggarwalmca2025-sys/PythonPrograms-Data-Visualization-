from numericcalculation import calculatorremainder
num = int(input("Enter a number: "))
if calculatorremainder(num,2) == 0:
    print(num, "is an even number.")
else:   
     print(num, "is an odd number.")