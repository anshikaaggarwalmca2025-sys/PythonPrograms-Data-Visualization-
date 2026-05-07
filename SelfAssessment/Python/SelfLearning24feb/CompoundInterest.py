#program to calculate compound interest
principal = float(input("Enter the principal(in Rs):"))
rate = float(input("Enter the rate of interest(in %):"))
time = float(input("Enter the time(in years):"))
#--------------------------------------------------
#calculating compound interest
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal
print("Principal : Rs", principal)
print("Rate of interest : % ", rate)    
print("Time : years", time)
print("The compound interest is: Rs", compound_interest)



output
Enter the principal(in Rs): 54000
Enter the rate of interest(in %): 5.5
Enter the time(in years): 3
Principal : Rs 54000.0
Rate of interest : %  5.5
Time : years 3.0
The compound interest is: Rs 9724.27500000001