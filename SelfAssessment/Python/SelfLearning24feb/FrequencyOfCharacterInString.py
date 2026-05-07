# Problem 89: Find frequency of each character in string

# Read input string
text = input("Enter a string: ")

# Create empty dictionary
freq = {}

# Count frequency of each character
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Print frequency
print("Character Frequency:")
for key in freq:
    print(key, ":", freq[key])



#output:
Enter a string: hello
Character Frequency:
h : 1
e : 1
l : 2
o : 1    