#program to calculate simple interest
principal = float(input("Enter the principal(in Rs): "))
rate = float(input("Enter the rate of interest(in %): "))
time = float(input("Enter the time(in years): "))
#calculating simple interest
simple_interest = (principal * rate * time) / 100
print("Principal : Rs", principal)
print("Rate of interest : % ", rate)
print("Time : years", time)

print("The simple interest is: Rs", simple_interest)



output
Enter the principal(in Rs): 10000
Enter the rate of interest(in %): 5     
Enter the time(in years): 3
Principal : Rs 50000.0
Rate of interest : %  2.0
Time : years 3.0
The simple interest is: Rs 3000.0