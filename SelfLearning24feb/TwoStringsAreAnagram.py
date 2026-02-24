# Problem 94: Check whether two strings are anagrams

# Read two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check if sorted characters are equal
if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")




#output:
Enter first string: listen
Enter second string: silent
Strings are Anagrams    