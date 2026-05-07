# Program to find the first non-repeating character in a string

# Input string
text = "programming"

# Loop through each character
for char in text:
    
    # If the character appears only once
    if text.count(char) == 1:
        print("First non-repeating character:", char)
        break



#output
First non-repeating character: p
