# geometry.py

def circle_area(radius):
    """Calculate the area of a circle."""
    import math
    return math.pi * radius**2

def circle_perimeter(radius):
    """Calculate the perimeter of a circle."""
    import math
    return 2 * math.pi * radius

def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def rectangle_perimeter(length, width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)
