def calculate_area(length: int, width: int) -> int:
    """
    Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle.
    """
    return length * width

length = 5
width = 3
area: int = calculate_area(length, width)
print(f"The area is: {area}")
