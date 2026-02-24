# Function to generate Fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    
    # Print Fibonacci series up to n terms
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

# Read input from standard input
terms = int(input())

# Call function
fibonacci(terms)


#output:
43
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296