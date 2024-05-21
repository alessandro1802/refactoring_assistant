from math import pi

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle.
        
    Returns:
        The area of the circle.
    """
    area = pi * radius ** 2
    return area

circle_radius = 5
circle_area = calculate_area(circle_radius)
print(f"The area of the circle with radius {circle_radius} is: {circle_area}")
