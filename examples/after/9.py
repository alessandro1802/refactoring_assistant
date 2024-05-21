from typing import Dict, List

def calculate_total_price(products: List[str], prices: Dict[str, float]) -> float:
    """
    Calculate the total price of products based on prices.

    Args:
        products: List of products
        prices: Dictionary of product prices

    Returns:
        Total price of products
    """
    total_price: float = 0
    for product in products:
        if product in prices:
            total_price += prices[product]
    return total_price

products: List[str] = ['apple', 'banana', 'orange']
prices: Dict[str, float] = {'apple': 1.0, 'banana': 0.5, 'grapes': 2.0}

result: float = calculate_total_price(products, prices)
print(f"Total price: {result}")
