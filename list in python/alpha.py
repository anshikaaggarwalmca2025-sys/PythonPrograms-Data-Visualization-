sentence = input("Enter a sentence: ")  
#to count the number of alphabets
count = 0
for x in sentence:
    #to check x is alphabet or not
    if x.isalpha():
        count += 1
print("Number of alphabets in the sentence:", count)