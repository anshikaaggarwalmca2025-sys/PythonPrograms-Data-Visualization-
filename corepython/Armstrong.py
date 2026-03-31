# Program to check if a number is an Armstrong number

# Input number
num = 153

# Store original number
original = num

# Initialize sum
sum = 0

# Find number of digits
digits = len(str(num))

# Calculate Armstrong sum
while num > 0:
    digit = num % 10
    sum += digit ** digits
    num = num // 10

# Check condition
if sum == original:
    print("True")
else:
    print("False")



#output
True