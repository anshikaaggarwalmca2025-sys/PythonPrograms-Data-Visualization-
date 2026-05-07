#to import the module
import numeric3dcalculation
#to display volume of a cone
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))
volume, total_surface_area, curved_surface_area = numeric3dcalculation.conecalculator(radius, height)
print("Volume of the cone: ", volume)
print("Total surface area of the cone: ", total_surface_area)
print("Curved surface area of the cone: ", curved_surface_area)