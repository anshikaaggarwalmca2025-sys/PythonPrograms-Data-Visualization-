# Program to count word frequency in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:", word_count)