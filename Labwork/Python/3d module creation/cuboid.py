#to import the module
import numeric3dcalculation
#to display volume of a cuboid
length = float(input("Enter the length of the cuboid: "))
breadth = float(input("Enter the breadth of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
volume, total_surface_area, curved_surface_area = numeric3dcalculation.cuboidcalculator(length, breadth, height)
print("Volume of the cuboid: ", volume)
print("Total surface area of the cuboid: ", total_surface_area)
print("Curved surface area of the cuboid: ", curved_surface_area)