from typing import List

def calculate_total(items: List[int]) -> int:
    """
    Calculate the total sum of items in a list.

    Args:
        items: A list of integers.

    Returns:
        The total sum of the items.
    """
    total = sum(items)
    return total

items_list: List[int] = [10, 20, 30, 40]
result: int = calculate_total(items_list)
print("Total:", result)
