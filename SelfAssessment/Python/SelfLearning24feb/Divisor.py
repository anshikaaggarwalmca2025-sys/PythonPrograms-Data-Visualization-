# Program to print all divisors of a number

# Taking input
n = int(input("Enter a number: "))

print("Divisors of", n, "are:")

# Loop from 1 to n
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")



output:
Enter a number: 4
Divisors of 4 are:
1 2 4     