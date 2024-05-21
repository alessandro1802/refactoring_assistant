from typing import List

def calculate_average(nums: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        nums: A list of numbers.

    Returns:
        The average of the input numbers.
    """
    total = sum(nums)
    count = len(nums)
    return total / count

# Example usage
numbers = [5, 10, 15, 20]
result = calculate_average(numbers)
print(f"The average is: {result}")
