def calculate_area(radius: float) -> float:
    """Calculate the area of a circle."""
    area: float = 3.14159 * radius ** 2
    return area

radius: float = 5
area_result: float = calculate_area(radius)
print(area_result)
