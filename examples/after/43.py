from typing import Union

def calculate_area(radius: Union[int, float]) -> float:
    """
    Calculate the area of a circle given the radius.

    Parameters:
    radius (int or float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    pi: float = 3.14159
    area: float = pi * radius ** 2
    return area

circle_radius: int = 5
circle_area: float = calculate_area(circle_radius)
print(circle_area)
