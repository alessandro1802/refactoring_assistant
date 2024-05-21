from typing import Union

def calculate_circle_area(radius: float) -> float:
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

r: float = 5
result: float = calculate_circle_area(r)
print("The area of the circle with radius", r, "is", result)
