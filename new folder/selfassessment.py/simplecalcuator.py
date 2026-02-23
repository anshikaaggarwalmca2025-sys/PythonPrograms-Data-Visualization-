# Program to perform basic arithmetic operations

# Take two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Take operator input
op = input("Enter operator (+, -, *, /): ")

# Perform operation based on operator
if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    # Check division by zero
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operator")