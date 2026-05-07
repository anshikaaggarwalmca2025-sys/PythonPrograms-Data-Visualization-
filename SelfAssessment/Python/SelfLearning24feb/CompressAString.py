# Problem 100: Compress a string using character counts

# Read input string
text = input("Enter a string: ")

compressed = ""
count = 1

# Loop through string
for i in range(len(text)):
    if i < len(text) - 1 and text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

# Print compressed string
print("Compressed string:", compressed)





#output:
Enter a string: aaabbc
Compressed string: a3b2c1