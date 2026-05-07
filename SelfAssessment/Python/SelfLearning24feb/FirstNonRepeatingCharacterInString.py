# Problem 96: Find first non-repeating character in string

# Read input string
text = input("Enter a string: ")

# Find first non-repeating character
for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")




#output:
Enter a string: swiss
First non-repeating character: w