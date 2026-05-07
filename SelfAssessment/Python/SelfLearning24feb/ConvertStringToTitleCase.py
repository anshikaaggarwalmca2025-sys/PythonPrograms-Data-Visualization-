# Problem 91: Convert string to title case manually

# Read input string
text = input("Enter a sentence: ")

# Convert entire string to lowercase first
text = text.lower()

# Initialize result string
result = ""
capitalize_next = True

# Traverse each character
for ch in text:
    if capitalize_next and ch != " ":
        result += ch.upper()
        capitalize_next = False
    else:
        result += ch
    
    # Capitalize next letter after space
    if ch == " ":
        capitalize_next = True

# Print title case string
print("Title Case:", result)



#output:
Enter a sentence: python is fun
Title Case: Python Is Fun