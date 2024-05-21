from typing import Union

def calculate_area(radius: float) -> float:
    """Calculate the area of a circle given the radius."""
    pi: float = 3.14159
    area: float = pi * radius ** 2
    return area

r: float = 5
result: float = calculate_area(r)
print("The area of the circle is:", result)
