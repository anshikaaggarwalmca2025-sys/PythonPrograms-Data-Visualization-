#program to generate Fibonacci series using while loop
# Read number of terms
n = int(input("Enter number of terms: "))

# Initialize first two terms
a = 0
b = 1

# Counter
count = 0

print("Fibonacci Series:")

# Generate series using while loop
while count < n:
    print(a)
    next_term = a + b   # Calculate next term
    a = b               # Update a
    b = next_term       # Update b
    count += 1          # Increase counter




#output:
Enter number of terms: 10
Fibonacci Series:
0
1
1
2
3
5
8
13
21
34
