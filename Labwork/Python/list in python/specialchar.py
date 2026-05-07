#write a program to find out number of special characters in a sentence
sentence = input("Enter a sentence: ")
count = 0       
for x in sentence:
    if not x.isalnum() :  # Check if character is not alphanumeric and not a space
        count += 1
print("Number of special characters in the sentence:", count)
