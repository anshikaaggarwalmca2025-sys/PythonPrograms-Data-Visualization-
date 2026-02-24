#program to check whether the number is armstrong number
# Read number from user
num = int(input("Enter a number: "))

# Store original number
original = num

# Count number of digits
temp = abs(num)
count = 0

while temp > 0:
    temp //= 10
    count += 1

# Reset temp value
temp = abs(num)
sum_power = 0

# Calculate sum of digits raised to power of count
while temp > 0:
    digit = temp % 10
    sum_power += digit ** count
    temp //= 10

# Check Armstrong condition
if sum_power == abs(original):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")



#output:
Enter a number: 153
Armstrong Number

Enter a number: 123
Not an Armstrong Number

Enter a number: -370
Armstrong Number

