from typing import List

def calculate_total(items: List[int]) -> int:
    """
    Calculate the total sum of items in the list.

    Args:
        items: A list of integers.

    Returns:
        The total sum of items.
    """
    total: int = 0
    for item in items:
        total += item
    return total

items: List[int] = [10, 20, 30]
result: int = calculate_total(items)
print(f"Total: {result}")
