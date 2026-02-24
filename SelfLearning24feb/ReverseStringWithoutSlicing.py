# Problem 86: Reverse a string without slicing

# Read input string
text = input("Enter a string: ")

# Initialize empty string for reversed result
reversed_text = ""

# Traverse string from end to beginning
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

# Print reversed string
print("Reversed string:", reversed_text)



#output:
Enter a string: hello
Reversed string: olleh