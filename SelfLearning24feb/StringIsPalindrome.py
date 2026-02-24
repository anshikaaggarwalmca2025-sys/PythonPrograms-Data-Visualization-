# Problem 87: Check whether string is palindrome

# Read input string
text = input("Enter a string: ")

# Reverse string manually
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

# Check palindrome condition
if text == reversed_text:
    print("String is Palindrome")
else:
    print("String is Not Palindrome")


#output:
Enter a string: madam
String is Palindrome    