# Problem 77: Count character frequency using dictionary

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

# Print frequency dictionary
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