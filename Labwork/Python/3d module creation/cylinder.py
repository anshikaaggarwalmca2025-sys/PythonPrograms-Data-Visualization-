#to import the module
import numeric3dcalculation
#to display volume of a cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
volume, total_surface_area, curved_surface_area = numeric3dcalculation.cylindercalculator(radius, height)
print("Volume of the cylinder: ", volume)
print("Total surface area of the cylinder: ", total_surface_area)
print("Curved surface area of the cylinder: ", curved_surface_area)