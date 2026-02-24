# Function to count vowels in a string
def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    
    # Loop through each character
    for char in s:
        if char in vowels:
            count += 1
    
    return count

# Read input from standard input
string = input()

# Call function and print result
print(count_vowels(string))



#output:
anshika
3