# Problem 93: Replace all vowels with *

# Read input string
text = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize result string
result = ""

# Replace vowels with *
for ch in text:
    if ch in vowels:
        result += "*"
    else:
        result += ch

# Print modified string
print("Modified string:", result)



#output:
Enter a string: Hello World
Modified string: H*ll* W*rld