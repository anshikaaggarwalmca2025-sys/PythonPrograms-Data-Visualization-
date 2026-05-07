# Problem 92: Find longest word in a sentence

# Read sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Assume first word is longest
longest = words[0]

# Find longest word
for word in words:
    if len(word) > len(longest):
        longest = word

# Print longest word
print("Longest word:", longest)




#output:
Enter a sentence: Python programming is interesting
Longest word: programming