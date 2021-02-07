import math
def rectangle_area(width, height):
    return width * height
def rectangle_perimeter(width, height):
    return (2*width) + (2*height)
def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3
def disk_area(radius):
    return radius * math.pi
def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
def triangle_area(side1, side2, side3):
    return (side1 + side2 + side3)/2