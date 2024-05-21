from math import pi

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.

    Args:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return pi * radius ** 2

radius = 5
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area}")
