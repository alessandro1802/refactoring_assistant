from math import pi

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.
    """
    area = pi * radius ** 2
    return area

circle_radius = 5
circle_area = calculate_circle_area(circle_radius)
print(circle_area)
