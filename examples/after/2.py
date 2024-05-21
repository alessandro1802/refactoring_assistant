def calculate_area_of_triangle(base: float, height: float) -> float:
    """
    Calculate the area of a triangle given the base and height.

    Args:
        base (float): The base of the triangle.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    area = 0.5 * base * height
    return area

b: float = 5
h: float = 10
result: float = calculate_area_of_triangle(b, h)
print(f'The area of the triangle with base {b} and height {h} is: {result}')
