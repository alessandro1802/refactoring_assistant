def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.
    """
    area = 3.14 * radius ** 2
    return area

radius = 5
circle_area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {circle_area}")
