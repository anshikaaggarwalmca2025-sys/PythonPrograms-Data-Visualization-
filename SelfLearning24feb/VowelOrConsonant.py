#program to check whether a character is vowel or consonant
char = input("Enter a character: ")
#checking if the character is a vowel or consonant  
if char.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(char, "is a vowel.")
elif char.isalpha():
    print(char, "is a consonant.")



    output:
Enter a character: A
A is a vowel.
Enter a character: b
b is a consonant.
Enter a character: 1
Enter a character: @
