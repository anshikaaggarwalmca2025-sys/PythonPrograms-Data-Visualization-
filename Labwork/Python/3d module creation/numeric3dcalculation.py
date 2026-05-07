import math

#fuction to perform all the 3d figure operations
#cube
def cubecalculator(side):
    volume = side ** 3
    total_surface_area = 6 * (side ** 2)
    curved_surface_area = 4 * (side ** 2)
    return volume, total_surface_area, curved_surface_area

#cuboid
def cuboidcalculator(length, width, height):
    volume = length * width * height
    total_surface_area = 2 * (length * width + length * height + width * height)
    curved_surface_area = 2 * (length * height + width * height)
    return volume, total_surface_area, curved_surface_area

#cylinder
def cylindercalculator(radius, height):
    volume = 3.14 * (radius ** 2) * height
    total_surface_area = 2 * 3.14 * radius * (radius + height)
    curved_surface_area = 2 * 3.14 * radius * height
    return volume, total_surface_area, curved_surface_area

#cone
def conecalculator(radius, height):
    volume = (1/3) * 3.14 * (radius ** 2) * height
    slant_height = ((radius ** 2) + (height ** 2)) ** 0.5
    total_surface_area = 3.14 * radius * (radius + slant_height)
    curved_surface_area = 3.14 * radius * slant_height
    return volume, total_surface_area, curved_surface_area

#sphere
def spherecalculator(radius):
    volume = (4/3) * 3.14 * (radius ** 3)
    total_surface_area = 4 * 3.14 * (radius ** 2)
    curved_surface_area = total_surface_area
    return volume, total_surface_area, curved_surface_area

#hemisphere
def hemispherecalculator(radius):
    volume = (2/3) * 3.14 * (radius ** 3)
    total_surface_area = 3 * 3.14 * (radius ** 2)
    curved_surface_area = 2 * 3.14 * (radius ** 2)
    return volume, total_surface_area, curved_surface_area