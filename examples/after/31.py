from math import pi

def calc_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.
    """
    area = pi * radius ** 2
    return area

def main() -> None:
    r: float = 5
    result: float = calc_area(r)
    print(f"The area of the circle with radius {r} is {result}")

if __name__ == "__main__":
    main()
