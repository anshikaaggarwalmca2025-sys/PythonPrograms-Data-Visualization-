#program to check whether a character is a digit or an alphabet
# Read a character from user
ch = input("Enter a character: ")

# Remove extra spaces
ch = ch.strip()

# Check if character is digit
if ch.isdigit():
    print("Digit")

# Check if character is alphabet
elif ch.isalpha():
    print("Alphabet")

# Otherwise it is special character
else:
    print("Special Character")



    output:
Enter a character: A
Alphabet
Enter a character: 5
Digit
Enter a character: @
Special Character
Enter a character: (space)
Special Character