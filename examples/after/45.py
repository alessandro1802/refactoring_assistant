def calculate_rectangle_area(width: int, height: int) -> int:
    """
    Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The area of the rectangle.
    """
    area = width * height
    return area

w: int = 5
h: int = 10
result: int = calculate_rectangle_area(w, h)
print("The area of the rectangle is:", result)
