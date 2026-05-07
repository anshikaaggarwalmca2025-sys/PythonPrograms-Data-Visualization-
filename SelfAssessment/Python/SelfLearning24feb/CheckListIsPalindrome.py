# Problem 65: Check whether list is palindrome

# Read list elements
lst = list(map(int, input("Enter list elements: ").split()))

# Check palindrome condition
if lst == lst[::-1]:
    print("List is Palindrome")
else:
    print("List is Not Palindrome")



#output
Enter list elements: 1 2 3 2 1
List is Palindrome    