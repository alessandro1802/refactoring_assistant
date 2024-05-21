def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given the radius."""
    pi: float = 3.14159
    area: float = pi * radius ** 2
    return area

result: float = calculate_circle_area(5)
print(f"The area of the circle is {result}")
