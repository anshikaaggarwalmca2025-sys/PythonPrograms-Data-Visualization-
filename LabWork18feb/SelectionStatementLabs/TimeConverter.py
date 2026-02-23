#program to input time in seconds and convert it to hours, minutes and seconds
#input of time in seconds
second = int(input("Enter time in seconds: "))
#---------------------------------------------------------
#initaializing number of hours and minutes  
minute = 0
hour = 0
#calculating hours
if(second >= 3600):
    hour = second // 3600
    #storing quotient as hours
    second = second % 3600
    #storing remainder as seconds
#calculating minutes
if(second >= 60):
    minute = second // 60
    #storing quotient as minutes
    second = second % 60
    #storing remainder as seconds
#printing time in hours, minutes and seconds    
print("Time in hours: ", hour)
print("Time in minutes: ", minute)
print("Time in seconds: ", second) 