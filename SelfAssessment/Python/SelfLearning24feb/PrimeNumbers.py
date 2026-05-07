#program to print prime numbers between 1 and N using while loop
# Read value of N
n = int(input("Enter a number: "))

print("Prime numbers between 1 and", n, "are:")

# Loop through numbers from 2 to N
num = 2

while num <= n:
    is_prime = True   # Assume number is prime
    
    i = 2
    # Check divisibility
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    
    # If number is prime, print it
    if is_prime:
        print(num)
    
    num += 1



#output:
Enter a number: 20
Prime numbers between 1 and 20 are:
2
3
5
7
11
13
17
19
    