from typing import Union

def calculate_area(radius: float) -> float:
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

result: float = calculate_area(5)
print("The area is:", result)
