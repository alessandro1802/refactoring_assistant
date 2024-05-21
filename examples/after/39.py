from math import pi

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius: The radius of the circle.
        
    Returns:
        The area of the circle.
    """
    area = pi * radius ** 2
    return area

radius = 5.0
circle_area = calculate_area(radius)
print("The area of the circle is:", circle_area)
