def calculate_area(width: int, height: int) -> int:
    """
    Calculates the area of a rectangle given its width and height.
    
    Args:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    
    Returns:
    int: The calculated area of the rectangle.
    """
    area = width * height
    return area

w: int = 5
h: int = 3
result: int = calculate_area(w, h)
print(f"The area is: {result}")
