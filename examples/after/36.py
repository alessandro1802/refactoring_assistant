from typing import Union

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.

    Args:
        radius: The radius of the circle.

    Returns:
        The calculated area of the circle.
    """
    PI: float = 3.14159
    area: float = PI * radius ** 2
    return area

def main():
    r: float = 5
    result: float = calculate_circle_area(r)
    print(result)

if __name__ == "__main__":
    main()
