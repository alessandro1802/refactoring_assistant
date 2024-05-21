def calculate_area(radius: float) -> float:
    """Calculate the area of a circle given the radius."""
    pi: float = 3.14159
    area: float = pi * radius ** 2
    return area

radius: float = 5
result: float = calculate_area(radius)
print(result)
