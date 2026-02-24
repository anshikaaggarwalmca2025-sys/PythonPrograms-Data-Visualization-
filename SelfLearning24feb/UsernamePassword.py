#program to validate username and password
# Predefined correct username and password
correct_username = "employee"
correct_password = "7410"

# Read username and password from user
username = input("Enter username: ")
password = input("Enter password: ")

# Check if both username and password match
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")



output:
Enter username: employee
Enter password: 7410
Login Successful
Enter username: employee
Enter password: 1234
Invalid Username or Password
Enter username: user
Enter password: 7410
Invalid Username or Password
Enter username: user
Enter password: 1234
Invalid Username or Password    