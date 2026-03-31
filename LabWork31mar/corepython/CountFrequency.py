# Program to count frequency of characters in a string

# Input string
text = "hello"

# Create empty dictionary
freq = {}

# Loop through each character
for char in text:
    
    # If character already exists, increase count
    if char in freq:
        freq[char] += 1
    else:
        # Otherwise add character with count 1
        freq[char] = 1

# Print dictionary
print("Character Frequency:", freq)



#output
Character Frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}