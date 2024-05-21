def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :return: The area of the circle.
    """
    pi: float = 3.14159
    area: float = pi * radius ** 2
    return area

radius_value: float = 5
result: float = calculate_circle_area(radius_value)
print(result)
