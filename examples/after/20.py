from typing import Union

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    pi: float = 3.14159
    area: float = pi * radius ** 2
    return area

radius: float = 5
area_result: float = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area_result}")
