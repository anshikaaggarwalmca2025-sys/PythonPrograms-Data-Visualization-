#take three angles from user
angle1 = float(input ("enter first angle"))
#validating
if(angle1 <= 0):
    print("Invalid angle")
    exit()
else:    
angle2 = float(input ("enter second angle"))
#validating
if(angle2 <= 0):
    print("Invalid angle")
    exit()
else:        
angle3 = float (input ("enter third angle"))
#validating
if(angle3 <= 0):
    print("Invalid angle")
    exit()
else:    
#verifying    
create a list of if(angle1+angle2+angle3 == 180):
    print("the angles form a triangle.")
else:
    print("the angle do not form a triangle.")  

