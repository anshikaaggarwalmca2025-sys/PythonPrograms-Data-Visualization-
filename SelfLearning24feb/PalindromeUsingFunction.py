# Function to check palindrome
def is_palindrome(s):
    # Reverse the string using slicing
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

# Read input from standard input
string = input()

# Call function and print result
print(is_palindrome(string))



output
543
Not Palindrome