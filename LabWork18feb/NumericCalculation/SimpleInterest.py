#program for calculating simple interest
Principal = float(input("Enter the principal(in Rs): "))
Rate = float(input("Enter the rate of interest(in %): "))
Time = float(input("Enter the time(in years): "))

#------------------------------------------------------
print("-----------------------------------------------")
#calculating simple interest
SimpleInterest = (Principal * Rate * Time) / 100
print("Principal: Rs ", Principal)
print("Rate of interest: % ", Rate)
print("Time: years ", Time)
#printing simple interest
print("Simple Interest is: Rs ", SimpleInterest)