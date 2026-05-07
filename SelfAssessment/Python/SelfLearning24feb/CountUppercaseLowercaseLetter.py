# Problem 97: Count uppercase and lowercase letters

# Read input string
text = input("Enter a string: ")

upper = 0
lower = 0

# Count uppercase and lowercase letters
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

# Print counts
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)




#output:
Enter a string: Hello World
Uppercase letters: 2
Lowercase letters: 8