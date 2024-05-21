from typing import Union

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.
    """
    PI: float = 3.14159
    area: float = PI * radius ** 2
    return area

circle_radius: float = 5
circle_area: float = calculate_area(circle_radius)
print("The area of the circle is:", circle_area)
