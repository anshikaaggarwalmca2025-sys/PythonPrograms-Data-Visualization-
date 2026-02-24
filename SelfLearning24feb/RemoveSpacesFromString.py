# Problem 90: Remove spaces from string

# Read input string
text = input("Enter a string: ")

# Initialize empty string
result = ""

# Remove spaces manually
for ch in text:
    if ch != " ":
        result += ch

# Print result
print("String without spaces:", result)



#output:
Enter a string: Python is easy
String without spaces: Pythoniseasy