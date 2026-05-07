# Program to check whether a character is vowel or consonant

char = input("Enter a character: ")

# Convert character to lowercase to handle uppercase letters
char = char.lower()

# Check if character is vowel
if char in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")