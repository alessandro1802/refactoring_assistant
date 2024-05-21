from math import pi

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.
    """
    area = pi * radius ** 2
    return area

radius = 5
area_result = calculate_area(radius)
print(f"The area is: {area_result}")
