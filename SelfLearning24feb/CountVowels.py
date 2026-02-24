# Program to count vowels in a string

# Taking input string
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

# Loop through each character
for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)



#output
Enter a string: my name is
Number of vowels: 3