from typing import Union

def calculate_area(radius: Union[int, float]) -> float:
    """
    Calculate the area of a circle given the radius.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.
    """
    pi: float = 3.14159
    area: float = pi * radius ** 2
    return area

radius: int = 5
result: float = calculate_area(radius)
print("The area of the circle is", result)
