#program for 1,8,27,64,.............,27000
z=6
y=1
x=1
while(x<=27000):
   print(x,end=',')
   x=x+y+z
   y=y+z
   z=z+6