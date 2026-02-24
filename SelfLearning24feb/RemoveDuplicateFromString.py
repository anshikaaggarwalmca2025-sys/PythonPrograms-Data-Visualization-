#Remove duplicate characters from string

# Read input string
text = input("Enter a string: ")

# Initialize empty string
result = ""

# Remove duplicates manually
for ch in text:
    if ch not in result:
        result += ch

# Print result
print("String without duplicates:", result)



#output:
Enter a string: programming
String without duplicates: progamin