from typing import List, Dict

def calculate_total_price(items: List[Dict[str, float]]) -> float:
    """
    Calculate the total price of a list of items.

    Args:
        items: A list of dictionaries where each dictionary represents an item with a 'price' key.

    Returns:
        The total price of all items.
    """
    total: float = 0
    for item in items:
        total += item['price']
    return total

items: List[Dict[str, float]] = [{'name': 'Apple', 'price': 1.50}, {'name': 'Banana', 'price': 0.75}]
result: float = calculate_total_price(items)
print(f'Total price: ${result}')
