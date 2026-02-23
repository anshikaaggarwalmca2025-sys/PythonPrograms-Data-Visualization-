#program for calculating simple interest
principal = float(input("Enter the principal (in rs): "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

#--------------------------------------------------------
print("------------------------------------------------")
#calculating simple interest
simple_interest = (principal * rate * time) / 100
print("Principal:rs", principal)
print("Rate of interest:", rate, "%")
print("Time:", time, "years")
print("Simple Interest:rs", simple_interest)
