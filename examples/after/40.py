def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    area = length * width
    return area

length = 5
width = 3
area = calculate_rectangle_area(length, width)
print(f"Area of the rectangle: {area}")
