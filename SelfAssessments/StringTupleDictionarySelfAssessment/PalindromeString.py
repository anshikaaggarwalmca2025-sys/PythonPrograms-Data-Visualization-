# Program to check if a string is palindrome

text = input("Enter a string: ")

# Compare original and reversed string
if text == text[::-1]:
    print("It is a palindrome")
else:
    print("Not a palindrome")