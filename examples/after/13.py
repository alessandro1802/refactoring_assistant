from typing import Union

def calculate_area(radius: Union[int, float]) -> float:
    """Calculate the area of a circle given the radius."""
    pi: float = 3.14159
    area: float = pi * radius ** 2
    return area

radius: Union[int, float] = 5
result: float = calculate_area(radius)
print("The area is:", result)
