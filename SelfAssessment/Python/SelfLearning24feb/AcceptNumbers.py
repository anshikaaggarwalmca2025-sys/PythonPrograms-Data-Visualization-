#program to accept numbers from user until they enter 0 and print sum
# Initialize sum variable
total = 0

print("Enter numbers (enter 0 to stop):")

while True:
    num = int(input())
    
    # Stop when user enters 0
    if num == 0:
        break
    
    total += num   # Add number to sum

# Print final sum
print("Sum of numbers is:", total)