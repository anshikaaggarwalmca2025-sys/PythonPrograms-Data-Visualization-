#program to determine the type of triangle 
# Read three sides of triangle
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Check triangle validity condition
if a + b > c and a + c > b and b + c > a:
    
    # Check for Equilateral Triangle
    if a == b == c:
        print("Equilateral Triangle")
    
    # Check for Isosceles Triangle
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    
    # Otherwise Scalene Triangle
    else:
        print("Scalene Triangle")

# If triangle inequality rule fails
else:
    print("Not a Valid Triangle")




#output:
Enter side 1: 5
Enter side 2: 5 
Enter side 3: 5
Equilateral Triangle

Enter side 1: 5
Enter side 2: 5
Enter side 3: 3
Isosceles Triangle

Enter side 1: 5
Enter side 2: 4
Enter side 3: 3
Scalene Triangle