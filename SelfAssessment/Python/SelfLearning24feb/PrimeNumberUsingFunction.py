# Function to check whether a number is prime
def is_prime(num):
    # Numbers less than 2 are not prime
    if num < 2:
        return False
    
    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

# Read input from user
number = int(input("Enter a number: "))

# Call function and print result
if is_prime(number):
    print(number, "is a Prime number")
else:
    print(number, "is not a Prime number")




#output:
Enter a number: 43
43 is a Prime number
    